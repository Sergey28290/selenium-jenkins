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
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    bat 'allure generate allure-results -o allure-report --clean'
                    bat 'powershell -Command "Compress-Archive -Path allure-report -DestinationPath allure-report.zip"'
                }
            }
        }
    }
    post {
        always {
            script {
                def testResult = currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class)
                if (testResult) {
                    def allTests = testResult.getTotalCount()
                    def failedTests = testResult.getFailCount()
                    def skippedTests = testResult.getSkipCount()
                    def passedTests = allTests - failedTests - skippedTests

                    def failedTestCases = testResult.getFailedTests()
                    def failedTestSummary = failedTestCases.collect { testCase ->
                        "${testCase.getFullName()}"
                    }.join("\n")

                    def allureReportPath = "${WORKSPACE}\\allure-report.zip"

                    def emailTemplate = readFile('email-template.html')

                    emailTemplate = emailTemplate
                        .replace('${BUILD_NUMBER}', "${currentBuild.number}")
                        .replace('${ALL_TESTS}', "${allTests}")
                        .replace('${PASSED_TESTS}', "${passedTests}")
                        .replace('${FAILED_TESTS}', "${failedTests}")
                        .replace('${SKIPPED_TESTS}', "${skippedTests}")
                        .replace('${FAILED_TEST_SUMMARY}', "${failedTestSummary}")
                        .replace('${ALLURE_REPORT_PATH}', "${allureReportPath}")

                    emailext(
                        subject: "Результаты тестов для ${currentBuild.number}",
                        body: emailTemplate,
                        to: 'your-email@example.com',
                        attachmentsPattern: 'allure-report.zip'
                    )
                } else {
                    echo 'No test results found.'
                }
            }
        }
    }
}
