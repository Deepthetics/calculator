# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on olla laskin, eli sillä  on mahdollista laskea erilaisia laskutoimituksia ja niistä muodostettuja lausekkeita reaaliluvuilla.

## Käyttäjät

Sovelluksella on alustavan suunnitelman mukaan vain yhdenlaisia käyttäjiä samoin oikeuksin.

## Käyttöliittymä

Sovellukseen on tarkoitus toteuttaa graafinen käyttöliittymä. **Tehty**
  
  - elementit ja näykymä laskutoimitusten syöttämistä ja tulostamista varten **Tehty**
  - elementit laskimen muistitoiminnallisuuksia varten **Tehty**
  - elementit ja näkymä laskimen laskuhistoriaa varten

## Suunnitellut toiminnallisuudet

### Ydintoiminnallisuus

Tässä lueteltu toiminnallisuus on tarkoitus toteuttaa ensin.

- käyttäjä voi syöttää laskutoimituksen tai laskutoimituksista muodostetun lausekkeen laskettavaksi **Tehty**
  - tuetut laskutoimitukset: yhteenlasku, vähennyslasku, kertolasku, jakolasku, potenssilasku **Tehty**
  - syötetyssä lausekkeessa on mahdollista käyttää sulkumerkintöjä laskujärjestyksen muuttamiseen **Tehty**
- käyttäjälle tulostetaan laskettu tulos **Tehty**
- lisää tuettuja laskutoimituksia: juuret, logaritmit, kertoma, modulo, itseisarvo, trigonometriset funktiot **Tehty osittain**
- vakiot: e, pi
- laskimen muistitoiminnallisuudet: tuloksen tallentaminen muistiin, tuloksen palauttaminen muistista, muistin tyhjentäminen **Tehty**
- laskuhistoria (toteutetaan muistitoiminnallisuuksien rinnalle tai niiden korvaajaksi):
  - käyttäjä näkee laskemansa laskutoimitukset ja niiden tulokset sekä pystyy suoraan syöttämään jo laskettuja tuloksia uusiin laskutoimituksiin
  - käyttäjä pystyy poistamaan laskuhistoriasta yksittäisiä laskutoimituksia/tuloksia tai tyhjentämään laskuhistorian kokonaan
- mahdollisuus laskea todennäköisyyksiä erilaisista todennäköisyysjakaumista

### Jatkokehitysideat

Tässä lueteltuja toiminnallisuuksia toteutetaan ajan salliessa, kun ydintoiminnallisuus on toteutettu.

- mahdollisuus luoda ja tallentaa omia funktioita
- mahdollisuus syöttää aineistoja ja laskea näistä tilastollisia tunnuslukuja
- graafisen laskimen toiminnallisuus
