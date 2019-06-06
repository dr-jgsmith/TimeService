class TimeService:

    def __init__(self, time_param):
        """
        Initialize with a time e.g. 9:05 AM
        :param time_param: string
        """
        # Split string sequence
        self.time_param = time_param
        timeset = self.time_param.split(' ')
        # set time variables
        self.hour = int(timeset[0].split(':')[0])
        self.minute = int(timeset[0].split(':')[1])
        self.meridiem = timeset[1]

    def get_time(self):
        """
        Call currently set time
        :return: string
        """
        return self.time_param


class TimeMachine(TimeService):

    def __init__(self, time_param, value):
        """
        Inherit properties from TimeService class
        :param time_param: string
        :param value: int
        """
        TimeService.__init__(self, time_param)
        self.value = value

    def add_minutes(self):
        """
        Add minutes to a given set time.
        :return: string
        """
        r = self.minute + self.value
        x = int((r / 60))

        self.hour = self.hour + x
        self.minute = r - (60 * x)

        cycles = int(self.hour / 12)
        if cycles > 0:
            if (cycles % 2) == 0:
                pass
            else:
                if self.meridiem == 'AM':
                    self.meridiem = 'PM'
                else:
                    self.meridiem = 'AM'

        self.hour = self.hour - cycles * 12
        if self.hour == 0:
            self.hour = 1

        if self.minute < 10:
            self.minute = str(0) + str(self.minute)

        new_time: str = str(self.hour) + ':' + str(self.minute) + ' ' + self.meridiem.upper()
        return new_time



