from django import forms

from FruitipediaApp.fruit_app.models import FruitModel


class FruitModelForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class DeleteFruitModelForm(FruitModelForm):
    class Meta:
        model = FruitModel
        fields = ('name', 'image_url', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
