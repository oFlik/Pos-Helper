from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///pos.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tecnicos = db.execute("SELECT name FROM equipes;")

        equipeName = request.form.get("equipe")
        data = request.form.get("data")
        clientId = request.form.get("clientId")
        telefone = request.form.get("telefone")
        feedback = request.form.get("feedback")
        iteracao = request.form.get("iteracao")
        nota = request.form.get("nota")

        if equipeName is None:
            return render_template("index.html", inform_sucess="Falha! Não esqueça de escolher a equipe! ID: " + clientId)

        equipeDict = db.execute("SELECT id FROM equipes WHERE name = ?;", equipeName)
        equipeId = equipeDict[0]["id"]

        db.execute("INSERT INTO avaliacao(equipe, data, clientId, telefone, feedback, iteracao, nota) VALUES (?, ?, ?, ?, ?, ?, ?)", equipeId, data, clientId, telefone, feedback, iteracao, nota)

        return render_template("index.html", tecnicos=tecnicos, inform_sucess="Sucesso! Último enviado: ID" + clientId)

    else:
        tecnicos = db.execute("SELECT name FROM equipes;")

        return render_template("index.html", tecnicos=tecnicos)


@app.route("/deleteDB")
def delete():
    db.execute("DELETE FROM avaliacao")
    db.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'avaliacao';")
    return redirect("/")


@app.route("/equipes", methods=["GET", "POST"])
def addEquipes():
    if request.method == "POST":
        db.execute("INSERT INTO equipes(name) VALUES (?);", request.form.get("equipe"))
        return render_template("equipes.html", informSucess="Sucesso!")

    return render_template("equipes.html")


@app.route("/deleteEquipes")
def deleteEquipes():
    db.execute("DELETE FROM equipes")
    db.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'equipes';")
    return redirect("/")


@app.route("/exportar", methods=["GET", "POST"])
def exportar():
    if request.method == "POST":
        tecnicos = db.execute("SELECT name FROM equipes;")

        avaliacoes = db.execute("SELECT * FROM avaliacao JOIN equipes WHERE equipes.id = avaliacao.equipe AND equipes.name = ?;", request.form.get("equipe"))
        for avaliacao in avaliacoes:
            avaliacao["equipe"] = request.form.get("equipe")

        return render_template("exportar.html", tecnicos=tecnicos, equipe=request.form.get("equipe"), avaliacoes=avaliacoes)
    else:
        tecnicos = db.execute("SELECT name FROM equipes;")
    
        return render_template("exportar.html", tecnicos=tecnicos)