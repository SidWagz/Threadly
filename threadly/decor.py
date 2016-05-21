
from functools import wraps
from flask import request, render_template

def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint.replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            print(f.__name__)
            print(args, kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)

        return decorated_function
    return decorator

def two_way_templated(get_template=None, post_template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            get_template_name = get_template
            post_template_name = post_template

            ctx = f(*args, **kwargs)
            print(f.__name__)
            print(args, kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx

            if request.method == 'GET':
                print(request.method)
                print(get_template_name)
                if get_template_name is None:
                    return ctx
                else:
                    return render_template(get_template_name, **ctx)

            if request.method == 'POST':
                print(request.method)
                print(post_template_name)
                if post_template_name is None:
                    return ctx
                else:
                    return render_template(post_template_name, **ctx)

        return decorated_function
    return decorator
