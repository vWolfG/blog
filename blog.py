from flask import Flask, render_template
app = Flask(__name__)
posts = [
    {
        'author': 'Veronika Goreva',
        'title': 'Post 1',
        'content': 'It is my first post.',
        'date': '17 2018'
    },
     {
        'author': 'Lolo Pupkin',
        'title': 'Post 2',
        'content': 'It is mine.',
        'date': '!!!!! 2018'
    }

]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
if __name__ == '__main__':
    app.run(debug=True)