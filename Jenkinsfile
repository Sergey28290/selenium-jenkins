pipeline {
    agent any

    environment {
        CHROMEDRIVER_PATH = "${WORKSPACE}\\chromedriver"
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
                    bat 'pytest'
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    bat 'allure generate allure-results -o allure-report'
                    powershell 'Compress-Archive -Path allure-report -DestinationPath allure-report.zip'
                }
            }
        }
    }
    post {
        always {
            script {
                def testResult = currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class)
                def allTests = testResult.getTotalCount()
                def failedTests = testResult.getFailCount()
                def skippedTests = testResult.getSkipCount()
                def passedTests = allTests - failedTests - skippedTests

                def failedTestCases = testResult.getFailedTests()
                def failedTestSummary = failedTestCases.collect { testCase ->
                    "${testCase.getFullName()}"
                }.join("\n")

                def allureReportPath = "${WORKSPACE}\\allure-report.zip"

                emailext(
                    subject: "Test Results for ${currentBuild.number}",
                    body: """
                        <html>
                        <body>
                          <h1>Test Results for Build ${currentBuild.number}</h1>
                          <p>Total Tests: ${allTests}</p>
                          <p>Passed Tests: ${passedTests}</p>
                          <p>Failed Tests: ${failedTests}</p>
                          <p>Skipped Tests: ${skippedTests}</p>
                          <h2>Failed Test Summary:</h2>
                          <pre>${failedTestSummary}</pre>
                          <h2>Allure Report:</h2>
                          <p><a href="${allureReportPath}">Download Allure Report</a></p>
                        </body>
                        </html>
                    """,
                    to: 'your-email@example.com',  // Укажите ваш email
                    attachments: allureReportPath
                )
            }
        }
    }
}
