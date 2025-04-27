from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re
from .models import Category
from .models import News
from django.core.exceptions import ValidationError
#title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class":"form-control"}))
#CharField просто должен быть небольшой текст # max_legth - максимальное кол-во символов # Verbose_name-имя которое будет указаано вместо titile
#content = forms.CharField(label='Текст', required='false', widget=forms.Textarea(attrs={"class":"form-control",
                                              #                                          'rows': 7}))
#TextField - Текстовое поле предназначеное для большого текста#blank - поле может быть пустым#null- поле не может быть пустым и зстандартное значение NULL
#is_published = forms.BooleanField(label='Опубликовано:', initial=True, required='true')
#photo = forms.ImageField(label='Прикрепить фото',   required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
#BooleanField  - галочка # default - исползуеться для обозначения условий - опублковано или нет
#category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию', widget=forms.Select(attrs={"class":"form-control"}))
class NewsForm(forms.ModelForm) :
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

