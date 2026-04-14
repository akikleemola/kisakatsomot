# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:67:0: C0301: Line too long (109/100) (line-too-long)
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:2:0: E0401: Unable to import 'flask' (import-error)
app.py:3:0: E0401: Unable to import 'flask' (import-error)
app.py:10:0: C0103: Constant name "app" doesn't conform to UPPER_CASE naming style (invalid-name)
app.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:43:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:76:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:111:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:129:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:169:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:182:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:169:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:189:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:210:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:226:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:210:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:233:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:244:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:271:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:275:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:291:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:300:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:291:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:310:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module places
places.py:1:0: C0114: Missing module docstring (missing-module-docstring)
places.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:15:0: R0913: Too many arguments (6/5) (too-many-arguments)
places.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:56:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:56:0: R0913: Too many arguments (6/5) (too-many-arguments)
places.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:93:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:100:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:104:0: C0116: Missing function or method docstring (missing-function-docstring)
places.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:32:4: R1705: Unnecessary "else" after "return" (no-else-return)

------------------------------------------------------------------
Your code has been rated at 7.70/10
```

Käydään seuraavaksi läpi tarkemmin raportin sisältö ja perustellaan, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Suuri osa raportin ilmoituksista on seuraavan tyyppisiä ilmoituksia:

```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
```
Nämä ilmoitukset tarkoittavat, että moduuleissa ja funktioissa ei ole docstring-kommentteja. Sovellusta tehdessä tein päätöksen että, en käytä docstring-kommentteja.

## Import-ilmoitukset

Raportissa on seuraavat ilmoitukset liittyen `import`-komentoihin:

```
app.py:2:0: E0401: Unable to import 'flask' (import-error)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
```

Pylint antaa jostain syystä nämä ilmoitukset, vaikka sekä Flask- että Werkzeug-kirjastot on asennettu kehitysympäristössä. Nämä ilmoitukset eivät haittaa, koska `import`-komennot toimivat sovelluksessa.

## Tarpeeton else

Raportissa on seuraavat ilmoitukset liittyen `else`-haaroihin:

```
app.py:182:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:226:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:300:8: R1705: Unnecessary "else" after "return" (no-else-return)
users.py:32:4: R1705: Unnecessary "else" after "return" (no-else-return)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa koodia:

```python
if "remove" in request.form:
            places.remove_place(place_id)
            return redirect("/")
        else:
            return redirect("/place/" + str(place_id))
```

Tämä koodi olisi mahdollista kirjoittaa seuraavasti tiiviimmin:

```python
if "remove" in request.form:
            places.remove_place(place_id)
            return redirect("/")
return redirect("/place/" + str(place_id))
```

Omasta mielestä else käyttäminen selkeyttää koodia, joten en korjannut niitä.

## Puuttuva palautusarvo

Raportissa on seuraavat ilmoitukset liittyen funktion palautusarvoon:

```
app.py:169:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:210:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:291:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Nämä ilmoitukset liittyvät tilanteeseen, jossa funktio käsittelee metodit `GET` ja `POST` mutta ei muita metodeja. Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
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
```

Tässä funktio palauttaa arvon, kun `request.method` on `GET` tai `POST`, mutta periaatteessa voisi tulla tilanne, jossa `request.method` on jotain muuta eikä koodi palauttaisi arvoa. Käytännössä tällainen tilanne ei ole kuitenkaan mahdollinen, koska funktion dekoraattorissa on vaatimus, että metodin tulee olla `GET` tai `POST`. Niinpä tässä tapauksessa ei ole riskiä, että funktio ei jossain tilanteessa palauttaisi arvoa.

## Vakion nimi

Raportissa on seuraava ilmoitus liittyen vakion nimeen:

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Tässä koodin päätasolla määritelty muuttuja tulkitaan vakioksi, jonka nimen tulisi olla kirjoitettu suurilla kirjaimilla. Kuitenkin sovelluksen kehittäjän näkemyksen mukaan tässä tilanteessa näyttää paremmalta, että muuttujan nimi on pienillä kirjaimilla. Muuttujaa käytetään koodissa näin:

```python
app.secret_key = config.secret_key
```

## Vaarallinen oletusarvo

Raportissa on seuraavat ilmoitukset liittyen vaaralliseen oletusarvoon:

```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```

Tässä parametrin oletusarvo `[]` on tyhjä lista. Pythonissa oletusarvona oleva tyhjä lista jaetaan kaikkien funktiokutsujen kesken, mikä voi aiheuttaa bugeja, jos listaa muokataan lennosta. Tässä sovelluksessa listaa käytetään kuitenkin ainoastaan SQL-kyselyiden muuttujien turvalliseen välittämiseen, eikä siihen koskaan lisätä uusia alkioita. Koska funktio ainoastaan lukee listan sisältöä, tämä rakenne ei aiheuta riskiä ja on täysin turvallinen.

## Liian monta argumenttia

Raportissa on seuraavat ilmoitukset liittyen liian moneen argumenttiin:

```
places.py:15:0: R0913: Too many arguments (6/5) (too-many-arguments)
places.py:56:0: R0913: Too many arguments (6/5) (too-many-arguments)
```
Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
def add_place(title, address, city, description, user_id, classes):
    sql = """INSERT INTO places (title, address, city, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, address, city, description, user_id])

    place_id = db.last_insert_id()

    sql = "INSERT INTO place_classes (place_id, title, value) VALUES (?, ?, ?)"

    for class_title, class_value in classes:
        db.execute(sql, [place_id, class_title, class_value])
    return place_id
```
Pylint suosittelee, että funktioilla olisi enintään viisi argumenttia. Sovelluksen `places.py` -tiedostossa joidenkin tietokantaan tallentavien funktioiden (esim. uuden paikan lisääminen tai muokkaaminen) on kuitenkin otettava kerralla vastaan useita kenttiä (nimi, osoite, kuvaus, kategoria, tekijä jne.). Näiden pakkaaminen erillisiin tietorakenteisiin ennen funktiota tekisi koodista tämän kokoisessa sovelluksessa tarpeettoman monimutkaista.

### Liian pitkä rivi

Raportissa on seuraavat ilmoitukset liittyen liian pitkään riviin:

```
app.py:67:0: C0301: Line too long (109/100) (line-too-long)
```
Ilmoitus koskee riviä:
```
return render_template("show_place.html", place=place, classes=classes, reviews=reviews, average=average)
```

Omasta mielestä selkeämpi, kun kaikki muuttujat on samalla rivillä.
