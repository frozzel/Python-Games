from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/moveit')
def moveit():
    return render_template('moveit.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)