import math
import secrets
import time

from flask import Flask
from flask import abort, redirect, render_template, request, session, flash, g
import markupsafe

import config
import places
import users

app = Flask(__name__)
app.secret_key = config.secret_key

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    elapsed_time = round(time.time() - g.start_time, 2)
    #print("elapsed time:", elapsed_time, "s")
    return response

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    page_size = 50
    total_places = places.place_count()
    page_count = math.ceil(total_places / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/1")
    if page > page_count:
        return redirect("/" + str(page_count))

    all_places = places.get_places(page, page_size)
    return render_template("index.html", places=all_places, page=page, page_count=page_count)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    all_places = users.get_places(user_id)
    return render_template("show_user.html", user=user, places=all_places)

@app.route("/find_place")
def find_place():
    query = request.args.get("query", "")
    # Haetaan sivu osoitteesta (esim. &page=2). Jos sitä ei ole, oletus on sivu 1.
    page = request.args.get("page", 1, type=int)
    page_size = 50

    if query:
        total_results = places.find_places_count(query)
        page_count = math.ceil(total_results / page_size)
        page_count = max(page_count, 1)

        # Tarkistetaan, ettei mennä olemattomille sivuille
        if page < 1:
            return redirect("/find_place?query=" + query + "&page=1")
        if page > page_count:
            return redirect("/find_place?query=" + query + "&page=" + str(page_count))

        results = places.find_places(query, page, page_size)
    else:
        results = []
        page = 1
        page_count = 1

    return render_template("find_place.html", query=query, results=results, page=page, page_count=page_count)

@app.route("/place/<int:place_id>")
def show_place(place_id):
    place = places.get_place(place_id)
    if not place:
        abort(404)
    classes = places.get_classes(place_id)
    reviews = places.get_reviews(place_id)

    if len(reviews) > 0:
        total = sum(review["stars"] for review in reviews)
        count = len(reviews)
        average = total / count
    else:
        average = 0

    return render_template("show_place.html", place=place, classes=classes, reviews=reviews, average=average)

@app.route("/new_place")
def new_place():
    require_login()
    classes = (places.get_all_classes())
    return render_template("new_place.html", classes=classes)

@app.route("/create_place", methods=["POST"])
def create_place():
    require_login()
    check_csrf()

    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    address = request.form["address"]
    if not address or len(address) > 50:
        abort(403)
    city = request.form["city"]
    if not city or len(city) > 50:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 1000:
        abort(403)
    user_id = session["user_id"]

    all_classes = places.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    place_id = places.add_place(title, address, city, description, user_id, classes)

    return redirect("/place/" + str(place_id))

@app.route("/edit_place/<int:place_id>")
def edit_place(place_id):
    require_login()
    place = places.get_place(place_id)
    if not place:
        abort(404)
    if place["user_id"] != session["user_id"]:
        abort(403)

    all_classes = places.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in places.get_classes(place_id):
        classes[entry["title"]] = entry["value"]

    return render_template("edit_place.html", place=place, classes=classes, all_classes=all_classes)

@app.route("/update_place", methods=["POST"])
def update_place():
    require_login()
    check_csrf()

    place_id = request.form["place_id"]
    place = places.get_place(place_id)
    if not place:
        abort(404)
    if place["user_id"] != session["user_id"]:
        abort(403)

    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    address = request.form["address"]
    if not address or len(address) > 50:
        abort(403)
    city = request.form["city"]
    if not city or len(city) > 50:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 1000:
        abort(403)

    all_classes = places.get_all_classes()
    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    places.update_place(place_id, title, address, city, description, classes)

    return redirect("/place/" + str(place_id))

@app.route("/remove_place/<int:place_id>", methods=["GET", "POST"])
def remove_place(place_id):
    require_login()
    place = places.get_place(place_id)
    if not place:
        abort(404)
    if place["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_place.html", place=place)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            places.remove_place(place_id)
            return redirect("/")
        else:
            return redirect("/place/" + str(place_id))

@app.route("/add_review", methods=["POST"])
def add_review():
    require_login()
    check_csrf()

    place_id = request.form["place_id"]
    try:
        stars = int(request.form["stars"])
        if stars < 1 or stars > 5:
            abort(403)
    except ValueError:
        abort(403)
    comment = request.form["comment"]

    user_id = session["user_id"]


    places.add_review(place_id, user_id, stars, comment)

    return redirect("/place/" + str(place_id))

@app.route("/delete_review/<int:review_id>", methods=["GET", "POST"])
def delete_review(review_id):
    require_login()
    review = places.get_review(review_id)

    if not review:
        abort(404)
    if review["user_id"] != session["user_id"]:
        abort(403)
    place_id = review["place_id"]

    if request.method == "GET":
        place = places.get_place(place_id)
        return render_template("delete_review.html", review=review, place=place)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            places.delete_review(review_id, session["user_id"])
            return redirect("/place/" + str(place_id))
        else:
            return redirect("/place/" + str(place_id))

@app.route("/edit_review/<int:review_id>")
def edit_review(review_id):
    require_login()
    review = places.get_review(review_id)
    if not review:
        abort(404)
    if review["user_id"] != session["user_id"]:
        abort(403)
    place = places.get_place(review["place_id"])
    return render_template("edit_review.html", review=review, place=place)

@app.route("/update_review", methods=["POST"])
def update_review():
    check_csrf()
    require_login()

    review_id = request.form["review_id"]
    review = places.get_review(review_id)
    user_id = session["user_id"]
    if not review:
        abort(404)
    if review["user_id"] != session["user_id"]:
        abort(403)

    place_id = request.form["place_id"]
    try:
        stars = int(request.form["stars"])
        if stars < 1 or stars > 5:
            abort(403)
    except ValueError:
        abort(403)
    comment = request.form["comment"]

    places.update_review(review_id, stars, comment, user_id)

    return redirect("/place/" + str(place_id))


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if password1 != password2:
        flash("VIRHE: Salasanat eivät ole samat.")
        return redirect("/register")
    if not users.create_user(username, password1):
        flash("VIRHE: Tunnus on jo varattu.")
        return redirect("/register")
    flash("Tunnus luotu onnistuneesti! Voit nyt kirjautua sisään.")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            flash("VIRHE: Väärä tunnus tai salasana.")
            return redirect("/login")

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")
