# Käyttöohje
projektin viimeisin [release](https://github.com/Deepthetics/ot-harjoitustyo/releases) otsikon "Assets" alta valitsemalla "Source code".

## Sovelluksen konfigurointi

Sovelluksen tietojen tallettamista varten käytettävien tiedostojen nimiä voi muokata juurihakemiston .env-tiedostossa. Käytettävät tiedostot luodaan samasta juurihakemistosta löytyvään data-kansioon. 

## Sovelluksen käynnistäminen

1. Asenna ensimmäiseksi riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sitten sovellus komennolla 

```bash
poetry run invoke start
```

## Sovelluksen käyttäminen

Sovellus avautuu Calculator-näkymään. Tähän näkymään pääsee myös painamalla yläpalkin painiketta "Calculator".

![](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/calculator_view.png)

### Calculator-näkymän käyttäminen:

Laskimen numeronäppäimet, operaattorinäppäimet, sulkunäppäimet sekä vakioita e ja pi kuvaavat näppäimet toimivat niin kuin yleensäkin laskimissa. Näiden näppäimien painaminen syöttää näissä näppäimissä kuvatun symbolin laskimen näytölle.

Muiden näppäimien käyttö:
- "="-näppäin laskee syötetyn lausekkeen arvon
- "^"-näppäin vastaa potenssioperaattoria ja näkyy laskimen näytöllä "**"-merkkinä
- "mod"-näppäin vastaa modulo-operaattoria ja näkyy laskimen näytöllä "%"-merkkinä
- "sqrt"-näppäin vastaa neliöjuurifunktiota (katso "Ylimääräinen huomio")
- "log"-näppäin vastaa luonnollista logaritmifunktiota (katso "Ylimääräinen huomio")
- backspace-näppäin poistaa viimeksi syötetyn symbolin laskimen näytöltä
- "C"-näppäin tyhjentää laskimen näytön
- "MS"-näppäin tallettaa viimeksi lasketun tuloksen laskimen muistiin
- "MR"-näppäin palauttaa viimeksi lasketun tuloksen laskimen muistista
- "MC"-näppäin tyhjentää laskimen muistin

Ylimääräinen huomio:

Funktionäppäimien "sqrt" ja "log" painaminen syöttää laskimen näytölle "sqrt(" ja "log(". Tämän jälkeen syötetään luku/lauseke funktiolleö. Lopuksi täytyy painaa vielä itse ")"-näppäintä, joka osoittaa, mihin funktiolle annettava syöte päättyy.

### History-näkymän käyttäminen:

History-näkymään pääsee painamalla yläpalkin painiketta "History".

![](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/history_view.png)

Laskin tallettaa kaikki lasketut lausekkeet ja niiden tulokset. History-näkymässä pystyy tarkastelemaan tätä laskuhistoriaa. Laskuhistoria toimii samalla laskimen muistina. Painamalla laskettua lauseketta kuvaavaa näppäintä, palautuu lausekkeen tulos muistista. Samalla sovellus siirtyy Calculator-näkymään ja valittu tulos syötetään Calculator-näkymän näytölle. Laskuhistorian voi tyhjentää painamalla "Clear History"-näppäintä.

### Stats-näkymän käyttäminen:

Stats-näkymään pääsee painamalla yläpalkin painiketta "Stats".

![](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/stats_view.png)

Tässä näkymässä pystyy toistaiseksi laskemaan ainoastaan normaalijakauman kertymäfunktion arvoja.

Normaalijakauman kertymäfunktion arvojen laskeminen:

- "x"-kenttään syötetään se kohta jakaumasta, missä kertymäfunktion arvo halutaan laskea
- "mean"-kenttään syötetään käytettävän normaalijakauman odotusarvo-parametri
- "sd"-kenttään syötetään käytettävän normaalijakauman keskihajonta-parametri

"Calculate"-näppäimen painaminen laskee kertymäfunktion arvon annetuilla syötteillä. Tämä arvo tulostuu "Calculate"-näppäimen viereiseen kenttään. Normaalijakaumaa käytettäessä keskihajonta-parametrin täytyy olla positiivinen reaaliluku.
