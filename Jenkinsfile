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
                        sh 'pytest --html=${WORKSPACE}/report/report.html --self-contained-html --alluredir=${WORKSPACE}@2/allure-results'
                    } catch (exc) {
                            echo 'testcase execute failed......'
                      }
                }
            }
       }

       stage("Apitest Report") {
            steps{
                script {
                    allure([
                        includeProperties:false,
                        reportBuildPolicy:'ALWAYS',
                        jdk:'',
                        results:[[path:'allure-results']],
                    ])

                    publishHTML(target:[
                        reportName:"pytest-html-report",
                        reportDir:"${WORKSPACE}@2/report",
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