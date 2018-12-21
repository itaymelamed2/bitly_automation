from page_objects import PageObject, PageElement
from selenium.webdriver.support.wait import WebDriverWait
import time


class HomePage(PageObject):
    _text_box = PageElement(id_='shorten_url')
    _submit_btn = PageElement(id_='shorten_btn')
    _short_link = PageElement(css='.short-url')

    def set_text_in_textbox(self, text):
        """
        :param text: the url to set in the input textbox
        """
        self._text_box = text
        time.sleep(2)

    def click_on_submit_btn(self):
        """
        Clicks on submit button
        """
        self._submit_btn.click()

    def get_short_link(self):
        """
        Wait for the short link <a href> element to load
        :return: The text value of the link
        """
        WebDriverWait(self.w, 10).until(lambda d: self._short_link and self._short_link.text)
        return self._short_link.text
