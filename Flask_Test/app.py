from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory structure to hold tickets
tickets = []

@app.route('/')
def index():
    return render_template('index.html', tickets=tickets)

@app.route('/add', methods=['POST'])
def add_ticket():
    title = request.form.get('title')
    description = request.form.get('description')
    tickets.append({'title': title, 'description': description})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
