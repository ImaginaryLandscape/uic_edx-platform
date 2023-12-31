""" Models for the User Tour Experience. """

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserTour(models.Model):
    """
    Model to track which tours a user needs to be shown.

    Note: This does not track which tours a user has seen, only the ones they should.

    .. no_pii:
    """
    class CourseHomeChoices(models.TextChoices):
        EXISTING_USER_TOUR = 'show-existing-user-tour', _('Show existing user tour')
        NEW_USER_TOUR = 'show-new-user-tour', _('Show new user tour')
        NO_TOUR = 'no-tour', _('Do not show user tour')

    course_home_tour_status = models.CharField(
        max_length=50, choices=CourseHomeChoices.choices, default=CourseHomeChoices.NO_TOUR
    )
    show_courseware_tour = models.BooleanField(default=False)
    user = models.OneToOneField(User, related_name='tour', on_delete=models.CASCADE)
