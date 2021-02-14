import os

print ("Inspired by https://www.julian.com/blog/life-planning")

if os.path.isfile("./user.profile") is False:
    print ("Let's start by defining your values. On a scale from 1 to 10, assign a value on the importance of each category. No two categories can have the same value. The categories are Knowledge, Adventure, Fame, Power, Money, Exercising Talent and Human Connection.")

    print ("Knowledge - Knowledge leads to personal growth. Personal growth via knowledge accumulation is how you avoid the intellectual stagnation of most jobs—that feeling of standing still while the world passes by.")
    knowledge = input()

    print ("Adventure - Adventure is about having memorable experiences. Activities that get you out of your comfort zone and that you can look back on.")
    adventure = input()

    print ("Fame - Fame is being known by people and having an audience. It's about seeing those huge numbers on social media when you post something and being interviewed a lot.")
    fame = input()

    print ("Power - Power focuses on the acquisition of resources and connections.")