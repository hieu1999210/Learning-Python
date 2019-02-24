# Feb, 24th, 2019
# This is an exercise from Vietnamese data structures and algorithms book by Nguyen Duc Nghia, p. 34


# There are n people in a meeting.
# A person is considered to be a special one of he/she knows no one in the meating,
# but everyone else knows he/she.
# Find a algorithm to find such special one (if any) in the meeting with time complexity of O(n).
# Given that the relationships of these n people can be represented by a n by n matrix A 
# that a[ij] = 1 if person i knows person j, = 0 if person i does not person j,
# and a[ii] = 1 for all is from 1 to n.   

# first of all, it is clear that there is at most 1 special person in the meeting
def findTheSpecialOne (matrix):
    
    PeopleNum = len(matrix)
    
    #chose a pair of people 
    firstPerson_index = 0
    secondPerson_index = 1

    while secondPerson_index < PeopleNum:

        # if the first person knows the second one:
        if matrix[firstPerson_index][secondPerson_index] == 0:
            #  then the second one definitely is not the special one
            
            # chose another person
            secondPerson_index +=1
        else:
            # if not, the first person is not the special one

            #chose another one
            firstPerson_index = secondPerson_index +1
            (firstPerson_index,secondPerson_index) = (secondPerson_index,firstPerson_index)

            # the index implementation ensures that 
            # i.   Index the second always higher than the first one.
            # ii.  All the people have lower indexes than the first person, or between the first and the second (if any) are not the special one.
            # iii. Those have higher indexes than the second one are not considered yet.

    # after the while loop there only one person left.
    # check if this is the special one
    for i in range(PeopleNum):
        #check if everyone knows s/he:
        if matrix[i][firstPerson_index] == 0:
            return "No special one"
        # check if s/he knows anybody:
        if matrix[firstPerson_index][i] == 1 and i != firstPerson_index:
            return "No special one"
    return firstPerson_index + 1

def testFindTheSpecialOne():
    matrix = [
                [1, 0, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [1, 0, 1, 1, 1],
                [0, 0, 0, 1, 0],
                [1, 1, 1, 1, 1]
             ]
    print(findTheSpecialOne(matrix))

testFindTheSpecialOne()


