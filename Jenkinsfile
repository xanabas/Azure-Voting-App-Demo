pipeline {
    agent any
    stages {
        stage('Verify Branch') {
            steps {
                echo "$GIT_BRANCH"
                //echo "hello World"
            }
        }
        stage('Example') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Docker Build'){
            steps{
                powershell(script: """
                    Write-Output 'Hello PowerShell!!'
                    Stop-Job  {"docker images -a"}
                    Invoke-Command {"docker images -a"}
                """)
            }
        }
    }
}
