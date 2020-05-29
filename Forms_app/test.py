# a="this is a string"
# b=''
# for i in a:
#     if i==' ':
#         b+='-'
#     else:
#         b+=i
# print(b)


# import re
# def splcharacter(test):
#     check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#     if (check.search(test) == None):
#         print("String does not contain Special Characters.")
#     else:
#         print("String contains Special Characters.")
# splcharacter("ujhhy%5")


# import mysql.connector
# db_connection = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root",
#   database="my_first_db"
#   )
# db_cursor = db_connection.cursor()
#
# db_cursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")
#
# db_cursor.execute("SHOW TABLES")
# for table in db_cursor:
# 	print(table)


# from string import digits
#
# s = 'abc123def456ghi789zero0'
# remove_digits = str.maketrans('', '', digits)
# res = s.translate(remove_digits)
# print(res)

#
# from itertools import groupby
# lst=[{"house":4, "sign":"arijijipi"}]
# for i in lst:
#     print(i[1])

import pandas as pd
df = pd.read_csv(csv_file)
column = df['column_name']
print(column)