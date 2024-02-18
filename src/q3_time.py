from typing import List, Tuple
from collections import Counter
import json


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path, 'r') as f:
        data = [json.loads(line)['mentionedUsers'] for line in f.readlines()]
    
    usernames = [user['username'] for obj in data if obj is not None for user in obj]
    return Counter(usernames).most_common(10)

if __name__ == "__main__":
    return_list = q3_time(file_path="farmers-protest-tweets-2021-2-4.json")
    print(return_list)


