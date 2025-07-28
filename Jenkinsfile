pipeline {
    agent any

    environment {
        IMAGE_NAME = 'metin-duzenleme-editoru'
        API_KEY = credentials('OPENAI_API_KEY')
    }

    stages {
        stage('Check User') {
            steps {
                sh 'whoami'
                sh 'id'
                sh 'ls -l /var/run/docker.sock'
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bernakart/metin_duzenleme_editoru.git'
            }
        }

        stage('Create .env') {
            steps {
                writeFile file: '.env', text: "OPENAI_API_KEY=${API_KEY}"
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Stop (Temizlik)') {
            steps {
                // Aynı image'dan çalışanları durdur
                sh '''
                  docker ps --filter "ancestor=$IMAGE_NAME" -q | xargs -r docker stop || true
                '''
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker run -d --rm --env-file .env -p 8501:8501 $IMAGE_NAME'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'rm -f .env'
            }
        }
    }
}
