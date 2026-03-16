from django import forms


class ServiceRequestForm(forms.Form):
    fname = forms.CharField(label="First Name", max_length=50)
    lname = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=12)

    address = forms.CharField(label="Street address", max_length=100)
    city = forms.CharField(label="City", max_length=50)
    state = forms.CharField(label="State", max_length=20)
    zip = forms.CharField(label="ZIP code", max_length=10)

    windows = forms.IntegerField(label="Number of windows", min_value=5, max_value=50)

    SERVICE_CHOICES = [
        ("inside", "Inside"),
        ("outside", "Outside"),
        ("both", "Inside & Outside"),
    ]

    service = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.RadioSelect)

    day = forms.DateField(label="Preferred date")

    notes = forms.CharField(
        label="Notes",
        required=False,
        widget=forms.Textarea
    )