from flask_app import app
from flask import Flask, render_template

@app.route('/')
def tabla_users():
    users_info = [
    {'Nombre' : 'Michael', 'Apellido' : 'Choi'},
    {'Nombre' : 'John', 'Apellido' : 'Supsupin'},
    {'Nombre' : 'Mark', 'Apellido' : 'Guillen'},
    {'Nombre' : 'KB', 'Apellido' : 'Tonel'}
]

    return render_template("index.html", users= users_info)
