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
                // 8501 portunu kullanan tüm containerları durdur
                sh '''
                  for id in $(docker ps -q --filter "publish=8501"); do
                    docker stop $id;
                  done
                '''
            }
        }

        stage('Docker Run (Opsiyonel)') {
            steps {
                sh 'docker run -d --rm --env-file .env -p 8501:8501 $IMAGE_NAME'
            }
        }
    }
}
