from django import forms

# django form
class ServiceRequestForm(forms.Form):
    
    # customer info
    fname = forms.CharField(label="First Name", max_length=50)
    lname = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=12)

    # address fields
    address = forms.CharField(label="Street address", max_length=100)
    city = forms.CharField(label="City", max_length=50)
    state = forms.CharField(label="State", max_length=20)
    zip = forms.CharField(label="ZIP code", max_length=10)

    # radio button selection for number of stories
    stories = forms.ChoiceField(
        choices=[(1, "1"), (2, "2")],
        widget=forms.RadioSelect
    
    )

    # integer field with validation (between 5 and 50) for number of windows
    windows = forms.IntegerField(label="Number of windows", min_value=5, max_value=50)

    # choices for type of service requested
    SERVICE_CHOICES = [
        ("inside", "Inside"),
        ("outside", "Outside"),
        ("both", "Inside & Outside"),
    ]

    # radio buttons for service type
    service = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.RadioSelect)

    # date picker input
    day = forms.DateField(label="Preferred date")

    # optional notes field
    notes = forms.CharField(
        label="Notes",
        required=False,
        widget=forms.Textarea
    )