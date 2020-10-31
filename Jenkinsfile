pipeline {
  agent any
  stages {
    stage('Git Checkout') {
      steps {
        git 'https://github.com/danieleh11/WorldOfGames.git'
      }
    }
    stage('Build Docker image') {
      steps{
      sh 'echo Building Image'
      sh 'docker-compose build'
      }
    }
    stage('Run Docker Container') {
      steps{
      sh 'echo running Docker container'
      sh 'docker-compose up -d'
      }
    }
    stage('e2e unit test') {
      steps{
      sh 'echo e2e test'
      sh 'python e2e.py'
      }
    }
    stage('Finalize'){
      steps{
      sh 'echo Docker compose down'
      sh 'docker-compose down'
      }
    }  
  }
}