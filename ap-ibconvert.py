from course import Course


def ApIbConverter(APScore3, APScore4, APScore5):
    print("ENTERED AP IB CONVERTER METHOD")

    apCourses = APScore3 + APScore4 + APScore5
    bioTwentyA = Course(dptmnt='BIO', dptmnt_num='20A', num_credits=5)
    bioTwentyB = Course(dptmnt='BIO', dptmnt_num='20B', num_credits=5)
    cseTen = Course(dptmnt='CSE', dptmnt_num='10', num_credits=5)
    cseFiveJ = Course(dptmnt='CSE', dptmnt_num='5J', num_credits=5)
    econTwo = Course(dptmnt='ECON', dptmnt_num='2', num_credits=5)
    econOne = Course(dptmnt='ECON', dptmnt_num='1', num_credits=5)
    amThree = Course(dptmnt='AM', dptmnt_num='3', num_credits=5)
    mathThree = Course(dptmnt='MATH', dptmnt_num='3', num_credits=5)
    mathElevenA = Course(dptmnt='MATH', dptmnt_num='11A', num_credits=5)
    mathNineteenA = Course(dptmnt='MATH', dptmnt_num='19A', num_credits=5)
    mathElevenB = Course(dptmnt='MATH', dptmnt_num='11B', num_credits=5)
    mathNineteenB = Course(dptmnt='MATH', dptmnt_num='19B', num_credits=5)
    physSixAL = Course(dptmnt='PHYS', dptmnt_num='6A/L', num_credits=6)
    physFiveAL = Course(dptmnt='PHYS', dptmnt_num='5A/L', num_credits=6)
    physSixCN = Course(dptmnt='PHYS', dptmnt_num='6C/N', num_credits=6)
    physFiveCN = Course(dptmnt='PHYS', dptmnt_num='5C/N', num_credits=6)
    psychOne = Course(dptmnt='PSYC', dptmnt_num='1', num_credits=5)
    statFive = Course(dptmnt='STAT', dptmnt_num='5', num_credits=5)
    psychTwo = Course(dptmnt='PSYC', dptmnt_num='2', num_credits=5)
    socThreeB = Course(dptmnt='SOCY', dptmnt_num='3B', num_credits=5)
    # anthTwo = Course(dptmnt='ANTH', dptmnt_num='2', num_credits=5)

    coursesEligible = []

    for courseIter in apCourses:
        
        if courseIter ==  'AP Art History': 
            NotImplemented
        elif courseIter ==  'AP Biology':
            coursesEligible.append(bioTwentyA)
            coursesEligible.append(bioTwentyB)
        elif courseIter ==  'AP Calculus AB':
            if courseIter in APScore3:
                coursesEligible.append(mathThree)
                coursesEligible.append(amThree)
            else:
                coursesEligible.append(mathThree)
                coursesEligible.append(amThree)
                coursesEligible.append(mathElevenA)
                coursesEligible.append(mathNineteenA)
        elif courseIter == 'AP Calculus BC':
            if courseIter in APScore3:
                coursesEligible.append(mathThree)
                coursesEligible.append(amThree)
                coursesEligible.append(mathElevenA)
                coursesEligible.append(mathNineteenA)
            else:
                coursesEligible.append(mathThree)
                coursesEligible.append(amThree)
                coursesEligible.append(mathElevenA)
                coursesEligible.append(mathElevenB)
                coursesEligible.append(mathNineteenA)
                coursesEligible.append(mathNineteenB)
        elif courseIter ==  'AP Computer Science A':
            coursesEligible.append(cseTen)
            coursesEligible.append(cseFiveJ)
        elif courseIter ==  'AP Computer Science Principles':
            coursesEligible.append(cseTen)
        elif courseIter ==  'AP Macroeconomics':
            coursesEligible.append(econTwo)
        elif courseIter ==  'AP Microeconomics':
            coursesEligible.append(econOne)
        elif courseIter ==  'AP Physics C: Electricity and Magnetism':
            coursesEligible.append(physSixAL)
            coursesEligible.append(physSixCN)
            coursesEligible.append(physFiveAL)
            coursesEligible.append(physFiveCN)
        elif courseIter ==  'AP Physics C: Mechanics':
            coursesEligible.append(physSixAL)
            coursesEligible.append(physSixCN)
            coursesEligible.append(physFiveAL)
            coursesEligible.append(physFiveCN)
        elif courseIter ==  'AP Psychology':
            coursesEligible.append(psychOne)
        elif courseIter ==  'AP Statistics':
            coursesEligible.append(statFive)
            coursesEligible.append(psychTwo)
            coursesEligible.append(socThreeB)
        return list(set(coursesEligible))
    

def main():
    
    APScore3 = ["AP Statistics", "AP Psychology", "AP Physics C: Mechanics"]
    APScore4 = ["AP Microeconomics", "AP Macroeconomics"]
    APScore5 = ["AP Calculus BC"]

    coursesEligible = ApIbConverter(APScore3, APScore4, APScore5)

    for course in coursesEligible:
        print("\nCourse: ", course ,"\n")

    # print("TESTING MAIN KUPER RATING: ", professorKuper.professorRating)
    # print("TESTING MAIN KUPER DIFFICULTY: ", professorKuper.professorDifficulty)
    # print("TESTING THIS IS KUPER: ", professorKuper.professorName)

if __name__ == '__main__':
    main()
    