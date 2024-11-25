pipeline {
    agent any

    environment {
        CHROMEDRIVER_PATH = "${WORKSPACE}\\chromedriver"
        PATH = "C:\\WINDOWS\\SYSTEM32;${env.PATH}"
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    bat 'python -m venv venv'
                    bat 'call venv\\Scripts\\activate'
                    bat 'pip install -r requirements.txt'
                    bat "set PATH=%PATH%;${CHROMEDRIVER_PATH}"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    bat 'pytest --junitxml=test-reports/report.xml'
                }
                junit 'test-reports/report.xml'
                script {
                    def testResult = currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class)
                    if (testResult) {
                        env.ALL_TESTS = "${testResult.getTotalCount()}"
                        env.FAILED_TESTS = "${testResult.getFailCount()}"
                        env.SKIPPED_TESTS = "${testResult.getSkipCount()}"
                        env.PASSED_TESTS = "${testResult.getTotalCount() - testResult.getFailCount() - testResult.getSkipCount()}"

                        def failedTestCases = testResult.getFailedTests()
                        env.FAILED_TEST_SUMMARY = failedTestCases.collect { it.getFullName() }.join("\n")
                    } else {
                        env.ALL_TESTS = "0"
                        env.FAILED_TESTS = "0"
                        env.SKIPPED_TESTS = "0"
                        env.PASSED_TESTS = "0"
                        env.FAILED_TEST_SUMMARY = "No test failures."
                    }
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    bat 'allure generate allure-results -o allure-report --clean'
                    bat 'powershell -Command "Compress-Archive -Path allure-report -DestinationPath allure-report.zip -Force"'
                }
            }
        }
        stage('Upload to Google Drive') {
            steps {
                script {
                    bat 'gdrive files upload --parent YOUR_FOLDER_ID allure-report.zip'
                    def fileId = bat(script: 'gdrive files list --query "name=\'allure-report.zip\'" --no-header', returnStdout: true).trim().split('\\s+')[0]
                    def link = bat(script: "gdrive files info ${fileId} --fields webViewLink", returnStdout: true).trim().split('\\s+')[1]
                    env.ALLURE_REPORT_LINK = link
                }
            }
        }
    }

    post {
        always {
            script {
                def config = readJSON file: 'recipients.json'
                def recipients = config.recipients.join(',')
                def emailTemplate = readFile('email-template.html')

                emailTemplate = emailTemplate
                    .replace('${BUILD_NUMBER}', "${currentBuild.number}")
                    .replace('${ALL_TESTS}', "${env.ALL_TESTS}")
                    .replace('${PASSED_TESTS}', "${env.PASSED_TESTS}")
                    .replace('${FAILED_TESTS}', "${env.FAILED_TESTS}")
                    .replace('${SKIPPED_TESTS}', "${env.SKIPPED_TESTS}")
                    .replace('${FAILED_TEST_SUMMARY}', "${env.FAILED_TEST_SUMMARY}")
                    .replace('${ALLURE_REPORT_LINK}', "${env.ALLURE_REPORT_LINK}")

                emailext(
                    subject: "Результаты тестов для сборки ${currentBuild.number}",
                    body: emailTemplate,
                    to: recipients,
                    mimeType: 'text/html'
                )
            }
        }
    }
}
