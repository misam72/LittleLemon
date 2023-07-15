from django.test import TestCase
from Restaurant.models import menu
from Restaurant.serializers import MenuSerializer


class TestMenu(TestCase):
    def setUp(self):
        self.item = menu.objects.create(title="Ice Cream", price=10, inventory=2)

    
    def test_menu(self):
        item_str = self.item.get_item()
        
        self.assertEqual(item_str, "Ice Cream: 10")
