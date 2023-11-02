from lib.caesar_cipher import *

def test_caesar_decode():
    encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
    decoded_message = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"
    assert caesar_decode(encoded_message, 10) == decoded_message

def test_caesar_encode():
    message = "hello my name is gemma and the use of modulo in this exercise confused me!"
    encoded_message = "xubbe co dqcu yi wuccq qdt jxu kiu ev cetkbe yd jxyi unuhsyiu sedvkiut cu!"
    assert caesar_encode(message, 10) == encoded_message