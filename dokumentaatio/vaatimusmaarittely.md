# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on olla laskin, eli sillä on mahdollista laskea erilaisia laskutoimituksia ja niistä muodostettuja lausekkeita reaaliluvuilla sekä todennäköisyysjakaumiin liittyviä tuloksia.

## Käyttäjät

Sovelluksella on alustavan suunnitelman mukaan vain yhdenlaisia käyttäjiä samoin oikeuksin.

### Käytössä olevan version tarjoama toiminnallisuus

- käyttäjä voi syöttää laskutoimituksen tai laskutoimituksista muodostetun lausekkeen laskettavaksi
  - tuetut laskutoimitukset: yhteenlasku, vähennyslasku, kertolasku, jakolasku, potenssilasku
  - syötetyssä lausekkeessa on mahdollista käyttää sulkumerkintöjä laskujärjestyksen muuttamiseen
- käyttäjälle tulostetaan laskettu tulos
- lisää tuettuja laskutoimituksia: juuret, logaritmit, kertoma, modulo, itseisarvo
- vakiot: e, pi
- laskimen muistitoiminnallisuudet: tuloksen tallentaminen muistiin, tuloksen palauttaminen muistista, muistin tyhjentäminen
- laskuhistoria:
  - käyttäjä näkee laskemansa laskutoimitukset ja niiden tulokset sekä pystyy suoraan syöttämään jo laskettuja tuloksia uusiin laskutoimituksiin
  - käyttäjä pystyy tyhjentämään laskuhistorian
- mahdollisuus laskea todennäköisyyksiä normaalijakaumasta

### Jatkokehitysideat

Tässä lueteltuja toiminnallisuuksia toteutetaan ajan salliessa, kun ydintoiminnallisuus on toteutettu.

- lisää tuettuja funktioita: trigonometriset funktiot, erikantaiset logaritmit...
- mahdollisuus luoda omia funktioita ja 
- mahollisuus piirtää funktioiden kuvaajia (graafisen laskimen toiminnallisuus)
- lisää tuettuja jakaumia: t-jakauma, diskreetit jakaumat...
- todennäköisyysjakaumien pistetodennäköisyys- ja tiheysfunktiot
- todennäköisyysjakaumien kvantiilifunktiot
- mahdollisuus syöttää aineistoja ja laskea näistä tilastollisia tunnuslukuja
