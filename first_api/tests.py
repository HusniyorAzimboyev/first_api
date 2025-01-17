from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()
class TestViewSet(APITestCase):
    def setUp(self):
        self.User = User.objects.create(username="ali",password="13521h0.")
    def test_user_get(self):
        url = reverse("user-list")
        self.client.force_authenticate(self.User)
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data),1)
    def test_user_post(self):
        url = reverse("user-list")
        self.client.force_authenticate(self.User)
        data = {
            "username":"newUser",
            "password":"newPassword"
        }
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code,201)