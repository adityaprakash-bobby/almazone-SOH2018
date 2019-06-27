from flask import render_template, request, Blueprint
from flaskblog.models import Post, Project
from flask_googlemaps import Map

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    projects = Project.query.order_by(Project.date_posted.desc())
    return render_template('home.html', posts=posts, projects=projects)


@main.route("/about")
def about():

    return render_template('about.html', title='Alumni Directory')

@main.route("/proj")
def proj():
    return render_template('proj.html')

@main.route('/funds')
def funds():
    return render_template('fundraising.html')

@main.route('/funds/blood_donation')
def bl_donation():
    return render_template('blood_donation.html')
