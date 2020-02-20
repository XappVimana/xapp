from flask import Flask, render_template, request, redirect, url_for, session, flash, app

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        if 'Projects' in request.form:
            return redirect(url_for('projects'))
        elif 'Name' in request.form:
            return redirect(url_for('name'))

        return render_template('About.html')


    else:

        return render_template('About.html')


@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        if 'Projects' in request.form:
            return redirect(url_for('projects'))
        elif 'About' in request.form:
            return redirect(url_for('about'))

        print('lalalal')
        details = request.form
        # amez = details['name']
        # namez=Names(name=namez,)
        # db.session.add(namez)
        # db.session.commit()

        return render_template('Names.html', name=[])


    else:

        return render_template('Names.html', name=[])


@app.route('/projects', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        if 'Name' in request.form:
            return redirect(url_for('name'))
        elif 'About' in request.form:
            return redirect(url_for('about'))

        return render_template('Projects.html')


    else:
        return render_template('Projects.html')


if __name__ == '__main__':
    app.run(debug=True)
