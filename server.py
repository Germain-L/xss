from flask import Flask, redirect, request, render_template_string, url_for

app = Flask(__name__)

comments = []

@app.route('/')
def home():
    comments_html = '<br>'.join(comments)
    return render_template_string(open('templates/index.html').read().replace('<!-- Les commentaires seront affichés ici -->', comments_html))

@app.route('/post_comment', methods=['POST'])
def post_comment():
    comment = request.form.get('comment')
    comments.append(comment)  # Stocke le commentaire sans aucune validation ou échappement
    return home()

@app.route('/reset_comments', methods=['POST'])
def reset_comments():
    comments.clear()  # Clears the comments list
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)