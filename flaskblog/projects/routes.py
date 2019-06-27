from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Project
from flaskblog.projects.forms import ProjectForm

projects = Blueprint('projects', __name__)


@projects.route("/project/new", methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(project)
        db.session.commit()
        flash('Your project has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_project.html', title='New Project',
                           form=form, legend='New Project')


@projects.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project.html', title=project.title, project=project)


@projects.route("/project/<int:project_id>/update", methods=['GET', 'POST'])
@login_required
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.author != current_user:
        abort(403)
    form = ProjectForm()
    if form.validate_on_submit():
        project.title = form.title.data
        project.content = form.content.data
        db.session.commit()
        flash('Your project has been updated!', 'success')
        return redirect(url_for('projects.project', project_id=project.id))
    elif request.method == 'GET':
        form.title.data = project.title
        form.content.data = project.content
    return render_template('create_project.html', title='Update project',
                           form=form, legend='Update project')


@projects.route("/project/<int:project_id>/delete", methods=['POST'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.author != current_user:
        abort(403)
    db.session.delete(project)
    db.session.commit()
    flash('Your project has been deleted!', 'success')
    return redirect(url_for('main.home'))
