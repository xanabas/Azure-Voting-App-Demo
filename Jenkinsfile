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
                sh """ #!/bin/bash
                       sudo docker images -a
                       cd azure-voting-app-redis/
			sudo docker images -a
			sudo docker build -t jenkins-pipeline .
                        sudo docker images -a
                        cd ..
                   """
                echo "${WORKSPACE}"
            }
        }
    }// end of stages
}
