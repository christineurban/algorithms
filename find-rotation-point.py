# https://www.interviewcake.com/question/ruby/find-rotation-point

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

def find_rotation_point(words):
    floor_index = 0
    ceiling_index = len(words)-1

    while True:
        mid_index = (ceiling_index-floor_index)/2
    
        # if current word is before previous word
        if words[mid_index] < words[mid_index-1]:
            return words[mid_index]
        # if current word is after previous word and after ceiling
        elif words[mid_index] > words[mid_index-1] and words[mid_index] > words[ceiling_index]:
            floor_index = mid_index+1
        # if current word is after previous word and before ceiling
        elif words[mid_index] > words[mid_index-1] and words[mid_index] < words[ceiling_index]:
            ceiling_index = mid_index-1
        
print find_rotation_point(words)