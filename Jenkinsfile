pipeline {
    agent any
    
    environment {
        BUILD_SCRIPT = './build.sh'
        PROFILES_ACTIVE_DEV = 'dev'
        PROFILES_ACTIVE_TEST = 'test'
    }

    stages {
        stage('Build') {
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
                        if (env.JOB_NAME.indexOf('test') != -1) {
                           sh 'pytest --html=./report/report.html --self-contained-html --alluredir=${WORKSPACE}/api_test_master/allure-results'
                        }
                        if (env.JOB_NAME.indexOf('dev') != -1) {
                            sh 'pytest --html=./report/report.html --self-contained-html --alluredir=${WORKSPACE}/api_test_master/allure-results'
                        }
                    } catch (exc) {
                            echo 'testcase execute failed......'
                      }
                }
            }
       }

       stage("Apitest Report") {


            steps{
                script {
                    publishHTML(target:[
                        reportName:"pytest-html-report",
                        reportDir:"${WORKSPACE}/report",
                        reportFiles:"report.html",
                        keepAll:true,
                        allowMissing:true,
                        alwaysLinkToLastBuild:false
                    ])
                }
            }
       }
    }
}