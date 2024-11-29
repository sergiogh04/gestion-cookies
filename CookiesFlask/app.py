from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def home():
    consent = request.cookies.get('cookies_consent')
    if consent:
        return render_template('home.html', consent=consent)
    return render_template('cookies.html')


@app.route('/accept_cookies')
def accept_cookies():
    response = make_response(redirect('/'))
    response.set_cookie('cookies_consent', 'accepted', max_age=30*24*60*60)  # Caduca en 30 días
    return response

@app.route('/reject_cookies')
def reject_cookies():
    response = make_response(redirect('/'))
    return response




if __name__ == '__main__':
    app.run()
