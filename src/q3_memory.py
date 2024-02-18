from typing import List, Tuple
import time
import json
from collections import Counter


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    users_counter = Counter()
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            
            mentioned_users = json.loads(line)['mentionedUsers']
            if mentioned_users is None:
                continue
            
            usernames = [user['username'] for user in mentioned_users]
            users_counter.update(usernames)

    return users_counter.most_common(10)

if __name__ == '__main__':
    initial_time = time.time()
    return_list = q3_memory(file_path="farmers-protest-tweets-2021-2-4.json")
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')
