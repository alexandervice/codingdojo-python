from flask import redirect, request, session
from flask_app import app
# from flask_app.models.user import User
# from flask_app.models.post import Post
from flask_app.models.comment import Comment

@app.route('/create_comment', methods=["POST"])
def create_comment():
    data = {
        "user_id": session['logged_in_user']["user_id"],
        "post_id": request.form["post_id"],
        "content" : request.form["content"]
    }
    if not Comment.validate_comment(data):
        print("comment creation rejected: bad form entry")
        return redirect('/wall')
    Comment.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/wall')
# NOTE never render_template on a POST route


@app.route('/comments/delete/<int:comment_id>')
def delete_comment(comment_id):
    Comment.delete(comment_id)
    return redirect('/wall')