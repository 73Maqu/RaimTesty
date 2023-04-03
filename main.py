from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/get_color')
def get_color():
  colors = ['red', 'blue', 'green']
  color = random.choice(colors)
  return jsonify(color)


@app.route('/get_data')
def get_data():
  sizes = [125,150,100]
  numbers = random.sample(range(1, 9), 2)
  bigger_circle = random.choice([0, 1])
  if numbers[0] > numbers[1]:
    command = 'Kliknij większe koło'
  else:
    command = 'Wybierz większą cyfrę'
  random_sizes = random.sample(sizes, 2)
  data = {
    'sizes': random_sizes if bigger_circle == 0 else random_sizes[::-1],
    'numbers': numbers,
    'bigger_circle': bigger_circle,
    'command': command
  }
  return jsonify(data)


if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
