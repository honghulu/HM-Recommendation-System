import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# articles_df = pd.read_csv("../input/h-and-m-personalized-fashion-recommendations/articles.csv",header=0)
customers_df = pd.read_csv("../input/h-and-m-personalized-fashion-recommendations/customers.csv", header=0)
transactions_df = pd.read_csv("../input/h-and-m-personalized-fashion-recommendations/transactions_train.csv",header=0)
# # 创建评分系统：根据所有用户的购买记录统计某一段时间内的单个 item 的 popularity
# print(transactions.columns[0])
# transactions['t_dat'].unique()
"""
['customer_id', 'FN', 'Active', 'club_member_status',
       'fashion_news_frequency', 'age', 'postal_code']
"""
# club_member_status: ACTIVE PRE-CREATE LEFT CLUB
# fashion_news_frequency: NONE Regularly Monthly None
club_member_status_dict = {
    'ACTIVE': 3,
    'PRE-CREATE': 2,
    'LEFT CLUB': 1
}
fashion_news_frequency_dict = {
    'NONE': 1,
    'Regularly': 2,
    'Monthly': 3,
    'None': 1
}
# print(customers_df['club_member_status'].unique())
customers_ids = []
customers_points = []

for i in range(len(customers_df['club_member_status'])):
    status1 = customers_df['club_member_status'][i]
    if status1 in club_member_status_dict:
        points = club_member_status_dict[status1]
    else:
        points = 1
    status2 = customers_df['fashion_news_frequency'][i]
    if status2 in fashion_news_frequency_dict:
        points += fashion_news_frequency_dict[status2]
    else:
        points += 1
    customers_ids.append(customers_df['customer_id'][i])
    customers_points.append(points)

temp_df = pd.DataFrame(list(zip(customers_ids, customers_points)), columns=['customer_id', 'weight'])
transactions_df = transactions_df.merge(temp_df, on='customer_id')

transactions_df.to_csv('transactions_weighted.csv')
