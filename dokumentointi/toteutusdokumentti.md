# Toteutusdokumentti

## Ohjelman yleisrakenne

![yleisrakenne](/dokumentointi/kuvat/rakenne.png)
- main-funktio kysyy käyttäjältä mitä karttaa vertailussa käytetään
- main-funktio hakee map_file-luokasta käyttäjän valitsemaa karttaa vastaavan Map-olion sekä tulostaa kuvan kartasta
- main-funktio kysyy käyttäjältä reitin aloitus- ja loppupisteen: ensin rivinumeron, jonka jälkeen käyttäjä voi valita rivin vapaana olevista pisteistä haluamansa
- main-funktio luo Dijkstra-olion, jonka syötteenä on kartan verkko sekä kartan leveys, sekä IdaStar-olion, jonka syötteenä on kartan verkko
- main-funktio kutsuu ida_star- ja dijkstra-funktiota, jotka molemmat palauttavat joko lyhimmän reitin pituuden tai tiedon siitä, että reittiä ei ole olemassa
- main-funktio tulostaa mahdolliset lyhimmät reitit ja algoritmien käyttämän ajan

## Saavutetut aika- ja tilavaativuudet

## Suorituskyky- ja O-analyysivertailu

## Työn mahdolliset puutteet ja parannusehdotukset

## Lähteet