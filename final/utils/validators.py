import os
from django.core.exceptions import ValidationError
from utils.constants import TASK_ALLOWED_EXTS


def document_size(value):

    if value.size > 10000000000000:
        raise ValidationError('invalid file size')


def document_extension(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in TASK_ALLOWED_EXTS:
        raise ValidationError(f'not allowed ext, allowed ({TASK_ALLOWED_EXTS})')

