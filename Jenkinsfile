pipeline {
    agent any

    environment {
        IMAGE_NAME = "smart_attendence"  // Use lowercase for consistency
        CONTAINER_NAME = "smart_attendence"  // Use lowercase for consistency
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Chiragdarshan/face-recognition-system.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker version'  // To verify Docker is accessible
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Check if the container is already running and stop it if it is
                    def containerStatus = sh(script: "docker ps -q -f name=${CONTAINER_NAME}", returnStdout: true).trim()
                    if (containerStatus) {
                        sh "docker stop ${CONTAINER_NAME}"
                        sh "docker rm ${CONTAINER_NAME}"
                    }

                    // Run the new container
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }
    }
}
