import datetime


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def convert(cls, date):
        number = int(date.replace('-', ''))
        return cls(number)

    @staticmethod
    def check_date(date):
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY")
        else:
            answer = 'Correct data format'
        return answer


dt1 = '16-01-2022'
test_classmethod = Date.convert(dt1)
print(test_classmethod.date)

test_statemethod1 = Date.check_date(dt1)
print(test_statemethod1)

dt2 = '33-01-2022'
test_statemethod2 = Date.check_date(dt2)
print(test_statemethod2)
