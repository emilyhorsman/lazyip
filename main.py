import sys
import os
import json

import requests
import mandrill

def data_file_path():
  return os.path.join(os.path.expanduser('~'), '.ipinfo.json')

def save(ipinfo):
  p = data_file_path()
  with open(p, 'w') as f:
    print('Saving {}'.format(p))
    json.dump(ipinfo, f)

def check(old, new):
  is_different = False
  output = []

  for old_key, old_value in old.items():
    if new[old_key] == old_value:
      continue

    output.append('{} has changed from {} to {}'.format(
      old_key,
      old_value,
      new[old_key]))

    is_different = True

  if is_different:
    save(new)
    body = "\n".join(output)
    print(body)
    send(body)

def send(body):
  api_key = os.environ.get('PYIPINFO_MANDRILL_API_KEY')
  send_to = os.environ.get('PYIPINFO_SEND_TO')
  if not api_key or not send_to:
    return

  try:
    client = mandrill.Mandrill(api_key)
    res = client.messages.send({
      'to': [{ 'email': send_to }],
      'from_email': send_to,
      'subject': 'ipinfo changed',
      'text': body })

    print(res)
  except mandrill.Error as e:
    print('Data saved but error occurred while sending with Mandrill.')
    print('{} - {}'.format(e.__class__, e))


if __name__ == '__main__':
  res = requests.get('http://ipinfo.io')
  if not res.ok:
    sys.exit('ipinfo.io request failed')

  ipinfo = res.json()

  try:
    with open(data_file_path(), 'r') as f:
      check(json.load(f), ipinfo)
  except:
    save(ipinfo)
