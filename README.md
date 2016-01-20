# Python ipinfo checker

Checks ipinfo.io and compares to `~/.ipinfo.json`. Sends an email if different.

```
$ PYIPINFO_MANDRILL_API_KEY='API_KEY' PYIPINFO_SEND_TO='name@foo.tld' python main.py
```

## Cron Job

Run every 30 minutes:

```
*/30 * * * * PYIPINFO_MANDRILL_API_KEY=\'API_KEY\' PYIPINFO_SEND_TO=\'name@foo.tld\' /home/user/.virtualenvs/lazyip/bin/python /home/user/src/lazyip/main.py >> /home/user/.ipinfo.log 2>&1
```
