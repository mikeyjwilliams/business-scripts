from selenium import webdriver  # type: ignore
from utils import Data as URL  # type: ignore
import auto_chromedriver  # type: ignore
ac = auto_chromedriver.auto_chromedriver_installer()
ac.install()


class Browser:
    '''
    class Browser
    parameter: driver
    '''

    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def browser(self, website: str = URL.AMAZON) -> str:
        '''
        function: browser
        params: 
            self
            Browser
        returns: 
            self.driver object

        description: opens chrome browser and returns
            self.driver object
            to be called when needed.
        '''
        return self.driver.get(website)

    def close_browser(self) -> None:
        '''
        function: close_browser
        params: self

        returns: None

        description: 
            closes chrome browser
            quits chrome browser         
        '''

        self.driver.close()
        self.driver.quit()
