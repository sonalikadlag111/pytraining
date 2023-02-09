class Animal:
    def __init__(self, species, gender):
     self.species = species
     self.gender = gender


fluffy = Animal('Dog', 'famale')
print(fluffy.gender,fluffy.species)

# class panda:
#     def __init__(self, studentName, RollNo, MobNo):
#         self.studentName = studentName
#         self.RollNo = RollNo
#         self.MobNo = MobNo
#
#     def __repr__(self):
#         return repr("studentName is " + self.studentName + "Roll No :-" + str(self.RollNo) + "Mob No" + str(self.MobNo))
#
#
# name = panda("shubhz", 12, 9022884536)
#
# print(name)
# repr(name)


