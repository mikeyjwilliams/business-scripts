from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from time import sleep


class Base:
    def __init__(self, driver):
        self.driver = driver

    def __str__(self):
        '''
        string representation of the driver object
        '''
        return f'Driver: {self.driver}'

    def __repr__(self):
        '''
        object representation of the driver object
        '''
        return f'{self.__class__.__name__}: {self.__self.__dict__}'

    def assert_not_false(self, bool_var: bool, assertion_phrase: str = None):
        '''
        function: assert_not_false
        params:
            bool_var
            assertion_phrase
        returns:
            None
        default:
            default_phrase
        Description: assertion against {False}
            should {NOT} be {FALSE}

        if error code err[assert(01)] appears
        using assert_is_false wrong.
        '''
        DEFAULT_ASSERT_FAIL: str = 'Assertion Failed'
        if bool_var == False:
            print('-----------------------------------------------------')
            print(f'Warning assert_not_false means {bool_var} != {False}.')
            print('if seeing this something went wrong with assertion check.')
            print('err[assert(01)]')
            print('-------------------------------------------------------')
        assert bool_var != False, assertion_phrase or DEFAULT_ASSERT_FAIL

    def click(self, locator: tuple):
        '''
        function: click
        description: locator variable decides where to click
        '''
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).click()

    def get_title(self, word_in_title: str):
        '''
        function: get_title
        params:
            word_in_title
        returns:
            bool - True or False

        '''
        return WebDriverWait(self.driver, 10).until(
            EC.title_contains(word_in_title)
        )
