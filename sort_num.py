# -*- coding: utf-8 -*-
"""
Description:  Code that asks your name, asks for favorite
numbers, prints favorite numbers, sorts favorite numbers.

Useage: Run from IDLE using F5.

"""
from __future__ import print_function
import os
import time
import pyttsx

def main(sleepint,numloops):
    #sleep commands to make easy screen reading.  
    #To Do: integrate text to voice as a challenge.
    #Could use pyttsx or AWS AVS??
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-25)
    intro_str = '\n Hello my name is ' + \
          os.getenv('DESKTOP_STARTUP_ID').split('-')[2]+ '.'
    print(intro_str)
    engine.say(intro_str)
    engine.runAndWait()
    time.sleep(sleepint)
    uname_str = ' What is your name? '
    engine.say(uname_str)
    engine.runAndWait()
    uname = raw_input(uname_str)
    hello_str = '\n Hello ' + uname + '.  Nice to meet you.'
    engine.say(hello_str)
    engine.runAndWait()
    print(hello_str)
    time.sleep(sleepint)
    loop_str = '\n What are ' + str(numloops) + \
               ' of your favorite numbers? '
    engine.say(loop_str)
    engine.runAndWait()
    print(loop_str)
    num_list = []
    time.sleep(1)
    for i in range(0,numloops):
        tell_str = ' Please tell me: '
        engine.say(tell_str)
        engine.runAndWait()
        unum = raw_input(tell_str)
        num_list.append(int(unum))
    time.sleep(sleepint)
    fav_str = '\n You said your favorite numbers are: '
    engine.say(fav_str)
    engine.runAndWait()
    print(fav_str)
    time.sleep(1)
    for n in num_list:
        engine.say(n)
        engine.runAndWait()
        time.sleep(1)
        print(' ' + str(n))
    time.sleep(sleepint)
    sort_str = '\n I will sort them for you: '
    engine.say(sort_str)
    engine.runAndWait()
    print(sort_str)
    time.sleep(1)
    num_list.sort()
    for n in num_list:
        engine.say(n)
        engine.runAndWait()
        time.sleep(1.5)
        print(' ' + str(n))
    bye_str = 'Thank-you.  Goodbye.'
    engine.say(bye_str)
    engine.runAndWait()
    time.sleep(1)
    print(bye_str)

    return num_list
        
if __name__ == "__main__":
    sorted_number_list = main(3,3)
