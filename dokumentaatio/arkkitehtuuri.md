# Arkkitehtuurikuvaus

## Rakenne

### Pakkauskaavio
![](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Pakkauskaavio.png)

Pakkaus entities sisältää ohjelman käyttämistä tietoa kuvaavista ja säilyttävistä luokista koostuvan ohjelmakoodin. Pakkaus ui sisältää käyttöliittymästä, pakkaus services sovelluslogiikasta ja pakkaus repositories tiedosto-operaatioista vastaavan ohjelmakoodin. 

## Käyttöliittymä

Käyttöliittymä koostuu kolmesta erllisestä näkymästä

- Calculator-näkymä
- History-näkymä
- Stats-näkymä

Käyttäjälle näkyy kerrallaan aina yksi näistä näkymistä. Jokainen näkymä on toteutettu omana luokkanaan. UI-luokka vastaa näkymien näyttämisestä käyttäjälle ja niiden välillä siirtymisestä. Käyttöliittymän lähdekoodi on mahdollisimman paljon erillään sovelluslogiikan lähdekoodista. Käyttöliittymä kutsuu services-pakkauksen luokkien [CalculatorService](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/services/calculator_service.py)- ja [StatsService](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/services/stats_service.py)-luokkien metodeita.

## Sovelluslogiikka

Sovelluksen käsittelemää tietoa kuvaavat entities-pakkauksen luokat [Equation](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/entities/equation.py) ja [Result](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/entities/result.py):

```mermaid
 classDiagram
      class Equation{
          expression
          result
      }
      class Result{
          value
          index
      }
```

Equation-luokan oliot kuvaavat yhtälöitä eli laskimella laskettuja lausekkeita, joita talletetaan laskimen laskuhistoriaan. Result-luokan oliot kuvaavat laskimella laskettuja tuloksia, joita voi tallettaa laskimen muistiin.

[CalculatorService](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/services/calculator_service.py)-luokka vastaa käyttöliittymän luokkien [CalculatorView](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/ui/calculator_view.py) ja [HistoryView](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/ui/history_view.py) tarjoamista toiminnallisuuksista. [StatsService](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/services/stats_service.py)-luokka vastaa käyttöliittymän luokan [StatsView](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/ui/stats_view.py) tarjoamasta toiminnallisuudesta. [CalculatorService](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/services/calculator_service.py)-luokka käsittelee sovelluksen tallettamia tietoja [EquationRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/repositories/equation_repository.py)- ja [ResultRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/repositories/result_repository.py)-luokkien tarjoaman toiminnallisuuksien kautta.

## Sovelluksen käyttämän tiedon pysyväistalletus

Tiedon pysyväistalletukseta vastaa repositories-pakkauksen luokat [EquationRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/repositories/equation_repository.py) ja [ResultRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/repositories/result_repository.py). Kumpikin luokka tallettaa tietoa csv-tiedostoon. Nämä luokat noudattavat Repository-suunnittelumallia, mikä mahdollistaa tiedon talletustavan vaivattomamman vaihtamisen tarvittaessa.

### Tiedostot

[EquationRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/repositories/equation_repository.py)- ja [ResultRepository](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/repositories/result_repository.py)-luokat tallettavat erillisiin tiedostoihin. Sovelluksen juuressa olevassa .env-tiedostossa määritellään käytettävien tiedostojen nimet.

Laskuhistoria talletetaan tiedostoon riveinä:
"equation.expression;equation.result;"

Yhtälön lauseketta kuvaa "equation.expression" ja lausekkeen tulosta "equation.result". Nämä arvot erotellaan toisistaan ";"-merkillä.

Laskimen muistiin talletetut tulokset talletetaan tiedostoon riveinä:
"result.value"

Tulosta kuvaa "result.value".

## Päätoiminnallisuudet

Tässä osiossa kuvataan sekvenssikaavioilla sovelluksen toimintalogiikkaa päätoiminnallisuuksien osalta.

### Lausekkeen laskeminen Calculator-näkymässä

Kun käyttäjä on klikkaillut tai kirjoittanut lausekkeen käyttöliittymän syötekenttään ja klikkaa painiketta "=", etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant CalculatorView
  participant CalculatorService
  participant EquationRepository
  participant Equation
  participant Result
  Note over User: click "=" button
  User->>CalculatorView: handle_equality_button_click()
  CalculatorView->>CalculatorService: calculate("2+3")
  CalculatorService->>Equation: Equation("2+3", 5)
  Equation-->>CalculatorService: equation
  CalculatorService->>EquationRepository: store_equation(equation)
  CalculatorService->>Result: Result(5)
  CalculatorService-->>CalculatorView: 5
```

Calculator-näkymästä vastaavan `CalculatorView`-luokan tapahtumankäsittelijä `handle_equality_button_click` kutsuu sovelluslogiikasta vastaavan `CalculatorService`-luokan metodia `calculate`, jolle annetaan parametrina käyttäjän syöttämä lauseke. Metodi `calculate` luo uuden `Equation`-luokan olion vastaamaan laskettua lauseketta ja pysyväistallettaa tämän tiedon tiedostoon kutsumalla `EquationRepository`-luokan metodia `store_equation`.  Metodi `calculate` luo myös uuden `Result`-luokan olion vastaamaan laskettua tulosta, jotta se voidaan tarvittaessa tallettaa laskimen muistiin. Tämän jälkeen metodi `calculate` palauttaa lasketun tuloksen käyttöliittymälle, joka päivittää näkymänsä niin, että käyttäjä näkee tuloksen.

### Laskuhistorian tyhjentäminen History-näkymässä

Kun käyttäjä klikkaa painiketta "Clear History", etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant HistoryView
  participant CalculatorService
  participant EquationRepository
  Note over User: click "Clear History" button
  User->>HistoryView: handle_clear_button_click()
  HistoryView->>CalculatorService: delete_all_equations()
  CalculatorService->>EquationRepository: delete_all()
  HistoryView->>HistoryView: initialize_equation_frame()
```

History-näkymästä vastaavan `HistoryView`-luokan tapahtumankäsittelijä `handle_equality_button_click` kutsuu sovelluslogiikasta vastaavan `CalculatorService`-luokan metodia `delete_all_equations`. Metodi `delete_all_equations` kutsuu `EquationRepository`-luokan metodia `delete_all`, joka alustaa laskuhistorian sisältävän tiedoston. Käyttöliittymä päivittää itsensä laskuhistorian sisältävän osan suhteen.

### Normaalijakauman kertymäfunktion arvon laskeminen Stats-näkymässä

Kun käyttäjä klikkaa painiketta "Calculate" syötettyään tarvittavat tiedot, etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant StatsView
  participant StatsService
  Note over User: click "Calculate" button
  User->>StatsView: handle_calculate_button_click()
  StatsView->>StatsService: normal_cdf(0, 0, 1)
  StatsService-->>StatsView: 0.5
```

Stats-näkymästä vastaavan `StatsView`-luokan tapahtumankäsittelijä `handle_calculate_button_click` kutsuu sovelluslogiikasta vastaavan `StatsService`-luokan metodia `normal_cdf`. Metodi `normal_cdf` laskee kertymäfunktion arvon annetuilla parametreilla ja palauttaa tuloksen käyttöliittymälle, joka päivittää näkymänsä niin, että käyttäjä näkee tuloksen.

## Tiedostetut heikkoudet sovelluksen rakenteessa

### Käyttöliittymä

Käyttöliittymän [CalculatorView](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/ui/calculator_view.py)-luokan lähdekoodissa on paljon toisteisuutta tämän näkymän painikkeiden luomisen ja näkymään sijoittamisen yhteydessä. Koska tähän näkymään on vielä tarkoitus lisätä uusia painikkeita uusia toiminnallisuuksia varten, mahdollinen silmukkarakenne, joka kävisi läpi listaa kaikkien näkymään sijoitettavien painikkeiden symboleista ja niiden sijainneista, täytyisi joka kerta kirjoittaa uudelleen, kun lisätään uusi painike ja/tai muutetaan painikkeiden sijainteja näkymässä.


### Tietoa kuvaavat luokat
[Result](https://github.com/Deepthetics/ot-harjoitustyo/blob/master/src/entities/result.py)-luokka, joka kuvaa laskimella laskettua tulosta, joka voidaan tallettaa laskimen muistiin on toistaiseksi vielä hieman triviaali, koska sillä on vain yksi käytössä oleva attribuutti: "value". Tulokset voitaisiin pysyväistallettaa ilman, että ne muutetaan Result-luokan olioiksi. Laskimen muistitoiminnallisuuksia on tarkoitus vielä laajentaa ja ottaa käyttöön tämän luokan toinen attribuutti: "index". Tämän on tarkoitus mahdollistaa yksittäisiin ja tiettyihin tuloksiin viittaaminen.
