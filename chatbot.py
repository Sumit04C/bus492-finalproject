#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:49:23 2024

@author: maluroldan
"""

import random
def chatter():
    greetings = ["Hi there!", "Hey, what's up?!", "Great to see you!", "Welcome!"]
    goodbyes = ["Take care!", "Catch you later!", "Peace out!", "Adios!"]

    keywords = ["TKL", "75%", "65%", "Full size"]
    responses = ["$70", "$60", "$50", "$80"]

    print(random.choice(greetings))
    user = input("What size Keyboard Case Layout would you like? (or type goodbye to quit): ")
    user = user.lower()

    while (user != "goodbye"):
        keyword_found = False

        for index in range(len(keywords)):
            if (keywords[index] in user):
                print("The price of your selected keyboard case layout is: " + responses[index])
                keyword_found = True

        if (keyword_found == False):
            new_keyword = input("I'm unsure how to respond to your request. What's the new keyword that you would expect me to response to? ")
            keywords.append(new_keyword)
            new_response = input("How would you like me to respond " + new_keyword + "? ")
            responses.append(new_response)

        user = input("What size Keyboard Case Layout would you like? (or type goodbye to quit): ")
        user = user.lower()

    print(random.choice(goodbyes))