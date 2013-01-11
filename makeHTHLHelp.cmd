SETLOCAL
rem TODO: adapt
path=%path%;C:\Program Files (x86)\HTML Help Workshop


call make.bat htmlhelp

hhc.exe build\htmlhelp\GitExtensionsDocdoc.hhp
start build\htmlhelp\GitExtensionsDocdoc.chm
