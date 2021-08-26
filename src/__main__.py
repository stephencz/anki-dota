from wiki import Wiki

if __name__ == '__main__':

    wiki = Wiki()

    result = input('Would you like to fetch item data? (Y/n)')
    if result == 'Y' or result == 'y':
        urls = wiki.get_item_urls()
        wiki.get_all_item_data(urls)

    wiki.shutdown()
  
        