from datetime import datetime


class DateConverter:
    regex = r'(((0[1-9])|([12][0-9])|(3[01]))-((0[0-9])|(1[012]))-((20[012]\d|19\d\d)|(1\d|2[0123])))'
    _date_format = '%d-%m-%Y'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self._date_format)

    def to_url(self, value: datetime) -> str:
        return value.strftime(self._date_format)
