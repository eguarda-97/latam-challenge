from typing import List, Tuple
from datetime import datetime
import json
from emoji import emoji_list
import time

def q2_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    with open(file_path, 'r') as f:
        emoji_counter = {}
        
        while True:
            line = f.readline()
            if not line:
                break
            
            tweet_content = json.loads(line)['content']
            tweet_content = emoji_list(tweet_content)
            for emoji_obj in tweet_content:
                emoji = emoji_obj['emoji']
                if emoji not in emoji_counter.keys():
                    emoji_counter[emoji] = 1
                else:
                    emoji_counter[emoji] += 1
    
    top_emojis = sorted(emoji_counter.keys(), key=lambda x: emoji_counter[x], reverse=True)[:10]
    return [(emoji, emoji_counter[emoji]) for emoji in top_emojis]

if __name__ == '__main__':
    initial_time = time.time()
    return_list = q2_memory(file_path="farmers-protest-tweets-2021-2-4.json")
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')
