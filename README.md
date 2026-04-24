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

### Sivutus ja tietokannan hitaus

Jotta selain ei jäätyisi näin isosta datamäärästä, tein etusivulle kurssimateriaalin esimerkin mukaisen sivutuksen (sivu näyttää 50 paikkaa kerrallaan). Pelkkä sivutus ei kuitenkaan riittänyt, koska tietokannan piti silti käydä läpi valtava määrä arvostelurivejä ja yhdistää ne paikkoihin keskiarvojen laskemista varten.

Mittasin etusivun sivutuksen latausaikoja Flaskin `@app.before_request` ja `@app.after_request` -funktioilla. Ilman indeksointia sivujen lataus kesti selvästi yli kaksi sekuntia:

```text
elapsed time: 2.64 s
127.0.0.1 - - [24/Apr/2026 11:37:14] "GET / HTTP/1.1" 200 -
elapsed time: 2.30 s
127.0.0.1 - - [24/Apr/2026 11:37:25] "GET /2 HTTP/1.1" 200 -
elapsed time: 2.33 s
127.0.0.1 - - [24/Apr/2026 11:37:34] "GET /3 HTTP/1.1" 200 -
```

### Tietokantaindeksi

Ratkaisin suorituskykyongelman lisäämällä `schema.sql`-tiedostoon indeksin. Se tehostaa huomattavasti arvostelujen hakemista tietyn paikan perusteella:

```sql
CREATE INDEX idx_place_reviews ON reviews (place_id);
```

Tämän pienen lisäyksen jälkeen tietokantakyselyt kevenivät ja latausajat putosivat murto-osaan aiemmasta. Sovellus latautuu nyt suurellakin datamäärällä salamannopeasti:

```text
elapsed time: 0.10 s
127.0.0.1 - - [24/Apr/2026 11:47:14] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.02 s
127.0.0.1 - - [24/Apr/2026 11:47:22] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.05 s
127.0.0.1 - - [24/Apr/2026 11:47:27] "GET /4 HTTP/1.1" 200 -
```
