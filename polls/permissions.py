from rest_framework import permissions


class IsPollAuthor(permissions.BasePermission):
	message = "Access restricted - only poll authors can view poll results"

	def has_object_permission(self, request, view, obj):
		return request.user == obj.author
