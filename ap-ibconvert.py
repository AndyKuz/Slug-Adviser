from course import Course
from courseInfo import get_courseInfo


def ApIbConverter(APScore3, APScore4, APScore5):
    # print("ENTERED AP IB CONVERTER METHOD")

    apCourses = APScore3 + APScore4 + APScore5
    # print("AP COURSES: ", apCourses)
    coursesEligible = []
    courseInfoDict = get_courseInfo()

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
    

# def main():
    
#     APScore3 = ["AP Statistics", "AP Psychology", "AP Physics C: Mechanics"]
#     APScore4 = ["AP Microeconomics", "AP Macroeconomics"]
#     APScore5 = ["AP Calculus BC"]

#     coursesEligible = ApIbConverter(APScore3, APScore4, APScore5)

#     # for course in coursesEligible:
#     #     print("\nCourse: ", course.dptmnt + " " + course.dptmnt_num ,"\n")

#     # print("TESTING MAIN KUPER RATING: ", professorKuper.professorRating)
#     # print("TESTING MAIN KUPER DIFFICULTY: ", professorKuper.professorDifficulty)
#     # print("TESTING THIS IS KUPER: ", professorKuper.professorName)

# if __name__ == '__main__':
#     main()
    