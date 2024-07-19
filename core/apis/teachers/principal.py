from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema
principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)


@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    all_submited_assignments = Teacher.get_all_teachers()
    teachers_assignments_dump = TeacherSchema().dump(all_submited_assignments, many=True)
    return APIResponse.respond(data=teachers_assignments_dump)
