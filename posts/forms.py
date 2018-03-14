from django.forms import ModelForm
from posts.models import Article


class ArticleForm(ModelForm):
    class Meta(ModelForm):
        model = Article
        fields = ('title', 'description')

    def __init__(self, *args, **kwargs):
        """ add bootstrap css classes to forms
        """
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control input', 'placeholder':'Title'})
        self.fields['description'].widget.attrs.update({'class':'form-control', 'placeholder': 'Description (optional)'})


    def clean(self):
        pass
