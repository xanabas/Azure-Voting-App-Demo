pipeline {
    agent any

    stages {
        stage('Verify Branch') {
            steps {
                echo "$GIT_BRANCH"
                //echo "hello World"
            }
        }
        stage('Docker Build'){
            steps{
            //list docker images on system
            //powershell 'docker images -a'
            powershell(script: """
                Write-Output 'Hello PowerShell!!'
                pwsh docker images -a
                """)
            
            }
        }
    }
}
