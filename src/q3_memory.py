from typing import List, Tuple
import json
from collections import Counter


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Se crea el objeto Counter para registrar los usernames.
    users_counter = Counter()
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            # Condición de fin para el loop while.
            if not line:
                break
            # Se obtiene la lista de users dentro de mentionedUsers. Si es None, continua con la siguiente línea para evitar errores mas adelante.
            mentioned_users = json.loads(line)['mentionedUsers']
            if mentioned_users is None:
                continue
            
            # Se obtienen los usernames y se actualiza el contador.
            usernames = [user['username'] for user in mentioned_users]
            users_counter.update(usernames)

    # Se retornan los 10 usernames mas mencionados.
    return users_counter.most_common(10)
