import os
import secrets
import sys
import uuid
from os import name
import colorama, threading, requests, time, random, stdiomask
from string import ascii_uppercase
from datetime import datetime
import json


good = f'[{colorama.Fore.GREEN}SUCCESS{colorama.Fore.RESET}]'
inpt = f'[{colorama.Fore.YELLOW}INPUT{colorama.Fore.RESET}]'
rprtng = f'[{colorama.Fore.LIGHTMAGENTA_EX}REPORTING{colorama.Fore.RESET}]'


reports = 0
reporterr = 0
reportSleep = 2
reportType = 0
reportWay = 0

location = ''
is_post = False
tag = ''
mediaid = ''

reportData = {}
reportData['spam'] = 1
reportData['self'] = 2
reportData['sale'] = 3
reportData['fraud'] = 3
reportData['nudity'] = 4
reportData['violent'] = 5
reportData['hate'] = 6
reportData['bully'] = 7
reportData['underage'] = 11

username = ''
passwd = ''

targetUsn = ''
targetID= ''

storiesArray = []
postsArray = []
highlightsArray = []

rprtSe = requests.session()



def auth():
    clearS()
    login()

def reportAccount(id):
    global rprtSe
    data = f"source_name=&reason_id={reportType}&frx_context="
    k = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54",
        "Host": "i.instagram.com",
        'cookie': "sessionid=" + rprtSe.cookies.get_dict()['sessionid'] ,
        "X-CSRFToken": "uNs1OZ6CPvJBSmmQOvWDKGFkm2frIDEY",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
    k2 = requests.post(f"https://i.instagram.com/users/{id}/flag/", headers=k, data=data)
    if k2.status_code == 404:
        print(f'\n{good} Banned @{str(targetUsn)} After {str(reports)} Reports')
        input('')
        quit()

def _send(url, data=None, post=True):
    headers = {
        'Cookie': 'sessionid=' + rprtSe.cookies.get_dict()['sessionid'],
        'User-Agent': 'Instagram 184.0.0.30.117 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 285855788)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    if post:
        res = requests.post(url, headers=headers, data=data)
    else:
        res = requests.get(url, headers=headers)
    return res

def select_multiple(first_tag, second_tag):
    global reports, reporterr
    url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/'
    if is_post:
        params = '%7B%22client_input_params%22%3A%7B%22tags%22%3A%7B%220%22%3A%22' + second_tag + '%22%2C%221%22%3A%22' + first_tag + '%22%7D%7D%2C%22server_params%22%3A%7B%22is_bloks%22%3A1%2C%22tag_source%22%3A%22tag_selection_screen%22%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_feed%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22bbd670bb-859d-4434-ba1b-e0a5ba294acd%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22' + first_tag + '%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22media_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + mediaid + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400363363986%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841401880492760%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22feed_timeline%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22184.0.0.30.117%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22inventory_source%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22media_or_ad%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22tag_source%5C%5C%5C%22%3A%5C%5C%5C%22tag_selection_screen%5C%5C%5C%22%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22feed_timeline%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%228504bbe4-897d-42c5-a42c-60932a0d0072%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D%7D'
    else:
        params = '%7B%22client_input_params%22%3A%7B%22tags%22%3A%7B%220%22%3A%22' + second_tag + '%22%2C%221%22%3A%22' + first_tag + '%22%7D%7D%2C%22server_params%22%3A%7B%22is_bloks%22%3A1%2C%22tag_source%22%3A%22tag_selection_screen%22%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_story%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%2295d9e95b-20c9-49d5-8153-b804ccbb26b8%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22' + first_tag + '%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22media_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + mediaid + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400363363986%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841401880492760%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22reel_feed_timeline%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22184.0.0.30.117%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22tag_source%5C%5C%5C%22%3A%5C%5C%5C%22tag_selection_screen%5C%5C%5C%22%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22reel_feed_timeline%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22665891ac-1572-487c-9655-272104c89ef9%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D%7D'
    data = 'params=' + params + '&_uuid=a4b3a866-b663-4fce-9dec-6b5f7e8bf9a5&bk_client_context=%7B%22bloks_version%22%3A%22befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30%22%2C%22styles_id%22%3A%22instagram%22%7D&nest_data_manifest=true&bloks_versioning_id=befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30'
    res = _send(url, data)
    if res.status_code == 200:
        reports += 1
    else:
        reporterr += 1


def send_report(tag):
    global reports, reporterr
    url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/'
    if is_post:
        params = '%7B%22server_params%22%3A%7B%22selected_option%22%3A%22report%22%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_feed%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%226865bcee-2311-4dbd-88d4-7dcedef57234%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22' + tag + '%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22media_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + mediaid + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400363363986%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841401175190745%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22feed_timeline%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22184.0.0.30.117%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22inventory_source%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22media_or_ad%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22tag_source%5C%5C%5C%22%3A%5C%5C%5C%22tag_selection_screen%5C%5C%5C%22%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22feed_timeline%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22d293c6ca-01ae-424a-bfac-b070f9683119%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D%7D'
    else:
        params = '%7B%22server_params%22%3A%7B%22selected_option%22%3A%22report%22%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_story%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22e5e4a6f6-b4ad-4a46-9f2b-18ced58703ef%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22' + tag + '%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22media_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + mediaid + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400363363986%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841401175190745%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22reel_feed_timeline%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22184.0.0.30.117%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22tag_source%5C%5C%5C%22%3A%5C%5C%5C%22tag_selection_screen%5C%5C%5C%22%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22reel_feed_timeline%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%2283519563-16da-460d-aca5-2a49c0d927ce%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D%7D'
    data = 'params=' + params + '&_uuid=a4b3a866-b663-4fce-9dec-6b5f7e8bf9a5&bk_client_context=%7B%22bloks_version%22%3A%22befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30%22%2C%22styles_id%22%3A%22instagram%22%7D&nest_data_manifest=true&bloks_versioning_id=befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30'
    res = _send(url, data)
    if res.status_code == 200:
        reports += 1
    else:
        reporterr += 1

def select_option(has_multiple=False, param='', second_tag=''):
    global reports
    url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/'
    if is_post:
        params = '%7B%22client_input_params%22%3A%7B%22tags%22%3A%5B%22' + param + '%22%5D%7D%2C%22server_params%22%3A%7B%22show_tag_search%22%3A1%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_feed%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22ac3b7f38-0b70-4ff3-a60b-b8cc7b70727e%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22media_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + mediaid + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400363363986%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841401175190745%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22feed_timeline%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22184.0.0.30.117%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22inventory_source%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22media_or_ad%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22feed_timeline%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22f347ddd0-50b6-4d93-bc51-ca8ffda344a0%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%2C%22is_bloks%22%3A1%2C%22tag_source%22%3A%22tag_selection_screen%22%7D%7D'
    else:
        params = '%7B%22client_input_params%22%3A%7B%22tags%22%3A%5B%22' + param + '%22%5D%7D%2C%22server_params%22%3A%7B%22show_tag_search%22%3A1%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_story%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22e5e4a6f6-b4ad-4a46-9f2b-18ced58703ef%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22media_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + mediaid + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400363363986%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841401175190745%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22reel_feed_timeline%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22184.0.0.30.117%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22reel_feed_timeline%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%2283519563-16da-460d-aca5-2a49c0d927ce%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%2C%22is_bloks%22%3A1%2C%22tag_source%22%3A%22tag_selection_screen%22%7D%7D'
    data = 'params=' + params + '&_uuid=a4b3a866-b663-4fce-9dec-6b5f7e8bf9a5&bk_client_context=%7B%22bloks_version%22%3A%22befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30%22%2C%22styles_id%22%3A%22instagram%22%7D&nest_data_manifest=true&bloks_versioning_id=befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30'
    res = _send(url, data)
    if res.status_code == 200:
        if has_multiple:
            select_multiple(param, second_tag)
        else:
            send_report(param)


def getTag():
    global tag
    if reportType == 1:
        tag = 'ig_spam_v3'
    elif reportType == 2:
        tag = 'ig_self_injury_v3'
    elif reportType == 3:
        tag = 'ig_drugs_v3'
    elif reportType == 4:
        tag = 'ig_nudity_or_pornography_v3'
    elif reportType == 5:
        tag = 'ig_dangerous_org_or_individual'
    elif reportType == 6:
        tag = 'ig_hate_speech_v3'
    elif reportType == 7:
        tag = 'ig_bullying_or_harassment_me_v3'
def reportPostStory(postOrNot : bool, mediaID):
    global mediaid, location
    mediaid = mediaID
    if postOrNot:
        location = 'ig_feed'
    else:
        location = 'ig_story'
    url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.ig.ixt.triggers.bottom_sheet.ig_content/'
    params = 'logging_extra=%7B%22inventory_source%22%3A%22media_or_ad%22%7D&trigger_event_type=ig_report_button_clicked&trigger_session_id=d293c6ca-01ae-424a-bfac-b070f9683119&ig_container_module=feed_timeline&entry_point=chevron_button&_uuid=a4b3a866-b663-4fce-9dec-6b5f7e8bf9a5&ig_object_value=' + mediaid + '&ig_object_type=1&is_in_holdout=0&bk_client_context=%7B%22bloks_version%22%3A%22befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30%22%2C%22styles_id%22%3A%22instagram%22%7D&nest_data_manifest=true&bloks_versioning_id=befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30&location=' + location
    res = _send(url, params)
    if res.status_code == 200:
        select_option(False, tag)


def clearS():
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(f'{good} plvq5 Report Bot v2 | @plvq5 \n')

def getPosts():
    global rprtSe
    woow = []
    headers = {
        'User-Agent': 'Instagram 177.0.0.30.119 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)',
    }
    response = requests.get("https://i.instagram.com/api/v1/feed/user/" + targetID + "/", headers=headers, cookies=rprtSe.cookies.get_dict())
    if response.status_code == 200:
        for item in response.json()['items']:
            woow.append(item['pk'])
        print(f'{good} Fetched {len(woow)} Posts For {targetUsn}')
        return woow
    else:
        print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] Error Fetching Posts')

def getStories():
    global rprtSe
    kaka = []
    headers = {
        'User-Agent': 'Instagram 177.0.0.30.119 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)',
    }
    response = requests.get("https://i.instagram.com/api/v1/feed/user/" + targetID + "/story/", headers=headers, cookies=rprtSe.cookies.get_dict())
    if response.status_code == 200:
        for item in response.json()['reel']['items']:
            kaka.append(item['pk'])
        print(f'{good} Fetched {len(kaka)} Stories For {targetUsn}')
        return kaka
    else:
        print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] Error Fetching Stories')

def getHighlights():
    global rprtSe
    media_ids = []
    headers = {
        'User-Agent': 'Instagram 177.0.0.30.119 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)',
    }
    response = requests.get("https://i.instagram.com/api/v1/highlights/" + targetID + "/highlights_tray/", headers=headers, cookies=rprtSe.cookies.get_dict())
    if response.status_code == 200:
        try:
            data = json.loads(response.text)
            ids = [element['id'] for element in data['tray']]
            if not ids:
                print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] Error Fetching Highlights')
            ids=[i.strip('highlight:') for i in ids]
            for hid in ids:
                response = requests.get("https://i.instagram.com/api/v1/feed/reels_media/?user_ids=highlight:" + str(hid), headers=headers, cookies=rprtSe.cookies.get_dict())
                hdata = json.loads(response.text)
                media_ids.extend(hdata['reels']['highlight:'+hid]['media_ids'])

            print(f'{good} Fetched {len(media_ids)} Stories For {targetUsn}')
            return media_ids
        except Exception as e:
            print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] Error Fetching Highlights')
            print(e)
    else:
        print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] Error Fetching Highlights')


def randGenStr(length : int):
    kStr = ''
    for i in range(length):
        kStr += f'{random.choice(ascii_uppercase)}'
    return kStr.lower()

def getID():
    global targetID, storiesArray, postsArray
    try:
        checkReq = rprtSe.get(f'https://instagram.com/{str(targetUsn)}/?__a=1').json()
        targetID = checkReq['logging_page_id'].split('_')[1]
        print(f"\n{good} {targetUsn}'s UserID is {targetID}")
    except:
        print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] Invalid Report Target')
        time.sleep(1)
        getReports()

def getReportType():
    global rprtSe
    global reportWay, targetUsn, reports, reporterr
    clearS()
    reports = 0
    reporterr = 0
    askStuff = f'''[{colorama.Fore.GREEN}1{colorama.Fore.RESET}] Profile
[{colorama.Fore.GREEN}2{colorama.Fore.RESET}] Stories
[{colorama.Fore.GREEN}3{colorama.Fore.RESET}] Posts
[{colorama.Fore.GREEN}4{colorama.Fore.RESET}] Highlights'''
    print(askStuff)
    repR = int(input(f'\n{inpt} Report: '))
    if repR == 1:
        targetUsn = input(f'{inpt} Target To Report: ')
        getID()
        sys.stdout.write('\n')
        while True:
            reportAccount(targetID)
            reports += 1
            sys.stdout.write(f"\r{good} Sent Reports: {str(reports)} | Reporting: @{targetUsn}'s Profile | 5s Rest Between Reports")
            time.sleep(1)
    elif repR == 2:
        targetUsn = input(f'{inpt} Target To Report: ')
        getID()
        getTag()
        storiesArray = getStories()
        sys.stdout.write('\n')
        for i in storiesArray:
            i = str(i)
            reportPostStory(False, i)
            sys.stdout.write(f"\r{good} Sent Reports: {str(reports)} | Errors: {str(reporterr)} | Reporting: @{targetUsn}'s Stories")
            time.sleep(1)
        sys.stdout.write(f"\n\n{good} Finished Reporting @{targetUsn}'s Stories, Reported {str(reports)} Stories")
        time.sleep(1)
        getReports()
    elif repR == 3:
        targetUsn = input(f'{inpt} Target To Report: ')
        getID()
        getTag()
        postsArray = getPosts()
        sys.stdout.write('\n')
        for i in postsArray:
            i = str(i)
            reportPostStory(True, i)
            sys.stdout.write(f"\r{good} Sent Reports: {str(reports)} | Errors: {str(reporterr)} | Reporting: @{targetUsn}'s Posts")
            time.sleep(1)
        sys.stdout.write(f"\n{good} Finished Reporting @{targetUsn}'s Posts, Reported {str(reports)} Posts")
        time.sleep(1)
        getReports()
    elif repR ==4:
        targetUsn = input(f'{inpt} Target To Report: ')
        getID()
        getTag()
        highlightsArray = getHighlights()
        sys.stdout.write('\n')
        for i in highlightsArray:
            i = str(i)
            reportPostStory(False, i)
            sys.stdout.write(f"\r{good} Sent Reports: {str(reports)} | Errors: {str(reporterr)} | Reporting: @{targetUsn}'s Highlights")
            time.sleep(1)
        sys.stdout.write(f"\n\n{good} Finished Reporting @{targetUsn}'s Stories, Reported {str(reports)} Stories")
        time.sleep(1)
        getReports()
        
    else:
        print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] The Option Selected Was Invalid')
        getReportType()


def getReports():
    global rprtSe
    clearS()
    global reportType
    askMsg = f'''[{colorama.Fore.GREEN}1{colorama.Fore.RESET}] Spam
[{colorama.Fore.GREEN}2{colorama.Fore.RESET}] Suicide Or Self Injury
[{colorama.Fore.GREEN}3{colorama.Fore.RESET}] Sale Of Illegal Goods
[{colorama.Fore.GREEN}4{colorama.Fore.RESET}] Scam Or Fraud
[{colorama.Fore.GREEN}5{colorama.Fore.RESET}] Nudity Or Pornography
[{colorama.Fore.GREEN}6{colorama.Fore.RESET}] Violence Or Dangerous Activity
[{colorama.Fore.GREEN}7{colorama.Fore.RESET}] Hate Speech
[{colorama.Fore.GREEN}8{colorama.Fore.RESET}] Bullying'''
    print(askMsg)
    repT = int(input(f'\n{inpt} Report For: '))
    if repT == 1:
        reportType = reportData['spam']
        getReportType()
    elif repT == 2:
        reportType = reportData['self']
        getReportType()
    elif repT == 3:
        reportType = reportData['sale']
        getReportType()
    elif repT == 4:
        reportType = reportData['fraud']
        getReportType()
    elif repT == 5:
        reportType = reportData['nudity']
        getReportType()
    elif repT == 6:
        reportType = reportData['violent']
        getReportType()
    elif repT == 7:
        reportType = reportData['hate']
        getReportType()
    elif repT == 8:
        reportType = reportData['bully']
        getReportType()
    else:
        print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] The Option Selected Was Invalid')
        time.sleep(1.5)
        getReports()
def login():
    global rprtSe
    global good, inpt, rprtng, username, passwd, rprtSe
    clearS()
    username = input(f'{inpt} Username: ')
    passwd = stdiomask.getpass(f'{inpt} Password: ')
    headers = {
        'User-Agent': 'Instagram 9.4.0 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)',
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": "uNs1OZ6CPvJBSmmQOvWDKGFkm2frIDEY"
    }

    guid = str(uuid.uuid1())

    data = "username=" + username + "&password=" + passwd + "&device_id=android-" +  secrets.token_hex(8) +"&_csrftoken=2C3OWk1zw20DXvUj3lr7YT8nCEgGmJJq&phone_id=" + guid + "&guid=" + guid
    response = rprtSe.post('https://b.i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
    if response.status_code == 200:
        getReports()

    else:
        print(response.text)
        print(f'[{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] Invalid Login Credentials Or Other Error Whilst Logging In')
try:
    auth()
except KeyboardInterrupt:
    print(f'\n[{colorama.Fore.BLUE}OTHER{colorama.Fore.RESET}] Bye..')
    quit()
