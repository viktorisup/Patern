from viktor_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('home.html', date=request.get('date', None))


class About:
    def __call__(self, request):
        return '200 OK', render('about1.html', date=request.get('date', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html', date=request.get('date', None))
