from flask import Blueprint, g
from prahvi.errors import ValidationError, bad_request, not_found
#from ..auth import auth
#from prahvi.decorators import rate_limit

blueprint = Blueprint('api', __name__)


@blueprint.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])


@blueprint.errorhandler(400)
def bad_request_error(e):
    return bad_request('invalid request')


@blueprint.errorhandler(404)
def not_found_error(e):
    return not_found('item not found')


#@api.before_request
#@rate_limit(limit=5, per=15)
#@auth.login_required
#def before_request():
#    pass


@blueprint.after_request
def after_request(response):
    if hasattr(g, 'headers'):
        response.headers.extend(g.headers)
    return response

# do this last to avoid circular dependencies
from prahvi.api.v1 import api 
