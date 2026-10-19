from django.test import TestCase
from rest_framework.test import APIClient
from .engine import detect_skills,recommend,skill_gap
class EngineTests(TestCase):
    def test_detects_skills(self):
        self.assertTrue({"Python","SQL","React"}.issubset(set(detect_skills("Python SQL React project"))))
    def test_data_scientist_match(self):
        self.assertEqual(recommend(["Python","SQL","Statistics","Machine Learning","Data Analysis","Pandas","Data Visualization"])[0]["title"],"Data Scientist")
    def test_gap(self): self.assertTrue(skill_gap(["Python"],"Data Scientist")["missing_skills"])
class ApiTests(TestCase):
    def setUp(self): self.client=APIClient()
    def test_health(self): self.assertEqual(self.client.get("/api/health/").status_code,200)
    def test_recommend(self): self.assertEqual(len(self.client.post("/api/recommend/",{"skills":["Python"]},format="json").data["recommendations"]),5)
    def test_invalid_extension(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        self.assertEqual(self.client.post("/api/resume/parse/",{"resume":SimpleUploadedFile("a.txt",b"hi")},format="multipart").status_code,400)
