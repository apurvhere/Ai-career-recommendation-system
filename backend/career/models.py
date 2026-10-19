from django.db import models
class AnalysisRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    candidate_name = models.CharField(max_length=120, blank=True)
    skills = models.JSONField(default=list)
    recommendations = models.JSONField(default=list)
    selected_career = models.CharField(max_length=120, blank=True)
