pipeline {
    agent any

    environment {
        IMAGE_NAME = "Smart_Attendence"
        CONTAINER_NAME = "Smart_Attendence"
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
                    sh "docker build -t smart_attendence ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // check if the container is already running and stop it if it is
                    def containerStatus = sh(script: "docker ps -q -f name=${CONTAINER_NAME}", returnStdout: true).trim()
                    if (containerStatus)
                    {
                        sh "docker stop ${CONTAINER_NAME}"
                        sh "docker rm ${CONTAINER_NAME}"
                    }
            }
        }
    }
}
