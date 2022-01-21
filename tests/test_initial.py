def test_webdriver(py):
    py.visit("https://google.com")
    els = py.find('a')
    for l in els:
        print(l.get_attribute('href'))
    assert "Google" in py.title()


def test_api(api):
    response = api.get("https://www.google.com")
    assert response.status_code == 200
