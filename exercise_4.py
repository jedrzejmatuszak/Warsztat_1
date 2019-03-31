from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def komputer_zgaduje():
    if request.method == 'POST':
        min_value = int(request.form['min_value'])
        max_value = int(request.form['max_value'])
        guess = int((max_value - min_value) / 2) + min_value
        if request.form['choice'] == 'za_malo':
            min_value = guess
            guess = int((max_value - min_value) / 2) + min_value
            return render_template("komputer_zgaduje.html", guess=guess, max_value=max_value, min_value=min_value)
        elif request.form['choice'] == 'za_duzo':
            max_value = guess
            guess = int((max_value - min_value) / 2) + min_value
            return render_template("komputer_zgaduje.html", guess=guess, max_value=max_value, min_value=min_value)
        else:
            return "Trafiłeś"
    else:
        min_value, max_value = 0, 1000
        guess = int((max_value - min_value) / 2) + min_value
        return render_template('komputer_zgaduje.html', guess=guess, min_value=min_value, max_value=max_value)

app.run()