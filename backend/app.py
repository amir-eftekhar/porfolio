import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Ensure the static/docs directory exists
os.makedirs('static/docs', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    pdf_url = url_for('static', filename='docs/Project_page.pdf')
    return render_template('projects.html', pdf_url=pdf_url)

@app.route('/resume')
def resume():
    pdf_url = url_for('static', filename='docs/Resume.pdf')
    return render_template('resume.html', pdf_url=pdf_url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
