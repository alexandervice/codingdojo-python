from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment

@app.route('/create_post', methods=["POST"])
def create_post():
    data = {
        "user_id": session['logged_in_user']["user_id"],
        "content" : request.form["content"]
    }
    if not Post.validate_post(data):
        print("post creation rejected: bad form entry")
        return redirect('/wall')
    Post.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/wall')
# NOTE never render_template on a POST route

@app.route('/posts/delete/<int:post_id>')
def delete_post(post_id):
    comments=Comment.get_all_comments_for_post_with_creator()
    for comment in comments:
        if comment.post.id == post_id:
            Comment.delete(comment.id)
    
    Post.delete(post_id)
    return redirect('/wall')