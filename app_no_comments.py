

from flask import Flask, render_template, session, redirect, url_for
from items_generator import generate_item, ItemRarity
import random

app = Flask(__name__)
app.secret_key = 'somesecretkey'

class Barbarian:
    def __init__(self):
        self.gold = 0
        self.experience = 0
        self.level = 1
        self.items = []
        self.auto_adventure = False

    def go_on_adventure(self):
        gold_earned = random.randint(10, 50)
        xp_earned = random.randint(5, 25)
        self.gold += gold_earned
        self.experience += xp_earned
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0

    def add_item(self, item):
        self.items.append(item)

class Shop:
    def __init__(self):
        self.items = {
            'sword': 100,
            'shield': 150
        }

@app.route('/')
def home():
    barbarian = session.get('barbarian')
    if not barbarian:
        barbarian = Barbarian()
        session['barbarian'] = barbarian

    return render_template('home.html', barbarian=barbarian, shop=Shop().items)

@app.route('/adventure', methods=['POST'])
def adventure():
    barbarian = session.get('barbarian')
    barbarian.go_on_adventure()
    item_found = generate_item()
    if item_found:
        barbarian.add_item(item_found)
    session['barbarian'] = barbarian
    return redirect(url_for('home'))

@app.route('/toggle_auto_adventure', methods=['POST'])
def toggle_auto_adventure():
    barbarian = session.get('barbarian')
    barbarian.auto_adventure = not barbarian.auto_adventure
    session['barbarian'] = barbarian
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()

