from flask import Flask
import pickle


app = Flask(__name__)
app.config['SECRET KEY'] = 'cdeac8f173801449a79cf1c89ab2b757'

model = pickle.load(open('model.pkl', 'rb'))

from app import routes
