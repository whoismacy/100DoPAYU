from flask import Flask, render_template, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL, Length
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe's Location URL", validators=[DataRequired(), Length(min=12), URL()])
    open_time = StringField("Cafe's Opening Time", validators=[DataRequired()])
    close_time = StringField("Cafe's Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField("Cafe's Coffee Rating", choices=('☕️', '☕️☕️', '☕️☕️☕️','☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'), validators=[DataRequired()])
    wifi_rating = SelectField("Cafe's Wi-fi Rating", choices=('💪', '💪💪', '💪💪💪','💪💪💪💪', '💪💪💪💪💪'), validators=[DataRequired()])
    power_rating = SelectField("Cafe's Power Rating", choices=('🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'), validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        desc = [form.cafe.data, form.location.data, form.open_time.data, form.close_time.data, form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
        try:
            with open ('cafe-data.csv', 'a', newline='', encoding='utf-8') as fd:
                print('\n')
                writer = csv.writer(fd)
                writer.writerow(desc)
            flash("Added Successfully!!", 'success')
            return url_for('cafes')
        except Exception as e:
            print(f"Error handling cafe-data.csv {e}")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        lengths = len(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, length=lengths)


if __name__ == '__main__':
    app.run(debug=True)

# with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
#     csv_data = csv.reader(csv_file, delimiter=',')
#     list_of_rows = []
#     for row in csv_data:
#         list_of_rows.append(row)
#     lengths = len(list_of_rows)
#
# print(list_of_rows[0][0])
