pipeline {
    agent any
    
    stages {
        stage('Lint') {
            steps {
                bat 'autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py'
                bat 'isort src --profile black'
                bat 'black src'
            }
        }

        stage('Build') {
            steps {
                bat 'pip install -r src/requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                bat 'pytest src/test_main.py'
                bat 'py.test --cov=src src/'
            }
        }
    }
}
