from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(required=False)
    contact = forms.CharField(label="Contact Number", required=False)


class VoteForm(forms.Form):
    CHOICES = [
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('bad', 'Bad'),
    ]

    vote = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )

class CGPAForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    marks = forms.IntegerField(label="Total Marks")

BRAND_CHOICES = [
    ('HP', 'HP'),
    ('Nokia', 'Nokia'),
    ('Samsung', 'Samsung'),
    ('Motorola', 'Motorola'),
    ('Apple', 'Apple'),
]

DEVICE_CHOICES = [
    ('Mobile', 'Mobile'),
    ('Laptop', 'Laptop'),
]

class OrderForm(forms.Form):
    brand = forms.ChoiceField(
        choices=BRAND_CHOICES,
        widget=forms.RadioSelect
    )

    device = forms.MultipleChoiceField(
        choices=DEVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    quantity = forms.IntegerField(min_value=1)

COURSE_CHOICES = [
    ('ASP-XML', 'ASP-XML'),
    ('DotNET', 'DotNET'),
    ('JavaPro', 'JavaPro'),
    ('Unix', 'Unix'),
    ('C', 'C'),
    ('C++', 'C++'),
]

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")

    course = forms.ChoiceField(
        label="Select Course",
        choices=COURSE_CHOICES,
        widget=forms.Select
    )

    feedback = forms.CharField(
        label="Feedback",
        widget=forms.Textarea
    )