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
    description = 't is a programm for translation words from english to russian'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('word', metavar='word', type=str, help='a word for translation')
    args = parser.parse_args()
    return args.word

def send_request(word):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    language = "en-ru"
    data = {"key":api_key, "text":word, "lang":language}
    r = requests.post(url, data=data)
    #print(r.text)
    return r.text # <str> with dict inside, like '{"code":200, "lang":"en-ru", "text":["Привет Мир"]}'

def parse_response(resp):
    resp_dict = ast.literal_eval(resp)
    arr = resp_dict["text"]
    return arr[0] # <str> with translated result

def show_result(word, result):
    # prints out '$word_to_translate -> $result_of_traslation and yandex.translate creds
    print('\n>>> ' + str(word) + ' -> ' + str(result) + '\n\nПереведено сервисом "Яндекс.Переводчик" http://translate.yandex.ru/ \n')


if __name__ == '__main__':
    word = read_arguments()
    result_dict = send_request(word)
    result = parse_response(result_dict)
    show_result(word, result)
