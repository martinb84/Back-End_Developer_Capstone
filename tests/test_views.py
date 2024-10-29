from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a test user and generate a token
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        
        self.client = APIClient() # If you're testing API views
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  # Add token to headers
        
        # Create a few test instances of the MenuItem model
        self.item1 = MenuItem.objects.create(title="IceCream", price=80.00, inventory=100)
        self.item2 = MenuItem.objects.create(title="Pizza", price=120.00, inventory=5)
        self.item3 = MenuItem.objects.create(title="Burger", price=50.00, inventory=15)
        
    def test_getall(self):
        #Get all the MenuItems via the view
        response = self.client.get(reverse('menu')) # Replace 'menu' with the correct URL name for your view
        
        #Serialize the data (for comparison)
        items = MenuItem.objects.all()
        serialized_items = MenuItemSerializer(items, many=True).data
        
        #Run the assertion to check if serialized data equals the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_items)