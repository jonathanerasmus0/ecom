from django.test import TestCase,tag, Client
from store import forms
from store.models import Customer
# Create your tests here.

class ShopTestCase( TestCase):
    def test_something(self):
        """Test a feature."""
        print("Testing something.")
    def test_something_else(self):
        """Test another feature."""
        print("Testing something else.")

class StoreTestCase(TestCase):
    def Signupform_is_valid(self):
        

        form = (Customer)
        print("hooray")
        self.assertEqual(form.is_valid(),True)
        


    

