from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Como se deben analizar pares fecha - usuario, se utiliza un default dict para simplificar el nesteo de datos.
    dates_dict = defaultdict(lambda: defaultdict(int))
    with open(file_path, 'r') as f:
        # Se analiza línea por línea para optimizar el uso de memoria.
        for line in f:
            tweet = json.loads(line)
            tweet_date = tweet['date'].split('T')[0]
            username = tweet['user']['username']
            
            # Se actualiza el contador de tweets escritos por un usuario en un día.
            dates_dict[tweet_date][username] += 1
    
    # Se ordenan las fechas según el número de usuarios (igual al número de tweets) que se publicaron ese día.
    top_dates = sorted(dates_dict.keys(), key=lambda x: sum(dates_dict[x].values()), reverse=True)[:10]
    
    # Se obtiene el usuario con mayor cantidad de tweets para cada fecha según el número registrado en el contador.
    top_users = [max(dates_dict[date], key=dates_dict[date].get) for date in top_dates]

    # Se pasan todas las fechas a formato datetime.date()
    top_dates = [datetime.strptime(date_str, "%Y-%m-%d").date() for date_str in top_dates]
    
    return list(zip(top_dates, top_users))
