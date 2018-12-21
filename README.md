# bitly_automation

## **Instructions to run the tests:**
1. Install Docker and Docker Compose
2. Clone the repo
3. Open command line and navigate to the repo dir
4. Type:
5.  >  docker compose up -d
6. This command will build containers with Selenium Hub Server, Chrome Node with a VNC server and Jenkins.
5. There are two options to tun the tests: locally or through Jenkins.

### **Jenkins**
1. Extract jenkins_data tar in you $HOME directory.
2. Open a browser on your local host and navigate to "http://127.0.0.1:8080/blue/organizations/jenkins/bitly_automation/branches".

3. Hover over the master branch.
![alt text](https://i.imgur.com/H95tInk.png)


4. On the right, click on the "Play button":
![alt text](https://i.imgur.com/6yU5DwI.jpg)

5.1 To run locally:
5.1.1 Install python 3.7 on your local machine.
5.1.2 > On command line navigate to bitly_automation and run "pip install pytest"
5.1.3 > Navigte to tests folder and run "pytest --env=production --browser=chrome"
