from app import app
from flask import render_template, url_for, request, flash


menu = [
    {'name': 'Home', 'url': 'home'},
    {'name': 'About', 'url': 'about'},
    {'name': 'Contact', 'url': 'contact'}
]

@app.route('/home')
def home():
    return render_template('index.html',title="Welcome to My Flask App", menu=menu)

@app.route('/about')
def about():
    return render_template('about.html', title="About Us", menu=menu)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Your message has been sent successfully', category='success')
        else:
            flash('Error', category='error')

    return render_template('contact.html', title="Contact Us", menu=menu)



if __name__ == "__main__":
    app.run(debug=True)