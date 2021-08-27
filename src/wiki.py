import json, re, time

from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup

class Wiki:

    # The base URLS for retrieving all the data
    BASE_URLS = {
        'site':'https://dota2.fandom.com',
        'items':'https://dota2.fandom.com/wiki/Items',
        'heros':'https://dota2.fandom.com/wiki/Heroes'
    }

    def __init__(self):
        self._driver = None

    """
    Gets a BeautifulSoup object from the passed in current webdriver source.
    @return BeautifulSoup
    """
    def get_soup(self):
        return BeautifulSoup(self._driver.page_source, 'html.parser')

    def get_page(self, url):
            self._driver.get(url)    
            self.maximize_window()
            self.remove_ads()
            time.sleep(5)

    def maximize_window(self):
        body = self._driver.find_element_by_tag_name('body')
        height = body.get_attribute('scrollHeight')
        self._driver.set_window_size(1920, int(height))

    def remove_ads(self):
        self._driver.execute_script("var element = document.getElementsByClassName(\"top-ads-container\")[0].remove();")

    def get_hero_urls(self):

        urls = {}

        # Load webdriver
        self._driver = webdriver.Firefox()
        self._driver.set_page_load_timeout(60)

        # At the main wiki page for items
        self.get_page(self.BASE_URLS['heroes'])
        soup = self.get_soup()


        return urls

    def get_hero_categories(self):
        pass

    """
    Retrieves wiki urls for all items that are currently implemented and
    available in game and returns them as a dictionary of lists with keys
    for each category. For example, basic_consumables will be the urls for
    all basic items that are consumables.
    """
    def get_item_urls(self):
            
        urls = {}

        # Load webdriver
        self._driver = webdriver.Firefox()
        self._driver.set_page_load_timeout(60)

        # At the main wiki page for items
        self.get_page(self.BASE_URLS['items'])
        soup = self.get_soup()

        # Retrieve Basic Item Urls
        urls['basic_consumables'] = self.get_item_category_urls(soup, 'Consumables')
        urls['basic_attributes'] = self.get_item_category_urls(soup, 'Attributes')
        urls['basic_equipment'] = self.get_item_category_urls(soup, 'Equipment')
        urls['basic_miscellaneous'] = self.get_item_category_urls(soup, 'Miscellaneous')
        urls['basic_secret'] = self.get_item_category_urls(soup, 'Secret')

        # Retrieve Upgrade Item Urls
        urls['upgraded_accessories'] = self.get_item_category_urls(soup, 'Accessories')
        urls['upgraded_support'] = self.get_item_category_urls(soup, 'Support')
        urls['upgraded_magical'] = self.get_item_category_urls(soup, 'Magical')
        urls['upgraded_armor'] = self.get_item_category_urls(soup, 'Armor')
        urls['upgraded_weapons'] = self.get_item_category_urls(soup, 'Weapons')
        urls['upgraded_artifacts'] = self.get_item_category_urls(soup, 'Artifacts')

        # Retrieve Neutral Item Urls
        urls['neutral_tier_1'] = self.get_item_category_urls(soup, 'Tier_1')
        urls['neutral_tier_2'] = self.get_item_category_urls(soup, 'Tier_2')
        urls['neutral_tier_3'] = self.get_item_category_urls(soup, 'Tier_3')
        urls['neutral_tier_4'] = self.get_item_category_urls(soup, 'Tier_4')
        urls['neutral_tier_5'] = self.get_item_category_urls(soup, 'Tier_5')

        # Retrieve Roshan Item Urls
        urls['roshan'] = self.get_item_category_urls(soup, 'Roshan_Drop')

        
        self._driver.quit()

        return urls

    """
    Gets lists of items by their category division on the wiki's main items category
    @param category The ID of the span inside the category's H3 header.
    @return A list of urls to pages from the category.
    """
    def get_item_category_urls(self, soup, category):
        temp = []

        item_list = soup.find('span', {'id': category }).parent.find_next_sibling('div')
        items = item_list.findChildren('div')
        for item in items:
            link = item.find('a')
            temp.append(link['href'])

        return temp

    """
    Retrieves data for all relevant Dota items, saves the data as a JSON, and returns the JSON
    @param A dictionary of lists holding urls for each category of item.
    @return A list of JSON objects
    """
    def get_all_item_data(self, urls):
        data = {}

        data['basic_consumables'] = self.get_item_category_data(urls, 'basic_consumables')
        data['basic_attributes'] = self.get_item_category_data(urls, 'basic_attributes')
        data['basic_equipment'] = self.get_item_category_data(urls, 'basic_equipment')
        data['basic_miscellaneous'] = self.get_item_category_data(urls, 'basic_miscellaneous')
        data['basic_secret'] = self.get_item_category_data(urls, 'basic_secret')

        data['upgraded_accessories'] = self.get_item_category_data(urls, 'upgraded_accessories')
        data['upgraded_support'] = self.get_item_category_data(urls, 'upgraded_support')
        data['upgraded_magical'] = self.get_item_category_data(urls, 'upgraded_magical')
        data['upgraded_armor'] = self.get_item_category_data(urls, 'upgraded_armor')
        data['upgraded_weapons'] = self.get_item_category_data(urls, 'upgraded_weapons')
        data['upgraded_artifacts'] = self.get_item_category_data(urls, 'upgraded_artifacts')

        data['neutral_tier_1'] = self.get_item_category_data(urls, 'neutral_tier_1')
        data['neutral_tier_2'] = self.get_item_category_data(urls, 'neutral_tier_2')
        data['neutral_tier_3'] = self.get_item_category_data(urls, 'neutral_tier_3')
        data['neutral_tier_4'] = self.get_item_category_data(urls, 'neutral_tier_4')
        data['neutral_tier_5'] = self.get_item_category_data(urls, 'neutral_tier_5')

        data['roshan'] = self.get_item_category_data(urls, 'roshan')

        with open('data/items.json', 'w') as file:
            file.write(json.dumps(data, sort_keys=True, indent=4))

        return data

    """
    Gets all items within a given category.
    @param urls A dictionary of lists holding urls for each category of item.
    @param category The key of the item category
    @return A list containing JSON objects.
    """
    def get_item_category_data(self, urls, category, delay=10):
        data = []

        # Load webdriver
        self._driver = webdriver.Firefox()
        self._driver.set_page_load_timeout(60)

        for url in urls[category]:
            data.append(self.get_single_item_data(url, category))
            time.sleep(delay)

        # Quit webdriver
        self._driver.quit()

        return data

    """
    Gets data for single item from a passed in wiki page url.
    @param url A url, for example '/wiki/Tango', to the item to get.
    @param category The category the item belongs to.
    @return A JSON Object.
    """
    def get_single_item_data(self, url, category):
        item = {}

        self.get_page(self.BASE_URLS['site'] + url)
        soup = self.get_soup()

        # Item category and name
        item['category'] = category
        item['wiki'] = self.BASE_URLS['site'] + url
        item['name'] = self.get_item_name(soup)
        item['id'] = re.sub('[^A-Za-z0-9_]+', '', item['name'].lower().replace(' ', '_'))

        # Take a screenshot of the page
        self.get_full_page_screenshot('temp/temp.png')

        # Open the screenshot and get images
        with open('temp/temp.png', 'r') as file:
            item['icon_path'] = self.get_item_icon_image(item['id'], 'temp/temp.png')
            item['infobox_path'] = self.get_item_infobox_image(item['id'], 'temp/temp.png')
            item['abilities'] = self.get_item_ability_images(item['id'], 'temp/temp.png')

        return item

    """
    Gets the display name of the Item.
    @return A String containing the Item's display name.
    """
    def get_item_name(self, soup):
        return re.sub('[^A-Za-z0-9 ]+', '', soup.find('h1', {'id': 'firstHeading'}).text)

    """
    Gets an image of the Item's icon, and returns the path to the image.
    @param id The Item's unique id.
    @param file The path to the temporary screenshot
    """
    def get_item_icon_image(self, id, file):
        icon_image = self._driver.find_element_by_xpath("//td[@id='itemmainimage']//a[@class='image']//img")

        if(icon_image != None):
            transform = self.get_element_transform(icon_image)
            
            image = Image.open(file)
            icon_crop = image.crop((transform[0], \
                                    transform[1], \
                                    transform[0] + transform[2], \
                                    transform[1] + transform[3]))

            icon_crop.save('assets/items/dota_deck_' + id + "_icon.png", 'PNG')

            return 'dota_deck_' + id + "_icon.png"

        return None


    """
    Gets an image of the Item's infobox, and returns the path to the image.
    @param id The Item's unique id.
    @param file The path to the temporary screenshot
    """
    def get_item_infobox_image(self, id, file):
        infobox_image = self._driver.find_element_by_xpath("//table[@class='infobox']")

        if(infobox_image != None):
            transform = self.get_element_transform(infobox_image)
            
            image = Image.open(file)
            icon_crop = image.crop((transform[0], \
                                    transform[1], \
                                    transform[0] + transform[2], \
                                    transform[1] + transform[3]))

            icon_crop.save('assets/items/dota_deck_' + id + "_infobox.png", 'PNG')

            return 'dota_deck_' + id + "_infobox.png"

        return None

    """
    Gets an image of the Item's abilities, and returns the path to the images.
    @param id The Item's unique id.
    @param file The path to the temporary screenshot
    """
    def get_item_ability_images(self, id, file):
        abilities = []

        elements = self._driver.find_elements_by_xpath("//div[@class='ability-background']")
        if elements != None:

            counter = 1
            for element in elements:
                temp = {}

                temp['ability_name'] = element.find_element_by_xpath("./child::*").find_element_by_xpath("./child::*").text

                transform = self.get_element_transform(element)

                image = Image.open(file)
                ability_crop = image.crop((transform[0], \
                                        transform[1], \
                                        transform[0] + transform[2], \
                                        transform[1] + transform[3]))
                
                ability_crop.save('assets/items/dota_deck_' + id + "_ability_" + str(counter) +".png", 'PNG')
                temp['ability_image_path'] = 'dota_deck_' + id + "_ability_" + str(counter) +".png"

                abilities.append(temp)

                counter = counter + 1

        return abilities

    def get_element_transform(self, element):

        location = element.location
        x = location['x']
        y = location['y']

        size = element.size
        w = size['width']
        h = size['height']

        return (x, y, w, h)

    """
    Takes a screenshot of the entire page.
    @param path The path to save the temporary image.
    """
    def get_full_page_screenshot(self, path):
        self._driver.save_screenshot(path)

    def shutdown(self):
        self._driver.quit()
