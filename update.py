
from Tkinter import Tk
from lxml import html
import requests
import codecs


raw_input("Disable ESET firewall and protection, and press any key to continue...")

provider_url = 'http://www.nod325.com'
converter_url = 'https://my.eset.com/convert?culture=en-us'

session_requests = requests.session()

print('Fetching username and password...')

response = session_requests.get(provider_url)
response.raise_for_status()
provider_html = html.fromstring(response.content)
item_index = 5 # in [2,9]
credential1 = provider_html.xpath('//*[@id="post-31"]/div[3]/p[' + str(item_index) + ']/text()[1]')[0].replace('\n','')
credential2 = provider_html.xpath('//*[@id="post-31"]/div[3]/p[' + str(item_index) + ']/text()[2]')[0].replace('\n','')
assert(credential1[:9] == 'Username:')
assert(credential2[:9] == 'Password:')
username = credential1[9:]
password = credential2[9:]
print('Credentials found:-')
print('Username: ' + username)
print('Password: ' + password)

print('Converting to license key...')

response = session_requests.get(converter_url)
response.raise_for_status()
converter_html = html.fromstring(response.content)
converter_form = converter_html.forms[0]
payload = dict(converter_form.fields)

payload['ctl00$body$txtLicKeyUsrn'] = username
payload['ctl00$body$txtLicKeyPss'] = password

response = session_requests.post(converter_url, payload)
response.raise_for_status()

converted_html = html.fromstring(response.content)
# license_key = converted_html.xpath('//*[@id="body_lblLicenseKey"]')[0].text
license_key = converted_html.get_element_by_id('body_lblLicenseKey').text

r = Tk()
r.withdraw() # don't popup screen window
r.clipboard_clear()
r.clipboard_append(license_key)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()

print('License key was copied to clipboard')