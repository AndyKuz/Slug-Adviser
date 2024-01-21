class StudentPreferences:
    def __init__(self, minHoursWork, maxHoursWork, minCreditsQuarter, maxCreditsQuarter, major, coursesTaken, APScore3, APScore4, APScore5):
        self.minHoursWork = minHoursWork
        self.maxHoursWork = maxHoursWork
        self.minCreditsQuarter = minCreditsQuarter
        self.maxCreditsQuarter = maxCreditsQuarter
        self.APScore3 = APScore3
        self.APScore4 = APScore4
        self.APScore5 = APScore5
        self.coursesTaken = coursesTaken
        # self.summerClasses = summerClasses
        self.major = major


    def get_min_hours_work(self):
        return self.minHoursWork

    def get_max_hours_work(self):
        return self.maxHoursWork

    def get_min_credits_quarter(self):
        return self.minCreditsQuarter

    def get_max_credits_quarter(self):
        return self.maxCreditsQuarter

    def get_major(self):
        return self.major

    def get_APScore3(self):
        return self.APScore3

    def get_APScore4(self):
        return self.APScore4

    def get_APScore5(self):
        return self.APScore5
