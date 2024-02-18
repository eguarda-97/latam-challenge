from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
import time

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    dates_dict = defaultdict(lambda: defaultdict(int))
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tweet_date = tweet['date'].split('T')[0]
            username = tweet['user']['username']
            dates_dict[tweet_date][username] += 1
    
    top_dates = sorted(dates_dict.keys(), key=lambda x: sum(dates_dict[x].values()), reverse=True)[:10]
    top_users = [max(dates_dict[date], key=dates_dict[date].get) for date in top_dates]
    top_dates = [datetime.strptime(date_str, "%Y-%m-%d").date() for date_str in top_dates]
    
    return list(zip(top_dates, top_users))

if __name__ == '__main__':
    initial_time = time.time()
    return_list = q1_memory(file_path="farmers-protest-tweets-2021-2-4.json")
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')
