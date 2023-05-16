from app import app

@app.route('/')
def index():
    dataHome = "INI page Home"
    return dataHome

@app.route('/profile')
def profile():
    dataHome = "INI page profile"
    return dataHome

@app.route('/contact')
def contact():
    dataHome = "INI page contact"
    return dataHome


@app.route('/about')
def about():
    dataHome = "INI page about"
    return dataHome