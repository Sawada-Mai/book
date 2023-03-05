from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    purpose = db.Column(db.Text)
    thoughts = db.Column(db.Text)
    memo = db.Column(db.Text)
    score = db.Column(db.String, nullable=False)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        posts = Post.query.all()
        return render_template('home.html', posts=posts)
    
    else:
      title = request.form.get('title')
      purpose = request.form.get('purpose')
      thoughts = request.form.get('thoughts')
      memo = request.form.get('memo')
      score = request.form.get('score')

      date = Post(title=title, purpose=purpose, thoughts=thoughts, memo=memo, score=score)
      db.session.add(date)
      db.session.commit()

      return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('edit.html', post=post)
    else:
        post.title = request.form.get('title')
        post.purpose = request.form.get('purpose')
        post.thoughts = request.form.get('thoughts')
        post.memo =  request.form.get('memo')

        db.session.commit()
        return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)