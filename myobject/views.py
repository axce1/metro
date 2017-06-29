from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import MyObjectForm, SObjectTypeForm, \
    SObjectMetroForm, SObjectHideForm
from .models import MyObject
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.utils import timezone
from black_list.models import BlackList
from myclient.forms import SerchNameForm
from django.db.models import Q


@login_required
def add_object(request):
    '''Добавление объекта'''
    if request.method == "POST":
        form = MyObjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # Есть ли номер в черном списке
            tel = form.cleaned_data['block_tel']
            if BlackList.objects.filter(tel=tel).exists():
                error = "Номер находится в черном списке"
            else:
                post.my_manager = request.user
                post.save()
                return redirect('my_object')
    else:
        form = MyObjectForm()
        error = ""
    return render(request, 'myobject/add-object.html',
                  {"form": form, 'error': error})


@login_required
def my_object(request):
    '''Мои объекты'''
    forms = {}
    forms['id'] = SerchNameForm(prefix="id")
    forms['adres'] = SerchNameForm(prefix="adres")
    forms['sobs'] = SerchNameForm(prefix="sobs")
    forms['type'] = SObjectTypeForm()
    forms['metro'] = SObjectMetroForm()
    forms['hide'] = SObjectHideForm()
    search = 3545
    if request.method == "POST":
        # Поиск по полям
        forms_id = SerchNameForm(request.POST, prefix="id")
        forms_adres = SerchNameForm(request.POST, prefix="adres")
        forms_sobs = SerchNameForm(request.POST, prefix="sobs")
        my_object = search_form(forms_id, forms_adres, forms_sobs)
        # Поиск по типу
        form_type = SObjectTypeForm(request.POST)
        if form_type.is_valid():
            search = form_type.cleaned_data['typeobj']
            my_object = MyObject.objects.filter(typeobj=search)
        # Поиск по метро
        form_metro = SObjectMetroForm(request.POST)
        if form_metro.is_valid():
            search = form_metro.cleaned_data['station_one']
            my_object = MyObject.objects\
                .filter(Q(station_one=search) | Q(station_two=search))
        # Скрытые/не скрытые
        form_hide = SObjectHideForm(request.POST)
        if form_hide.is_valid():
            search = form_hide.cleaned_data['hide']
            if search == "no":
                my_object = MyObject.objects\
                    .filter(my_manager_id=request.user.id, hide="0")
            else:
                my_object = MyObject.objects\
                    .filter(my_manager_id=request.user.id)
    else:
        my_object = MyObject.objects.filter(my_manager_id=request.user.id)

    return render(request, 'myobject/my-object.html',
                  {"myobjects": my_object, "forms": forms, 'search': search})


def search_form(id_o, adres, sobs):
    '''Обработка поиска по полям'''
    if id_o.is_valid() and id_o.cleaned_data['search'] != '':
        search = id_o.cleaned_data['search']
        query = MyObject.objects.filter(id=search)

    elif adres.is_valid() and adres.cleaned_data['search'] != '':
        search = adres.cleaned_data['search']
        query = MyObject.objects.filter(adres=search)

    elif sobs.is_valid() and sobs.cleaned_data['search'] != '':
        search = sobs.cleaned_data['search']
        query = MyObject.objects\
            .filter(Q(block_name=search) | Q(block_tel=search))
    else:
        query = 0
    return query


@login_required
def hide_obj(request, pk):
    '''Скрыть клиента'''
    hide = MyObject.objects.get(id=pk)
    hide.hide_date = "1970-01-01"
    hide.hide = '1'
    hide.save()
    return redirect('my_object')


@login_required
def show_obj(request, pk):
    '''Открытия клиента'''
    try:
        hide = MyObject.objects.get(id=pk)
        hide.hide_date = "1970-01-01"
        hide.hide = '0'
        hide.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('my_object')


class ObjDelete(LoginRequiredMixin, DeleteView):
    '''Удаление объекта'''
    model = MyObject
    template_name = 'myobject/delete-obj.html'

    # редирект на страницу мои объекты
    def get_success_url(self):
        return reverse('my_object')


class ObjUpdate(LoginRequiredMixin, UpdateView):
    '''Редактирование объекта'''
    model = MyObject
    form_class = MyObjectForm
    template_name = 'myobject/update-obj.html'


class ObjCopy(LoginRequiredMixin, UpdateView):
    '''Копирование объекта'''
    model = MyObject
    template_name = "myobject/copy-obj.html"
    form_class = MyObjectForm

    def form_valid(self, form):
        form.instance.my_manager = self.request.user
        # Для копирования устанавливаю pk и id в None
        form.instance.pk = None
        form.instance.id = None
        form.instance.zvon = timezone.now()
        return super(ObjCopy, self).form_valid(form)


@login_required
def zvon_obj(request, pk):
    '''Прозвон объекта'''
    zvon = MyObject.objects.get(id=pk)
    zvon.zvon = timezone.now()
    zvon.save()
    return redirect('my_object')

def look_obj(request, pk):
    #Просмотр страницы объекта менеджером
    obj = get_list_or_404(MyObject, pk=pk)
    return render(request, 'site/obj-single.html', {'obj_single': obj})
