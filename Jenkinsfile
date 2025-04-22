pipeline {
    agent any

    environment {
        IMAGE_NAME = "smart_attendence"
        CONTAINER_NAME = "smart_attendence"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "📥 Cloning repository..."
                git branch: 'main', url: 'https://github.com/Chiragdarshan/face-recognition-system.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🐳 Checking Docker version..."
                    sh 'docker version'

                    echo "🔨 Building Docker image: ${IMAGE_NAME}"
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "🛑 Checking if container '${CONTAINER_NAME}' is already running..."
                    def containerStatus = sh(script: "docker ps -q -f name=${CONTAINER_NAME}", returnStdout_
