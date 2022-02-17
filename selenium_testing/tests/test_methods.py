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


def test_weather_site(py, pages):
    assert_list = []

    get_temp = pages.home.goto_weather_site()
    if not py.should().contain_title('Current Temperature'):
        assert_list.append(f"Did not land on the homepage. Actual page is {py.title()}")

    if not isinstance(get_temp, int):
        assert_list.append(f"The temp did not display correctly. Actual was {get_temp}")

    pages.home.click_buy_moisturizers()

    if not py.should().contain_title('Moisturizers'):
        assert_list.append(f"The site did not navigate correctly to the purchase moisturizers page. "
                           f"Actual page it {py.title()}")

    assert not assert_list, assert_list


def test_api(api):
    response = api.get("https://www.google.com")
    assert response.status_code == 200


# def test_login_to_instagram_and_grab_pictures(py, the_gram):
#     username = config("USERNAME")
#     password = config("PASSWORD")
#     the_gram.login.login_to_the_gram(username, password)
