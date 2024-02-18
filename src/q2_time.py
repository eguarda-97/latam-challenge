from typing import List, Tuple
import json
from emoji import emoji_list
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Primero, se obtienen todos los objetos de tweets de una vez.
    with open(file_path, 'r') as f:
        tweets = f.readlines()

    # Luego se obtiene un gran string que contenga todos los contenidos de los tweets.
    single_string = ""
    for tweet in tweets:
        single_string += json.loads(tweet)['content']
    
    # Usando el metodo emoji_list, se analiza todo el string y se obtienen todos los emojis presentes.
    emojis = [emoji['emoji'] for emoji in emoji_list(single_string)]

    # Se cuentan los emojis y se devuelven los 10 mas utilizados.
    return Counter(emojis).most_common(10)
