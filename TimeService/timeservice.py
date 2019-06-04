class TimeService:

    def __init__(self, time_param):
        """
        Initialize with a time e.g. 9:05 AM
        :param time_param: string
        """
        # Split string sequence
        timeset = time_param.split(' ')
        # set time variables
        self.hour = int(timeset[0].split(':')[0])
        self.minute = int(timeset[0].split(':')[1])
        self.merdieum = timeset[1].lower()

    def time(self):
        """
        Call currently set time
        :return: string
        """
        return str(self.hour) + ':' + str(self.minute) + ' ' + self.merdieum


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
        if r > 59:
            self.hour = self.hour + 1
            self.minute = r - 60

        if self.hour > 12:
            self.hour = 1
            if self.merdieum == 'am':
                self.merdieum = 'pm'
            else:
                self.merdieum = 'am'

        if self.minute > 9:
            pass
        else:
            self.minute = str(0) + str(self.minute)

        formatted_time = str(self.hour) + ':' + str(self.minute) + ' ' + self.merdieum.upper()
        return formatted_time

