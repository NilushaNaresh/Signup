from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///names.db'
db =SQLAlchemy(app)


class BlogNames(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=True)
    password = db.Column(db.Text,nullable=True)

    def __repr__(self):
        return 'Names' + str(self.id)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['username']
        user_password = request.form['password']
        new_names = BlogNames(username = user_name, password = user_password)
        db.session.add(new_names)
        db.session.commit()
        return redirect('/welcome')
    else:
        return render_template('base.html')


@app.route('/welcome', methods=['GET','POST'])
def welcome():
    all_names=db.session.query(BlogNames.username).all()
    db.session.commit()
    return render_template('welcome.html', add_names=all_names)


if __name__ == '__main__':
    app.run(debug=True)
