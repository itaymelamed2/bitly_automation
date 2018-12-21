# bitly_automation

## **Instructions to run the tests:**
1. Install Docker and Docker Compose
2. Clone the repo
3. Open command line and navigate to the repo dir
4. Type "docker compose up -d". This command will build containers with Selenium Hub Server, Chrome Node with a VNC server and Jenkins.
5. There are two options to tun the tests: locally or through Jenkins.
5.1 To run locally:
5.1.1 Install python 3.7 on your local machine.
5.1.2 On command line navigate to bitly_automation and run "pip install pytest"
5.1.3 Navigte to tests folder and run pytest --env=production --browser=chrome
