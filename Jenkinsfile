pipeline {
    agent none
    stages {
        stage('Test') { 
            agent {
                docker {
                    image 'python:3.7' 
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest -v --junit-xml test-reports/results.xml tests/test_ui.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}