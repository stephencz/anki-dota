# anki-dota
A programmatically generated Anki flashcard deck for Dota 2 items and heroes. 

Dota 2 is an exceptionally hard game to learn. There are over two hundred unique items, over one hundred unique heros, and nuanced game mechanics.
To make the process of learning the game easier, I created this Anki deck generator. The generator works by scraping data about items and heroes from the Dota 2 wiki,
mostly in the form of images, and compiles that data into logically structure decks.

In an effort to keep the deck from becoming overwhelming, I made a heavy use of Anki's ability to nest decks. Items are broken divided into Basic, Upgraded, Neutral, and Roshan drop items, and then further divided into their categories such as consumables, attribute items, weapons, etc. This allows new players to study discrete sections of the game without having to be overwhelmed with information. After learning these individual sections they can graduate to studying the cards more broadly. 

## To Do

* ~~Implement item data scraping~~
* Implement hero data scraping
* Implement item card and deck generation
* Implement hero card and deck generation
* Release the first deck.

