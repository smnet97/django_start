from django import forms
from .models import PostModel


class PostCreateForm(forms.ModelForm):
    title_uz = forms.TextInput()

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        print(type(self.fields))
        for k, v in self.fields.items():

            self.fields[k].required = False
        # self.fields['title_uz'].required = True
        # self.fields['title_en'].required = True
        # self.fields['body'].required = False
    class Meta:
        model = PostModel
        # fields = ['title_uz', 'title_ru', 'title_en', 'body', 'image']
        exclude = ['created_at', 'updated_at', 'user', 'post_view', 'title', 'body']




# class PostCreateForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput())
#     body = forms.CharField(widget=forms.Textarea)
#     image = forms.ImageField(widget=forms.FileInput)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'body', 'image']
