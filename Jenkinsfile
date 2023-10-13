pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                bat 'pip install -r src/requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                bat 'pytest src/test_main.py'
            }
        }
        
        // stage('Deploy') {
        //     steps {
        //         sh 'python deploy.py'
        //     }
        // }
    }
}
