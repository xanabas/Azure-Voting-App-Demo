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
        stage('Start test app'){
            steps{
                sh """ #!/bin/bash
			# Start app line missing
			./scripts/test_container.ps1
                   """
            }
	    post {
		success {
			echo "App started successfully"
		}
		failure {
			echo "App failed to start :("
		}
	    }
        }
	stage {
	   steps {
		sh """ 
			#!/bin/bash
			pytest ./tests/test_sample.py
		"""
	    }
	}
	stage {
	   steps {
		sh """
			#!/bin/bash
			sudo docker-compose down
		"""
	    }
	}
    }// end of stages
}
