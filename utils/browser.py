from selenium import webdriver


class Browser:
    '''
    class Browser
    parameter: driver
    '''

    def __init__(self):
        self.driver = webdriver.Chrome()

    def browser(self):
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
        return self.driver

    def close_browser(self):
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
