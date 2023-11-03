from lib.vigenere_cipher import *

def test_vigenere_decode():
    message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
    keyword = "friends"
    decoded_message = "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
    assert vigenere_decode(message, keyword) == decoded_message

def test_vigenere_encode():
    message = "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
    keyword = "friends"
    encoded_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
    assert vigenere_encode(message, keyword) == encoded_message