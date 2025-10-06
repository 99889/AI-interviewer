from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ResumeUploadForm, MissingFieldsForm
from .models import Candidate
from .utils import extract_resume_fields
import os

def upload_resume(request):
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()
            resume_path = candidate.resume.path

            extracted = extract_resume_fields(resume_path)
            candidate.name = extracted.get("name")
            candidate.email = extracted.get("email")
            candidate.phone = extracted.get("phone")
            candidate.save()

            if not all([candidate.name, candidate.email, candidate.phone]):
                return redirect("fill_missing_fields", pk=candidate.pk)
            else:
                return redirect("start_interview", pk=candidate.pk)
    else:
        form = ResumeUploadForm()

    return render(request, "upload_resume.html", {"form": form})


def fill_missing_fields(request, pk):
    candidate = Candidate.objects.get(pk=pk)
    if request.method == "POST":
        form = MissingFieldsForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect("start_interview", pk=candidate.pk)
    else:
        form = MissingFieldsForm(instance=candidate)
    return render(request, "fill_missing_fields.html", {"form": form})
