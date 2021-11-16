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
                Eg: powershell(". '.Test.ps1'") 
            }
        }
    }
}
