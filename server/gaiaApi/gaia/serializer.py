from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    date = serializers.CharField(allow_blank=False)
    sentiment = serializers.CharField(allow_blank=False)
    title = serializers.CharField(allow_blank=False)
    description = serializers.CharField(allow_blank=False)
    article_id = serializers.CharField(allow_blank=False)
    url = serializers.URLField(allow_blank=False)
    brand = serializers.CharField(allow_blank=False)

class ArticlesSerializer(serializers.Serializer):
    prev = serializers.URLField()
    next = serializers.URLField(allow_blank=False)
    results = serializers.ListField(child=ArticleSerializer())

class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=False)
    score = serializers.FloatField(max_value=1.0, min_value=0)
    sentiment = serializers.CharField(allow_blank=False)