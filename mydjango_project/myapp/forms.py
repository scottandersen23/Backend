from django import forms
from .models import Post, Comment, Subscriber


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags", "image"]  # Adjust fields as needed
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 10}
            ),  # Optional: Adjust textarea size
        }

    def __str__(self):
        return self.instance.title  # Use the post's title for string representation


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __str__(self):
        return self.cleaned_data.get("content")[:20]  # Truncate comment preview


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email"]

    def __str__(self):
        return self.cleaned_data.get("email")
