# Voting Flask
Is a little project for testing and learning flask, the main goal is to keep track of people votes over their favourite team,
It uses firebase for the Register and Login and it keeps track if an user has already voted so it won't let it vote again.
It uses WebSocket to automatically update the score without refreshing the website but as of September 2023 PythonAnyWhere does not supports websocket, the only way to test if websocket is working deploying the project and run it on your local machine, then the browser will stablish a websocket conection on localhost:5000 and will update each other (the local deployment of the aplication and the web version).

I'm still looking for alternatives, I've already tried render.com and railway, but they were extremly slow.
