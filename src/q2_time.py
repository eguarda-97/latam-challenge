from typing import List, Tuple
import json
from emoji import emoji_list
import pandas as pd
import time

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path, 'r') as f:
        tweets = f.readlines()

    single_string = ""
    for tweet in tweets:
        single_string += json.loads(tweet)['content']
    
    emojis = emoji_list(single_string)
    df = pd.DataFrame.from_dict(emojis)
    emoji_counter = df['emoji'].value_counts(sort=True, ascending=False)
    emoji_counter = emoji_counter.iloc[:10].to_dict()
    keys = emoji_counter.keys()
    
    return [(key, emoji_counter[key]) for key in keys]

if __name__ == "__main__":
    initial_time = time.time()
    return_value = q2_time(file_path="farmers-protest-tweets-2021-2-4.json")
    print(return_value)
    print(f"EXECUTION TIME: {time.time() - initial_time}")
