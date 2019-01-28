# -*- coding: utf-8 -*-
"""
t is a simple command-line programm that simplify one-word translations 
from english to russian with help of 
http://translate.yandex.ru service
"""

import argparse
import ast
import requests
from api_creds import api_key


def read_arguments():
    # returns an 'inf' Object with proper arguments
    description = 't is a programm for translation words from english to russian'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('word', metavar='word', type=str, help='a word for translation')
    #TODO add 'lang' and 'dic' arguments
    args = parser.parse_args() # args is a Namespace object with attribute 'word'= $word_to_translate
    return inf(args.word)

def show_result(word, result):
    # prints out '$word_to_translate -> $result_of_traslation and yandex.translate creds
    print(f'\n>>> {word} -> {result}\n\nПереведено сервисом "Яндекс.Переводчик" \nhttp://translate.yandex.ru/')

def parse_response(resp):
    # makes <str> from response a usable <dict> and gets a value by the "text" key
    resp_dict = ast.literal_eval(resp)
    arr = resp_dict["text"]
    return arr[0]


class inf:

    def __init__(self, word, lang=None, dic=None):
        self.word = word
        if lang is None: # 'lang' is an argument that controls what languages from and to a word should be translated 
            self.lang = "en-ru" # translation from english to russian is a default statement for 'lang' argument
        else:
            self.lang = lang
        if dic is None:
            self.dic = None #TODO a 'dic' argument should control wether a transation is needed or definition from the dictionary

    def send_request(self, word):
        if self.dic is None: # if there is no kwarg 'dic' that needed to send a request for a definition of the word
            url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
            data = {"key":api_key, "text":self.word, "lang":self.lang}
            r = requests.post(url, data=data) 
            result = parse_response(r.text) # r.text is a <str> with dict inside, like '{"code":200, "lang":"en-ru", "text":["Привет Мир"]}'
            return result  # <str> with translated result
        else:
            #TODO send request to another API
            pass


if __name__ == '__main__':
    infobj = read_arguments()
    word = infobj.word
    result = infobj.send_request(word)
    show_result(word, result)
