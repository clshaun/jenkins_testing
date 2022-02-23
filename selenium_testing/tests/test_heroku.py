import pytest


@pytest.mark.heroku
def test_home_page_navigation(py, pages):
    pages.home.goto_heroku_home_page()
    assert py.title() == "The Internet", f"Did not navigate correctly to the home page. Actual site: {py.title()}"


@pytest.mark.heroku
def test_add_remove_elements(py, pages, teardown_add_remove_elements):
    assert_list = []
    els = []

    pages.add_remove.goto()
    pages.add_remove.click_add_element()
    els = pages.add_remove.get_all_new_elements()
    if not len(els) == 1:
        assert_list.append("Clicking 'Add Element' did not create a new element box")

    pages.add_remove.click_add_element()
    els = pages.add_remove.get_all_new_elements()
    if not len(els) == 2:
        assert_list.append("A second element box was not created after clicking 'Add Element' a second time")

    pages.add_remove.delete_all_elements()
    els = pages.add_remove.get_all_new_elements()
    if els:
        assert_list.append("Not all elements were deleted")

    random_amount = pages.add_remove.create_random_amount_of_element_boxes()
    els = pages.add_remove.get_all_new_elements()
    if len(els) != random_amount:
        assert_list.append(f"Not all elements were created. Expected: {random_amount}. Actual: {len(els)}")

    assert not assert_list, assert_list


@pytest.fixture
def teardown_add_remove_elements(pages):
    yield
    pages.add_remove.delete_all_elements()