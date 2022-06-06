from datetime import datetime, timedelta
from calendar import HTMLCalendar
from consultar.models import Consulta


class Calendar(HTMLCalendar):
    cssclasses = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
    cssclasses_weekday_head = cssclasses

    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.user = user
        super(Calendar, self).__init__()

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s</th>' % (
            self.cssclasses_weekday_head[day],self.cssclasses_weekday_head[day])

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(data__day=day)

        if day != 0:
            if len(events_per_day) > 0:
                return f"<td><a class='evento' name={day} id={day}>{day}</a></td>"
            else:
                return f"<td><a class='date'>{day}</a></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        if self.user.cargo == 'PI':
            events = Consulta.objects.filter(data__year=self.year, data__month=self.month)
        else:
            events = Consulta.objects.filter(data__year=self.year, data__month=self.month, cliente_id=self.user.pessoa)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

