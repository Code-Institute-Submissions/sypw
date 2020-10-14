from django import forms
from .models import UserProfile, Company


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'company_team', )

    def __init__(self, *args, **kwargs):
        """Add placeholders and classes"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'company_name': 'Name of your Company',
            'company_team': 'How many people do you employ?',
        }
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'border rounded profile-form-input'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'default_company', 'is_manager')

    def __init__(self, *args, **kwargs):
        """Add placeholders and classes"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_county': 'County or State',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border rounded profile-form-input'
            self.fields[field].label = False
