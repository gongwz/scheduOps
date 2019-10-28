# _*_ encoding=utf-8 _*_

__author__ = 'weizhen'

from django import forms


class DateTimePickerInput(forms.TextInput):
    template_name = 'formcurd/forms/widgets/datetime_picker.html'
