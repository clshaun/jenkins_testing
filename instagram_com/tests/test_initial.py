from decouple import config

def test_webdriver(py):
    py.visit("https://google.com")
    els = py.find('a')
    for l in els:
        print(l.get_attribute('href'))
    assert "Google" in py.title()


def test_google_search_stuff(py):
    py.visit("https://www.google.com")
    py.get('[name="q"]').type("This is a test")
    py.get('[name="btnK"]').submit()
    assert py.should().contain_title('This is a test')


def test_login_to_instagram_and_steal_pictures(py, the_gram):
    username = config("USERNAME")
    password = config("PASSWORD")
    the_gram.login.login_to_the_gram(username, password)


def test_api(api):
    response = api.get("https://www.google.com")
    assert response.status_code == 200
