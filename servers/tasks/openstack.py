
# Imports ###########################################################

from celery import task
from django.contrib.auth import get_user_model


# Tasks #############################################################

@task()
def nova_boot(x, y):
    User = get_user_model()
    openstack_id = User.objects.all()

    # nova boot --image 'ubuntu-precise-12.04-amd64-201308' \
    #           --flavor e.1-cpu.10GB-disk.2GB-ram \
    #           --key_name laptop 
    #           --poll \
    #           --availability_zone bm0007 \
    #           --security_groups edx,default 
    #           edx
    #
    #openstack_id = 'fa5c2162-506d-4d95-af58-0457326edabd'
    return openstack_id
