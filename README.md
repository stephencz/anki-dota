# anki-dota
A programmatically generated Anki flashcard decks for Dota 2 items and heroes. 

## How to Use
To use the deck, it is advisable to simply download the latest release and import it into Anki. Compiling a deck for yourself is time consuming, unenjoyable, and
generally not worth the effort. 

## Compiling your own deck

1. Create a folder called temp in the src/ directory.
2. Run __main__.py
3. Say yes to collecting item data and yes to collecting hero data. The process takes a very long time (45 minutes or more)
4. Import each csv file into Anki. Set the delimiter from a comma t a semicolon.
5. The cards can be imported into seperate decks for each csv, or into one big deck. This is entirely up to you.
6. Done.

## FAQ

**Q: How accurate is this deck?**

All cards in this deck are created using data from this [Dota 2 Wiki](https://dota2.fandom.com/wiki/Dota_2_Wiki). Therefore, the cards are as accurate as the Wiki.

**Q: How up-to-date is this deck?**

I try to release an updated version of the deck with every major release. Collecting the data the deck uses is a time consuming process. And organizing the resulting
csv files into a single, coherent deck of cards, also takes some time. Therefore, I don't update the deck when there are minor updates. I don't believe this is an issue 
as the use of the deck is more in gaining a general understanding of the game's items and heroes. Small changes to values generally won't matter if you understand the
gist of what an item or hero does.

