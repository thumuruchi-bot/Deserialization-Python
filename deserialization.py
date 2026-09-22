import pickle

with open("student.pkl", "rb") as file:
    student = pickle.load(file)

print(student)
