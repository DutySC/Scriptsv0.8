import NSO.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from conftest import browser_SNILS

# снилс = 764-657-726 57
# карта пациента = 11/142208

class search_patient_locators:
    LOCATOR_SEARCH_PATIENT_1 = (By.XPATH, '//span[contains(text(), "Регистратура")]')
    LOCATOR_SEARCH_PATIENT_2 = (By.XPATH, '//tbody/tr[11]/td[2]/a[1]/span[1]')
    LOCATOR_NEW_PATIENT = (By.XPATH, '//td[contains(text(), "Новый пациент")]')
    LOCATOR_LAST_NAME = (By.XPATH, '//body[1]/div[7]//div[7]/table[1]//tr[3]/td[1]//input[1]')
    LOCATOR_FIRST_NAME = (By.XPATH, '//body[1]/div[7]//div[7]/table[1]//tr[3]/td[2]//input[1]')
    LOCATOR_SURNAME = (By.XPATH, '//body[1]/div[7]//div[7]/table[1]//tr[3]/td[3]//input[1]')
    LOCATOR_BIRTHDAY = (By.XPATH, '//tbody/tr[4]/td[2]/span[1]/div[1]/div[1]/input[1]')
    LOCATOR_CARD_NUMBER = (By.XPATH, '//body[1]/div[7]//div[7]/table[1]//tr[5]/td[2]//img[1]')
    LOCATOR_SNILS = (By.XPATH, '//body[1]/div[7]//div[7]/table[1]//tr[6]/td[1]//input[1]')
    LOCATOR_ENTER_POLIS = (By.XPATH, '//body[1]/div[7]//td[1]/div[1]//div[1]/div[2]//td[2]//input[1]')
    LOCATOR_INSURANCE_COMPANY = (By.XPATH, '//body[1]/div[7]//tr[2]/td[1]//td[1]/div[1]//tr[4]//img[1]')
    LOCATOR_OBLAST_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_TYPE_OF_POLIS = (By.XPATH, '//body[1]/div[7]//div[1]/div[1]//div[1]//td[1]/div[1]/div[2]//tr[2]//img[1]')
    LOCATOR_CHOOSE_POLIS = (By.XPATH, '//span[contains(text(), "Временное свидетельство")]')
    LOCATOR_DATA_1 = (By.XPATH, '//body[1]/div[7]//div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]//tr[4]//div/div/div[1]')
    LOCATOR_DATA_2 = (By.XPATH, '//div[contains(text(), "Сегодня")]')
    LOCATOR_TAB_STATUS = (By.XPATH, '//div[contains(text(), "Соц.")]')
    LOCATOR_STATUS_OPEN = (By.XPATH, '//body[1]/div[7]//td[1]/div[1]//div[3]/div[2]//img[1]')
    LOCATOR_STATUS_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_TAB_DOCUMENTS = (By.XPATH, '//div[contains(text(),"Документы")]')
    LOCATOR_TYPE_OF_DOCUMENTS = (By.XPATH, '//body[1]/div[7]//td[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]//tr[2]//img[1]')
    LOCATOR_CHOOSE_DOCUMENT = (By.XPATH, '//span[contains(text(), "Вид на жительство")]')
    LOCATOR_DATA_3 = (By.XPATH, '//body[1]/div[7]//td[1]/div[2]//tr[4]//div/div/div[1]')
    LOCATOR_DATA_4 = (By.XPATH, '//div[contains(text(), "Сегодня")]')
    LOCATOR_WHO_GAVE = (By.XPATH, '//body[1]/div[7]//td[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]//textarea[1]')
    LOCATOR_TAB_AREAS = (By.XPATH, '//body[1]/div[7]//td[1]/div[2]/table[1]/tbody[1]/tr[1]//div[2]/div[2]')
    LOCATOR_AREA = (By.XPATH, '//body[1]/div[7]//tbody[1]/tr[2]//tr[2]/td[1]//td[1]/div[1]//tr[2]//img[1]')
    LOCATOR_AREA_DJERZINSKI = (By.XPATH, '// span[contains(text(), "Дзержинский")]')
    LOCATOR_AREA_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_ENTER_AREA_1 = (By.XPATH, '//body[1]/div[7]//tr[2]/td[1]/div[2]//td/div[1]//tr[3]//img[1]')
    LOCATOR_ENTER_AREA_2 = (By.XPATH, '//a[contains(text(), "Адыгея")]')
    LOCATOR_ENTER_AREA_3 = (By.XPATH, '//a[contains(text(), "Адыгейск")]')
    LOCATOR_ENTER_AREA_4 = (By.XPATH, '//a[contains(text(), "Абадзехская")]')
    LOCATOR_HOME = (By.XPATH, '//body[1]/div[7]//tbody[1]//tbody[1]//tbody[1]/tr[2]//tr[2]/td[1]/div[1]//tr[4]/td[2]//input[1]')
    LOCATOR_OK = (By.XPATH, '//td[contains(text(), "ОК")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_1 = (By.XPATH, '//span[contains(text(), "Еще")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_2 = (By.XPATH, '//span[contains(text(), "Словари")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_3 = (By.XPATH, '//span[contains(text(), "Контрагенты")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_4 = (By.XPATH, '//span[contains(text(), "Карты пациентов")]')
    LOCATOR_CREATE_DATA = (By.XPATH, '//body[1]/div[1]//td[7]//td[3]//img[1]')
    LOCATOR_LAST_NAME_NEWVERSION_1 = (By.XPATH, '//span[contains(text(), "Новаяверсия")]')
    LOCATOR_DELETE_USER_1 = (By.XPATH, '//body[1]/div[2]/div[2]/div[4]/table[1]/tbody[1]/tr[5]/td[2]')
    LOCATOR_DICTIONARY_INDIVIDUAL_1 = (By.XPATH, '//span[contains(text(), "Еще")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_2 = (By.XPATH, '//span[contains(text(), "Словари")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_3 = (By.XPATH, '//span[contains(text(), "Контрагенты")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_4 = (By.XPATH, '//body[1]//tr[3]//span[contains(text(), "Контрагенты")]')
    LOCATOR_HEAD = (By.XPATH, '//body//div[1]/div/div/div/div/div[3]/div[1]')
    LOCATOR_FILTER_CATALOGS_1 = (By.XPATH, '//body//div[1]/div[2]//span[contains(text(), "Показать фильтр")]')
    LOCATOR_FILTER_CATALOGS_2 = (By.XPATH, '//body[1]//div[3]/div[1]//td[4]//input[1]')
    LOCATOR_FILTER_CATALOGS_3 = (By.XPATH, '//body[1]//div[3]/div[1]//td[5]//input[1]')
    LOCATOR_FILTER_CATALOGS_4 = (By.XPATH, '//body[1]//div[3]/div[1]//td[6]//input[1]')
    LOCATOR_CATALOGS_1 = (By.XPATH, '//div[@id="TreeArea_CATALOGS_DEFAULT"]')
    LOCATOR_CATALOGS_2 = (By.XPATH, '//td[contains(text(), "Список")]')
    LOCATOR_LAST_NAME_NEWVERSION_2 = (By.XPATH, '//tbody/tr[1]/td[6]/span[1][contains(text(), "Новаяверсия")]')
    LOCATOR_DELETE_USER_2 = (By.XPATH, '//body[1]/div[2]/div[2]//td[2][contains(text(), "Удалить")]')

class search_patient(BasePage):
    def create_patient(self):
        self.find_element(search_patient_locators.LOCATOR_SEARCH_PATIENT_1).click()  # вкладка "Регистратура"
        self.find_element(search_patient_locators.LOCATOR_SEARCH_PATIENT_2).click()  # вкладка "Поиск пациентов"
        self.find_element_pb()  # прогрессбар
        time.sleep(3)  # ожидание
        self.find_element(search_patient_locators.LOCATOR_NEW_PATIENT).click()  # создание нового пациента
        self.find_element_pb()  # прогрессбар
        self.find_element_pb()  # прогрессбар
        time.sleep(5) # ожидание
        search_string_1 = self.find_element(search_patient_locators.LOCATOR_LAST_NAME)  # ввод фамилии
        search_string_1.send_keys(prm.last_name)  # указывается фамилия
        search_string_2 = self.find_element(search_patient_locators.LOCATOR_FIRST_NAME)  # ввод имени
        search_string_2.send_keys(prm.first_name)  # указывается имя
        search_string_3 = self.find_element(search_patient_locators.LOCATOR_SURNAME)  # ввод отчетсва
        search_string_3.send_keys(prm.surname)  # указывается отчетсво
        self.find_element(search_patient_locators.LOCATOR_BIRTHDAY).click() # дата рождения
        search_string_4 = self.find_element(search_patient_locators.LOCATOR_BIRTHDAY)  # дата рождения
        search_string_4.send_keys(prm.data) # указывается дата рождения
        self.find_element(search_patient_locators.LOCATOR_CARD_NUMBER).click()  # кнопка для выдачи номера карты
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_SNILS).click()  # ввод СНИЛС
        search_string_5 = self.find_element(search_patient_locators.LOCATOR_SNILS)  # ввод СНИЛС
        search_string_5.send_keys(prm.snils) # указывается статичный СНИЛС
        # search_string_5.send_keys(browser_SNILS())  # указывается динамический СНИЛС
        search_string_6 = self.find_element(search_patient_locators.LOCATOR_ENTER_POLIS)  # ввод номера полиса
        search_string_6.send_keys(prm.rand)  # указывается номер полиса
        self.find_element(search_patient_locators.LOCATOR_INSURANCE_COMPANY).click()  # окно для указания страховой компании
        self.find_element_pb()  # прогрессбар
        self.find_element_pb()  # прогрессбар
        time.sleep(2)  # ожидание
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_OBLAST_OK).click()  # кнопка "Ок"
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_TYPE_OF_POLIS).click()  # выбор вида полиса
        self.find_element(search_patient_locators.LOCATOR_TYPE_OF_POLIS).click()  # выбор вида полиса
        self.find_element(search_patient_locators.LOCATOR_CHOOSE_POLIS).click()  # указать временное свидетельство
        self.find_element(search_patient_locators.LOCATOR_DATA_1).click()  # дата выдачи
        self.find_element(search_patient_locators.LOCATOR_DATA_2).click()  # указать дату выдачи
        self.find_element(search_patient_locators.LOCATOR_TAB_STATUS).click() # вкладка Соц. статус
        self.find_element(search_patient_locators.LOCATOR_STATUS_OPEN).click() # окно выбора соц. статуса
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_STATUS_OK).click()  # подтверждения соц. статуса
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_TAB_DOCUMENTS).click()  # вкладка Документы/Адреса
        self.find_element(search_patient_locators.LOCATOR_TAB_DOCUMENTS).click()  # вкладка Документы/Адреса
        self.find_element(search_patient_locators.LOCATOR_TYPE_OF_DOCUMENTS).click()  # тип документа
        self.find_element(search_patient_locators.LOCATOR_CHOOSE_DOCUMENT).click()  # указать тип документа "Вид на жительство"
        self.find_element(search_patient_locators.LOCATOR_DATA_3).click()  # дата выдачи
        self.find_element(search_patient_locators.LOCATOR_DATA_4).click()  # указать дату выдачи
        search_string_7 = self.find_element(search_patient_locators.LOCATOR_WHO_GAVE)  # кем выдан
        search_string_7.send_keys(prm.mvd) # указать кем выдан - "МВД"
        self.find_element(search_patient_locators.LOCATOR_TAB_AREAS).click()  # подвкладка "Адреса"
        self.find_element(search_patient_locators.LOCATOR_AREA).click()  # ввод района
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_AREA_DJERZINSKI).click() #
        self.find_element(search_patient_locators.LOCATOR_AREA_OK).click()  # кнопка "Ок"
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_ENTER_AREA_1).click()  # ввод адреса
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_ENTER_AREA_2).click() # ввод адреса
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_ENTER_AREA_3).click() # ввод адреса
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_ENTER_AREA_4).click() # ввод адреса
        self.find_element_pb()  # прогрессбар
        search_string_8 = self.find_element(search_patient_locators.LOCATOR_HOME)  # выбрать дом
        search_string_8.send_keys(prm.home) # указать номер дома
        self.find_element(search_patient_locators.LOCATOR_OK).click()  # кнопка "ОК"
        self.find_element_pb()  # прогрессбар
        print('✅ Тестовый пользователь - создан') # вывод

    def delete_patient(self):
        self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_1).click() # вкладка "Еще"
        self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_2).click() # вкладка "Словари"
        self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_3).click() # вкладка "Контрагенты"
        self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_4).click() # вкладка "Карты пациентов"
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_CREATE_DATA).click() # фильтр даты создания мед. карты
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_CREATE_DATA).click() #  фильтр даты создания мед. карты
        self.find_element_pb()  # прогрессбар
        self.actionchains(search_patient_locators.LOCATOR_LAST_NAME_NEWVERSION_1).perform()  # ПКМ по имени созданного пациента
        self.find_element(search_patient_locators.LOCATOR_DELETE_USER_1).click() # кнопка "Удалить"
        self.driver.switch_to.alert.accept()  # принятие всплывающего окна
        self.find_element_pb()  # прогрессбар
        self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_1).click()  # вкладка "Еще"
        self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_2).click() # вкладка "Словари"
        self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_3).click() # вкладка "Контрагенты"
        self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_4).click() # вкладка "Контрагенты"
        try:
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
        except TimeoutException:
            time.sleep(50)
        self.find_element(search_patient_locators.LOCATOR_FILTER_CATALOGS_1).click()  # открыть поиск по фильтрам
        search_string_9 = self.find_element(search_patient_locators.LOCATOR_FILTER_CATALOGS_2) # фамилия
        search_string_9.send_keys(prm.last_name) # написать фамилию
        search_string_10 = self.find_element(search_patient_locators.LOCATOR_FILTER_CATALOGS_3) # имя
        search_string_10.send_keys(prm.first_name) # написать имя
        search_string_11 = self.find_element(search_patient_locators.LOCATOR_FILTER_CATALOGS_4) # отчество
        search_string_11.send_keys(prm.surname) # написать отчество
        self.actionchains(search_patient_locators.LOCATOR_CATALOGS_1).perform()  # ПКМ по каталогу
        self.find_element(search_patient_locators.LOCATOR_CATALOGS_2).click()  # поиск по списку
        try:
            self.find_element_pb()  # прогрессбар
        except TimeoutException:
            time.sleep(10)
        self.actionchains(search_patient_locators.LOCATOR_LAST_NAME_NEWVERSION_2).perform() # ПКМ по имени созданного пациента
        self.find_element(search_patient_locators.LOCATOR_DELETE_USER_2).click() # кнопка "Удалить"
        self.driver.switch_to.alert.accept()  # принятие всплывающего окна
        self.find_element_pb()  # прогрессбар
        print('✅ Тестовый пользователь - удален') # вывод