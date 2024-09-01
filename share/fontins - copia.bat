reg import fuente.reg
copy /Y aAreaStencil.ttf %windir%\fonts
sc stop FontCache
del %windir%\system32\FNTCACHE.DAT
sc start FOntCache