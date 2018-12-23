# bitly_automation

## **Instructions to run the tests:**
1. Install Docker and Docker Compose
2. Clone the repo
3. Open command line and navigate to the repo dir
4. Type:
5.  >  docker compose up -d
6. This command will build containers with **Selenium Hub Server, Chrome Node with a VNC server and Jenkins**.
5. There are two options to tun the tests: locally or through Jenkins.
6. In order to watch the tests live on server, please download: https://www.realvnc.com/en/connect/download/viewer/
6.1. open the vnc viewer ,type localhost:5900 on the top navigate bar and click enter.
password is: 'secret'

**Live tests on selenium chrome container***
![alt text](https://i.imgur.com/oPIfgoT.png)


### **Locally**
In order to avoid operating system and python interpator versions problems, I've created a docker image based on python 3.7 with the selenium depandencies. To run the tests just typd in the command line:
> docker run --network bitly_automation_default -e "ENV=production" -e "BROWSER=chrome" imelamed/pytest:3.7

 you can see the tests running live with the vnc viewr.


### **Jenkins**
1. Extract jenkins_data.tar in your $HOME directory:
> tar xopf jenkins_data.tar
2. On command line type:
> docker jenkins restart (Could take up to 5 minutes)
3. Open a browser on your local host and navigate to "http://127.0.0.1:8080/blue/organizations/jenkins/bitly_automation/branches".

4. Hover over the master branch row. On the right, click on the "Play button".
![alt text](https://imgur.com/laqLcI5.jpg)

5. In order to see pipline, click on the Master branch.

6. In order to see test results, click to Test link in the tope menu:
![alt text](https://imgur.com/lgwOwgs.jpg)

![alt text](https://imgur.com/JUSOoh1.jpg)
