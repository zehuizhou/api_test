pipeline {
    agent any
    
    environment {
        BUILD_SCRIPT = './build.sh'
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
                        sh 'pytest --alluredir=/var/jenkins_home/workspace/api_test_master/report'
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
            allure includeProperties:false, jdk:'', results:[[path:'report']]
        }
    }
}
