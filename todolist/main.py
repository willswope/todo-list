from flask import request, render_template, redirect, url_for, current_app
from todolist import todo_task, create_app, db

# Initialize the application and db.
app = create_app()
db.create_all(app=app)


@app.route('/')
def homepage():
    """Display the main page of the application."""
    return render_template(
        'main.html',
        active_tasks=todo_task.Task.query.filter_by(
            active=True).order_by(todo_task.Task.target_date).all(),
        completed_tasks=todo_task.Task.query.filter_by(
            active=False).order_by(todo_task.Task.target_date).all()
    )


@app.route('/task/new/', methods=['GET', 'POST'])
def add_task():
    """If the request is a GET request, show the form to create a new Task, or
    if the request is a POST request, attempt to create a new Task instance."""
    if request.method == 'GET':

        # Show the form page.
        return render_template('new_task.html')

    elif request.method == 'POST':

        # Create new task.
        new_task = todo_task.Task(
                title=request.form['taskTitle'],
                target_date=request.form['targetDate']
            )
        db.session.add(new_task)

        app.logger.debug(
            'Attempting to create task: {}'.format(new_task)
        )

        db.session.commit()

        # Redirect the user back to the homepage after creating the new Task.
        return redirect(url_for('homepage'))


@app.route('/task/<int:task_id>/remove/')
def remove_task(task_id):
    """Delete the task with the specified task ID."""

    # Try to find the specified task by ID number, and throw a 404 if the ID is not found.
    task = todo_task.Task.query.filter_by(id=task_id).first_or_404()

    db.session.delete(task)

    app.logger.debug(
            'Attempting to delete task: {}'.format(task)
        )

    db.session.commit()

    # Redirect the user back to the homepage after deleting the task.
    return redirect(url_for('homepage'))


@app.route('/task/<int:task_id>/toggle/')
def toggle_task_active(task_id):
    """Toggle the completion status of a task, based on the given task ID."""

    # Try to find the specified task by ID number, and throw a 404 if the ID is not found.
    task = todo_task.Task.query.filter_by(id=task_id).first_or_404()

    # Toggle the "active" status of the task.
    task.active = not task.active

    app.logger.debug(
        'Attempting to set the \'active\' flag to {} for task: {}'.format(task.active, task)
    )

    db.session.commit()

    # Redirect the user back to the homepage after epdating the task.
    return redirect(url_for('homepage'))
