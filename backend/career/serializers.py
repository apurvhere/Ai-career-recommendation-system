from rest_framework import serializers
from .models import AnalysisRecord
class ResumeUploadSerializer(serializers.Serializer):
    resume = serializers.FileField()
    def validate_resume(self, value):
        if value.size > 5*1024*1024: raise serializers.ValidationError("Maximum file size is 5 MB.")
        ext=value.name.lower().rsplit(".",1)[-1] if "." in value.name else ""
        if ext not in {"pdf","docx"}: raise serializers.ValidationError("Upload a PDF or DOCX file.")
        return value
class SkillsSerializer(serializers.Serializer):
    skills=serializers.ListField(child=serializers.CharField(max_length=80),allow_empty=True)
class SkillGapSerializer(SkillsSerializer):
    career=serializers.CharField(max_length=120)
class AnalysisRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnalysisRecord
        fields=["id","created_at","candidate_name","skills","recommendations","selected_career"]
