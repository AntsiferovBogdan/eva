from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class RegForm(FlaskForm):
    sex = RadioField(
        'Пол', [DataRequired()],
        choices=['мужчина', 'женщина', 'другое'],
        render_kw={'class': 'checkbox style-2'},
        )
    age = RadioField(
        'Возраст', [DataRequired()],
        choices=['18-21', '22-25', '26-29'],
        render_kw={'class': 'checkbox style-2'},
        )
    education = RadioField(
        'Образование', [DataRequired()],
        choices=[
            'ниже среднего',
            'среднее',
            'среднее специальное',
            'неоконченное высшее',
            'высшее',
            ],
        render_kw={'class': 'checkbox style-2 pull-left'},
        )
    marriage_status = RadioField(
        'Семейное положение', [DataRequired()],
        choices=[
            'не женат/не замужем',
            'женат/замужем',
            'гражданский брак',
            ],
        render_kw={'class': 'checkbox style-2 pull-left'},
        )
    submit = SubmitField(
        'Далее',
        render_kw={'class': 'btn btn-success'},
        )
