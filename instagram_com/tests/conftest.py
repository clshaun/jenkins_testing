import pytest

from instagram_com.pages.the_gram import TheGram


@pytest.fixture
def the_gram(py):
    return TheGram(py)


