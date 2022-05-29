from django.test import TestCase
from .models import *
from datetime import dt


# Create your tests here.
class PaparazzoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.neal= Paparazzo(first_name = 'Neal', last_name ='Waga', email ='nw@gmail.com')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neal,Paparazzo))

    # Testing Save Method
    def test_save_method(self):
        self.neal.save_paparazzo()
        paparazzo = Paparazzo.objects.all()
        self.assertTrue(len(paparazzo) > 0)

