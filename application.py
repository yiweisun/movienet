# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import pandas as pd



application = Flask(__name__) # create the application instance :)
application.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable




data = pd.read_csv("result.csv")
#data.to_csv("result.csv")
#print(data)
def out_similar(movieid):
    #print(movieid)
    try:
        result = data.loc[data['0'] == movieid]
        for i in result.iterrows():
            index, output = i
            output = output.tolist()
            output[14] = output[14][1:-1].replace("'","").split(",")
            with open('movielist','r') as f:
                x = f.read().split('\n')
            output.append(x)
            return  output
    except:
        return 0

'''
@application.route('/')
def main():
    with open('movielist','r') as f:
        movies = f.read().split('\n')
    return render_template('home.html',movieList = movies)


@application.route('/movie', methods=['GET', 'POST'])
def searchMovie():
    error = None
    if request.method == 'POST':
        movieid = request.form['search']
        result = out_similar(movieid)
        print(result)
        if result == None:
            return render_template('404.html')
        return render_template('mainpage.html', movieList=result)
    return render_template('mainpage.html', movieList=out_similar("The Dark Knight Rises"))

'''
@application.route('/', methods=['GET', 'POST'])
def searchMovie():
    error = None
    if request.method == 'POST':
        movieid = request.form['search']
        result = out_similar(movieid)
       # print(result)
        if result == None:
            return render_template('404.html')
        return render_template('mainpage.html', movieList=result)
    return render_template('mainpage.html', movieList=out_similar("The Dark Knight Rises"))

@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()