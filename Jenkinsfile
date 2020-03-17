pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation.'
                  }
                       }
            
        stage('test') {
            steps{
            echo 'Running test cases.'
            }
        }
        
        stage('deploy')  {
            steps{
             input("Do you want to proceed?")   
            }
        }
    }
    post {
        always {
            emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }
    }
}
