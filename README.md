# Voting Flask
Is a little project for testing and learning flask, the main goal is to keep track of people votes over their favourite team,
It uses firebase for the Register and Login and it keeps track if an user has already voted so it won't let it vote again.
It uses WebSocket to automatically update the score without refreshing the website.

Sadly the deployment is on render.com, but the http with the html response is extremly slow, sometime 50 seconds, 25 seconds and some times just a couple of miliseconds. But the website works!
For a better experience I would recomend to clone this repo and run it with gunicorn, all the requierments are on requierments.txt, so it should work.
