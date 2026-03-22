from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # 自动寻找 templates 文件夹下的 index.html
    return render_template("index.html")

if __name__ == "__main__":
    app.run()