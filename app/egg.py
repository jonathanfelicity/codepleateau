import json
import random



with open('quotes.json', 'r') as file:
  quote = json.load(file)
  for x in quote:
    print(x['text'])



def unlock():
    return """

   _____          _      _____  _       _                        ____   ___  
  / ____|        | |    |  __ \| |     | |                      |___ \ / _ \ 
 | |     ___   __| | ___| |__) | | __ _| |_ ___  __ _ _   _       __) | | | |
 | |    / _ \ / _` |/ _ \  ___/| |/ _` | __/ _ \/ _` | | | |     |__ <| | | |
 | |___| (_) | (_| |  __/ |    | | (_| | ||  __/ (_| | |_| |     ___) | |_| |
  \_____\___/ \__,_|\___|_|    |_|\__,_|\__\___|\__,_|\__,_|    |____(_)___/ 
                                                                        
    """
def quote():
  return "something...."