
class HltvScraper:

    def __init__(self, base: str, webdriver):
        self.base = base
        self.driver = webdriver

    def opening_base(self):
        print(f"Opening {self.base}...")

        print(type(self.driver))

        self.driver.get(self.base)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()