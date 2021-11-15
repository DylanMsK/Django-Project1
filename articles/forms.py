from django import forms

from articles import models

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = "__all__"

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = models.Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already is use.")
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        if "office" in title:
            self.add_error("title", "title error")
        content = cleaned_data.get("content")
        if "office" in content:
            self.add_error("title", "content error")
        return cleaned_data
