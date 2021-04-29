from random import randint

from views import Index, Help, ContactUs, StudyPrograms, CoursesList, CreateCourse, CreateCategory, CategoryList, \
    CopyCourse

routes = {
    '/': Index(),
    '/help/': Help(),
    '/contact_us/': ContactUs(),
    '/study_programs/': StudyPrograms(),
    '/courses_list/': CoursesList(),
    '/create_course/': CreateCourse(),
    '/create_category/': CreateCategory(),
    '/categories_list/': CategoryList(),
    '/copy_course/': CopyCourse(),
}


def some_front(request):
    request['data'] = randint(0, 50)


def other_front(request):
    request['key'] = 'key'


fronts = [some_front, other_front]
