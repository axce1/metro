from django import forms

from myclient.models import Naznach


class SearchObjectFront(forms.Form):
    ''' Форма поиска объекта для клиента '''
    search = forms.CharField(label='',
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Номер объекта'}),
                             max_length=30, error_messages={'required': ''})


class SearchMetroFront(forms.Form):
    ''' Форма поиска метро для клиента '''
    search = forms.CharField(label='',
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Станция метро'}),
                             max_length=30, error_messages={'required': ''})


class SearchObjFullFront(forms.Form):
    ''' Форма поиска объекта по параметрам '''
    PREMISE = (
        ('small', 'Маленькое до 20 кв.м.'),
        ('middle', 'Среднее от 20 до 80 кв.м.'),
        ('large', 'Большое до 80 кв.м.')
    )
    REGION = (
        ('1', 'Центер и ТТК'),
        ('2', 'Север'),
        ('3', 'Юг'),
        ('4', 'Восток'),
        ('5', 'Запад'),
        ('6', 'Область')
    )
    PRICE = (
        ('1', '50000'),
        ('2', '100000'),
        ('3', '250000'),
        ('4', '500000'),
        ('5', '1000000'),
        ('6', '10000000'),
    )

    premise = forms.ChoiceField(label='ПОМЕЩЕНИЕ',
                                widget=forms.RadioSelect, choices=PREMISE)
    region = forms.ChoiceField(label='РАЙОНЫ МОСКВЫ',
                               widget=forms.RadioSelect, choices=REGION)
    price = forms.ChoiceField(label='АРЕНДА В МЕСЯЦ',
                              widget=forms.RadioSelect, choices=PRICE)
    naznach = forms.ModelChoiceField(queryset=Naznach.objects.all(),
                                     label='ВИД ДЕЯТЕЛЬНОСТИ',
                                     widget=forms.RadioSelect)
