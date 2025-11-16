from django.forms import ModelForm
from django import forms
from .models import Portfolio, Review, Category, Stock

class CustomModelChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return obj.name 

class PortfolioForm(ModelForm):

    related_object = CustomModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Portfolio
        fields = ['name', 'description', 'related_object', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker']

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body']

        labels = {
            'body': 'Discuss portfolio'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})