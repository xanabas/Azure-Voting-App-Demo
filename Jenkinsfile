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
                /*powershell(script: """
                    Write-Output 'Hello PowerShell!!'
                    
                    Invoke-Command {"docker images -a"}
                """)*/
                script {
                    'touch output.txt'
                    'docker images -a >>> output.txt'
                }
            }
        }
    }// end of stages
    
    post {
        always {
            archiveArtifacts artifacts: './output.txt', fingerprint: false
        }
    }
}
