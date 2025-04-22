pipeline {
    agent any

    environment {
        IMAGE_NAME = "smart_attendence"
        CONTAINER_NAME = "smart_attendence"
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
                    sh 'docker version'
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    def containerStatus = sh(script: "docker ps -q -f name=${CONTAINER_NAME}", returnStdout: true).trim()
                    
                    if (containerStatus) {
                        sh "docker stop ${CONTAINER_NAME}"
                        sh "docker rm ${CONTAINER_NAME}"
                    }

                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }
    }
}
