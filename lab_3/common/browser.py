from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    def __init__(self):
        self.browser = None

    def get(self):
        if not self.browser:
            self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
        return self.browser

    def quit(self):
        self.browser.quit()