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
                powershell (script: 'docker images -a')
                
            /*powershell(script: """
                Write-Output 'Hello PowerShell!!'
                PowerShell 'docker images -a'
                """)
            */
            }
        }
    }
}
