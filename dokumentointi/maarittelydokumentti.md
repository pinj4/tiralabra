# Määrittelydokumentti

- Kieli: suomi
- Ohjelmointikieli: Python
- Opinto-ohjelma: Tietojenkäsittelytieteen kandi

Toteutan ohjelman, joka löytää verkon lyhyimmän reitin pisteestä toiseen kahdella eri algoritmillä. Kartassa voidaan liikkua sivusuuntiin sekä diagonaalisesti. Vertailen tässä Dijsktra ja IDA* algoritmia. Käytän ohjelmassa Movin AI LAb:in sivuilta ladattuja [MAPF-karttoja](https://www.movingai.com/benchmarks/mapf/index.html)

## Algoritmit

Valitsin Dijkstran algortimin, koska minulla on tästä jo etukäteen tietoa. IDA*-algoritmin valitsin, koska se vaikutti mielenkiintoiselta, sekä tarpeeksi erilaiselta Dijkstraan verrattuna. Näin siis suoritusteen vertailussakin on jotain järkeä.

### Dijkstra

Aikavaativuus: 
O(|E| + |V| log |V|), jossa V on solmujen lukumäärä ja E on kaarien lukumäärä

Tilavaativuus: 
O(V^2), jossa V on solmujen lukumäärä


### IDA*

Aikavaativuus: 
IDA* algoritmille ei ole yksiselitteistä parasta aikavaativuutta, vaan se riippuu painotetun verkon tyypistä ja heurestiikasta.

Tilavaativuus:
O(d), jossa d on reitin pituus