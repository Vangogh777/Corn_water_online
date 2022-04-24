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
@app.route('/node2')
def node2():
    return render_template("node2.html")
@app.route('/node3')
def node3():
    return render_template("node3.html")
@app.route('/node4')
def node4():
    return render_template("node4.html")
@app.route('/node5')
def node5():
    return render_template("node5.html")
@app.route('/node6')
def node6():
    return render_template("node6.html")
@app.route('/node7')
def node7():
    return render_template("node7.html")
@app.route('/node8')
def node8():
    return render_template("node8.html")
@app.route('/node9')
def node9():
    return render_template("node9.html")
@app.route('/node10')
def node10():
    return render_template("node10.html")

@app.route('/test')
def test():
    return render_template("test.html")



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
