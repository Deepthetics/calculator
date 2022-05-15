# Testausdokumentti

Sovellusta on testattu automatisoiduilla yksikkötesteillä ja manuaalisesti toteutetuilla järjestelmätason testeillä.

## Yksikkötestaus

### Service-luokat

Sovelluslogiikasta vastaavaa [CalculatorService](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/services/calculator_service.py)-luokkaa testaa [TestCalculatorService](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/tests/services/calculator_service_test.py)-luokka ja [StatsService](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/services/stats_service.py)-luokkaa testaa [TestStatsService]()-luokka.

### Repositorio-luokat

Tiedon pysyväistalletuksesta vastaavaa luokkaa [EquationRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/repositories/equation_repository.py)-luokkaa testaa [TestEquationRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/tests/repositories/equation_repository_test.py)-luokka ja [ResultRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/tests/repositories/result_repository_test.py)-luokkaa testaa [TestResultRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/repositories/result_repository.py)-luokka. Näiden luokkien toimintaa testataan erillisillä testejä varten luoduilla tiedostoilla. Näiden tiedostojen nimet on määritelty sovelluksen juuressa olevassa .env.test-tiedostossa.

### Testauskattavuus

Käyttöliittymän lähdekoodia lukuunottamatta sovelluksen testien haarautumakattavuus on 90%.

![](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage.png)

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on tehty manuaalisesti.

### Asennus

Sovellus on asennettu [käyttöohjeen](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) ohjeiden mukaan ja sitä on testattu Linux-ympäristössä.

### Toiminnallisuudet

[Määrittelydokumentissa](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.mds) kuvatut toiminnallisuudet on testattu. Syötekenttiin on yritetty syöttää erilaisia virheellisiä syötteitä.

## Tiedostetut ongelmat sovelluksen toiminnassa

Järjestelmätestauksessa huomattiin, että Calculator-näkymän näyttöön tulostuu "Invalid input", jos lasketun lausekkeen arvo on 0. Syy tähän on selvillä, mutta tätä ei ehditty korjaamaan, koska se havaittiin viimeisten sovellukseen tehtyjen muutosten jälkeen vasta hiljattain.
