## Luokkakaavio Monopolista

```mermaid
classDiagram
classPelaaja "1" -- "1" ClassPelinappula
classPelilauta "1" -- "40" ClassPeliruutu
ClassPeliruutu "1" -- "1" ClassPelinappula
class Peliruutu{
seuraava
}
ClassNoppa{
pisteluku
}
