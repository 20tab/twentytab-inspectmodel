from django.template import Library
import inspect_model

register = Library()


@register.filter
def inspect_doc(model, field):
    try:
        func = getattr(model, field, None)
        return func.__doc__
    except:
        return ""


@register.filter
def inspect_source(model, field):
    try:
        func = getattr(model, field, None)
        code = inspect_model.getsource(func).replace('\n', '<br />').replace('    ', '&nbsp;&nbsp;&nbsp;&nbsp;')
        return code
    except:
        return ""