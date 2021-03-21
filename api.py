from flask import Flask
from flask_restful import Resource,Api, reqparse

app = Flask(__name__)
api = Api(app)

STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}

class StudentsList(Resource):
    def get(self):
        return STUDENTS
    # def set(Resource):
        # pass
class Student(Resource):
    def get(self, student_id):
      if student_id not in STUDENTS:
        return "Not found", 404
      else:
        return STUDENTS[student_id]
        
api.add_resource(Student, '/students/<student_id>')
api.add_resource(StudentsList, '/students/')
if __name__ == "__main__":
  app.run(debug=True)