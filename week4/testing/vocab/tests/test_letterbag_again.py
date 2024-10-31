from ..letterbag import LetterBag
import pytest

def test_as_string():
    """Test that as_string sorts the letters."""
    letter_bag = LetterBag("rat")
    assert letter_bag.as_string() == "art"
    assert LetterBag("cbaabaa").as_string() == "aaaabbc"

@pytest.fixture
def aab_bag():
    """Return a LetterBag for 'aab'."""
    return LetterBag("aab")

@pytest.mark.parametrize("test_input,expected", [("abb","aabb"), ("","aab")])
def test_merge(test_input, expected, aab_bag):
    """Test that merge of letterbags for 'aab' and 'abb'
    produces 'aabb'.
    """
    letter_bag = aab_bag
    letter_bag.merge(LetterBag(test_input))
    assert letter_bag.as_string() == expected
