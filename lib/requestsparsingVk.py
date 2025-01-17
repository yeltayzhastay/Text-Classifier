import requests
import json
import csv
from time import sleep
from datetime import datetime


class parsingVk:
    def __init__(self, token):
        self.token = token
        
    def get_posts(self, owner_id):
        choice = 'owner_id' if type(owner_id) != type('') else 'domain'
        posts = []
        version = 5.21
        count = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': self.token,
                                'v': version,
                                'type': 'post',
                                choice: owner_id,
                                'count': 1,
                                'offset': 0}).json()['response']['count']//100

        i = 0
        while i <= count:
            posts_info = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': self.token,
                                'v': version,
                                'type': 'post',
                                choice: owner_id,
                                'count': 100,
                                'offset': 100*i}).json()['response']
            hundred_items = []
            for post_info in posts_info['items']:
                if post_info['post_type'] == 'post':
                    hundred_items.append([post_info['id'], post_info['from_id'], post_info['text']])
            posts += hundred_items
            i += 1
        return posts


if __name__ == '__main__':
    token = '8bbb4daf8bbb4daf8bbb4daf0c8bcf8d4a88bbb8bbb4dafebb491b8847b23c3736b59f0'
    url = 'kaz_sport2016'
    parse = parsingVk(token)
    print(parse.get_posts(url))                   