# ----------------------------------------------------------------------
# Name:        lecture27
# Purpose:     Demonstrate web development with Flask
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing a starter web application to be used in lecture 27.

Download and save into your PyCharm project.
Run the program.
Point your browser to http://localhost:5000/
"""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)  # running main
# set environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs122.db'
db = SQLAlchemy(app)


class Review(db.Model):
    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)


@app.route('/')
@app.route('/home')
def welcome():
    return render_template('home.html')


@app.route('/about')
def about():
    results = Review.query.all()
    # results = results, sql table as content for html
    return render_template('about.html', results=results)



@app.route('/review', methods=["POST", "GET"])
def review():
    if request.method == "POST":
        rating = request.form.get('rating', None)
        new_review = Review(text=rating)
        db.session.add(new_review)
        db.session.commit()

    return render_template('review.html')


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
