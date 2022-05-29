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

class PicTestClass(TestCase):

    def setUp(self):
        # Creating a new paparazzo and saving it
        self.neal= Paparazzo(first_name = 'Neal', last_name ='Waga', email ='wn@gmail.com')
        self.neal.save_paparazzo()

        # Creating a new tag and saving it
        self.new_tags = tags(name = 'testing')
        self.new_tags.save()

        self.new_photo= Pic(photo = 'pictures/6_1_of_1.jpg',caption = 'Test caption',paparazzo = self.neal)
        self.new_photo.save()

        self.new_photo.tag.add(self.new_tags)

    def test_get_news_today(self):
        today_art = Pic.todays_art()
        self.assertTrue(len(today_art)>0)

  

    def test_get_art_by_date(self):
        test_date = '2020-06-24'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        art_by_date = Pic.days_news(date)
        self.assertTrue(len(art_by_date) > 0)

    def tearDown(self):
        Paparazzo.objects.all().delete()
        tags.objects.all().delete()
        Pic.objects.all().delete()