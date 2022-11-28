from process import preparation, generate_response
from flask import Flask, render_template, request

# download nltk
preparation()

#Start Chatbot
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about_us.html")

@app.route("/bot")
def BOT():
    return render_template("index.html")

@app.route("/blog")
def Blog():
    return render_template("Blog.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/Feedback")
def feedback():
    return render_template("Feedback.html")

@app.route("/portofolio")
def portofolio():
    return render_template("portofolio.html")

@app.route("/berita_utama")
def beritaUtama():
    return render_template("Berita_Utama.html")

@app.route("/berita1")
def berita1():
    return render_template("berita1.html")

@app.route("/berita2")
def berita2():
    return render_template("berita2.html")

@app.route("/berita3")
def berita3():
    return render_template("berita3.html")

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

if __name__ == "__main__":
    app.run(debug=True)