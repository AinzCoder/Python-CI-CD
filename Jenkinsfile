
pipeline {

    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {

        stage('Build') {
            steps {
                echo 'Starting Python build...'

                bat 'py -3.13 --version'

                bat 'py -3.13 -m compileall -q calculator.py test_calculator.py'

                echo 'Python compilation successful!'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'

                bat 'py -3.13 -m venv .venv'

                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'

                bat '.venv\\Scripts\\python.exe -m pytest -v --junitxml=report.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'report.xml'
        }

        success {
            echo 'BUILD SUCCESS: All tests passed!'
        }

        failure {
            echo 'BUILD FAILURE: Check the failed stage and test report.'
        }
    }
}
