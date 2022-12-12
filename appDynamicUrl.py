
## Bulding the Url dynamically using Variable rules and URL binding

from flask import Flask, redirect, url_for

app =Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to bulding the URL dynamically"

@app.route('/success/<int:score>')
def success(score):
    return 'The success rate is '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The fail rate is '+str(score)

#result checker
@app.route('/result/<int:marks>')
def result(marks):
    result = ''
    if marks<50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks)) 




if __name__ == '__main__':
    app.run(debug=True)