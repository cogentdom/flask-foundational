from flask import Flask, reder_template, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    mylist = [10, 20, 30, 40, 50]
    return render_template(template_name_or_list='index.html')

if __name__ == 'main':
    app.run(host='0.0.0.0', debug=True)