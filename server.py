from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
     return "hello people"
   # return render_template('index.html')


@app.route('/handle_data')
def handle_data():
    print('I got clicked!')
    return 'Click.'

if __name__ == '__main__':
    app.run(debug=True)