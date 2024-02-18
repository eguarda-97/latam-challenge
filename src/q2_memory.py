from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
from emoji import emoji_list
import time

def q2_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    emoji_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
            tweet_content = json.loads(line)['content']
            tweet_emojis = [emoji['emoji'] for emoji in emoji_list(tweet_content)]
            emoji_counter.update(tweet_emojis)
    
    return emoji_counter.most_common(10)

if __name__ == '__main__':
    initial_time = time.time()
    return_list = q2_memory(file_path="farmers-protest-tweets-2021-2-4.json")
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')
