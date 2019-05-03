from todolist import db
from datetime import datetime
from sqlalchemy.orm import validates


class Task(db.Model):

    # Unique ID for a Task, for internal use.
    id = db.Column(db.Integer, primary_key=True)

    # The display text for a Task, e.g. "Wash the car."
    title = db.Column(db.String)

    # The desired completion date of a Task.
    target_date = date_created = db.Column(db.Date)

    # A boolean value to mark a task as complete.
    active = db.Column(db.Boolean, default=True)

    # A timestamp representing when a Task was created. Might not use this in practice.
    date_created = db.Column(db.DateTime, default=datetime.now)

    @validates('title')
    def validate_title(self, key, title):
        """Validates the 'title' value sent to the server by ensuring that
        the value is not null and not empty."""
        if not title or title == '':
            raise AssertionError('No title was provided.')
        return title

    @validates('target_date')
    def validate_target_date(self, key, target_date):
        """Validates the 'target_date' value sent to the server by ensuring that
        the value can be parsed as a valid python date object."""
        if not target_date:
            raise AssertionError('No target date was provided.')
        try:
            return datetime.strptime(target_date, '%Y-%m-%d').date()
        except ValueError:
            raise AssertionError(
                'Could not interpret the target date provided.')

    def __repr__(self):
        return 'To-Do Item #{} - "{}" - Created on {}'.format(
            self.id,
            self.title,
            self.date_created
        )
