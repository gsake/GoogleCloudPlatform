# gcp-marketplace

A. Setup the MP builder environment 

1. Create a Debian VM instance in GCP (f1-micro)

2. Install the docker following the guideline:

https://docs.docker.com/engine/install/debian/

3. Execute the following commands:

3.1. sudo apt-get -y update && sudo apt-get install -y wget && sudo apt-get install zip

3.2. sudo wget https://github.com/GoogleCloudPlatform/marketplace-tools/releases/download/v0.1.0/mpdev_linux_amd64_v0.1.0.tar.gz -P /mpdev 

3.3. sudo tar -xf /mpdev/mpdev_linux_amd64_v0.1.0.tar.gz -C /mpdev

B. Example 1: Deploy a Single VM running Wordpress following the guideline:

https://github.com/GoogleCloudPlatform/marketplace-tools/tree/master/examples/deployment-manager/autogen/singlevm






