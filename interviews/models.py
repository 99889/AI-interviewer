from django.db import models


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    final_score = models.FloatField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.name) if self.name else "Unnamed Candidate"


class InterviewSession(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="in-progress")  # in-progress | completed
    current_question = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Session {self.id} - {str(self.candidate)}"


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    session = models.ForeignKey(InterviewSession, on_delete=models.CASCADE)
    text = models.TextField()
    difficulty = models.CharField(max_length=10)  # Easy, Medium, Hard  
    order = models.IntegerField()

    def __str__(self) -> str:
        return f"Q{self.order} ({self.difficulty}) - {self.text[:30]}..."


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    session = models.ForeignKey(InterviewSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField()
    score = models.FloatField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Answer to Q{self.question.order} (Score: {self.score})"
