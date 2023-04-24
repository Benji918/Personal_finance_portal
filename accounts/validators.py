from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


def validate_strong_password(password):
    min_length = 8
    min_digits = 2

    # Validate the password length
    if len(password) < min_length:
        raise serializers.ValidationError(f"Password must be at least {min_length} characters long.")

    # Validate the number of digits in the password
    if sum(1 for c in password if c.isdigit()) < min_digits:
        raise serializers.ValidationError(f"Password must contain at least {min_digits} digits.")

    # Use Django's built-in password validator to check for common password patterns
    validate_password(password)
