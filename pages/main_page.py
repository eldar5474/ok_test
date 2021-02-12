from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OkSettingLocators:
    LOCATOR_TEXT_FIELD = {"Логин": (By.XPATH, '//input[@id="field_email"]'),
                          "Пароль": (By.XPATH, '//input[@id="field_password"]'),
                          "Имя": (By.XPATH, '//input[@id="field_name"]'),
                          "Фамилия": (By.XPATH, '//input[@id="field_surname"]'),
                          "Город проживания": (By.XPATH, '//input[@id="field_citySugg_SearchInput"]'),
                          "Родной город": (By.XPATH, '//input[@id="field_cityBSugg_SearchInput"]')}
    LOCATOR_BUTTON = {"Войти в Одноклассники": (By.XPATH, '//input[@value="Войти в Одноклассники"]'),
                      "Мои настройки": (By.XPATH, '//div[text() = "Мои настройки"]'),
                      "Основные": (By.XPATH, '//div[text() = "Основные"]'),
                      "Редактировать личные данные": (By.XPATH, '//div[text() = "Личные данные"]'),
                      "Сохранить": (By.XPATH, '//input[@value="Сохранить"]')}
    LOCATOR_TITLE = {"Основное": (By.XPATH, '//div[text() = "Основное"]'),
                     "Изменить личные данные": (By.XPATH, '//div[text() = "Изменить личные данные"]'),
                     "Личные данные": (By.XPATH, '//div[text()="Личные данные"]/following-sibling::div/div'),
                     "Имя и фамилия на главной": (By.XPATH, '//div[@class="tico ellip"]'),
                     "Ваши настройки сохранены": (By.XPATH, '//div[text() = "Ваши настройки сохранены"]'),
                     "Имя": (By.XPATH, '//label[@for="field_name"]'),
                     "Фамилия": (By.XPATH, '//label[@for="field_surname"]'),
                     "Дата рождения": (By.XPATH, '//label[@for="field_bday"]'),
                     "Пол": (By.XPATH, '//label[@for="field_gender"]'),
                     "Город проживания": (By.XPATH, '//label[@for="field_citySugg_SearchInput"]'),
                     "Родной город": (By.XPATH, '//label[@for="field_cityBSugg_SearchInput"]')}
    LOCATOR_DROP_DOWN = {"День рождения": (By.XPATH, '//select[@id="field_bday"]'),
                         "Месяц рождения": (By.XPATH, '//select[@id="field_bmonth"]'),
                         "Год рождения": (By.XPATH, '//select[@id="field_byear"]')}
    LOCATOR_RADIOBUTTON = {"Пол мужской": (By.XPATH, '//input[@id="field_gender_1"]'),
                           "Пол женский": (By.XPATH, '//input[@id="field_gender_2"]')}
    LOCATOR_ERROR = {"Ошибка на пустое поле Имя": (By.XPATH, '//input[@id="field_name"]/../following-sibling::span'),
                     "Ошибка на пустое поле Фамилия": (
                         By.XPATH, '//input[@id="field_surname"]/../following-sibling::span'),
                     "Ошибка на пустое поле Город проживания": (
                         By.XPATH, '//div[@id="citySugg_InputContainer"]/../following-sibling::span'),
                     "Ошибка на не выбранный День рождения": (By.XPATH, '//div[@data-l="t,birthday"]/span[text()]'),
                     "Ошибка на частую смену имени": (By.XPATH, '//div[@id="notifyPanel_msg"]')}


class OkSetting(BasePage):
    def input_field(self, field, value):
        field = self.find_element(OkSettingLocators.LOCATOR_TEXT_FIELD[field])
        field.click()
        field.send_keys(value)
        return field

    def press_button(self, button_name):
        self.click_to_element(OkSettingLocators.LOCATOR_BUTTON[button_name])

    def element_visibility(self, element_name, element_type):
        element_dict = {"Заголовок": OkSettingLocators.LOCATOR_TITLE,
                        "Поле": OkSettingLocators.LOCATOR_TEXT_FIELD,
                        "Ошибка": OkSettingLocators.LOCATOR_ERROR}
        element = self.wait_visibility(element_dict[element_type][element_name])
        error_message = f'Элемент "{element}" не найден на странице'
        assert element, error_message

    def clear_text_field(self, field_name):
        clear_field = self.clear_field(OkSettingLocators.LOCATOR_TEXT_FIELD[field_name])
        return clear_field

    def verification_personal_data(self, variable, value, location):

        if variable == "Имя":
            name = self.get_text(OkSettingLocators.LOCATOR_TITLE[location]).split()[0]
            error_message = f'Имя {value} не совпадает с именем {name} найденным по локатору'
            assert value == name, error_message
        elif variable == "Фамилия":
            surname = self.get_text(OkSettingLocators.LOCATOR_TITLE[location]).split()[1]
            surname = surname.replace(',', '')
            error_message = f'Фамилия {value} не совпадает с фамилией {surname} найденной по локатору'
            assert value == surname, error_message
        elif variable == "День рождения":
            birthday = self.get_text(OkSettingLocators.LOCATOR_TITLE[location]).split()[3]
            error_message = f'День рождения {value} не совпадает с днем рождения {birthday} найденной по локатору'
            assert value == birthday, error_message
        elif variable == "Месяц рождения":
            month_dict = {"1": "января", "2": "февраля", "3": "марта", "4": "апреля", "5": "мая", "6": "июня",
                          "7": "июля", "8": "августа", "9": "сентября", "10": "октября", "11": "ноября",
                          "12": "декабря"}
            month = self.get_text(OkSettingLocators.LOCATOR_TITLE[location]).split()[4]
            error_message = f'Месяц рождения {value} не совпадает с днем рождения {month} найденной по локатору'
            assert month_dict[value] == month, error_message
        elif variable == "Год рождения":
            year = self.get_text(OkSettingLocators.LOCATOR_TITLE[location]).split()[5]
            year = year.replace(',', '')
            error_message = f'Год рождения {value} не совпадает с годом рождения {year} найденной по локатору'
            assert value == year, error_message
        elif variable == "Город проживания":
            city = self.get_text(OkSettingLocators.LOCATOR_TITLE[location]).split()[13]
            error_message = f'Год рождения {value} не совпадает с годом рождения {city} найденной по локатору'
            assert value == city, error_message
        elif variable == "Признак пола":
            gender_dict = {"Пол мужской": "родился", "Пол женский": "родилась"}
            gender = self.get_text(OkSettingLocators.LOCATOR_TITLE[location]).split()[2]
            error_message = f'Год рождения {value} не совпадает с годом рождения {gender} найденной по локатору'
            assert gender_dict[value] == gender, error_message

    def drop_drown_select(self, value, field_name):
        self.select(locator=OkSettingLocators.LOCATOR_DROP_DOWN[field_name], value=value)

    def update_drop_down_select(self, field, value):
        field = self.find_element(OkSettingLocators.LOCATOR_TEXT_FIELD[field])
        field.click()
        field.send_keys(value)
        path = '//div[@class="caption"]/div[text() = "variable"]'
        path = path.replace('variable', value)
        variable = self.find_element((By.XPATH, path))
        variable.click()

    def status_radiobutton(self, radiobutton_name):
        status_radiobutton = self.radiobutton_status(OkSettingLocators.LOCATOR_RADIOBUTTON[radiobutton_name])
        message = 'Чекбокс не активирован'
        assert status_radiobutton, message

    def checked_radiobutton(self, radiobutton_name):
        self.click_to_element(OkSettingLocators.LOCATOR_RADIOBUTTON[radiobutton_name])

    def compare_text(self, text, element_type, locator_name):
        element_dict = {"Заголовок": OkSettingLocators.LOCATOR_TITLE,
                        "Ошибка": OkSettingLocators.LOCATOR_ERROR}
        locator_text = self.get_text(element_dict[element_type][locator_name])
        error_message = f'Текст {text} не совпадет с текстом {locator_text} найденным по локатору'
        assert text == locator_text, error_message
