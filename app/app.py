from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        reviews = request.form.get('reviews')
        # Placeholder: Analyze the reviews (dummy result for now)
        result = "Positive" if "good" in reviews.lower() else "Negative"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
