from TimeService.timeservice import TimeService, TimeMachine


def test_setting_time():
    time_obj = TimeService('9:15 AM')
    assert time_obj.hour == 9
    assert time_obj.minute == 15


def test_setting_time_and_future_time():
    time_obj = TimeMachine('9:15 AM', 10)
    assert time_obj.value == 10
    assert time_obj.get_time() == '9:15 AM'


def test_add_time():
    new_time = TimeMachine('9:15 AM', 10).add_minutes()
    assert new_time == '9:25 AM'

