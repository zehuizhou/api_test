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
                        sh 'rm -rf ${WORKSPACE}/api_test/allure-results'
                        sh 'pytest --alluredir=${WORKSPACE}/api_test/allure-results'
                    } catch (exc) {
                            echo 'testcase execute failed......'
                      }
                }
            }
       }

    }

    post{
        always{
            allure includeProperties:false, jdk:'', results:[[path:'api_test/allure-results']]
        }
    }
}