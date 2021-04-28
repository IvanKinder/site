import copy
import quopri


class User:
    pass


class Teacher(User):
    pass


class Student(User):
    pass


# Абстрактная фабрика
class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    # Фабричный метод
    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


# Прототип
class CoursePrototype:

    def clone(self):
        return copy.deepcopy(self)


class Course(CoursePrototype):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)


class InteractiveCourse(Course):
    pass


class RecordedCourse(Course):
    pass


class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


# Абстрактная фабрика
class CourseFactory:
    types = {
        'interactive': InteractiveCourse,
        'recorded': RecordedCourse
    }

    # Фабричный метод
    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for category in self.categories:
            print('category', category.id)
            if category.id == id:
                return category
        raise Exception(f'Нет категории с id = : {id}')

    @staticmethod
    def create_course(type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_course(self, name):
        for course in self.courses:
            if course.name == name:
                return course
