from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

# SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
from charities.models import Benefactor, Charity


class IsBenefactor(BasePermission):

    def has_permission(self, request, view):
        try:
            Benefactor.objects.get(user=request.user) and request.user.is_authenticated
            return True
        except ObjectDoesNotExist:
            return False


class IsCharity(BasePermission):

    def has_permission(self, request, view):
        try:
            Charity.objects.get(user=request.user) and request.user.is_authenticated
            return True
        except ObjectDoesNotExist:
            return False
