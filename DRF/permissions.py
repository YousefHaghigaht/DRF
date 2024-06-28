from rest_framework.permissions import BasePermission,SAFE_METHODS
from rest_framework.metadata import BaseMetadata


class CustomMetadata(BaseMetadata):

    def determine_metadata(self, request, view):
        return {
            'name' : view.get_view_name(),
            'renderer' : [renderer.media_type for renderer in view.renderer_classes ],
            'parser' : [parser.media_type for parser in view.parser_classes ]
        }


class IsOwnerOrReadOnly(BasePermission):
    message = 'Permission denied.You are not owner'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user

