pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    bat 'python -m venv venv'
                    bat 'call venv\\Scripts\\activate'
                    bat 'pip install -r requirements.txt'
                    bat 'set PATH=%PATH%;%WORKSPACE%\\chromedriver'
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
                    bat 'powershell Compress-Archive -Path allure-report -DestinationPath allure-report.zip'
                }
            }
        }
    }
    post {
        always {
            script {
                emailext(
                    subject: "Результаты тестов для ${currentBuild.number}",
                    body: """
                        <html>
                        <body>
                          <h1>Результаты тестов для билда ${currentBuild.number}</h1>
                          <p>Всего тестов: ${currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class).getTotalCount()}</p>
                          <p>Пройденные тесты: ${currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class).getTotalCount() - currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class).getFailCount() - currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class).getSkipCount()}</p>
                          <p>Проваленные тесты: ${currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class).getFailCount()}</p>
                          <p>Пропущенные тесты: ${currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class).getSkipCount()}</p>
                          <h2>Саммари по проваленным:</h2>
                          <pre>${currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class).getFailedTests().collect { testCase -> "${testCase.getFullName()}" }.join("\n")}</pre>
                          <h2>Отчет Allure:</h2>
                          <p><a href="${currentBuild.rawBuild.getWorkspace().child("allure-report.zip").getRemote()}">Скачать Allure отчет</a></p>
                        </body>
                        </html>
                    """,
                    attachmentsPattern: '**/allure-report.zip'
                )
            }
        }
    }
}
