import pytest
import json
from pages.home_page import HomePage

with open('tests_data.json', 'r') as f:
    tests_data = json.loads(open('tests_data.json').read())


@pytest.mark.parametrize("test_url", tests_data["test_urls"])
def test_verify_shorten_link_expends_to_original_url(browser, test_url, config):
    """
    Navigate to the app website(url depends on config object). Types the test data (tested url) in the url input text
    box and clicks on submit buttons. After, get the value of the shortened link and navigate to it. Get the browser's
    current url after redirection and assert it is equal the the original url that was inserted at start.
    If not, test fails and an assertion exception is raised. The test will be executed 2 times as it parametrized with 2
    different urls.
    :param browser: a new instance as a fixture.
    :param test_url: the url to test.
    :param config: tests configurations: selenium hub server endpoint, app url and system timeout.
    """
    browser.get(config.url)
    home_page = HomePage(browser)
    home_page.set_text_in_textbox(test_url)
    home_page.click_on_submit_btn()
    shorted_link = home_page.get_short_link()

    # navigating to the shorted link
    browser.get(shorted_link)
    cur_url = browser.current_url

    assert test_url == cur_url, "Shorted link didn't redirect to expected url."
