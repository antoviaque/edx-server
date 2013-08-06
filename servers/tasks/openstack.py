
# Imports ###########################################################

from celery import task
from django.conf import settings
from novaclient.exceptions import NotFound
from novaclient.v1_1 import client


# Tasks #############################################################

@task()
def nova_boot(vm_name):
    """
    Launch new image with `vm_name`
    """
    
    nova = client.Client(settings.OS_USERNAME,
                         settings.OS_PASSWORD,
                         settings.OS_TENANT_NAME,
                         settings.OS_AUTH_URL,
                         service_type="compute")
    image = nova.images.find(name=settings.OS_BASE_IMAGE)
    flavor = nova.flavors.find(name='m1.small')
    
    # Check that server doesn't already exist with same name
    try:
        server = nova.servers.find(name=vm_name)
    except NotFound:
        pass
    else:
        raise KeyError, 'VM "{0}" already exists'.format(vm_name)

    server = nova.servers.create(name=vm_name,
                                 image=image,
                                 flavor=flavor,
                                 availability_zone=settings.OS_AVAILABILITY_ZONE,
                                 security_groups=[
                                     'default', 
                                     settings.OS_SECURITY_GROUP_SINGLEVM],
                                 key_name=settings.OS_KEY_NAME)
    #                            meta={'foo': 'bar'},
    #                            userdata="hello moto",
    #                            files={
    #                               '/etc/passwd': 'some data', # a file
    #                               '/tmp/foo.txt': StringIO.StringIO('data'), # a stream

    return server.id
