from typing import List, Tuple
from datetime import datetime
import pandas as pd
import time

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    df = pd.read_json(file_path, lines=True).loc[:, ['date', 'user']]
    df.date = pd.to_datetime(df.date).dt.date
    top_dates = df['date'].value_counts(ascending=False).index.to_list()
    top_dates = top_dates[:10] if len(top_dates) > 10 else top_dates
    df['username'] = df['user'].apply(lambda x: x['username'])
    df = df.loc[df['date'].isin(top_dates)] 
    top_users = [df.loc[df['date']==date, 'username'].value_counts(ascending=False).index.to_list()[0] for date in top_dates]
    return [(top_dates[i], top_users[i]) for i in range(len(top_dates))]


if __name__ == '__main__':
    initial_time = time.time()
    return_list = q1_time(file_path="farmers-protest-tweets-2021-2-4.json")
    
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')

