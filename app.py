from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sahte kullanıcı veri tabanı
users = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) == password:
            return f"Hoş geldin, {username}!"
        else:
            return "Hatalı giriş"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
