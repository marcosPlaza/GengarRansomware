Private Sub AutoOpen()
commando = "powershell.exe echo hola"
ret = Shell(command, 1)
End Sub