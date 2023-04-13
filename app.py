from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reviews', methods=['POST'])
def reviews():
    url = request.form['url']
    reviews = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        reviews = soup.find_all('p', {'class': '_2-N8zT'})
    except:
        pass
    return render_template('reviews.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)
