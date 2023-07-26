from selene import have, be
from selene.support.shared import browser
from allure import step as title


def test_search():
    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('BrowserStack')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Software company based in India»').should(be.visible)


def test_search_with_tap_delete_text():
    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('Appium')
    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Automation for Apps»').should(be.visible)
    with title('Verify content after tap for delete text'):
        browser.element('#search_close_btn').tap()
        browser.element('#search_src_text').should(have.text('Search…'))
        browser.all('#page_list_item_title').should(have.size(0))
