from django.shortcuts import render

# Create your views here.
class BaseLoader(View):
    # this class is used to find all catagorys in the database bring them
    # in, and check if a catagory is selected and load things accordingly

    def __init__(self):
        self.catagories = 