import requests

import config


def get_video_url(session_id):
    session = requests.get(f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
                           auth=(config.settings.userName, config.settings.accessKey)).json()
    video_url = session['automation_session']['video_url']
    return video_url
