Automation with Ansible:

The aim of this project is to deploy a FLASK application into multiple host servers and use a HAproxy server as load balancer to handle the services requests between clients in internet and the remote Host Servers. A Bastion Host is used as a SSH server that can be used to hop into the other hosts in that network, allowing users to automate remote task execution over SSH.
 
Requirements:

5 remote servers all forming an internal network:

Three Host Servers : Host_A Host_B Host_C : These are the Host Servers that carry out the response services to incoming requests. 
Bastion Host: Used to configure the internal network and deploy application using ansible
HAproxy Loadbalancer: Used to handle load across the servers

hosts: contains the inventory of ansible of hostnames
config: contains the SSH configuration of the hosts file
application2.py: contains the flask application code to be run on the host servers
haproxy.cfg.j2: contains the haproxy configuration
site.yaml: contains the code for installation and deployment in HAproxy and Webservers.

The deployment of tasks to the Hosts and HAproxy server is done on the Bastion Host by SSH from a localhost. Ansible playbook is run for the site.yaml code for deployment and automation and is run on the hosts file using command:

ansible-playbook -i hosts site.yaml 

(NOTE: this command can be directly used in the directory where all the files are stored. Else use the path of location of the directory where these codes given in repository are stored.)

On success of the running of above code, Through Bastion Host, we use CURL command on HAproxy server, to get response from one of the webserver.(We have used roundrobin algorithm for the loadbalancing in HAproxy server.).

NGinx as Loadbalancer: additionally Nginx is used as a load balancer to handle SNMP monitoring of backend nodes. The SNMP collected data can be accessed through HAproxy server IP:8011port with '/server_stats'

 
