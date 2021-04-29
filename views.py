from datetime import date

from patterns.creational_patterns import Engine, Logger
from templator import render


site = Engine()
logger = Logger('main')


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class PageNotFound404:
    def __call__(self, request):
        return '404 BAD REQUEST', 'Page not found'


class Help:
    def __call__(self, request):
        return '200 OK', 'some help text'


class ContactUs:
    def __call__(self, request):
        return '200 OK', render('contact_us.html')


class StudyPrograms:
    def __call__(self, request):
        return '200 OK', render('study_programs.html', data=date.today())


class CoursesList:
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', render('course_list.html', objects_list=category.courses, name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'Нет курсов'


class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render('course_list.html', objects_list=category.courses, name=category.name, id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'Нет категорий'


class CreateCategory:

    def __call__(self, request):
        if request['method'] == 'POST':
            print(request)
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
