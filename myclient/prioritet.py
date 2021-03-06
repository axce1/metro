from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PrioritetForm
from .models import Prioritet
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Список приоритетов
class PrioritetList(LoginRequiredMixin, ListView):
    context_object_name = 'prioritet'
    queryset = Prioritet.objects.all()
    template_name = 'myclient/prioritet/prioritet.html'

# Добавление приоритета
class AddPrioritet(LoginRequiredMixin, CreateView):
    model = Prioritet
    template_name = "myclient/prioritet/add_prioritet.html"
    form_class = PrioritetForm

# Редактирование приоритета
class PrioritetUpdate(LoginRequiredMixin, UpdateView):
    model = Prioritet
    form_class = PrioritetForm
    template_name = 'myclient/prioritet/update.html'

# Удаление приоритета
class PrioritetDelete(LoginRequiredMixin, DeleteView):
    model = Prioritet
    template_name = 'myclient/prioritet/delete.html'

    def get_success_url(self):
        return reverse('prioritet')

# Удаление приоритета
@csrf_exempt
@login_required
def del_prio(request):
    if request.is_ajax():
        if request.method == "POST":
            if 'pk' in  request.POST:
                pk = request.POST.get('pk')
                pk = int(pk)
                post = Prioritet.objects.get(id=pk)
                post.delete()
                return HttpResponse("YES")
    else:
        return HttpResponse("NO")
