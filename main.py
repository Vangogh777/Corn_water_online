from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__, static_folder='', static_url_path='')


# app.config.from_object('setting.DevelopmentConfig')
@app.route('/')
def main_show():
    return render_template("main_show.html")
    # return "hello,world"

@app.route('/node1')
def node1():
    return render_template("node1.html")
@app.route('/node1')
def node1():
    return render_template("node1.html")
@app.route('/node1')
def node1():
    return render_template("node1.html")
@app.route('/node1')
def node1():
    return render_template("node1.html")
@app.route('/node1')
def node1():
    return render_template("node1.html")
@app.route('/node1')
def node1():
    return render_template("node1.html")
@app.route('/node1')
def node1():
    return render_template("node1.html")
@app.route('/node1')
def node1():
    return render_template("node1.html")
@app.route('/node1')
def node1():
    return render_template("node1.html")

@app.route('/test')
def test():
    return render_template("line-simple.html")

# @app.route('/node1', methods=['GET', 'POST'])
# def node1():
#     if request.method == 'POST':
#         return redirect(url_for('main_show'))
#     return render_template("node1.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
