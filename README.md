# SmashGgSeedGenerator
Generates smash.gg seeds based off of win rate. 

___

In order for this to work you will have to update 
``
authToken = ""
``
at the top of `scrape.py` in order to use the SmashGG API. 

___
Dependencies: 

`python -m pip install graphqlclient`
___
Usage: 

``
python3 main.py my-tournament-name
``