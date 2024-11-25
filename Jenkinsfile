pipeline {
    agent any

    environment {
        CHROMEDRIVER_PATH = "${WORKSPACE}\\chromedriver"
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    powershell 'python -m venv venv'
                    powershell '.\\venv\\Scripts\\Activate.ps1'
                    powershell 'pip install -r requirements.txt'
                    powershell "\$env:PATH += \";${CHROMEDRIVER_PATH}\""
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    powershell 'pytest --junitxml=test-reports/report.xml'
                }
                junit 'test-reports/report.xml'
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    powershell 'allure generate allure-results -o allure-report'
                    powershell 'Compress-Archive -Path allure-report -DestinationPath allure-report.zip'
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

                    emailext(
                        subject: "Результаты тестов для ${currentBuild.number}",
                        body: """
                            <html>
                            <body>
                              <h1>Результаты тестов для билда ${currentBuild.number}</h1>
                              <p>Всего тестов: ${allTests}</p>
                              <p>Пройденные тесты: ${passedTests}</p>
                              <p>Проваленные тесты: ${failedTests}</p>
                              <p>Пропущенные тесты: ${skippedTests}</p>
                              <h2>Саммари по проваленным:</h2>
                              <pre>${failedTestSummary}</pre>
                              <h2>Отчет Allure:</h2>
                              <p><a href="${allureReportPath}">Скачать Allure отчет</a></p>
                            </body>
                            </html>
                        """,
                        to: 'your-email@example.com',
                        attachments: allureReportPath
                    )
                } else {
                    echo 'No test results found.'
                }
            }
        }
    }
}
