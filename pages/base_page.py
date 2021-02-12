from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://ok.ru/'

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_to_element(self, locator):
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator)).click()
        except StaleElementReferenceException:
            WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator)).click()

    def wait_visibility(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator))

    def clear_field(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator)).clear()

    def get_text(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator)).text

    def select(self, locator, value):
        select = Select(WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator)))
        return select.select_by_value(value)

    def radiobutton_status(self, locator):
        status = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator))
        status = status.is_selected()
        return status
