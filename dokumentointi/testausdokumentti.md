# Testausdokumentti

## Yksikkötestauksen kattavuusraportti
![viimeisin kattavuusraportti](/dokumentointi/kuvat/kattavuusraportti.png)

## Mitä on testattu ja miten?
Algoritmien testeissä testataan löytävätkö algoritmit kartasta lyhyimmän reitin ja palauttavatko oikean polun. Testataan myös, että algoritmit toimivat halutulla tavalla, kun polkua ei löydy. Testaamisessa käytettiin samoja karttoja kuin mitä ohjelmaan on ladattu.
Main.py testeissä keskitytään enemmän siihen, että tulostetaan ja haetaan luokista oikeat asiat. 
Map_file.py testeissä testataan, että luokkka muuttaa kartan verkoksi halutulla tavalla, jotta algoritmien toimiminen ei jäisi verkon toteutuksesta kiinni. 

Yksikkötestien lisäksi manuaalinen testaus useilla eri syötteillä on ollut suuressa roolissa. Etenkin algoritmien testaamisessa painotettiin tätä, jotta on saatu varmuus niiden toimimisesta mahdollisimman monipuolisissa tilanteissa.

## Minkälaisilla syötteillä testaus tehtiin?
Testaamisessa käytettiin ohjelmaan ladattuja karttoja. Käyttäjän input syötteisiin käytettiin apuna myös invoken mock-moduulia.

## Miten testit voidaan toistaa?

Testit voidaan toistaa komennolla 

 ```poetry run invoke coverage-report```

jolloin ohjelma toteuttaa testit ja palauttaa html-kattavuusraportin


