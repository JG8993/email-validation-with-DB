@app.route('/edit_user/<int:id>')
def edit_user(id):
    data ={
        "id": id
    }
    return render_template("edit.html", user=User.getUser(data))