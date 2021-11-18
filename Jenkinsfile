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
			cd /mnt/d/Zain/Devops/Source/Repos/azure-voting-app-redis/azure-vote/
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
