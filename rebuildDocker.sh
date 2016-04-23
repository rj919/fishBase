# Define Variables
APP_DOCKER_IMAGE=rc42/fishbase

# Test presence of environmental variable file & trigger build
if [ `ls cred/envDocker.sh` = cred/envDocker.sh ]
then
    # Define Environmental Variables
    source cred/envDocker.sh
    # Initiate Request to Trigger Automated Build
    curl -H "Content-Type: application/json" --data '{"docker_tag": "latest"}' -X POST https://registry.hub.docker.com/u/$APP_DOCKER_IMAGE/trigger/$DOCKER_BUILD_TOKEN/
else
    # Warning about missing environmental variables
    echo rebuildDocker.sh requires cred/envDocker.sh credentials
fi


