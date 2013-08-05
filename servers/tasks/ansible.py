
# Imports ###########################################################

from celery import task


# Tasks #############################################################

@task()
def playbook(x, y):
    # ansible-playbook -vvv \
    #                  --user=ubuntu \
    #                  -i ../../edx-flouzo/hosts_production.lst \
    #                  -s \
    #                  --private-key=../../edx-flouzo/id_rsa \
    #                  --extra-vars="secure_dir=../../edx-flouzo" \
    #                  edx_sandbox.yml
    log = '<Insert playbook output log>'
    return log
