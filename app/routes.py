from app import app
from flask import render_template, url_for, request, flash
from datetime import datetime


menu = [
    {'name': 'Home', 'url': 'home'},
    {'name': 'About', 'url': 'about'},
    {'name': 'Contact', 'url': 'contact'}
]

@app.route('/home')
def home():
    current_time = datetime.now()
    return render_template('index.html',title="Welcome to My Flask App", menu=menu, current_time=current_time)

@app.route('/about')
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template('about.html', title="About Us", menu=menu, team=team_members)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    manager = {
        'name': 'Polly',
        'contacts': {
            'phone_number': 88009005555,
            'city': 'Moscow',
            'street': 'Aviators St',
            'zip': 119620
        }
    }

    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Your message has been sent successfully', category='success')
        else:
            flash('Error', category='error')

    return render_template('contact.html', title="Contact Us", menu=menu, manager=manager)



if __name__ == "__main__":
    app.run(debug=True)