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
            //list docker images on system
                //powershell 'docker images -a'
                
            /*powershell(script: """
                Write-Output 'Hello PowerShell!!'
                powershell 'docker images -a'
                """)
            */
                pwsh(script: 'docker images -a')
            }
        }
    }
}
