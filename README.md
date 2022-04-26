# Ohjelmistotekniikka, harjoitustyö

## Release

[Release](https://github.com/Deepthetics/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio
- [Arkkitehtuurikuvaus](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Vaatimusmäärittely](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelma suoritetaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti luodaan komennolla:

```bash
poetry run invoke coverage-report
```

Raportti tallentuu _htmlcov_-hakemistoon.

### Pylint

Tiedostossa [.pylintrc](./.pylintrc) määritetyt laatutarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```

PEP-8 tyyliohjeiden mukainen formatointi suoritetaan komennolla:

```bash
poetry run invoke format
```
