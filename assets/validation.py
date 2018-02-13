from django.core.exceptions import ValidationError
def expansionIMG(value):
    expensions=['jpg','png','jpeg']
    if value in expensions:
        raise ValidationError("Nie poprawene roszerzenie ")
    return value