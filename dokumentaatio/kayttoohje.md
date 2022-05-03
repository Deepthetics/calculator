# Käyttöohje
projektin viimeisin [release](https://github.com/Deepthetics/ot-harjoitustyo/releases) otsikon "Assets" alta valitsemalla "Source code".

## Konfigurointi

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

