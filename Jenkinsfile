pipeline {
    agent any
    
    environment {
        BUILD_SCRIPT = './build.sh'
        PROFILES_ACTIVE_DEV = 'dev'
        PROFILES_ACTIVE_TEST = 'test'
    }

    stages {
        stage('Build Python Image') {
            steps {
                sh '$BUILD_SCRIPT'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'api_pytest:latest'
                }
            }
            steps {
                script {
                    try {
                        sh 'pytest --alluredir=${WORKSPACE}/report'
                        sh 'echo ${WORKSPACE}'
                    } catch (exc) {
                            echo 'testcase execute failed......'
                      }
                }
            }
       }

    }

    post{
        always{
            allure results: [[path: 'report']]
        }
    }
}