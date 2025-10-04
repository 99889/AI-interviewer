
from django.contrib import admin
from .models import Candidate, InterviewSession, Question, Answer

admin.site.register(Candidate)
admin.site.register(InterviewSession)
admin.site.register(Question)
admin.site.register(Answer)
