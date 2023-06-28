# Toteutusdokumentti

## Ohjelman yleisrakenne

![yleisrakenne](/dokumentointi/kuvat/rakenne.png)
- main-funktio kysyy käyttäjältä mitä karttaa vertailussa käytetään
- main-funktio hakee map_file-luokasta käyttäjän valitsemaa karttaa vastaavan Map-olion sekä tulostaa kuvan kartasta
- main-funktio kysyy käyttäjältä reitin aloitus- ja loppupisteen: ensin rivinumeron, jonka jälkeen käyttäjä voi valita rivin vapaana olevista pisteistä haluamansa
- main-funktio luo Dijkstra- ja IDA*-oliot, joiden molempien syötteenä on kartan verkko, aloitus- ja lopetussolmu sekä kartan leveys
- main-funktio kutsuu ida_star- ja dijkstra-funktiota, jotka molemmat palauttavat joko lyhyimmän reitin sekä sen pituuden, tai tiedon siitä, että reittiä ei ole olemassa
- main-funktio tulostaa reittien pituuden, sekä reitit valitussa kartassa. Tämä haetaan map_file-luokasta. Vaihtoehtoisesti tulostaa tiedon siitä, ettei reittiä ole. Molemmissa tapauksissa tulostetaan algoritmien käyttämät ajat ja vertaillaan näitä toisiinsa

## Aika- ja tilavaativuudet

Dijkstra
> Aikavaativuus: 
> O(|E| + |V| log |V|), jossa V on solmujen lukumäärä ja E on kaarien lukumäärä
>
> Tilavaativuus: 
> O(V^2), jossa V on solmujen lukumäärä

IDA*
> Aikavaativuus: 
> IDA*-algoritmille ei ole yksiselitteistä parasta aikavaativuutta, vaan se riippuu painotetun verkon tyypistä ja heurestiikasta.
>
> Tilavaativuus:
> O(d), jossa d on reitin pituus

## Suorituskyky- ja O-analyysivertailu

| kartta | solmujen määrä | O(|E| + |V| log |V|)| Dijkstran 10:n toiston keskiarvo| IDA*:n 10:n toiston keskiarvo |
|:------:|:--------------:|:-------------------:|:-------------------------------:|:-----------------------------:|
|4x4     |16              |80                   |0.0001039                        |0.0002835                      |
|8x8     |64              |410                  |0.0001215                        |0.0003617                      |
|16x16   |256             |2350                 |0.0009472                        |0.0551402                      |
|32x32   |1024            |11884                |0.0089881                        |1.1370921                      |
|64x64   |4096            |59510                |0.1597089                        |0.0280987                      |

Toistot tehtiin ohjelmassa olevilla kartoilla niiden ensimmäisestä vapaasta solmusta niiden viimeisimpään vapaaseen solmuun. Keskiarvojen mukaan Dijkstra on kaikilla syötteillä nopeampi, paitsi 64x64-kartalla, eli kun solmuja on 4096. Tuloksissa täytyy kuitenkin ottaa huomioon, että koska keskiarvomittaukset tehtiin vain tietyn kartan perusteella, voisivat ne olla erilaiset muilla kartoilla mitattuna.

## Työn mahdolliset puutteet ja parannusehdotukset
Työhön voisi etsiä enemmän monipuolisempia karttoja. Myös verkon luomisen kartan pohjalta voisi toteuttaa tehokkaammin.
Graafisesta puolesta saisi tehtyä siistimmän ja käyttäjäystävällisemmän.
Työhön voisi myös lisätä ominaisuuden, jossa se käy reitin läpi automaattisesti n-kertaa ja laskee näistä molemmille algoritmeille niiden käyttämän aikojen keskiarvon, jolloin vertailu olisi astetta laadukkaampaa.

## Lähteet

IDA*: https://en.wikipedia.org/wiki/Iterative_deepening_A*
IDA* heurestiikka: https://www.growingwiththeweb.com/2012/06/a-pathfinding-algorithm.html 
Dijkstra: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
