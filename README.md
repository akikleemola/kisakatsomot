# Kisakatsomot

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään uusia kisakatsomoita/urheilubaareja sekä muokkaamaan ja poistamaan omia lisäyksiään.
* Käyttäjä näkee kaikki sovellukseen lisätyt paikat.
* Käyttäjä pystyy etsimään paikkoja hakusanalla (esim. kaupungin tai nimen perusteella).
* Sovelluksessa on käyttäjäsivu, joka näyttää montako paikkaa ja arvostelua käyttäjä on lisännyt, sekä listan näistä.
* Käyttäjä pystyy valitsemaan paikalle yhden luokittelun (baari, ravintola, torikatsomo)
* Käyttäjä pystyy antamaan katselupaikalle sanallisen arvostelun ja arvosanan (1-5). Paikan tiedoissa näytetään kaikki arvostelut ja niiden keskiarvo.

## Sovelluksen asennus

Käytä git clone komentoa saadaksesi koodin. 

Asenna 'flask' -kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot: 
```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin: 

```
$ flask run
```

## Suuren tietomäärän testaus

Testasin sovellusta isolla tietomäärällä tekemällä erillisen `seed.py` -skriptin. Se tekee tietokantaan:
* 1 000 käyttäjää
* 100 000 paikkaa
* 1 000 000 arvostelua

**Sivutus**
Jotta selain ei jäätyisi näin isosta datamäärästä, tein etusivulle kurssimateriaalin esimerkin mukaisen sivutuksen. Nyt sivu näyttää 50 paikkaa kerrallaan.

**Ajanmittaus ja indeksit**
Mittasin etusivun latausaikaa Flaskin `@app.before_request` ja `@app.after_request` -funktioilla.
* Ilman indeksiä etusivun lataus kesti tällä datamäärällä noin **2.65 sekuntia**.
* Hitaus johtui siitä, että tietokannan piti käydä läpi miljoona arvosteluriviä ja yhdistää ne paikkoihin keskiarvojen laskemista varten.
* Lisäsin `reviews`-taulun `place_id`-sarakkeeseen indeksin: `CREATE INDEX idx_place_reviews ON reviews (place_id);`
* Tämän pienen lisäyksen jälkeen latausaika putosi **0.03 sekuntiin**.