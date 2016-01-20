import sys
import os
import json
import requests

def data_file_path():
  return os.path.join(os.path.expanduser('~'), '.ipinfo.json')

def save(ipinfo):
  p = data_file_path()
  with open(p, 'w') as f:
    print('Saving {}'.format(p))
    json.dump(ipinfo, f)

def check(old, new):
  is_different = False

  for old_key, old_value in old.items():
    if new[old_key] == old_value:
      continue

    print('{} has changed from {} to {}'.format(
      old_key,
      old_value,
      new[old_key]))

    is_different = True

  if is_different:
    save(new)

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
