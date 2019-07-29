from django.contrib import admin

# Register your models here.

from Threshold import models

admin.site.register([
    models.Problem,
    models.Contest,
    models.StudentContest,
    models.Submission
])
