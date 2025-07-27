pipeline {
    agent any

    environment {
        IMAGE_NAME = 'metin-duzenleme-editoru'
        API_KEY = credentials('OPENAI_API_KEY')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bernakart/metin_duzenleme_editoru.git'
            }
        }

        stage('Create .env') {
            steps {
                writeFile file: '.env', text: "OPENAI_API_KEY=".toString() + API_KEY

            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Run (Opsiyonel)') {
            steps {
                sh 'docker run -d --rm --env-file .env -p 8501:8501 $IMAGE_NAME'
            }
        }
    }
}
