declare-option str night 'rgb:2b292d'
declare-option str ash   'rgb:383539'
declare-option str umber 'rgb:4d424b'
declare-option str bark  'rgb:6f5d63'
declare-option str mist  'rgb:d1d1e0'
declare-option str sage  'rgb:b1b695'
declare-option str blush 'rgb:fecdb2'
declare-option str coral 'rgb:ffa07a'
declare-option str rose  'rgb:f6b6c9'
declare-option str ember 'rgb:e06b75'
declare-option str honey 'rgb:f5d76e'

set-face global Default            "%opt{blush},%opt{night}"
set-face global PrimarySelection   "%opt{bark}+r"
set-face global PrimaryCursor      "+r"
set-face global SecondarySelection "%opt{umber}+r"
set-face global SecondaryCursor    "%opt{umber}+r"
set-face global LineNumbers        "%opt{bark}"
set-face global LineNumbersCursor  "%opt{blush}"
set-face global LineNumbersWrapped "%opt{bark},%opt{night}+F"
set-face global MenuForeground     "%opt{coral},%opt{ash}+b"
set-face global MenuBackground     "%opt{blush},%opt{ash}"
set-face global MenuInfo           "%opt{blush},%opt{ash}"
set-face global Information        "%opt{blush},%opt{ash}"
set-face global Error              "%opt{ember}"
set-face global DiagnosticError    "%opt{ember}+b"
set-face global DiagnosticWarning  "%opt{honey}+i"
set-face global StatusLine         "%opt{blush},%opt{ash}"
set-face global StatusLineMode     "%opt{rose}"
set-face global StatusLineValue    "%opt{coral}"
set-face global StatusCursor       "%opt{ash},%opt{blush}"
set-face global Prompt             "%opt{coral}"
set-face global MatchingChar       "%opt{night},%opt{bark}"
set-face global WrapMarker         "%opt{bark}"
set-face global BufferPadding      "%opt{night},%opt{night}"

# prog
set-face global value         "%opt{sage}"
set-face global type          "%opt{rose}+i"
set-face global variable      "%opt{blush}"
set-face global module        "%opt{blush}"
set-face global function      "%opt{coral}+b"
set-face global string        "%opt{sage}+i"
set-face global keyword       "%opt{mist}+b"
set-face global operator      "%opt{mist}"
set-face global attribute     "%opt{blush}"
set-face global comment       "%opt{bark}+i"
set-face global documentation "%opt{bark}+bi"
set-face global meta          "%opt{mist}"
set-face global builtin       "%opt{rose}+i"

# markup
set-face global title  "+b"
set-face global header "%opt{sage}+b"
set-face global bold   "+b"
set-face global italic "+i"
set-face global mono   "%opt{bark}"
set-face global block  "%opt{coral}"
set-face global link   "%opt{rose}+u"
set-face global bullet "%opt{bark}"

