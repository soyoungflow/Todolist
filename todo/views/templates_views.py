from django.shortcuts import render
from ..models import Todo
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy


def todo_list(request):  #  함수형
    todos = Todo.objects.all()
    return render(request, "todo/list.html", {"todos": todos})


class TodoListView(View):  # 클래스형
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, "todo/list.html", {"todos": todos})


class TodoCreateView(CreateView):
    model = Todo
    fields = ["name", "description", "complete", "exp"]
    template_name = "todo/create.html"
    success_url = reverse_lazy("todo:list")


class TodoListGenericView(ListView):  # 제너릭뷰
    model = Todo
    template_name = "todo/list.html"  # 기본값: todo_list.html
    context_object_name = "todos"  # 기본값: object_list


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/detail.html"
    context_object_name = "todo"


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["name", "description", "complete", "exp"]
    template_name = "todo/update.html"
    context_object_name = "todo"
    success_url = reverse_lazy("todo:list")
