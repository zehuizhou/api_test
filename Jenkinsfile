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
                        cd ${WORKSPACE}/api_test
                        sh 'pytest --alluredir=allure-results'
                    } catch (exc) {
                            echo 'testcase execute failed......'
                      }
                }
            }
       }

    }

    post{
        always{
            allure includeProperties:false, jdk:'', results:[[path:'**/allure-results']]
        }
    }
}