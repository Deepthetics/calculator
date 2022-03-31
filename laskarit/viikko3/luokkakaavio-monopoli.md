## Luokkakaavio Monopolista

```mermaid
classDiagram
  class Noppa{
    pisteluku
  }
  Pelaaja "1" -- "1" Pelinappula
  Pelilauta "1" -- "40" Peliruutu
  Peliruutu "1" -- "1" Pelinappula
  Peliruutu : seuraava_ruutu
```
