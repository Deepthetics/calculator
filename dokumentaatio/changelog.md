# Changelog

## Viikko 3
- lisätty CalculatorService-luokka, joka vastaa sovelluslogiikasta
- lisätty UI-luokka, joka vastaa käyttöliittymästä (tällä hetkellä käytössä alustava tekstikäyttöliittymä)
- testattu, että CalculatorService-luokkaan toteutettu toiminnallisuus toimii oikein

## Viikko 4
- lisätty Result-luokka, joka kuvaa laskettua tulosta
- lisätty ResultRepository-luokka, joka vastaa tiedosto-operaatioista, joita laskimen muistitoiminnallisuudet käyttävät
- lisätty laskimen muistitoiminnallisuudet CalculatorService-luokkaan
- lisätty toiminnallisuutta vielä väliaikaisesti käytössä olevaan tekstikäyttöliittymään (graafisen käyttöliittymän suunnittelu aloitettu)

## Viikko 5
- lisätty uusi graafista käyttöliittymää vastaava UI-luokka, joka korvaa alkuperäisen tekstikäyttöliittymän
- muokattu CalculatorService-luokkaa vastaamaan paremmin erilaisiin virhetilanteisiin

## Viikko 6
- lisätty Equation-luokka, joka kuvaa laskettua lauseketta
- lisätty EquationRepository-luokka, joka vastaa tiedosto-operaatioista, joita laskimen laskuhistoriaan liittyvät toiminnallisuudet käyttävät
- lisätty laskuhistoriaan liittyvät toiminnallisuudet Calculator-Service-luokkaan sekä tuki vakioiden e, pi ja logaritmi-funktion käyttöön
- käyttöliittymään käytettävyyttä parannettu (erityisesti sopimattoman syötteen jälkeen uusien laskutoimitusten syöttäminen nyt helpompaa)
- toteuttu laskuhistorianäkymää vastaava luokka HistoryView käyttöliittymään ja mahdollisuus siirtyä eri näkymien välillä (tämä näkymä ei ole vielä oletusarvoisesti käytössä bugien ja vähäisen testaamisen vuoksi)
- testattu, että tiedosto-operaatioista vastaaviin Repository-luokkiin toteutettu toiminnallisuus toimii oikein
