from tkinter import *
from tkinter import ttk
from subprocess import Popen as po
from subprocess import call as rn
from tkinter import messagebox as sms
import os
from pathlib import Path
import webbrowser
os.chdir("/home/estheryj/Descargas/App/share")

def wn():
    
    nm="#303030"
    nf="#0DE7A1"
    ent="<Enter>"
    lv="<Leave>"
    fuente="a Area Stencil"
    back="#151515"
    w=Tk()
    w.title("N3T-JC")
    w.attributes("-alpha",0)
    w.configure(bg=back)
    win=Toplevel()
    win.overrideredirect()
    root=win
    win.configure(bg=back)
    ancho_ventana = 300
    alto_ventana = 400
    orange="#e7650d"

    #IMAGENES USADAS   
    mini=PhotoImage(file="mini.png")

    capture=PhotoImage(file="1.png")

   # capture2=PhotoImage(file="2.png")
    
   # capture3=PhotoImage(file="3.png")

    #icono=PhotoImage(file="logo.png")

    #w.iconbitmap("ico.ico")

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)

    def on_iconify(event):
        win.withdraw()

    def on_deiconify(event):#funcion de disminimizar
        win.deiconify()
    #bindins de ventana
    w.bind("<Map>", on_deiconify)
    w.bind("<Unmap>", on_iconify)

    #MINIATURA DE VENTANA EN BARRA DE TAREAS
    lb2= Label(w, image=capture, bg=back)
    lb2.pack()


        
    def close(): #funcion cerrar
        w.destroy()
        
    def escit(event): #funcion cerrar con argumento event
        w.destroy()

    win.bind("<Key-F4>",escit)
    w.bind("<Key-F4>",escit)

    def minimize():#Funcion de minimizar
        win.withdraw()
        w.iconify()
        
    #__BARRA__TITULO
    barra_titulo=Frame(win,bg="black",height=20,width=300)
    barra_titulo.pack()
    #ITEMS DE BARRA DE TITULO:
    btn_close = Button(barra_titulo, text="X", command=close,font=(fuente,15),bg="black",borderwidth=0,fg="white")
    btn_minimize = Button(barra_titulo, text="-",font=(fuente,15) ,command=minimize,bg="black",borderwidth=0,fg="white")
    title_lb= Label(barra_titulo, text=w.title(),font=(fuente,15) ,fg=nf, bg="black")
    btn_close.pack(side=RIGHT, padx=10, pady=10)
    btn_minimize.pack(side=RIGHT, pady=10)
    title_lb.pack(side=BOTTOM, padx=10, pady=10)
    
    ###FUNCIONES :

    def start_move(event):#FUNCION QUE INICIA LA MOVILIDAD DE LA VENTANa
        win._x = event.x
        win._y = event.y

    def stop_move(event):#FUNCION QUE DETIENE LA MOVILIDAD DE LA VENTANa
        win._x = None
        win._y = None

    def on_move(event):####FUNCIONE DE MOVIMIENTO de la ventana
        deltax = event.x - win._x
        deltay = event.y - win._y
        new_pos = "+{}+{}".format(win.winfo_x() + deltax, win.winfo_y() + deltay)
        win.geometry(new_pos)
        w.geometry(new_pos)

    win.overrideredirect(True)

    win._x = 0
    win._y = 0

    #_BORDE____BARRA__TITULO__BINDINS
    borde = barra_titulo
    borde.pack(side=TOP, fill=BOTH)
    borde.bind("<ButtonPress-1>", start_move)
    borde.bind("<ButtonRelease-1>", stop_move)
    borde.bind("<B1-Motion>", on_move)
    title_lb.bind("<ButtonPress-1>", start_move) 
    title_lb.bind("<ButtonRelease-1>", stop_move)
    title_lb.bind("<B1-Motion>", on_move)

    fps=1500#VARIABLE FPS
    #####____ACCIONES___DE__LOS_BOTONES___DE__WIN#

    def boost():
        #po("wscript boost.vbs")
        loadin.pack()
        loadin["text"]="▄"
        loadin.configure(font=("Comic Sans MS",40))
        loadin.place(x=40,y=180)
        texto1=Label(win,text='''Testeando DNS'S y aplicando la
    mas rapida''',bg=orange,fg="white",font=(fuente,10))
        texto1.pack()
        win.update()
        psico()
        def fin():
            loadin["text"]='''¡¡¡Internet Acelerado!!!'''
            loadin.configure(font=(fuente,15))
            loadin.place(x=20,y=230)
            texto1.destroy()
            psico()
        def lo3():
            loadin["text"]="▄ ▄ ▄"
            win.update()
            texto1["text"]='''finalizando'''
            win.after(fps,fin)
            
        def lo2():
            loadin["text"]="▄ ▄"
            texto1["text"]='''aplicando ajustes'''
            win.update()
            win.after(fps,lo3)
        win.after(fps,lo2)
           
    def btn_mo(event):
        txt39.pack()
        btn_boost["bg"]=nf
        btn_boost["fg"]="white"
        
    def btn_mf(event):
        btn_boost["bg"]=nm
        btn_boost["fg"]="white"
        txt39.forget()
        
    def btn_c(event):
        txt93.pack()
        btn_config["bg"]=orange
        btn_config["fg"]="white"

    def psico():
        def psico2():
            loadin["fg"]=nf
            loadin.update()
            loadin.after(150,psico)
        loadin["fg"]=orange
        loadin.update()
        loadin.after(150,psico2)
    def btn_cc(event):
        txt93.forget()
        btn_config["bg"]=nm
        btn_config["fg"]="white"

        
    #def fwall():po("fab/Fab.exe")
    #def appc():po("cmd /C app.bat")
    #def veri():po("WNetWatcher.exe")

    def clk_cfg():
        lb2.config(image=capture2)
        def wback():
            lb2.config(image=capture)
            fr.destroy()
            bac.destroy()
            fire.destroy()
            view.destroy()
            cmd.destroy()
            txt.destroy()
            rs.destroy()
        def vent(e):
            txt3990.pack()
            view["bg"]=orange
        def ven2(e):
            txt3990.forget()
            view["bg"]=nm
        def fwa(e):
            txt3939.pack()
            fire["bg"]=orange
        def fw(e):
            txt3939.forget()
            fire["bg"]=nm
        def a9(e):
            txt3992.pack()
            cmd["bg"]=orange
        def a3(e):
            txt3992.forget()
            cmd["bg"]=nm
        def b(event):
            bac["bg"]=nf
        def b2(event):
            bac["bg"]=orange
        def reset_CFG():
            po("dnsjumper.exe")
        def rs_CFG(event):
            txt3999.pack()
            rs["bg"]=orange
        def rs_CFG2(event):
            txt3999.forget()
            rs["bg"]=nm
        
        fr=Frame(win,bg=back,width=3000,height=4000)
        
        bac=Button(win,text="<",font=(fuente,24),bg=orange,borderwidth=0,command=wback)
        
        fr.pack()#__SE__PRESENTA EL BOTON
        fr.place(x=0,y=55)#__UBICACION DEL BOTON
        bac.pack()##SE INSERTA EL BOTON EN LA VENTANA
        bac.place(x=0,y=55)#__UBICACION DEL BOTON
        
        fire=Button(win,text="FIREWALL",font=(fuente,24),bg=nm,fg="white",borderwidth=0,command=fwall)
        fire.pack()
        fire.place(x=20,y=270)
        
        view=Button(win,text="VER IP'S",font=(fuente,24),bg=nm,fg="white",borderwidth=0,command=veri)
        view.pack()
        view.place(x=20,y=190)
        
        cmd=Button(win,text="APP DE CMD",font=(fuente,24),bg=nm,fg="white",borderwidth=0,command=appc)
        cmd.pack()
        cmd.place(x=20,y=112)
        
        rs=Button(win,text="DNS JUMPER",font=(fuente,18),bg=nm,fg="white",borderwidth=0,command=reset_CFG)
        rs.pack()
        rs.place(x=20,y=350)
        
        txt=Label(win,text="Configuraciones",font=(fuente,18),bg=back,fg=orange,borderwidth=0)
        txt.pack()
        txt.place(x=45,y=67)
        #Bindins o ejecutores de acciones
        fire.bind(ent,fwa)
        fire.bind(lv,fw)
        cmd.bind(ent,a9)
        cmd.bind(lv,a3)
        view.bind(ent,vent)
        view.bind(lv,ven2)
        bac.bind(ent,b)
        bac.bind(lv,b2)
        rs.bind(ent,rs_CFG)
        rs.bind(lv,rs_CFG2)
        txt3939=Label(win,text='''Bloquea aplicaciones y de permisos a otras
        para usar su internet''',fg="white",bg=orange)
        txt3990=Label(win,text='''Vea la dirección IP de las personas
        conectadas a su wifi''',fg="white",bg=orange)
        txt3992=Label(win,text='''Abra la App de CMD que permite acelerar el internet
        mediante la consola de comandoss''',fg="white",bg=orange)
        txt3999=Label(win,text='''Abra DNSJUMPER pruebe y aplique 
        la mejor DNS para su conexion''',fg="white",bg=orange)
    def ab22(e):
        txt293.pack()
        about_it["bg"]=orange
    def ab2(e):
        txt293.forget()
        about_it["bg"]=nm
    def about():
        lb2.config(image=capture3)
        def wback():
            lb2.config(image=capture)
            fr2.destroy()
            bac2.destroy()
            texto.destroy()
            tx2t.destroy()
        def b3(event):
            bac2["bg"]=nf
        def b4(event):
            bac2["bg"]=orange

        fr2=Frame(win,bg=back,width=3000,height=4000)
        fr2.pack()
        fr2.place(x=0,y=55)
        bac2=Button(win,text="<",font=(fuente,24),bg=orange,borderwidth=0,command=wback)
        bac2.pack()
        bac2.place(x=0,y=55)
        bac2.bind(ent,b3)
        bac2.bind(lv,b4)
        texto=Label(win,text='''N3T-JC
Es una aplicación gratuita 
desarrollada por FrancKEyJC 
para acelerar el internet 
con solo dar un click al
boton "BOOST",el cual cuando
se da click prueba las dns's 
disponibles y aplica la
DNS más rapida.Tambien se 
aplican una serie de ajustes
para mejorar la conexion

Agradecimientos especiales a python 
sordum nircsoft y a GNU.''',font=("Arial Black",10),bg=back,fg="white")
        texto.pack()
        texto.place(x=10,y=108)
        tx2t=Label(win,text="Acerca de ",font=(fuente,18),bg=back,fg=orange,borderwidth=0)
        tx2t.pack()
        tx2t.place(x=45,y=67)
        webbrowser.open("tinyurl.com/franckeychannel")


    #elementos_De__LA___VENTANA__WIN
    btn_boost=Button(win,text="BOOST",font=(fuente,45),command=boost,borderwidth=0,bg=nm,fg="white")
    btn_boost.pack()
    btn_boost.place(x=14,y=80)
    btn_boost.bind("<Enter>",btn_mo)
    btn_boost.bind("<Leave>",btn_mf)

    btn_config=Button(win,text="config",font=(fuente,24),bg=nm,borderwidth=0,fg="white",command=clk_cfg)
    btn_config.pack()
    btn_config.place(x=20,y=280)
    btn_config.bind("<Enter>",btn_c)
    btn_config.bind("<Leave>",btn_cc)

    copyrights=Label(win,text="Made by FrancKEyJC",font=(fuente,15),bg=back,fg=orange)
    copyrights.pack()
    copyrights.place(x=20,y=360)
    loadin=Label(win,text="▄",font=("Comic Sans MS",40),fg=nf,bg=back)

    mins=Label(win,image=mini,bg=back)
    mins.pack()
    mins.place(x=230,y=275)

    txt39=Label(win,text="Clickee aquí para acelerar su internet",fg="white",bg=orange)
    txt93=Label(win,text='''Clickee aquí para ver configuraciones y herramientas 
    extras que trae N3T-JC''',fg="white",bg=orange) 
    txt293=Label(win,text="Clickee aquí para saber más acerca de N3T-JC",fg="white",bg=orange)




    about_it=Button(win,text="?",borderwidth=0,bg=nm,font=(fuente,24),fg="white",command=about)
    about_it.pack()
    about_it.place(x=180,y=280)
    about_it.bind(ent,ab22)
    about_it.bind(lv,ab2)
    win.attributes("-topmost",True)
    def notop():
        win.attributes("-topmost",False)
    win.after(1000,notop)
   
               
    w.mainloop()

def wn_light():
    nm="#363636"
    lll="#363636"
    nf="#0DE7A1"
    ent="<Enter>"
    lv="<Leave>"
    fuente="a Area Stencil"
    back="white"
    w=Tk()
    w.title("N3T-JC")
    w.attributes("-alpha",0)
    w.configure(bg=back)
    win=Toplevel()
    win.overrideredirect()
    root=win
    win.configure(bg=back)
    ancho_ventana = 300
    alto_ventana = 400
    orange="#e7650d"

    #IMAGENES USADAS   
    mini=PhotoImage(file="mini.png")

    capture=PhotoImage(file="1.png")

    capture2=PhotoImage(file="2.png")
    
    capture3=PhotoImage(file="3.png")

    icono=PhotoImage(file="logo.png")

    w.iconbitmap("ico.ico")

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)

    def on_iconify(event):
        win.withdraw()

    def on_deiconify(event):#funcion de disminimizar
        win.deiconify()
    #bindins de ventana
    w.bind("<Map>", on_deiconify)
    w.bind("<Unmap>", on_iconify)

    #MINIATURA DE VENTANA EN BARRA DE TAREAS
    lb2= Label(w, image=capture, bg=back)
    lb2.pack()


        
    def close(): #funcion cerrar
        w.destroy()
        
    def escit(event): #funcion cerrar con argumento event
        w.destroy()

    win.bind("<Key-F4>",escit)
    w.bind("<Key-F4>",escit)

    def minimize():#Funcion de minimizar
        win.withdraw()
        w.iconify()
        
    #__BARRA__TITULO
    barra_titulo=Frame(win,bg=lll,height=20,width=300)
    barra_titulo.pack()
    #ITEMS DE BARRA DE TITULO:
    btn_close = Button(barra_titulo, text="X", command=close,font=(fuente,15),bg=lll,borderwidth=0,fg="white")
    btn_minimize = Button(barra_titulo, text="-",font=(fuente,15) ,command=minimize,bg=lll,borderwidth=0,fg="white")
    title_lb= Label(barra_titulo, text=w.title(),font=(fuente,15) ,fg=nf, bg=lll)
    btn_close.pack(side=RIGHT, padx=10, pady=10)
    btn_minimize.pack(side=RIGHT, pady=10)
    title_lb.pack(side=BOTTOM, padx=10, pady=10)
    
    ###FUNCIONES :

    def start_move(event):#FUNCION QUE INICIA LA MOVILIDAD DE LA VENTANa
        win._x = event.x
        win._y = event.y

    def stop_move(event):#FUNCION QUE DETIENE LA MOVILIDAD DE LA VENTANa
        win._x = None
        win._y = None

    def on_move(event):####FUNCIONE DE MOVIMIENTO de la ventana
        deltax = event.x - win._x
        deltay = event.y - win._y
        new_pos = "+{}+{}".format(win.winfo_x() + deltax, win.winfo_y() + deltay)
        win.geometry(new_pos)
        w.geometry(new_pos)

    win.overrideredirect(True)

    win._x = 0
    win._y = 0

    #_BORDE____BARRA__TITULO__BINDINS
    borde = barra_titulo
    borde.pack(side=TOP, fill=BOTH)
    borde.bind("<ButtonPress-1>", start_move)
    borde.bind("<ButtonRelease-1>", stop_move)
    borde.bind("<B1-Motion>", on_move)
    title_lb.bind("<ButtonPress-1>", start_move) 
    title_lb.bind("<ButtonRelease-1>", stop_move)
    title_lb.bind("<B1-Motion>", on_move)

    fps=1500#VARIABLE FPS
    #####____ACCIONES___DE__LOS_BOTONES___DE__WIN#

    def boost():
        #po("wscript boost.vbs")
        loadin.pack()
        loadin["text"]="▄"
        loadin.configure(font=("Comic Sans MS",40))
        loadin.place(x=40,y=180)
        texto1=Label(win,text='''Testeando DNS'S y aplicando la
    mas rapida''',bg=orange,fg="white",font=(fuente,10))
        texto1.pack()
        win.update()
        psico()
        def fin():
            loadin["text"]='''¡¡¡Internet Acelerado!!!'''
            loadin.configure(font=(fuente,15))
            loadin.place(x=20,y=230)
            texto1.destroy()
            psico()
        def lo3():
            loadin["text"]="▄ ▄ ▄"
            win.update()
            texto1["text"]='''finalizando'''
            win.after(fps,fin)
            
        def lo2():
            loadin["text"]="▄ ▄"
            texto1["text"]='''aplicando ajustes'''
            win.update()
            win.after(fps,lo3)
        win.after(fps,lo2)
           
    def btn_mo(event):
        txt39.pack()
        btn_boost["bg"]=nf
        btn_boost["fg"]="white"
        
    def btn_mf(event):
        btn_boost["bg"]=nm
        btn_boost["fg"]="white"
        txt39.forget()
        
    def btn_c(event):
        txt93.pack()
        btn_config["bg"]=orange
        btn_config["fg"]="white"

    def psico():
        def psico2():
            loadin["fg"]=nf
            loadin.update()
            loadin.after(150,psico)
        loadin["fg"]=orange
        loadin.update()
        loadin.after(150,psico2)
    def btn_cc(event):
        txt93.forget()
        btn_config["bg"]=nm
        btn_config["fg"]="white"

        
    #def fwall():po("fab/Fab.exe")
    #def appc():po("cmd /C app.bat")
    #def veri():po("WNetWatcher.exe")

    def clk_cfg():
        lb2.config(image=capture2)
        def wback():
            lb2.config(image=capture)
            fr.destroy()
            bac.destroy()
            fire.destroy()
            view.destroy()
            cmd.destroy()
            txt.destroy()
            rs.destroy()
        def vent(e):
            txt3990.pack()
            view["bg"]=orange
        def ven2(e):
            txt3990.forget()
            view["bg"]=nm
        def fwa(e):
            txt3939.pack()
            fire["bg"]=orange
        def fw(e):
            txt3939.forget()
            fire["bg"]=nm
        def a9(e):
            txt3992.pack()
            cmd["bg"]=orange
        def a3(e):
            txt3992.forget()
            cmd["bg"]=nm
        def b(event):
            bac["bg"]=nf
        def b2(event):
            bac["bg"]=orange
        def reset_CFG():
            po("dnsjumper.exe")
        def rs_CFG(event):
            txt3999.pack()
            rs["bg"]=orange
        def rs_CFG2(event):
            txt3999.forget()
            rs["bg"]=nm
        
        fr=Frame(win,bg=back,width=3000,height=4000)
        
        bac=Button(win,text="<",font=(fuente,24),bg=orange,borderwidth=0,command=wback)
        
        fr.pack()#__SE__PRESENTA EL BOTON
        fr.place(x=0,y=55)#__UBICACION DEL BOTON
        bac.pack()##SE INSERTA EL BOTON EN LA VENTANA
        bac.place(x=0,y=55)#__UBICACION DEL BOTON
        
        fire=Button(win,text="FIREWALL",font=(fuente,24),bg=nm,fg="white",borderwidth=0,command=fwall)
        fire.pack()
        fire.place(x=20,y=270)
        
        view=Button(win,text="VER IP'S",font=(fuente,24),bg=nm,fg="white",borderwidth=0,command=veri)
        view.pack()
        view.place(x=20,y=190)
        
        cmd=Button(win,text="APP DE CMD",font=(fuente,24),bg=nm,fg="white",borderwidth=0,command=appc)
        cmd.pack()
        cmd.place(x=20,y=112)
        
        rs=Button(win,text="DNS JUMPER",font=(fuente,18),bg=nm,fg="white",borderwidth=0,command=reset_CFG)
        rs.pack()
        rs.place(x=20,y=350)
        
        txt=Label(win,text="Configuraciones",font=(fuente,18),bg=back,fg=orange,borderwidth=0)
        txt.pack()
        txt.place(x=45,y=67)
        #Bindins o ejecutores de acciones
        fire.bind(ent,fwa)
        fire.bind(lv,fw)
        cmd.bind(ent,a9)
        cmd.bind(lv,a3)
        view.bind(ent,vent)
        view.bind(lv,ven2)
        bac.bind(ent,b)
        bac.bind(lv,b2)
        rs.bind(ent,rs_CFG)
        rs.bind(lv,rs_CFG2)
        txt3939=Label(win,text='''Bloquea aplicaciones y de permisos a otras
        para usar su internet''',fg="white",bg=orange)
        txt3990=Label(win,text='''Vea la dirección IP de las personas
        conectadas a su wifi''',fg="white",bg=orange)
        txt3992=Label(win,text='''Abra la App de CMD que permite acelerar el internet
        mediante la consola de comandoss''',fg="white",bg=orange)
        txt3999=Label(win,text='''Abra DNSJUMPER pruebe y aplique 
        la mejor DNS para su conexion''',fg="white",bg=orange)
    def ab22(e):
        txt293.pack()
        about_it["bg"]=orange
    def ab2(e):
        txt293.forget()
        about_it["bg"]=nm
    def about():
        lb2.config(image=capture3)
        def wback():
            lb2.config(image=capture)
            fr2.destroy()
            bac2.destroy()
            texto.destroy()
            tx2t.destroy()
        def b3(event):
            bac2["bg"]=nf
        def b4(event):
            bac2["bg"]=orange

        fr2=Frame(win,bg=back,width=3000,height=4000)
        fr2.pack()
        fr2.place(x=0,y=55)
        bac2=Button(win,text="<",font=(fuente,24),bg=orange,borderwidth=0,command=wback)
        bac2.pack()
        bac2.place(x=0,y=55)
        bac2.bind(ent,b3)
        bac2.bind(lv,b4)
        texto=Label(win,text='''N3T-JC
Es una aplicación gratuita 
desarrollada por FrancKEyJC 
para acelerar el internet 
con solo dar un click al
boton "BOOST",el cual cuando
se da click prueba las dns's 
disponibles y aplica la
DNS más rapida.Tambien se 
aplican una serie de ajustes
para mejorar la conexion

Agradecimientos especiales a python 
sordum nircsoft y a GNU.''',font=("Arial Black",10),bg=back,fg="black")
        texto.pack()
        texto.place(x=10,y=108)
        tx2t=Label(win,text="Acerca de ",font=(fuente,18),bg=back,fg=orange,borderwidth=0)
        tx2t.pack()
        tx2t.place(x=45,y=67)
        #webbrowser.open("tinyurl.com/franckeychannel")


    #elementos_De__LA___VENTANA__WIN
    btn_boost=Button(win,text="BOOST",font=(fuente,45),command=boost,borderwidth=0,bg=nm,fg="white")
    btn_boost.pack()
    btn_boost.place(x=14,y=80)
    btn_boost.bind("<Enter>",btn_mo)
    btn_boost.bind("<Leave>",btn_mf)

    btn_config=Button(win,text="config",font=(fuente,24),bg=nm,borderwidth=0,fg="white",command=clk_cfg)
    btn_config.pack()
    btn_config.place(x=20,y=280)
    btn_config.bind("<Enter>",btn_c)
    btn_config.bind("<Leave>",btn_cc)

    copyrights=Label(win,text="Made by FrancKEyJC",font=(fuente,15),bg=back,fg=orange)
    copyrights.pack()
    copyrights.place(x=20,y=360)
    loadin=Label(win,text="▄",font=("Comic Sans MS",40),fg=nf,bg=back)

    mins=Label(win,image=mini,bg=back)
    mins.pack()
    mins.place(x=230,y=275)

    txt39=Label(win,text="Clickee aquí para acelerar su internet",fg="white",bg=orange)
    txt93=Label(win,text='''Clickee aquí para ver configuraciones y herramientas 
    extras que trae N3T-JC''',fg="white",bg=orange) 
    txt293=Label(win,text="Clickee aquí para saber más acerca de N3T-JC",fg="white",bg=orange)




    about_it=Button(win,text="?",borderwidth=0,bg=nm,font=(fuente,24),fg="white",command=about)
    about_it.pack()
    about_it.place(x=180,y=280)
    about_it.bind(ent,ab22)
    about_it.bind(lv,ab2)
    win.attributes("-topmost",True)
    def notop():
        win.attributes("-topmost",False)
    win.after(1000,notop)
    w.mainloop()
wn()

