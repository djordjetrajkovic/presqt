from presqt.targets.github.functions.fetch import github_fetch_resources, github_fetch_resource
from presqt.targets.github.functions.download import github_download_resource 
from presqt.targets.curate_nd.functions.fetch import (
    curate_nd_fetch_resources, curate_nd_fetch_resource)
from presqt.targets.curate_nd.functions.download import curate_nd_download_resource
from presqt.targets.osf.functions.fetch import osf_fetch_resources, osf_fetch_resource
from presqt.targets.osf.functions.download import osf_download_resource
from presqt.targets.osf.functions.upload import osf_upload_resource


class FunctionRouter(object):
    """
    This class acts as a router to allow dynamic function calls based on a given variable.

    Each attribute links to a function. Naming conventions are important. They must match the keys
    we keep in the target.json config file. They are as follows:

    Target Resources Collection:
        {target_name}_resource_collection

    Target Resource Detail:
        {target_name}_resource_detail

    Target Resource Download:
        {target_name}_resource_download

    Target Resource Upload:
        {target_name}_resource_upload

    """
    @classmethod
    def get_function(cls, target_name, action):
        """
        Extracts the getattr() function call to this class method so the code using this class
        is easier to work with.
        """
        return getattr(cls, '{}_{}'.format(target_name, action))

    osf_resource_collection = osf_fetch_resources
    osf_resource_detail = osf_fetch_resource
    osf_resource_download = osf_download_resource
    osf_resource_upload = osf_upload_resource

    curate_nd_resource_collection = curate_nd_fetch_resources
    curate_nd_resource_detail = curate_nd_fetch_resource
    curate_nd_resource_download = curate_nd_download_resource

    github_resource_collection = github_fetch_resources
    github_resource_detail = github_fetch_resource
    github_resource_download = github_download_resource
