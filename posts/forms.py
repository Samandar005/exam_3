from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя',
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        })
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Ваш комментарий',
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        })
    )

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) <= 10:
            raise forms.ValidationError("Комментарий должен быть длиннее 10 символов.")
        return comment
