pipeline {
    agent any
    stages {
        stage('Get code from repo') {
            git 'https://github.com/itaymelamed/bitly_automation.git'
        }
        stage('Test') { 
            agent {
                docker {
                    image 'python:3.7' 
                }
            }
            steps {
                dir('bitly_automation') {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest -v --junit-xml test-reports/results.xml tests/test_ui.py'
                }
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}