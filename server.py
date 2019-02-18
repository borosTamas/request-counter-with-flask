from flask import Flask, render_template, request, redirect

app = Flask(__name__)
counter = {'GET': 0,
           'POST': 0,
           }


@app.route('/')
def index():
    return render_template('index.html', )


@app.route('/request_counter', methods=['GET', 'POST', 'DEL'])
def request_counter():
    if request.method == 'GET':
        counter['GET'] += 1
    elif request.method == 'POST':
        counter['POST'] += 1
    return redirect('/'), counter


@app.route('/statics')
def statics():
    return render_template('statics.html', counter=counter)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
