# # create awesome forms to collect and build the data we need for our web application.

# from logging import PlaceHolder
# from django import forms
# from .models import Destination, Activity, Testimonial, HeroImage


# # # making a query set that accesses our db.
# # choices = Category.objects.all().values_list('name', 'name')

# # # creating a list to store our query set's values.
# # choice_list = []

# # # appending the choices in our query set to our choice list.
# # for choice in choices:
# #     choice_list.append (choice)


# class DestinationCollectionForm(forms.ModelForm):
#     class Meta:
#         model = Destination
#         fields = ("image", "name", "location", "description",)

#         widgets = {
#             "image" : forms.ImageField(attrs={'class': "form-control"}),
#             "name" : forms.TextInput(attrs={'class': "form-control"}),
#             "location" : forms.TextInput(attrs={'class': "form-control"}),
#             "description" : forms.Textarea()(attrs={'class': "form-control"}),
#         }


# class ActivityCreationForm(forms.ModelForm):
#     class Meta:
#         model = Activity
#         fields = ("name", "category", "description",)

#         widgets = {
#             "name" : forms.TextInput(attrs={'class': "form-control"}),
#             "category" : forms.TextInput(attrs={'class': "form-control"}),
#             "description" : forms.Textarea(attrs={'class': "form-control"}),
#         }











