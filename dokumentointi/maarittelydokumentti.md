# Määrittelydokumentti

- Kieli: suomi
- Ohjelmointikieli: Python
- Opinto-ohjelma: Tietojenkäsittelytieteen kandi

Toteutan ohjelman, joka löytää lyhimmän reitin painotetusta verkosta pisteestä toiseen kahdella eri algoritmillä. Vertailen tässä Dijsktra ja IDA* algoritmia. 

## Algoritmit

Valistin Dijkstran algortimin, koska minulla on tästä jo etukäteen tietoa. IDA*-algoritmin valistin, koska se vaikutti mielenkiintoiselta, sekä tarpeeksi erilaiselta Dijkstraan verrattuna. Näin siis suoritusteen vertailussakin on jotain järkeä.

### Dijkstra

Aikavaativuus: 
O(|E| + |V| log |V|), jossa V on solmujen lukumäärä ja E on kaarien lukumäärä. 

Tilavaativuus: 
O(V^2), jossa V on solmujen lukumäärä


### IDA*

Aikavaativuus: 
IDA* algoritmille ei ole yksiselitteistä parasta aikavaativuutta, vaan se riippuu painotetun verkon tyypistä ja heurestiikasta. 

Tilavaativuus:
O(d), jossa d on reitin pituus