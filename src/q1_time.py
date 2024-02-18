from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
import time

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    with open(file_path, 'r') as f:
        data = [[json.loads(line)['date'].split('T')[0], json.loads(line)['user']['username']]  for line in f.readlines()]

    most_common_dates = Counter([d[0] for d in data]).most_common(10)
    most_common_users = [Counter([d[1] for d in data if d[0] == date[0]]).most_common(1)[0][0] for date in most_common_dates]

    return list(zip([datetime.strptime(date[0], "%Y-%m-%d").date() for date in most_common_dates], most_common_users))



if __name__ == '__main__':
    initial_time = time.time()
    return_list = q1_time(file_path="farmers-protest-tweets-2021-2-4.json")

    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')

