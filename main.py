from flask import Flask

app= Flask(__name__)

@app.route("/hola")
def index():
    return "hola mundo"

@app.route("/chau")
def goodbye():
    return "chau"

@app.route("/saludo/<nombre>")
def salute(nombre):
    return f"Hola, {nombre}"

app.run()