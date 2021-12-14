from .. import db
from ..models.user import User
from sqlalchemy import ForeignKey
import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    task_desc = db.Column(db.String(100))
    task_date = db.Column(db.String(20))
    status = db.Column(db.String(20))

    def __init__(self, user_id, task_desc):
        """
        constructor
        :param user_id: string
        :param task_desc: strings
        :param task_date: string
        :param task_time: string
        """
        self.user_id = user_id
        self.task_desc = task_desc
        self.task_date = datetime.datetime.now().strftime('%d/ %m/ %Y - %H:%M')
        self.status = 'Open'

    def __repr__(self) -> str:
        return f'{self.task_desc} - {self.task_date}'

    def get_status(self):
        return self.status

    def change_completed(self):
        self.status = 'Completed'

    def change_trashed(self):
        self.status = 'Trashed'

    def delete_task(self):
        self.status = 'Deleted'
