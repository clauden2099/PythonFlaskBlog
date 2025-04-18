from flask import Flask,render_template, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

def crear_app():
    app = Flask(__name__)
    cliente = MongoClient(os.getenv("MONGODB_URI"))
    #Se agrega la BD a flask
    app.db = cliente.Blog


    @app.route("/", methods=["GET","POST"])
    def principal():
        if request.method == "POST":
            titulo = request.form.get("titulo")
            contenido = request.form.get("contenido")
            nueva_publicacion = {"titulo" : titulo, "contenido" : contenido}

            app.db.Publicaciones.insert_one(nueva_publicacion)

        publicaciones = list(app.db.Publicaciones.find())
        return render_template("index.html", publicaciones=publicaciones)
    return app


if __name__ == "__main__":
    app = crear_app()
    app.run(debug=True)