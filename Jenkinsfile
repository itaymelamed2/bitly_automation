pipeline {
    agent any
    stages {
        stage('Test') { 
            agent {
                docker {
                    image 'python:3.7'
                    args '--network bitly_automation_default'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'cd tests && pytest -v --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'tests/test-reports/results.xml' 
                }
            }
        }
    }
}
