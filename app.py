from flask import Flask, render_template, redirect, request, flash, session, url_for
import requests

ENDPOINT_API = "https://api.thecatapi.com/v1/images/search"

app = Flask(__name__)

app.secret_key = "CH@ve_secret&"


# Rota da página inicial
@app.route("/", methods=["GET"])
def index():
    name = session.get("name")
    url_image = session.get("url_image")
    return render_template("index.html", name=name, url_image=url_image)


# Rota para processar a solicitação
@app.route("/cat", methods=["GET", "POST"])
def cat():
    if request.method == "GET":
        return redirect("/")
    name = request.form.get("name", None)

    if not name:
        flash("ERRO! Você precisa digitar um nome!")
        return redirect("/")

    answer = requests.get(ENDPOINT_API)

    if answer.status_code == 200:
        dates = answer.json()  # JSON para Dicionário
        url_image = dates[0]["url"]
    else:
        flash("Os gatos estão dormindo")
        return redirect("/")

    session["name"] = name
    session["url_image"] = url_image

    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    session.clear()  # Isso apaga o nome e a imagem da memória do navegador
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
