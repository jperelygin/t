import pytest
import t

def test_t_hello():
    word = "Hello"
    wordObj = t.inf(word)
    word_from_wordObj = wordObj.word
    result = wordObj.send_request(word_from_wordObj)
    assert (result == 'Привет')

def test_t_cirillic():
    word = 'Морковь'
    wordObj = t.inf(word)
    word_from_wordObj = wordObj.word
    result = wordObj.send_request(word_from_wordObj)
    assert (result == 'Carrots')