pipeline {
    agent any

    environment {
        IMAGE_NAME = 'cloudops-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                    ./venv/bin/pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }
    }

    post {
        success {
            echo 'CloudOps pipeline completed successfully!'
        }
        failure {
            echo 'CloudOps pipeline failed. Check the console output.'
        }
    }
}
