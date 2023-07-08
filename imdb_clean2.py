import pandas as pd
import matplotlib.pyplot as plt




data=pd.read_csv("imdb_clean2.csv")
print(data)
print("v",data.info)
"""تعداد کل فیلم های منتشر شده"""
film=data["title"].count()
print("films is: ",film)

"""در چه سالی بیشترین فیلم تولید شده؟"""

print(data["release_year"].value_counts().idxmax())

"""کمترین فیبم تولید شده در چه سالی هست؟"""

print(data["release_year"].value_counts().idxmin())

"""کمترین تایم نمایش فیلم چفدر بوده؟"""

print("min_time",data["runtime"].min())


"""بیشترین تایم نمایش برای کدون فیلم بوده"""

print("max_film",data["runtime"].max())

"""قدیمیترین فیلم"""
print("old_film",data["release_year"].min())

"""جدیدترین قیلم"""
print("new_film",data["release_year"].max())

"""نام جدیدترین فیلم"""
new=data["release_year"].max()
print(data[data["release_year"]==new]["title"])
"""تعداد فیلم های جدید"""
print(data[data["release_year"]==new]["title"].value_counts())


"""سال تولید بهترین انیمیشن"""

imdb=data["rating"].max()
print("best_animation is :",data[data["rating"]==imdb]["title"])


"""چندتا فیلم درام اکشن و فانتزی داریم؟"""
print("drama",data[data["genre"]=="Drama"].count())
print("Crime",data[data["genre"]=="Crime"].count())

"""بیشترین فیلمی که تولید شده در چه ژانری هست؟"""
title=(data["title"].max())
print(title, data[data["title"]==title]["genre"])

"""کمترین imdb مال کدومم فیلم هست؟"""
min_imdb=data["rating"].min()
print("min_imdb", data[data["rating"]==min_imdb]["title"])

"""تعداد فیلم هایی مه کمترین imdbزو دارن"""
print("min_imdb", data[data["rating"]==min_imdb]["title"].count())

"""چندتاا imdbبیشتر از 9 داریم؟"""
print("imdb>9", data[data["rating"]>9].count())
print("imdb>9", data[data["rating"]>9]["title"])


"""نمایش فیلم هایی که سال انتشار انهاا از 2020 به بعد باشد."""


print(data[data["release_year"]>2020]["title"])



"""رسم نمودار """
x=data["genre"]
y=data["rating"]
plt.title("genre & rating")
plt.plot(x,y)
plt.show()
