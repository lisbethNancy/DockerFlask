from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker Lisbeth Nancy Torre Abregu ( ͡❛ ͜ʖ ͡❛) </h2>'


if __name__ == "__main__":
    app.run(debug=True)
