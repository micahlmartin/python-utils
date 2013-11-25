from datetime import datetime, timedelta

MINUTE_SECONDS = 60
HOUR_SECONDS = 3600
DAY_SECONDS = 86400
MONTH_SECONDS = 2592000
YEAR_SECONDS = 31536000

JUST_NOW = "just now"
A_MINUTE_AGO = "one minute ago"
MINUTES_AGO = "%s minutes ago"
AN_HOUR_AGO = "an hour ago"
HOURS_AGO = "%s hours ago"
A_DAY_AGO = "a day ago"
DAYS_AGO = "%s days ago"
A_MONTH_AGO = "a month ago"
MONTHS_AGO = "%s months ago"
A_YEAR_AGO = "a year ago"
YEARS_AGO = "%s years ago"


def format_date_text(date, now=None):

    if now is None:
        now = datetime.now()

    diff_seconds = (now - date).total_seconds()

    if(diff_seconds <= MINUTE_SECONDS):
        return JUST_NOW

    if(diff_seconds < (MINUTE_SECONDS * 2)):
        return A_MINUTE_AGO

    if(diff_seconds < HOUR_SECONDS):
        return MINUTES_AGO % (int(diff_seconds/MINUTE_SECONDS))

    if(diff_seconds < HOUR_SECONDS * 2):
        return AN_HOUR_AGO

    if(diff_seconds < HOUR_SECONDS * 24):
        return HOURS_AGO % (int(diff_seconds/HOUR_SECONDS))

    if(diff_seconds < DAY_SECONDS * 2):
        return A_DAY_AGO

    if(diff_seconds < DAY_SECONDS * 30):
        return DAYS_AGO % (int(diff_seconds/DAY_SECONDS))

    if(diff_seconds < MONTH_SECONDS * 2):
        return A_MONTH_AGO

    if(diff_seconds < MONTH_SECONDS * 12):
        return MONTHS_AGO % (int(diff_seconds/MONTH_SECONDS))

    if(diff_seconds < YEAR_SECONDS * 2):
        return A_YEAR_AGO

    return YEARS_AGO % (int(diff_seconds/YEAR_SECONDS))
