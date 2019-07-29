from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Question
from .forms import QuestionForm


class QuestionListView(ListView):
    model = Question


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm


class QuestionDetailView(DetailView):
    model = Question


class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionForm

