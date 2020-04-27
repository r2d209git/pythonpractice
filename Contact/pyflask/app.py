from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
#    return 'Hello Flask'
    return render_template('index.html')

@app.route('/info')
def info():
#    return 'Info'
    return render_template('info.html')

@app.route('/<username>')
def show_user(username):
    return username

@app.route('/message/<message_id>')
def show_message_id(message_id):
    return message_id

#http://127.0.0.1:8090/reverse?message=bae 입력시 reverse 결과인 eab 리턴
@app.route("/reverse")
def reverse():
    message = request.values["message"]
    return "".join(reversed(message))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8090')