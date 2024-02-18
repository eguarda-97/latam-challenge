from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
from emoji import emoji_list

def q2_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Este objeto se irá actualizando por cada lista de emojis que se encuentren en cada línea.
    emoji_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
            tweet_content = json.loads(line)['content']
            
            # Se obtienen los emojis de la línea analizada
            tweet_emojis = [emoji['emoji'] for emoji in emoji_list(tweet_content)]
            
            # Se actualiza el contador externo con los emojis encontrados en esta línea.
            emoji_counter.update(tweet_emojis)
    
    # Se devuelven los 10 emojis mas presentes en todo el archivo.
    return emoji_counter.most_common(10)
