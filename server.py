from flask import Flask
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return '<h1>Why so easy</h1>'

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://school.nextacademy.com/courses/full-stack-web-development-bootcamp-with-python/lessons/2947
   app.run()
