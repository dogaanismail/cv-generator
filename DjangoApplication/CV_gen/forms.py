from django import forms


class cvDataForm(forms.Form):
    first_name = forms.CharField(label="First Name",
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'id': 'first_name', 'name': 'first_name'}),
                                 required=False)

    last_name = forms.CharField(label="Last Name",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'id': 'last_name', 'name': 'last_name'}),
                                required=False)

    email = forms.CharField(label="Email",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'id': 'email', 'name': 'email'}),
                            required=False)

    phone = forms.CharField(label="Phone Number",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'id': 'phone', 'name': 'phone'}),
                            required=False)

    about_yourself = forms.CharField(label="About Yourself",
                                     widget=forms.Textarea(
                                         attrs={'class': 'form-control', 'id': 'about_yourself',
                                                'name': 'about_yourself'}),
                                     required=False)

    interest = forms.CharField(label="Interest",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'id': 'input_interests', 'name': 'input_interests'}),
                               required=False)

    university = forms.CharField(label="University",
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'id': 'university', 'name': 'university'}),
                                 required=False)

    degree = forms.CharField(label="Degree",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'id': 'degree', 'name': 'degree'}),
                             required=False)

    gpa = forms.DecimalField(label="GPA",
                             widget=forms.NumberInput(
                                 attrs={'class': 'form-control', 'id': 'gpa', 'name': 'gpa'}),
                             required=False)

    job_title = forms.CharField(label="Job Title",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'id': 'job_title', 'name': 'job_title'}),
                                required=False)

    company_name = forms.CharField(label="Company Name",
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'id': 'company_name', 'name': 'company_name'}),
                                   required=False)

    start_date = forms.DateField(label="Start Date",
                                 widget=forms.DateInput(
                                     attrs={'type': 'date', 'class': 'form-control', 'id': 'start_date',
                                            'name': 'start_date'}),
                                 required=False)

    end_date = forms.DateField(label="End Date",
                               widget=forms.DateInput(
                                   attrs={'type': 'date', 'class': 'form-control', 'id': 'end_date',
                                          'name': 'end_date'}),
                               required=False)

    other_information = forms.CharField(label="Other Information",
                                        widget=forms.Textarea(
                                            attrs={'class': 'form-control', 'id': 'other_information',
                                                   'name': 'other_information'}),
                                        required=False)

    skills = forms.CharField(label="Skills",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'id': 'input_skills', 'name': 'input_skills'}),
                             required=False)
