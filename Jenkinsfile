pipeline {
    agent any
    stages {
        stage('Test') { 
            agent {
                docker {
                    image 'python:3.7' 
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m pytest -v --junit-xml test-reports/results.xml tests/test_ui.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}
