pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Chiragdarshan/face-recognition-system.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t face-recog-app .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name face-app face-recog-app'
                }
            }
        }
    }
}
