import io
from PIL import Image

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from . import page
from project.models import Worker
from django.urls import reverse
import time

def generate_photo_file():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return 


class UrbanTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        
        self.driver.set_window_size(1920, 1080)
        self.new_worker = Worker.objects.create(
        name = 'jan',
        surname = 'kowalski',
        profession = 'mechanik',
        age = 34,
        image = generate_photo_file()
        )
        self.new_worker.save()
        self.pk = self.new_worker.id


    def tearDown(self):
        self.driver.close()


    def test_indexpage(self):
        self.driver.get(self.live_server_url)
        index_page = page.IndexPage(self.driver)
        assert index_page.is_title_matches()
        assert index_page.is_index_heading_displayed_correctly()
        assert index_page.is_worker_heading_displayed_correctly()
        assert index_page.is_average_link_works()
        assert index_page.is_home_link_works()
        assert index_page.is_create_link_works()
        assert index_page.is_logo_link_works()

    def test_detailpage(self):
        self.driver.get(self.live_server_url + reverse('worker-detail',args=(self.pk,)))
        detail_page = page.DetailPage(self.driver)
        assert detail_page.is_title_matches()
        assert detail_page.is_worker_detail_displayed_correctly()


    def test_updatepage(self):
        self.driver.get(self.live_server_url + reverse('worker-update',args=(self.pk,)))
        update_page = page.UpdatePage(self.driver)
        assert update_page.is_update_form_works()

    def test_deletepage(self):
        self.driver.get(self.live_server_url)
        delete_page = page.DeletePage(self.driver)
        assert delete_page.is_delete_button_works()

    def test_updatepage(self):
        self.driver.get(self.live_server_url + reverse('worker-create'))
        create_page =page.CreatePage(self.driver)
        assert create_page.is_create_worker_form_works()


