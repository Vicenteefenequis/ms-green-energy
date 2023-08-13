from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.common.models import TimeStampedModel

User = get_user_model()


class Profile(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = "M", _("Male"),
        FEMALE = "F", _("Female"),
        OTHER = "O", _("Other"),
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(verbose_name=_(
        'phone number'), max_length=30, default="+5562982622387")
    about_me = models.TextField(verbose_name=_(
        'about me'), default="say something about yourself")
    gender = models.CharField(
        verbose_name=_("gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20
    )

    city = models.CharField(verbose_name=_(
        "city"), max_length=50, default="Goiânia", blank=False, null=False)

    def __str__(self):
        return f"{self.user.first_name}'s Profile"
