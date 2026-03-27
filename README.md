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
