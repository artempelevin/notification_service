import re

from django.core.exceptions import ValidationError


def phone_validator(phone: str) -> None:
    if not bool(re.fullmatch(r'7\d{10}', phone)):
        raise ValidationError('The phone format should be 7XXXXXXXXXX')


def mobile_operator_validator(mobile_operator: str) -> None:
    if not mobile_operator.isnumeric():
        raise ValidationError('The mobile operator code must be a number')
