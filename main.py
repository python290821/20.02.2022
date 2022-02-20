from flask import Flask, render_template

app = Flask(__name__)

# localhost:5000/
# static page
# dynamic page
@app.route("/")
def home():
    print('hi')
    return '''
        <html>
            Hello main page!
            <button><a href="/ajax">show post</a></button>
        </html>
    '''

@app.route("/ajax")
def ajax():
    print('hi')
    return render_template('home.html')

@app.route('/customers', methods = ['GET'])    
def get_customers():
    return '[{"id" : 1, "name": "danny"}, {"id": 2, "name": "moshe"}]'

@app.route('/customers/1', methods = ['GET'])    
def get_customer_by_id():
    return '{"id" : 1, "name": "danny"}'    

app.run()

