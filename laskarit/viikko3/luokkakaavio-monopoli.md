## Luokkakaavio Monopolista

```mermaid
classDiagram
Pelaaja "1" -- "1" Pelinappula
Pelilauta "1" -- "40" Peliruutu
Peliruutu "1" -- "1" Pelinappula
Peliruutu : seuraava
Noppa : pisteluku
