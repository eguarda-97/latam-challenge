from typing import List, Tuple
import json
from emoji import emoji_list
from collections import Counter
import time

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path, 'r') as f:
        tweets = f.readlines()

    single_string = ""
    for tweet in tweets:
        single_string += json.loads(tweet)['content']
    
    emojis = [emoji['emoji'] for emoji in emoji_list(single_string)]
    return Counter(emojis).most_common(10)


if __name__ == "__main__":
    initial_time = time.time()
    return_value = q2_time(file_path="farmers-protest-tweets-2021-2-4.json")
    print(return_value)
    print(f"EXECUTION TIME: {time.time() - initial_time}")
