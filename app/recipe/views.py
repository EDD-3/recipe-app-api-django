"""
View for the recipe APIs.

"""

from core.models import Recipe
from recipe import serializers
from rest_framework import authentication, permissions, viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    """Views for manager recipe APIs."""

    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by("-id")
