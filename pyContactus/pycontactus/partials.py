from tg import expose

@expose('pycontactus.templates.little_partial')
def something(name):
    return dict(name=name)