from typing import List, Tuple
from datetime import datetime
import json
import time

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    with open(file_path, 'r') as f:
        dates_dict = {}
        
        while True:
            line = f.readline()
            if not line:
                break
            
            tweet = json.loads(line)
            date = tweet['date'].split('T')[0]
            username = tweet['user']['username']
            if date not in dates_dict.keys():
                dates_dict[date] = {username: 1}
            else:
                if username not in dates_dict[date].keys():
                    dates_dict[date][username] = 1
                else:
                    dates_dict[date][username] += 1
    
    top_dates = sorted(dates_dict.keys(), key=lambda x: sum(dates_dict[x].values()), reverse=True)
    top_dates = top_dates[:10] if len(top_dates) > 10 else top_dates
    top_users = [max(dates_dict[i].keys(), key=lambda x: dates_dict[i][x]) for i in top_dates]
    return [(datetime.strptime(top_dates[i], "%Y-%m-%d").date(), top_users[i]) for i in range(len(top_dates))]

if __name__ == '__main__':
    initial_time = time.time()
    return_list = q1_memory(file_path="farmers-protest-tweets-2021-2-4.json")
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')
