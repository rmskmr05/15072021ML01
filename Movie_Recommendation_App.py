# -*- coding: utf-8 -*-

import pandas as pd
import tkinter as tk

app = tk.Tk(__name__)
app.title('Movie Recommendarion System')
app.geometry('400x300')

data = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'ts'])
items = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', names=['item_id', 'movie_title', 'year']+[str(i) for i in range(21)])
movies = pd.merge(data.drop('ts', axis=1), items[['item_id', 'movie_title']], on='item_id')
pt = movies.pivot_table(index='user_id', columns='movie_title', values='rating')



## Variables to store form data
query = tk.Variable(app)
query.set('')
msg = tk.Variable(app)
msg.set('')

def recommed():
    global pt, movies
    q = query.get()
    if q.replace(' ', '').isalnum():
        movie = [c for c in pt.columns if q.lower() in c.lower()]
        sim_mat = pd.DataFrame(pt.corrwith(pt[movie[0]]).dropna(), columns=['Corr'])
        rating = pd.DataFrame(movies.groupby('movie_title')['rating'].mean())
        rating['count'] = movies.groupby('movie_title')['rating'].count()
        sim_mat['rating'] = rating['rating']
        sim_mat['count'] = rating['count']
        q_rating = rating['rating'][movie].values[0]
        
        sim_mat[(sim_mat['rating']>=q_rating)&(sim_mat['count']>100)].sort_values('Corr',ascending=False)
        
        rec = sim_mat[(sim_mat['rating']>=q_rating)&(sim_mat['count']>100)].sort_values('Corr',ascending=False).head().index
        
        rec = [r for r in rec if r not in movie][:5]
        rec_movies=''
        for m in rec:
            rec_movies += str(m)+'\n'
        
        msg.set("-:You may like:-\n"+rec_movies)
    else:
        msg.set("Enter a Valid Movie Name")




## Labels and Entries
tk.Label(app, text="Enter Your Movie Name", font=('Arial',15)).place(x=70,y=20)
tk.Entry(app, textvariable = query, font=('Arial',15)).place(x=70, y=60)

tk.Button(app, text='Recommend', command=recommed, font=('Arial',15)).place(x=120,y=100)
tk.Label(app, textvariable = msg, font=('Arial',12)).place(x=80,y=150)
app.mainloop()