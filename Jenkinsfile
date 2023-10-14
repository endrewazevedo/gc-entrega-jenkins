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
                script {
                    def testExitCode = bat returnStatus: true, script: 'pytest src/test_main.py -s'
                    if (testExitCode != 0) {
                        currentBuild.result = 'UNSTABLE'
                    }
                }

                script {
                    def testExitCode = bat returnStatus: true, script: 'py.test --cov=src src/'
                    if (testExitCode != 0) {
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }
    }

    post {
        unstable {
            always()
        }
    }
}
