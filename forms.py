from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,

from wtforms import validators, ValidationError


class MainForm(Form):
    plot_type = SelectField('Plot Type', choices=["Scatter Plot",
                                                "Bar Chart",
                                                "Box Plot",
                                                "Heatmap",
                                                "Histogram",
                                                "Histogram 2D",
                                                "Area Plot",
                                                "Pie Chart",
                                                "Contour Plot",
                                                "Histogram 2D contour",
                                                "3D Scatter Plot",
                                                "Surface Plot",
                                                "3D Mesh",
                                                ]
                            )



    language = SelectField('Languages', choices=[('cpp', 'C++'),
                                                 ('py', 'Python')])
    submit = SubmitField("Send")