from typing import List, Tuple
from collections import Counter
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Se obtienen las listas de usuarios mencionados en cada tweet
    with open(file_path, 'r') as f:
        data = [json.loads(line)['mentionedUsers'] for line in f.readlines()]
    
    # Se obtiene el username de cada user dentro de cada lista de mentionedUsers, exceptuando las listas vacias (caso None).
    usernames = [user['username'] for obj in data if obj is not None for user in obj]

    # Se retornan los 10 usernames mas comunes usando la clase Counter para contar y sortear.
    return Counter(usernames).most_common(10)
