# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, validators


class ContactForm(Form):
    name = TextAreaField("Name", [validators.DataRequired("Please enter your company name"),
                                  validators.Regexp(message="Please, enter valid name",
                                                    regex='^[A-za-zА-яа-я_\s-]+$')])
    email = TextAreaField("Email", [validators.DataRequired("Please enter your email address"),
                                    validators.Email("Please enter valid email address")])
    subject = TextAreaField("Subject", [validators.DataRequired("Please enter subject"),
                                        validators.Regexp(message="Please enter valid subject",
                                                          regex='^[A-za-zА-яа-я_\s-]+$')])
    phone = TextAreaField("Phone", [validators.DataRequired("Please enter your phone number"),
                                    validators.Regexp(message="Please enter valid phone number",
                                                      regex='^\+[0-9]{12,15}$')])
    message = TextAreaField("Message", [validators.DataRequired("Please enter your message"),
                                        validators.Regexp(message="Please enter valid message",
                                                          regex='^[A-za-zА-яа-я,;\.\s]+$')])
