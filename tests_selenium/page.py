from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import IndexPageLocators, AveragePageLocators, DetailPageLocators, UpdatePageLocators, CreatePageLocators



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def fill_create_worker_form(self, name, surname, age, profession):
        self.do_clear(CreatePageLocators.NAME_FIELD)
        self.do_clear(CreatePageLocators.SURNAME_FIELD)
        self.do_clear(CreatePageLocators.AGE_FIELD)
        self.do_clear(CreatePageLocators.PROFESSION_FIELD)
        self.do_send_keys(CreatePageLocators.NAME_FIELD, name)
        self.do_send_keys(CreatePageLocators.SURNAME_FIELD, surname)
        self.do_send_keys(CreatePageLocators.AGE_FIELD, age)
        self.do_send_keys(CreatePageLocators.PROFESSION_FIELD, profession)
        self.do_click(CreatePageLocators.CREATE_BUTTON)

    


class IndexPage(BasePage):

    def is_title_matches(self):
        return 'Home | Workers' in self.driver.title

    def is_index_heading_displayed_correctly(self):
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'List of Workers'
        return text in index_heading

    def is_worker_heading_displayed_correctly(self):
        worker_heading = self.get_element_text(IndexPageLocators.WORKER_HEADING)
        text = 'Jan Kowalski'
        return text in worker_heading

    def is_average_link_works(self):
        self.do_click(IndexPageLocators.AVERAGE_LINK)
        profession_text = self.get_element_text(AveragePageLocators.PROFESSION)
        return 'mechanik' in profession_text

    def is_home_link_works(self):
        self.do_click(IndexPageLocators.HOME_LINK)
        return 'Home | Workers' in self.driver.title

    def is_create_link_works(self):
        self.do_click(IndexPageLocators.CREATE_LINK)
        return 'Create | Workers' in self.driver.title

    def is_logo_link_works(self):
        self.do_click(IndexPageLocators.LOGO_LINK)
        return 'Home | Workers' in self.driver.title

    def is_update_link_works(self):
        self.do_click(IndexPageLocators.UPDATE_LINK)
        return 'Update | Workers' in self.driver.title

class DetailPage(BasePage):

    def is_title_matches(self):
        return 'Detail | Workers' in self.driver.title

    def is_worker_detail_displayed_correctly(self):
        worker_heading = self.get_element_text(DetailPageLocators.NAME_HEADING)
        text = 'Jan'
        return text in worker_heading

class UpdatePage(BasePage):

    def is_update_form_works(self):
        self.do_clear(UpdatePageLocators.NAME_FIELD)
        self.do_send_keys(UpdatePageLocators.NAME_FIELD, 'Wojtek')
        self.do_click(UpdatePageLocators.UPDATE_BUTTON)
        worker_heading = self.get_element_text(IndexPageLocators.WORKER_HEADING)
        text = 'Wojtek Kowalski'
        return text in worker_heading

class DeletePage(BasePage):

    def is_delete_button_works(self):
        self.do_click(IndexPageLocators.DELETE_BUTTON)
        worker_headings = self.driver.find_elements_by_id('worker-detail')
        return len(worker_headings) == 0

class CreatePage(BasePage):

    def is_create_worker_form_works(self):
        self.fill_create_worker_form(
            name='maciej', 
            surname='jaroszewski',
            age=18,
            profession='player'
            )
        msg_text = self.get_element_text(CreatePageLocators.MSG_TEXT)
        return 'Worker was created successfully' in msg_text

