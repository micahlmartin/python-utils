import unittest
from datetime import datetime, timedelta
import utils
from utils import format_date_text


class TestFormatDateText(unittest.TestCase):

    def test_date_is_less_than_a_minute(self):
        now = datetime.now()
        text = format_date_text(now)
        self.assertEquals(utils.JUST_NOW, text)

    def test_date_is_between_1_and_2_minutes(self):
        now = datetime.now() - timedelta(seconds=utils.MINUTE_SECONDS)
        text = format_date_text(now)
        self.assertEquals(utils.A_MINUTE_AGO, text)

        now = datetime.now() - timedelta(seconds=(utils.MINUTE_SECONDS*2) - 1)
        text = format_date_text(now)
        self.assertEquals(utils.A_MINUTE_AGO, text)

    def test_date_is_between_2_and_60_minutes(self):
        now = datetime.now() - timedelta(minutes=59)
        text = format_date_text(now)
        self.assertEquals(utils.MINUTES_AGO % 59, text)

    def test_date_is_between_1_and_2_hours(self):
        now = datetime.now() - timedelta(hours=1)
        text = format_date_text(now)
        self.assertEquals(utils.AN_HOUR_AGO, text)

    def test_date_is_between_2_and_24_hours(self):
        now = datetime.now() - timedelta(hours=2)
        text = format_date_text(now)
        self.assertEquals(utils.HOURS_AGO % 2, text)

    def test_date_is_between_1_and_2_days(self):
        now = datetime.now() - timedelta(days=1)
        text = format_date_text(now)
        self.assertEquals(utils.A_DAY_AGO, text)

    def test_date_is_between_2_and_30_days(self):
        now = datetime.now() - timedelta(days=2)
        text = format_date_text(now)
        self.assertEquals(utils.DAYS_AGO % 2, text)

    def test_date_is_between_1_and_2_months(self):
        now = datetime.now() - timedelta(days=30)
        text = format_date_text(now)
        self.assertEquals(utils.A_MONTH_AGO, text)

    def test_date_is_between_2_and_12_months(self):
        now = datetime.now() - timedelta(days=60)
        text = format_date_text(now)
        self.assertEquals(utils.MONTHS_AGO % 2, text)

    def test_date_is_between_1_and_2_years(self):
        now = datetime.now() - timedelta(days=365)
        text = format_date_text(now)
        self.assertEquals(utils.A_YEAR_AGO, text)

    def test_date_is_2_years_or_greater(self):
        now = datetime.now() - timedelta(days=365*2)
        text = format_date_text(now)
        self.assertEquals(utils.YEARS_AGO % 2, text)
