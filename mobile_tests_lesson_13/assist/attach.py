import allure
from allure_commons.types import AttachmentType
from mobile_tests_lesson_13.assist import browserstack


def add_video_from_browserstack(browser):
    video_url = browserstack.get_video_url(browser.driver.session_id)
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
