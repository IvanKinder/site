from random import randint

from views import Index, Help, ContactUs

routes = {
    '/': Index(),
    '/help/': Help(),
    '/contact_us/': ContactUs(),
    '/study_programs/': '',
    '/courses_list/': 'ContactUs()',
    '/create_course/': 'ContactUs()',
    '/create_category/': 'ContactUs()',
    '/categories_list/': 'ContactUs()',
    '/copy_course/': 'ContactUs()',
}


def some_front(request):
    request['data'] = randint(0, 50)


def other_front(request):
    request['key'] = 'key'


fronts = [some_front, other_front]
