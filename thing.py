import json
from pprint import pprint
import sys
import requests
from pathlib import Path
import random
import webbrowser
import pyautogui
import time
import mouse
import cv2
import cropping_main
import cropping_comment
import audiomaker
import keyboard

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
sub=''
waba = 0
imagelist= []

client_id = open(Path("apikeys/redditclient.txt"), "r").read()
secret_key = open(Path("apikeys/redditsecret.txt"), "r").read()

auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    
data = {
    'grant_type': 'password',
    'username': open(Path("apikeys/username.txt")),
    'password': open(Path("apikeys/password.txt"))
    }

headers = {'User-Agent': 'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

token=res.json()['access_token']

headers['Authorization'] = f'bearer {token}'

sub="askreddit"
feed="top"


def main1(post1):
    global bruh2
    global bruh
    global post
    global title
    link= 'https://oauth.reddit.com/r/'+sub+'/'+feed+'?limit=100'
    bruh = requests.get(link, headers=headers)
    bruh = bruh.json()
    
    post = post1

    link2 = 'https://oauth.reddit.com/r/'+sub+'/comments/'+bruh['data']['children'][post]['data']['id']
    bruh2 = requests.get(link2, headers=headers)
    bruh2 = bruh2.json()

    comment = bruh2[1]['data']['children'][post]['data']['body']
    title = bruh['data']['children'][post]['data']['title']

    lis = [title, comment]
    return lis

def testing(comment1):
    global commenting
    global commentlink
    global comment

    if len(comment1)>800:
        commenting+=1
        comment = bruh2[1]['data']['children'][commenting]['data']['body']
        commentlink = 'reddit.com'+str(bruh2[1]['data']['children'][commenting]['data']['permalink'])
        testing(comment)
    else:
        comment = bruh2[1]['data']['children'][commenting]['data']['body']
        commentlink = 'reddit.com'+str(bruh2[1]['data']['children'][commenting]['data']['permalink'])

def main2(post1):
    global post
    global commenting
    global comment
    global commentlink
    url = 'reddit.com'+ str(bruh['data']['children'][post]['data']['permalink'])

    commenting = 1

    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)
    time.sleep(10)
    ss = pyautogui.screenshot()
    ss.save(Path('images/main.png'))
    keyboard.press_and_release('ctrl+w') 
    
    cropping_main.doinmain(str(post1)+'amain')
    audiomaker.audio(title, str(post1)+"amain")
    
    for i in range(3):
        commentlink = 'reddit.com'+str(bruh2[1]['data']['children'][commenting]['data']['permalink'])
        comment = bruh2[1]['data']['children'][commenting]['data']['body']
        testing(str(comment))

        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(commentlink)
        time.sleep(10)
        mouse.wheel(delta=-3)
        time.sleep(1)
        ss = pyautogui.screenshot()
        ss.save(Path(Path('images/main.png')))
        keyboard.press_and_release('ctrl+w')


        cropping_comment.doincomment(str(post)+"comment"+str(i))
        audiomaker.audio(comment, str(post)+"comment"+str(i))
        commenting = int(commenting) + 1
        

    
def main3(post1):
    main1(post1)
    main2(post1)


def main():
    pass

if __name__ == "__main__":
   main()












