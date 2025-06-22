from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kiruthika.murug@gmail.com' 
app.config['MAIL_PASSWORD'] = 'Dingdi@321'  
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact_no = request.form['contact_no']
        message = request.form['message']

        msg = Message(f'New Contact Form Submission from {name}',
                      recipients=['your_email@gmail.com'])
        msg.body = f'''
        Name: {name}
        Email: {email}
        Contact No: {contact_no}
        Message: {message}
        '''

        mail.send(msg)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
