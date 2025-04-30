from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class WebdriverInstaller:

    @staticmethod
    def install_webdriver(browser: str):
        match browser:
            case "chrome":
                from selenium.webdriver.chrome.options import Options
                from selenium.webdriver.chrome.service import Service
                options = Options()
                # options.add_argument("--headless")

                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            case "firefox":
                from selenium.webdriver.firefox.options import Options
                from selenium.webdriver.firefox.service import Service
                
                options = Options()

                # options.add_argument("--headless")
                
                driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
            case _:
                try:
                    print("No browser selected. Trying to install Chrome...")
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                except:
                    raise Exception("No browser found. Please install Chrome or Firefox.")
    
        return driver
    