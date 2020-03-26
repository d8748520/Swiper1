from django import forms

from user.models import User
from user.models import Profile
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname","gender","birthday","location"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    def clean_max_distance(self):
        cleaned_data = super().clean()  #通过父类 clean()方法数据清洗
        if cleaned_data["max_distance"]<cleaned_data["min_distance"]:
            raise forms.validationError("max_distance 必须大与 min_distance")
        else:
            return cleaned_data["max_distance"]

    def clean_max_dating_age(self):
        cleaned_data = super().clean()  #通过父类 clean()方法数据清洗
        if cleaned_data["max_dating_age"]<cleaned_data["min_dating_age"]:
            raise forms.validationError("max_dating_age 必须大与 min_dating_age")
        else:
            return cleaned_data["max_dating_age"]