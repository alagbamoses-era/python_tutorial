#!/usr/bin/python3



subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']

del subjects[3]

print('New list of subjects after del: ', subjects)

subjects.remove("History")
print('New list of subjects after subjects.remove: ',  subjects)
