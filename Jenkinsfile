pipeline {
    agent master
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
		node ("master"){
			stage('Start test app'){
				steps{
					sh """ #!/bin/bash
							cd /mnt/d/Zain/Devops/Source/Repos/azure-voting-app-redis/
							###sudo docker-compose up -d --no-recreate
							sudo bash ./scripts/test_container.sh
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
		}
        
        stage('Run test python') {
           steps {
                sh """
                        #!/bin/bash
			cd /mnt/d/Zain/Devops/Source/Repos/azure-voting-app-redis/
                        pytest ./tests/test_sample.py
                """
            }
        }
        stage('Stop Test app') {
           steps {
                sh """
                        #!/bin/bash
                        cd /mnt/d/Zain/Devops/Source/Repos/azure-voting-app-redis/
                        sudo docker-compose down
                """
            }
        }
    }// end of stages
}
