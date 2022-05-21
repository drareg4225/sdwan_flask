from flask import (Flask, render_template , abort , jsonify , request,
                    redirect, url_for)
# from model import db, save_db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html", cards=db)


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", 
                                card = card , 
                                index=index ,
                                max_index= len(db) -1 )
    except IndexError:
        abort(404)