from django.urls import reverse
from rest_framework import serializers

from presqt.api_v1.utilities import action_checker, link_builder


class SupportedActions(serializers.Serializer):
    """
    Serializer for supported_actions objects inside the Target JSON.
    """
    resource_collection = serializers.BooleanField()
    resource_detail = serializers.BooleanField()
    resource_download = serializers.BooleanField()
    resource_upload = serializers.BooleanField()


class TargetsSerializer(serializers.Serializer):
    """
    Serializer for multiple Target objects.
    """
    name = serializers.CharField(max_length=256)
    supported_actions = SupportedActions()
    supported_hash_algorithms = serializers.StringRelatedField(many=True)
    links = serializers.SerializerMethodField()

    def get_links(self, instance):
        """
        Translate the `links` property to a custom array of Hyperlink values.

        Parameters
        ----------
        instance : Target Obj instance

        Returns
        -------
        A list of hyperlink urls for Target detail API endpoint
        """
        reversed_target_detail = reverse(
            'target', kwargs={'target_name': instance['name']})
        return [{"name": 'Detail', "link": self.context['request'].build_absolute_uri(
            reversed_target_detail), "method": "GET"}]


class TargetSerializer(serializers.Serializer):
    """
    Serializer for a Target object.
    """
    name = serializers.CharField(max_length=256)
    supported_actions = SupportedActions()
    supported_hash_algorithms = serializers.StringRelatedField(many=True)
    links = serializers.SerializerMethodField()

    def get_links(self, instance):
        """
        Translate the `links` property to a custom array of Hyperlink values.

        Parameters
        ----------
        instance : Target Obj instance

        Returns
        -------
        A list of hyperlink urls for Target detail API endpoint
        """
        reversed_collection = reverse('resource_collection', kwargs={
            'target_name': instance['name']})
        return [{"name": "Collection", "link": self.context['request'].build_absolute_uri(
            reversed_collection), "method": "GET"}]
