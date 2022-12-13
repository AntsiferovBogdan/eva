from collections import Counter
from form import RegForm
from model import db, Answer, Question, User
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    title = 'Анкета'
    return render_template(
        'index.html',
        title=title,
    )


@app.route('/reg')
def reg():
    title = 'Персональные данные'
    form = RegForm()
    return render_template(
        'reg.html',
        title=title,
        form=form,
    )


@app.route('/req-process', methods=['POST'])
def reg_process():
    form = RegForm()
    new_user = User(
        sex=form.sex.data,
        age=form.age.data,
        education=form.education.data,
        marriage_status=form.marriage_status.data,
    )
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id
    return redirect(url_for('quest'))


@app.route('/quest')
def quest():
    title = 'Опрос'
    data = Question.query.all()
    return render_template(
        'quest.html',
        title=title,
        data=data,
    )


@app.route('/quest_process', methods=['post'])
def quest_process():
    data = request.form
    for k in data:
        new = Answer(
            answers=k[1],
            user_id=session['user_id'],
            question_id=int(k[0])
        )
        db.session.add(new)
    db.session.commit()
    return redirect(url_for('bye'))


@app.route('/bye')
def bye():
    return render_template('bye.html')


@app.route('/stats')
def stats():
    data = {}
    data['Возраст'] = Counter([i[0] for i in User.query.with_entities(User.age).all()])
    data['Пол'] = Counter([i[0] for i in User.query.with_entities(User.sex).all()])
    data['Образование'] = Counter([i[0] for i in User.query.with_entities(User.education).all()])
    data['Семейное положение'] = Counter([i[0] for i in User.query.with_entities(User.marriage_status).all()])
    return render_template(
        'stats.html',
        data=data,
        )


if __name__ == '__main__':
    app.run(debug=True)
