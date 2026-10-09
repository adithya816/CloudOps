
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'cloudops-app'
        IMAGE_TAG = 'latest'
        CONTAINER_NAME = 'cloudops-container'
        DOCKER_NETWORK = 'app-net'
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

        stage('Deploy') {
            steps {
                sh '''
                    docker network inspect ${DOCKER_NETWORK} >/dev/null
                    docker rm -f ${CONTAINER_NAME} 2>/dev/null || true
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        --network ${DOCKER_NETWORK} \
                        -p 5000:5000 \
                        ${IMAGE_NAME}:${IMAGE_TAG}

                    sleep 5
                    docker inspect -f '{{.State.Running}}' ${CONTAINER_NAME} | grep -q true
                    curl --fail --silent --show-error http://localhost:5000/health
                '''
            }
        }
    }

    post {
        success {
            echo 'CloudOps pipeline completed successfully, including deployment!'
        }
        failure {
            echo 'CloudOps pipeline failed. Check the console output.'
        }
    }
}
