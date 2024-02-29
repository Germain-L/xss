from flask import Flask, request, render_template

app = Flask(__name__)

comments = []

@app.route('/')
def home():
    # Pass the comments list to the template
    return render_template('index.html', comments=comments)

@app.route('/post_comment', methods=['POST'])
def post_comment():
    comment = request.form.get('comment')
    comments.append(comment)  # Store the comment
    return home()

if __name__ == "__main__":
    app.run(debug=True)
