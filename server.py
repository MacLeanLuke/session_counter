from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'clicks' not in session:
        session['clicks'] = 0
    else:
        session['clicks'] += 1
    # session.modified = True
    return render_template('index.html')

@app.route('/add_click', methods=['POST'])
def add_click():
    if 'clicks' in session:
        session['clicks']+=1
    # session['clicks'] = True
    return redirect('/')

@app.route('/reset_click', methods=['POST'])
def reset_click():
    session.clear()
    session.modified = True
    return redirect('/')

    

if __name__=="__main__":
    app.run(debug=True)