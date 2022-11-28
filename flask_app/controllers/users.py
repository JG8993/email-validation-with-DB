from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template('create.html')

@app.route('/read')
def create():
    return render_template("read.html", users=User.get_all())


@app.route('/create_user', methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        return redirect("/")
    User.save(request.form)
    return redirect('/read')


@app.route('/delete_users')
def delete_users():
    print(request.form)
    User.delete_all(request.form)
    return redirect ('/read')

@app.route('/edit_user/<int:id>')
def edit_user(id):
    data ={
        "id": id
    }
    return render_template("edit.html", user=User.getUser(data))

@app.route('/show_user/<int:id>')
def show_user(id):
    data ={
        "id": id
    }
    return render_template("show.html", user=User.getUser(data))

@app.route('/update_user', methods=["POST"])
def update_user():
    User.updateUser(request.form)
    return redirect('/read')

@app.route('/destroy_one/<int:id>')
def destroy_one(id):
    data={
        "id": id
    }
    User.destroyUser(data)
    return redirect('/read')
