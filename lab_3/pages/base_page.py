import common.helpers as HL
from selenium.webdriver.common.by import By

class BasePage:
    BASE_URL = "http://demo-store.seleniumacademy.com"
    
    ACCOUNT_MENU = (By.CSS_SELECTOR, f"a[href='{BASE_URL}/customer/account/']")

    LOGIN_OPTION = (By.CSS_SELECTOR, "a[title='Log In']")
    LOGOUT_OPTION = (By.CSS_SELECTOR, "a[title='Log Out']")
    REGISTER_OPTION = (By.CSS_SELECTOR, "a[title='Register']")

    SEARCH_INPUT = (By.ID, "search")
    SEARCH_AUTOCOMPLETE = (By.ID, "search_autocomplete")
    SEARCH_AUTOCOMPLETE_OPTION = (By.XPATH, '//*[@id="search_autocomplete"]//li[@title]')
    
    PAGE_TITLE = (By.XPATH, '//div[contains(@class, "page-title")]/h1')

    SUBCATEGORY_XPATH = '//a[contains(@class, "level1")]'

    WOMEN_TAB_XPATH = '//*[@id="nav"]//*[contains(@class, "level0")][contains(text(),"Women")]'
    WOMEN_TAB = (By.XPATH, WOMEN_TAB_XPATH)
    WOMEN_TAB_SUBCATEGORY = (By.XPATH, f'{WOMEN_TAB_XPATH}/following-sibling::ul{SUBCATEGORY_XPATH}')

    MEN_TAB_XPATH = '//*[@id="nav"]//*[contains(@class, "level0")][contains(text(),"Men")]'
    MEN_TAB = (By.XPATH, MEN_TAB_XPATH)
    MEN_TAB_SUBCATEGORY = (By.XPATH, f'{MEN_TAB_XPATH}/following-sibling::ul{SUBCATEGORY_XPATH}')

    ACCESSORIES_TAB_XPATH = '//*[@id="nav"]//*[contains(@class, "level0")][contains(text(),"Accessories")]'
    ACCESSORIES_TAB = (By.XPATH, ACCESSORIES_TAB_XPATH)
    ACCESSORIES_TAB_SUBCATEGORY = (By.XPATH, f'{ACCESSORIES_TAB_XPATH}/following-sibling::ul{SUBCATEGORY_XPATH}')
    
    HOME_DECOR_TAB_XPATH = '//*[@id="nav"]//*[contains(@class, "level0")][contains(text(),"Home & Decor")]'
    HOME_DECOR_TAB = (By.XPATH, HOME_DECOR_TAB_XPATH)
    HOME_DECOR_TAB_SUBCATEGORY = (By.XPATH, f'{HOME_DECOR_TAB_XPATH}/following-sibling::ul{SUBCATEGORY_XPATH}')

    SALE_TAB_XPATH = '//*[@id="nav"]//*[contains(@class, "level0")][contains(text(),"Sale")]'
    SALE_TAB = (By.XPATH, SALE_TAB_XPATH)
    SALE_TAB_SUBCATEGORY = (By.XPATH, f'{SALE_TAB_XPATH}/following-sibling::ul{SUBCATEGORY_XPATH}')

    VIP_TAB_XPATH = '//*[@id="nav"]//*[contains(@class, "level0")][contains(text(),"VIP")]'
    VIP_TAB = (By.XPATH, VIP_TAB_XPATH)
    VIP_TAB_SUBCATEGORY = (By.XPATH, f'{VIP_TAB_XPATH}/following-sibling::ul{SUBCATEGORY_XPATH}')

    SEARCH_FILTERS = (By.XPATH, '//*[@id="narrow-by-list"]/dd//a')

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.BASE_URL)

    def select_option(self, option_locator) -> None:
        HL.click_button(self.ACCOUNT_MENU, self.browser)
        HL.click_button(option_locator, self.browser)
    
    def select_tab(self, tab_locator) -> None:
        HL.click_button(tab_locator, self.browser)
    
    def search_page_title(self) -> str:
        return HL.get_element(BasePage.PAGE_TITLE, self.browser).text