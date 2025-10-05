import requests


resp = requests.get("http://app.zazvonov.course.prafdin.ru/ping/")

assert resp.text == '<html>\n    status: ok\n</html>'

assert 200 <= resp.status_code < 300