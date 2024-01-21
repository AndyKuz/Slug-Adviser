import courseInfo

def ApIbConverter(userPref):
    # print("ENTERED AP IB CONVERTER METHOD")
    
    # userPreferences = parse_json(FRONT_END_DATA)
    
    APScore3 = userPref.APScore3
    APScore4 = userPref.APScore4
    APScore5 = userPref.APScore5


    apCourses = APScore3 + APScore4 + APScore5
    # print("AP COURSES: ", apCourses)
    coursesEligible = []
    courseInfoDict = courseInfo.get_courseInfo()

    for courseIter in apCourses:
        # print("COURSEITER: ", courseIter)
        if courseIter ==  'AP Art History': 
            pass
        elif courseIter ==  'AP Biology':
            # coursesEligible.append()
            # coursesEligible.append(bioTwentyB)
            pass #till bio classes are released
        elif courseIter ==  'AP Calculus AB':
            if courseIter in APScore3:
                coursesEligible.append(courseInfoDict['math_3'])
                # coursesEligible.append(amThree)
            else:
                coursesEligible.append(courseInfoDict['math_3'])
                # coursesEligible.append(amThree)
                # coursesEligible.append(mathElevenA)
                coursesEligible.append(courseInfoDict['math_19a'])
        elif courseIter == 'AP Calculus BC':
            if courseIter in APScore3:
                coursesEligible.append(courseInfoDict['math_3'])
                # coursesEligible.append(amThree)
                # coursesEligible.append(mathElevenA)
                coursesEligible.append(courseInfoDict['math_19a'])
            else:
                coursesEligible.append(courseInfoDict['math_3'])
                # coursesEligible.append(amThree)
                # coursesEligible.append(mathElevenA)
                # coursesEligible.append(mathElevenB)
                coursesEligible.append(courseInfoDict['math_19a'])
                coursesEligible.append(courseInfoDict['math_19b'])
        elif courseIter ==  'AP Computer Science A':
            # coursesEligible.append(cseTen)
            # coursesEligible.append(cseFiveJ)
            pass
        elif courseIter ==  'AP Computer Science Principles':
            # coursesEligible.append(cseTen)
            pass
        elif courseIter ==  'AP Macroeconomics':
            # coursesEligible.append(econTwo)
            pass
        elif courseIter ==  'AP Microeconomics':
            # coursesEligible.append(econOne)
            pass
        elif courseIter ==  'AP Physics C: Electricity and Magnetism':
            # coursesEligible.append(courseInfoDict['phys_6a']) #'phys_6a'
            # coursesEligible.append(courseInfoDict['phys_6c']) #'phys_6c'
            coursesEligible.append(courseInfoDict['phys_5a']) #'phys_5a'
            coursesEligible.append(courseInfoDict['phys_5c']) #'phys_5c'
        elif courseIter ==  'AP Physics C: Mechanics':
            # coursesEligible.append(courseInfoDict['phys_6a']) #'phys_6a'
            # coursesEligible.append(courseInfoDict['phys_6c']) #'phys_6c'
            coursesEligible.append(courseInfoDict['phys_5a']) #'phys_5a'
            coursesEligible.append(courseInfoDict['phys_5c']) #'phys_5c'
        elif courseIter ==  'AP Psychology':
            # coursesEligible.append(psychOne)
            pass
        elif courseIter ==  'AP Statistics':
            # coursesEligible.append(statFive)
            # coursesEligible.append(psychTwo)
            # coursesEligible.append(socThreeB)
            pass
    return list(set(coursesEligible))

class StudentPreferences:
    def __init__(self, minHoursWork, maxHoursWork, minCreditsQuarter, maxCreditsQuarter, major, coursesTaken, currentYear, APScore3, APScore4, APScore5):
        self.minHoursWork = minHoursWork
        self.maxHoursWork = maxHoursWork
        self.minCreditsQuarter = minCreditsQuarter
        self.maxCreditsQuarter = maxCreditsQuarter
        self.APScore3 = APScore3
        self.APScore4 = APScore4
        self.APScore5 = APScore5
        self.coursesTaken = list(set(ApIbConverter(self) + coursesTaken))
        self.currentYear = currentYear
        # self.summerClasses = summerClasses
        self.major = major

    def get_courses_taken(self):
        return self.coursesTaken

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
    
    def get_current_year(self):
        return self.currentYear

    def get_APScore3(self):
        return self.APScore3

    def get_APScore4(self):
        return self.APScore4

    def get_APScore5(self):
        return self.APScore5
