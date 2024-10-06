from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    date = models.DateField()
    note = models.TextField()
    #pomyśleć w późniejszym czasie, jak zachować ślad po usuniętym użytkowniku(personelu medycznym)
    staff_signature = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Report from {self.date} by {self.staff_signature}"
