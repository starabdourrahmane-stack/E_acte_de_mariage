from django.core.exceptions import ValidationError

class ContainsletterValidator:
    def validate(self, password, user= None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'le mot de passe doit contenir une lettre',
                 code ='password_no_letter'            )
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'

# Mot de passe contain un chiffre
class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any (character.isdigit() for character in password):
            raise ValidationError('le mot de passe doit contenir un chiffre', code='password_no_number')
    def get_help_text(self):
        return 'le mot de passe doit contenir au moins un chiffre'