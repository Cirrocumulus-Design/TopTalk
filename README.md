# SA Top 100 Talkers

**Displays the top 100 talkers of a Cisco ASA on a local web page using ansible, python. and a little shell scripting.**

## Equipment used:
* Workstation w/ Ubuntu 16.04.6 LTS (Any linux should do)
	* Apache2 web server
	* Python 2.7/3.0
	* Ansible
* ASA 5505 asa917-16-k8.bin


## Preparing the workstation:
Using the package manager (apt / yum) get the latest updates and install Apache2, and Ansible. Since most linux distros come with python already installed, type "which python" at the command line to see if python is installed.

## Setting up ansible:
Once ansible is installed, it should be ready out of the box. The ansible config file typically lives in the /etc/ansible directory. But by, putting the ansible.cfg file in the directory with your playbooks will override the ansible defaults and allow you to customize the ansible environment to your needs.

Before we start playing with the ansible config though, we need a directory structure. This playbook is built on this structure:


 ~/playbooks  

   |- toptalk  
	  
      |- files  
		   
      |- vars  
		   

Where the top talk directory contains the ansible config file, playbook yml file, and the inventory, .vault_pass, and the .gitignore files. The {dot}filenames will be explained later. 

Clone the repo to you local workstation. If you need more information on how to setup and use GitHub on your linux workstation see - https://www.howtoforge.com/tutorial/install-git-and-github-on-ubuntu/

Create a directory named playbooks in your user directory, and copy the toptalk directory and folders to the new playbook directory.

## Ansible configuration file:
Since this is an exercise in security, and is automation for a security appliance, we need to be conscious about plain text passwords. The main engine of this "application" is cron. Cron jobs run application at defined intervals, in this case every 5 minutes. Without embedding plain text password into the cron job table (crontab), this ansible playbook will fail because we are using ansible vault to secure the ASA password and secret. Therefore we need to build our script using a vault password file readable only by root. We can pass that argument to ansible using the ansible configuration file (ansible.cfg)

The ansible configuration file looks like this:

[defaults]
inventory = ./inventory 
vault_password_file = ./.vault_pass

A sample .vault-sample_pass is included.

This example is point to the local directory inventory file because I'm lazy and don't want to put the inventory location argument on the command line to run my ansible playbooks.

You should also notice the .vault_pass, this file with just contains only the vault password which gets created when you encrypt a file or a phrase on the command line. 

***IMPORTANT**
If you back your script up on to a GitHub site , be sure to have a .gitignore file. This file contains a list of file names to exclude when uploading or updating files to a GitHub site. You should include the .vault_pass to prevent your vault password from being pushed out to the wild.*

## Preparing the Web Server
Once apache2 is installed, it should be ready to run out of the box for most linux distros. Typical installations put the DocumentRoot at /var/www/html. Check your apache or http conf files for this location.

The ansible playbook writes data to a directory named data inside the DocumentRoot folder. This directory along with css and scripts need to be created and have the same rights as the parent directory. The playbook takes data from the ASA and parses it using shell and python scripts into an html table which is ingested into the html page index.html.


 /var  

   |-www  
   
       |- html  
       
             |- data  
	     
             |- css  
	     
             |- scripts  
	     

Place the index.html file into the html directory, or wherever your DocumentRoot folder is located. This html page uses some html5 constructs, so be sure to copy the style.css to the css folder and the functions.js to the scripts folder.

## Setting up the playbook:
You will need to edit the inventory and vars/vars.yml files for this playbook to work in your environment. Instructions are provided inside those files. Once the modification have been made, you are ready to test. Be sure to edit and rename the .vault-sample_pass file.

To test the script from the command line do the following:
   Make sure you are in the playbooks/toptalk directory
	pwd
   Run the playbook
        sudo ansible-playbook toptalk.yml

Once the playbook is confirmed to run clean with no errors, it is time to turn it up by adding it to a cron job.

## Starting cron job to run the play book:

This application uses cron to keep the data from the ASA up to date: Once you have run you playbooks without errors, use the command sudo crontab -e, enter you credentials, and paste the following line at the end of the file.

*/1 * * * * cd /home/[your_user_name]/playbooks/toptalk && ansible-playbook toptalk.yml >/dev/null 2>&1

Save the file, and the TopTalk page should update every 5 minutes.

***For problems or questions about this script contact:
Mark Rogers
mark.rogers@wwt.com***

## Author
Mark Rogers, SDN Architect, World Wide Technology

"*made on a Mac*" ask me about the right way to setup python on MacOS
