import datetime

from wtforms import DateField
from wtforms.validators import ValidationError


class TimeCondition:
    def __init__(self, date: 'datetime.date or DateField'):
        self.date = date

    @staticmethod
    def date_from_field(datefield, form):
        """Set self.date to a `datetime.date` object if it currently is a `DateField`"""
        try:
            datefield = form[datefield].data
        except KeyError:
            raise ValidationError(f'Invalid field name {date}')

        if not isinstance(datefield, datetime.date):
            raise ValidationError(f'Not a DateField')

        return datefield

    def check_date(self, form):
        if not isinstance(self.date, datetime.date):
            date_from_field(self.date, form)


class Before(TimeCondition):
    def __init__(self, date, message=None):
        super().__init__(date)
        if not message:
            message = f'The chosen date must be before the {date}'
        self.message = message

    def __call__(self, form, field):
        self.check_date(form)
        if field.data < self.date:
            raise ValidationError(self.message)


class After(TimeCondition):
    def __init__(self, date, message=None):
        super().__init__(date)
        if not message:
            message = f'The chosen date must be after the {date}'
        self.message = message

    def __call__(self, form, field):
        self.check_date(form)
        if field.data > self.date:
            raise ValidationError(self.message)
