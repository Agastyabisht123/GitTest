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
            echo 'Running test.'
            }
        }
        
        stage('deploy')  {
            steps{
             input("Do you want to proceed?")   
            }
        }
    }
}
