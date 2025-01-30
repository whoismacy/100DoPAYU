class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def days_in_month(self):
        if self.month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif self.month in {4, 6, 9, 11}:
            return 30
        elif self.month == 2:
            return 28
    
    def advance(self):
        carry, self.day = divmod(self.day + 1, self.days_in_month())
        if carry:
            self.month += 1
            if self.month > 12:
                self.month = 1

    def __str__(self):
        return f"{self.month}/{self.day}"

    def __eq__(self, p1):
        return self.month or self.day == p1.month or p1.day

    def absolute_day(self):
        days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        counter = 0

        for i in range(1, self.month):
            counter += days[i]
        
        return counter + self.day

    def from_absolute_day(self, abs_val):
        days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        counter = 0

        for i in range(1, 13):
            if counter + days[i] >= abs_val:
                self.month = i
                self.day = abs_val - counter

date = Date(10,31)
