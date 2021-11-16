def PowerShell(psCmd) {
    psCmd=psCmd.replaceAll("%", "%%")
    bat "powershell.exe -NonInteractive -ExecutionPolicy Bypass -Command \"\$ErrorActionPreference='Stop';[Console]::OutputEncoding=[System.Text.Encoding]::UTF8;$psCmd;EXIT \$global:LastExitCode\""
}
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
            PowerShell(". '.\\disk-usage.ps1'; du -Verbose")
            powershell(script: """
                Write-Output 'Hello PowerShell!!'
                PowerShell 'docker images -a'
                """)
            
            }
        }
    }
}
