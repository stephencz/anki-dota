from wiki import Wiki
import deck

if __name__ == '__main__':

    wiki = Wiki()

    # Retrieves data about items
    result = input('Would you like to fetch item data? (Y/n) ')
    if result == 'Y' or result == 'y':
        urls = wiki.get_item_urls()
        wiki.get_all_item_data(urls)

    # Retrieves data about heroes
    result = input('Would you like to fetch hero data? (Y/n) ')
    if result == 'Y' or result == 'y':
        urls = wiki.get_hero_urls()
        wiki.get_all_hero_data(urls)

    # Builds Item Decks
    deck.generate_item_deck('data/items.json', 'basic_consumables', 'csv/basic_cosumables.csv', 'Dota::Items::Basic::Consumables')
    deck.generate_item_deck('data/items.json', 'basic_attributes', 'csv/basic_attributes.csv', 'Dota::Items::Basic::Attributes')
    deck.generate_item_deck('data/items.json', 'basic_equipment', 'csv/basic_equipment.csv', 'Dota::Items::Basic::Equipment')
    deck.generate_item_deck('data/items.json', 'basic_miscellaneous', 'csv/basic_miscellaneous.csv', 'Dota::Items::Basic::Miscellaneous')
    deck.generate_item_deck('data/items.json', 'basic_secret', 'csv/basic_secret.csv', 'Dota::Items::Basic::Secret')

    deck.generate_item_deck('data/items.json', 'upgraded_accessories', 'csv/upgraded_accessories.csv', 'Dota::Items::Upgraded::Accessories')
    deck.generate_item_deck('data/items.json', 'upgraded_support', 'csv/upgraded_support.csv', 'Dota::Items::Upgraded::Support')
    deck.generate_item_deck('data/items.json', 'upgraded_magical', 'csv/upgraded_magical.csv', 'Dota::Items::Upgraded::Magical')
    deck.generate_item_deck('data/items.json', 'upgraded_armor', 'csv/upgraded_armor.csv', 'Dota::Items::Upgraded::Armor')
    deck.generate_item_deck('data/items.json', 'upgraded_weapons', 'csv/upgraded_weapons.csv', 'Dota::Items::Upgraded::Weapons')
    deck.generate_item_deck('data/items.json', 'upgraded_artifacts', 'csv/upgraded_artifacts.csv', 'Dota::Items::Upgraded::Artifacts')
    
    deck.generate_item_deck('data/items.json', 'neutral_tier_1', 'csv/neutral_tier_1.csv', 'Dota::Items::Neutral::Tier 1')
    deck.generate_item_deck('data/items.json', 'neutral_tier_2', 'csv/neutral_tier_2.csv', 'Dota::Items::Neutral::Tier 2')
    deck.generate_item_deck('data/items.json', 'neutral_tier_3', 'csv/neutral_tier_3.csv', 'Dota::Items::Neutral::Tier 3')
    deck.generate_item_deck('data/items.json', 'neutral_tier_4', 'csv/neutral_tier_4.csv', 'Dota::Items::Neutral::Tier 4')
    deck.generate_item_deck('data/items.json', 'neutral_tier_5', 'csv/neutral_tier_5.csv', 'Dota::Items::Neutral::Tier 5')
   
    deck.generate_item_deck('data/items.json', 'roshan', 'csv/roshan.csv', 'Dota::Items::Roshan::Drops')


    # Builds Hero Decks


    wiki.shutdown()
  
        