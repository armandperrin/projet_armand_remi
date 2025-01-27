pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/<votre-utilisateur>/<votre-repo>.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --junitxml=tests-reports/results.xml'
            }
        }
        stage('Generate Reports') {
            steps {
                junit 'tests-reports/results.xml'
            }
        }
    }
}
