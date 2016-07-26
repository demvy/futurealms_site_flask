from flask import Flask, render_template, request
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()
app = Flask('application')
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'futurealms.site@gmail.com'
app.config["MAIL_PASSWORD"] = 'demes661'

app.secret_key = 'futurealms'

mail.init_app(app)

@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('contact.html', form=form, scroll='contact1')
        else:
            msg = Message(form.subject.data, sender='futurealms.site@gmail.com', recipients=['futurealms.site@gmail.com'])
            msg.body = """From: %s,<%s> \nPhone: %s\nMessage:%s """ % (form.name.data, form.email.data,
                                                                       form.phone.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True, scroll='contact1')

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)