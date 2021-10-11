from django.http import response
from django.test import TestCase
from .models import CDB

# Teste Post
class TestPost(TestCase):
    def TestRequestMessage(self):
        data = {
            "investmentDate": "2016-11-14",
            "cdbRate": 103.5,
            "currentDate": "2016-12-26"
        }
        response = self.client.post("/cdb/",data=data)
        self.assertEqual(CDB.objects.count(),1)