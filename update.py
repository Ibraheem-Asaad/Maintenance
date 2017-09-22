
"""Fetch Eset Smart Security license key and copy it to clipboard"""

from random import randint
from Tkinter import Tk
from lxml import html
import requests

PROVIDER_URL = 'http://www.nod325.com'
CONVERTER_URL = 'https://my.eset.com/convert?culture=en-us'


def copy2clipboard(text):
    """Copies text to clipboard"""

    interface = Tk()
    interface.withdraw()  # don't popup screen window
    interface.clipboard_clear()
    interface.clipboard_append(text)
    interface.update()  # now it stays on the clipboard after the window is closed
    interface.destroy()


def scrape_credentials():
    """Scrape Eset Nod32 username and password from PROVIDER_URL"""

    raw_input("Disable ESET firewall and protection, press Enter to continue...")
    session_requests = requests.session()
    print 'Fetching username and password...'
    response = session_requests.get(PROVIDER_URL)
    response.raise_for_status()
    provider_html = html.fromstring(response.content)
    item_index = randint(2, 9)
    credential1 = provider_html.xpath(
        '//*[@id="post-31"]/div[3]/p[' + str(item_index) + ']/text()[1]')[0].replace('\n', '')
    credential2 = provider_html.xpath(
        '//*[@id="post-31"]/div[3]/p[' + str(item_index) + ']/text()[2]')[0].replace('\n', '')
    assert credential1[:9] == 'Username:'
    assert credential2[:9] == 'Password:'

    return credential1[9:], credential2[9:]


def convert2key(username, password):
    """Convert Eset Nod32 username and password to Eset Smart Security license key"""

    session_requests = requests.session()
    response = session_requests.get(CONVERTER_URL)
    response.raise_for_status()
    converter_html = html.fromstring(response.content)
    converter_form = converter_html.forms[0]
    payload = dict(converter_form.fields)
    payload['UserName'] = username
    payload['Password'] = password
    response = session_requests.post(CONVERTER_URL, payload)
    response.raise_for_status()
    converted_html = html.fromstring(response.content)
    return converted_html.get_element_by_id('body_lblLicenseKey').text


def fetch_key():
    """Web scrape Eset Smart Security credentials and convert them to License Key"""

    username, password = scrape_credentials()
    print 'Credentials found:-'
    print 'Username: ' + username
    print 'Password: ' + password
    print 'Converting to license key...'
    license_key = convert2key(username, password)
    copy2clipboard(license_key)
    print 'License key was copied to clipboard'
