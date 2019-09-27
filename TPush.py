#!/usr/bin/python

import os
import requests
import sys


MAX_FILE_SIZE = 50000000 # 50MB size limit
BOT_TOKEN = os.environ.get('TPUSH_BOT_TOKEN')
CHAT_ID = os.environ.get('TPUSH_TARGET_ID')


if not BOT_TOKEN:
    print('Must provide Telegram Bot Token!')
    sys.exit(1)

if not CHAT_ID:
    print('Must provide Telegram Chat ID!')
    sys.exit(1)

BASE_URL = 'https://api.telegram.org/bot{}/'.format(BOT_TOKEN)


def validation(filepath):
    size = os.path.getsize(filepath)
    if size > MAX_FILE_SIZE:
        return False
    return True


def sendDocument(**kargs):
    chat_id = kargs['chat_id']
    filepath = kargs['file']
    if 'caption' in kargs:
        caption = kargs['caption']
    else:
        caption = ''

    data = {
        'chat_id': chat_id,
        'caption': caption
    }

    document = {
        'document': open(filepath, 'rb')
    }

    r = requests.post(BASE_URL + 'sendDocument', data = data, files = document)
    assert r.status_code == 200


def parseArgs():
    message = None
    for arg in range(0, len(sys.argv)):
        if sys.argv[arg] == '-m':
            try:
                message = sys.argv[arg + 1]
            except IndexError:
                message = None
    return message

def main():
    if len(sys.argv) < 2:
        print("Pass file to send as argument!")
        sys.exit(1)
    filepath = sys.argv[1]
    message = parseArgs()
    if validation(filepath):
        if message:
            sendDocument(chat_id = CHAT_ID, file = filepath, caption = message)
        else:
            sendDocument(chat_id = CHAT_ID, file = filepath)
    


if __name__ == '__main__':
    main()
