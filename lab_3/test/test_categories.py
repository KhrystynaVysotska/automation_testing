import unittest
import common.helpers as HL
from common.browser import Browser
from pages.base_page import BasePage


class CategoriesTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser().get()
        self.main_page = BasePage(self.browser)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_should_succeed_when_user_can_navigate_to_women_category(self):
        self.main_page.open()
        
        self.main_page.select_tab(BasePage.WOMEN_TAB)
        
        actual_url = self.browser.current_url
        expected_url = f"{BasePage.BASE_URL}/women.html"
        self.assertEqual(actual_url, expected_url)

        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "WOMEN")
    
    def test_should_succeed_when_women_category_has_clickable_subcategories(self):
        self.main_page.open()

        HL.hover_element(BasePage.WOMEN_TAB, self.browser)
        subcategories = HL.get_elements(BasePage.WOMEN_TAB_SUBCATEGORY, self.browser)
        
        for subcategory in subcategories:
            self.assertTrue(HL.is_clickable(subcategory, self.browser))
        
        actual_subcategories = list(map(lambda option: option.text, subcategories))
        expected_subcategories = ["View All Women", "New Arrivals", "Tops & Blouses", "Pants & Denim", "Dresses & Skirts"]
        self.assertEqual(actual_subcategories, expected_subcategories)

    def test_should_succeed_when_user_can_navigate_to_men_category(self):
        self.main_page.open()
        
        self.main_page.select_tab(BasePage.MEN_TAB)
        
        actual_url = self.browser.current_url
        expected_url = f"{BasePage.BASE_URL}/men.html"
        self.assertEqual(actual_url, expected_url)

        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "MEN")
    
    def test_should_succeed_when_men_category_has_clickable_subcategories(self):
        self.main_page.open()

        HL.hover_element(BasePage.MEN_TAB, self.browser)
        subcategories = HL.get_elements(BasePage.MEN_TAB_SUBCATEGORY, self.browser)
        
        for subcategory in subcategories:
            self.assertTrue(HL.is_clickable(subcategory, self.browser))
        
        actual_subcategories = list(map(lambda option: option.text, subcategories))
        expected_subcategories = ["View All Men", "New Arrivals", "Shirts", "Tees, Knits and Polos", "Pants & Denim", "Blazers"]
        self.assertEqual(actual_subcategories, expected_subcategories)
    
    def test_should_succeed_when_user_can_navigate_to_accessories_category(self):
        self.main_page.open()
        
        self.main_page.select_tab(BasePage.ACCESSORIES_TAB)
        
        actual_url = self.browser.current_url
        expected_url = f"{BasePage.BASE_URL}/accessories.html"
        self.assertEqual(actual_url, expected_url)

        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "ACCESSORIES")

    def test_should_succeed_when_accessories_category_has_clickable_subcategories(self):
        self.main_page.open()

        HL.hover_element(BasePage.ACCESSORIES_TAB, self.browser)
        subcategories = HL.get_elements(BasePage.ACCESSORIES_TAB_SUBCATEGORY, self.browser)
        
        for subcategory in subcategories:
            self.assertTrue(HL.is_clickable(subcategory, self.browser))
        
        actual_subcategories = list(map(lambda option: option.text, subcategories))
        expected_subcategories = ["View All Accessories", "Eyewear", "Jewelry", "Shoes", "Bags & Luggage"]
        self.assertEqual(actual_subcategories, expected_subcategories)

    def test_should_succeed_when_user_can_navigate_to_home_and_decor_category(self):
        self.main_page.open()
        
        self.main_page.select_tab(BasePage.HOME_DECOR_TAB)
        
        actual_url = self.browser.current_url
        expected_url = f"{BasePage.BASE_URL}/home-decor.html"
        self.assertEqual(actual_url, expected_url)

        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "HOME & DECOR")

    def test_should_succeed_when_home_and_decor_category_has_clickable_subcategories(self):
        self.main_page.open()

        HL.hover_element(BasePage.HOME_DECOR_TAB, self.browser)
        subcategories = HL.get_elements(BasePage.HOME_DECOR_TAB_SUBCATEGORY, self.browser)
        
        for subcategory in subcategories:
            self.assertTrue(HL.is_clickable(subcategory, self.browser))
        
        actual_subcategories = list(map(lambda option: option.text, subcategories))
        expected_subcategories = ["View All Home & Decor", "Books & Music", "Bed & Bath", "Electronics", "Decorative Accents"]
        self.assertEqual(actual_subcategories, expected_subcategories)
    
    def test_should_succeed_when_user_can_navigate_to_sale_category(self):
        self.main_page.open()
        
        self.main_page.select_tab(BasePage.SALE_TAB)
        
        actual_url = self.browser.current_url
        expected_url = f"{BasePage.BASE_URL}/sale.html"
        self.assertEqual(actual_url, expected_url)

        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "SALE")

    def test_should_succeed_when_sale_category_has_clickable_subcategories(self):
        self.main_page.open()

        HL.hover_element(BasePage.SALE_TAB, self.browser)
        subcategories = HL.get_elements(BasePage.SALE_TAB_SUBCATEGORY, self.browser)
        
        for subcategory in subcategories:
            self.assertTrue(HL.is_clickable(subcategory, self.browser))
        
        actual_subcategories = list(map(lambda option: option.text, subcategories))
        expected_subcategories = ["View All Sale", "Women", "Men", "Accessories", "Home & Decor"]
        self.assertEqual(actual_subcategories, expected_subcategories)

    def test_should_succeed_when_user_can_navigate_to_vip_category(self):
        self.main_page.open()
        
        self.main_page.select_tab(BasePage.VIP_TAB)
        
        actual_url = self.browser.current_url
        expected_url = f"{BasePage.BASE_URL}/vip.html"
        self.assertEqual(actual_url, expected_url)

        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "VIP")

    def test_should_succeed_when_vip_category_has_no_subcategories(self):
        self.main_page.open()

        HL.hover_element(BasePage.VIP_TAB, self.browser)
        subcategories = HL.get_elements(BasePage.VIP_TAB_SUBCATEGORY, self.browser)
        
        self.assertEqual(subcategories, [])

    def test_should_succeed_when_search_input_has_clickable_autocompletion(self):
        self.main_page.open()

        HL.insert_input(BasePage.SEARCH_INPUT, "skirt", self.browser)
        
        autocomplete_options = HL.get_elements(BasePage.SEARCH_AUTOCOMPLETE_OPTION, self.browser)
        
        for option in autocomplete_options:
            self.assertTrue(HL.is_clickable(option, self.browser))

        actual_options = list(map(lambda option: option.get_attribute("title"), autocomplete_options))
        self.assertEqual(actual_options, ["skirt", "skirts"])
    
    def test_should_succeed_when_search_by_material_denim(self):
        self.main_page.open()

        HL.insert_input(BasePage.SEARCH_INPUT, "denim", self.browser)
        HL.click_enter(BasePage.SEARCH_INPUT, self.browser)
        
        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "SEARCH RESULTS FOR 'DENIM'")

        search_filters = HL.get_elements(BasePage.SEARCH_FILTERS, self.browser)
        
        for filter in search_filters:
            self.assertTrue(HL.is_clickable(filter, self.browser))

        actual_search_filters = list(map(lambda filter: filter.text, search_filters))
        self.assertEqual(actual_search_filters, ["Women (1)", "Men (1)"])

    def test_should_succeed_when_search_by_clother_type_shirt(self):
        self.main_page.open()

        HL.insert_input(BasePage.SEARCH_INPUT, "shirt", self.browser)
        HL.click_enter(BasePage.SEARCH_INPUT, self.browser)
        
        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "SEARCH RESULTS FOR 'SHIRT'")

        search_filters = HL.get_elements(BasePage.SEARCH_FILTERS, self.browser)
        
        for filter in search_filters:
            self.assertTrue(HL.is_clickable(filter, self.browser))

        actual_search_filters = list(map(lambda filter: filter.text, search_filters))
        self.assertEqual(actual_search_filters, ["Men (3)"])

    def test_should_succeed_when_search_by_color_black(self):
        self.main_page.open()

        HL.insert_input(BasePage.SEARCH_INPUT, "black", self.browser)
        HL.click_enter(BasePage.SEARCH_INPUT, self.browser)
        
        actual_page_title = self.main_page.search_page_title()
        self.assertEqual(actual_page_title, "SEARCH RESULTS FOR 'BLACK'")

        search_filters = HL.get_elements(BasePage.SEARCH_FILTERS, self.browser)
        
        for filter in search_filters:
            self.assertTrue(HL.is_clickable(filter, self.browser))

        actual_search_filters = list(map(lambda filter: filter.text, search_filters))
        self.assertEqual(actual_search_filters, ["Women (2)", "Men (3)", "Accessories (4)"])