import pytest
from decouple import config
from faker import Faker


@pytest.mark.wordpress
def test_login_to_word_press(py, pages):
    pages.login.login_to_wordpress(config("WORDPRESSUSERNAME"),
                                   config("WORDPRESSPASSWORD"))
    assert "My Profile" in py.title()


@pytest.mark.wordpress
def test_fill_out_random_info_for_my_profile(py, pages, setup, teardown):
    fake = Faker()
    assert_list = []
    my_profile = {"first_name": fake.first_name(),
                  "last_name": fake.last_name(),
                  "display_name": fake.user_name(),
                  "about_me": fake.paragraph()}

    pages.home.fill_out_profile_text_boxes(**my_profile)
    values = pages.home.get_all_text_values()

    if values != my_profile:
        assert_list.append(f"One or more fields did not populate correctly. Expected: {my_profile}. Actual: {values}")

    pages.home.save_profile()
    pages.home.logout()
    pages.login.login_to_wordpress(config("WORDPRESSUSERNAME"),
                                   config("WORDPRESSPASSWORD"))

    saved_values = pages.home.get_all_text_values()
    if saved_values != my_profile:
        assert_list.append(f"One or more fields did not save correctly. Expected: {my_profile}. Actual: {saved_values}")

    if saved_values["display_name"] != pages.home.left_side_profile_username(my_profile['display_name']):
        assert_list.append("The profile username did not update correctly.")

    assert not assert_list, assert_list


@pytest.mark.wordpress
def test_add_file_links(py, pages, fake, setup, teardown):
    url = fake.domain_name()
    description = fake.text(25)
    pages.home.click_add_profile_links()
    pages.home.fill_out_add_url_section(url, description)
    py.reload()
    for x in [url, description]:
        py.getx("//div[@class='card']//div").should().contain_text(x)


@pytest.fixture
def setup(py, pages):
    username = config("WORDPRESSUSERNAME")
    password = config("WORDPRESSPASSWORD")
    pages.login.login_to_wordpress(username, password)


@pytest.fixture()
def teardown(py, pages):
    yield
    pages.home.fill_out_profile_text_boxes(first_name="Jenkins",
                                           last_name="Tester",
                                           display_name="JenkinsTester",
                                           about_me=" ")
    pages.home.save_profile()
    pages.home.del_profile_links()
    pages.home.logout()



