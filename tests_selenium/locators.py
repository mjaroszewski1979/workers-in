from selenium.webdriver.common.by import By


class IndexPageLocators(object):
    
    INDEX_HEADING = (By.ID, 'index-heading')
    WORKER_HEADING = (By.ID, 'worker-detail')
    AVERAGE_LINK = (By.ID, 'average-link')
    HOME_LINK = (By.ID, 'home-link')
    CREATE_LINK = (By.ID, 'create-link')
    LOGO_LINK = (By.ID, 'logo-link')
    UPDATE_LINK = (By.ID, 'worker-update')
    DELETE_BUTTON = (By.ID, 'worker-delete')

class AveragePageLocators(object):

    PROFESSION = (By.ID, 'profession')

class DetailPageLocators(object):

    NAME_HEADING = (By.ID , 'worker-name')

class UpdatePageLocators(object):

    NAME_FIELD = (By.NAME, 'name')
    UPDATE_BUTTON = (By.ID, 'update-button')

class CreatePageLocators(object):

    NAME_FIELD = (By.NAME, 'name')
    SURNAME_FIELD = (By.NAME, 'surname')
    AGE_FIELD = (By.NAME, 'age')
    PROFESSION_FIELD = (By.NAME, 'profession')
    CREATE_BUTTON = (By.ID, 'create-button')
    MSG_TEXT = (By.ID, 'message-text')




