# is v.s ==
# 'is' is for reference equality. Use it when you would like to know if two references refer to the same object.
# '==' is  for value equality. Use it when you would like to know if two objects have the same value.

'''
(1)
>>> a = 500
>>> b = 500
>>> a == b
True
>>> a is b
False

(2)
>>> c = 200
>>> d = 200
>>> c == d
True
>>> c is d
True

Python caches integer objects in the range -5~256 as singleton instances for performance reasons.
'''

# return an inner function with an outer function
'''
def add(n1):
    def func(n2):
        return n1 + n2
    return func

print(add(1)(2))  # output 3
'''

# lamda (anonymous function)
'''
max = lambda m, n: m if m > n else n
print(max(10, 3))  # output 10
'''

# zip
'''
>>> a = [1, 2, 3] 
>>> b = [4, 5 ,6] 
>>> c = [4, 5, 6, 7, 8] 
>>> zipped = zip(a, b) # zipped = [(1, 4), (2, 5), (3, 6)]

>>> zip(a, c) # Result = [(1, 4), (2, 5), (3 ,6)] 
>>> zip(*zipped) # *zipped -> unzipped， return a two-dimensional array [(1, 2, 3), (4, 5, 6)]

Ex: https://github.com/KBLin1996/NIAC_FaceRecognition/blob/master/opencv.py
for(top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
'''
