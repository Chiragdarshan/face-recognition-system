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
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove existing container if any
                    sh "docker rm -f $CONTAINER_NAME || true"
                    // Run container
                    sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME"
                }
            }
        }
    }
}
