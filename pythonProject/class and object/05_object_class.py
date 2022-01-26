class teacher:

    def teaching(self):

        return 'Teacher is teaching'

    class student:                #class inside class

        def studying(self):

           return 'Students are studying'



x1=teacher()

print(x1.teaching())

x2=teacher.student()

print(x2.studying())