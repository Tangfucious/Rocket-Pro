import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import tkinter as tk
import math

import subprocess
cmd = 'CMD命令'
subprocess.call(cmd,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

root = tk.Tk()
root.title('Rocket Pro')
root.geometry('550x375')

a = 340.29
nn = 0.98
nc = 0.98
Pe = 101325  # Exhaust pressure (Pa)
Pi = 3.141592653589793

run_click_num = 0

solver_type = None

# global variables
Propellant_temp = tk.StringVar()
Fv_temp = tk.DoubleVar()
Qmc_temp = tk.DoubleVar()
y_temp = tk.DoubleVar()
Isp_temp = tk.DoubleVar()
R_temp = tk.DoubleVar()
Tc_temp = tk.DoubleVar()
Pc_temp = tk.DoubleVar()
Me_temp = tk.DoubleVar()
Lc_star_temp = tk.DoubleVar()
p_temp = tk.DoubleVar()
k_temp = tk.DoubleVar()
conv_angle_temp = tk.DoubleVar()
div_angle_temp = tk.DoubleVar()
Cd_fuel_temp = tk.DoubleVar()
Cd_oxi_temp = tk.DoubleVar()
rough_oxi_temp = tk.DoubleVar()
rough_fuel_temp = tk.DoubleVar()
Pp_temp = tk.DoubleVar()
oxi_injector_amount_temp = tk.IntVar()
fuel_injector_amount_temp = tk.IntVar()
MR_temp = tk.DoubleVar()

conv_zone_temp = tk.StringVar()
div_zone_temp = tk.StringVar()
cooling_system_temp = tk.StringVar()
conv_zone = StringVar()
div_zone = StringVar()
cooling_system = StringVar()

Propellatn = StringVar()
Fv = 0.0
Qmc = 0.0
y = 0.0
Isp = 0.0
R = 0.0
Tc = 0.0
Pc = 0.0
Me = 0.0
Lc_star = 0.0
p = 0.0
k = 0.0
conv_angle = 0.0
div_angle = 0.0
Cd_fuel = 0.0
Cd_oxi = 0.0
rough_oxi = 0.0
rough_fuel = 0.0
Pp = 0.0
ee = 0.0
oxi_injector_amount = 0.0
fuel_injector_amount = 0.0
MR = 0.0
Oxi_Weight_PS = 0.0
Fuel_Weight_PS = 0.0
O_density = 0.0
F_density = 0.0

# value to solve
Ae = 0.0
De = 0.0
At = 0.0
Dt = 0.0
Ac = 0.0
Dc = 0.0
ee = 0.0
ec = 0.0
Lc2 = 0.0
Lc1 = 0.0
h = 0.0
H = 0.0
Y = 0.0
R2 = 0.0
R1 = 0.0
A_oxi = 0.0
D_oxi = 0.0
A_fuel = 0.0
D_fuel = 0.0
Fv_status = 0
Qmc_status = 0
Me_status = 0
Pc_status = 0

# file creation, open and saving
path = StringVar()
file_name = StringVar()
def selectPath():
    path.set(askdirectory())


def create_file():
    global dirs
    global file
    dirs = path.get() + "/" + file_name.get() + ".txt"
    if not os.path.exists(dirs):
        file = open(dirs, 'w')
        file.write("1")
        tkinter.messagebox.showinfo('Warning', 'File Created')
    else:
        tkinter.messagebox.showerror('Warning', 'File Already Exists')
def export_data():
    global dirs
    print(dirs)
    with open(dirs, "w") as file:
        global Qmc
        global Fv
        global Pc
        global Me
        global At
        global Dt
        global Ac
        global Dc
        global Ae
        global De
        global ee
        global ec
        global Lc2
        global Lc1
        global h
        global H
        global Y
        global R2
        global R1
        global A_oxi
        global D_oxi
        global A_fuel
        global D_fuel
        global Fuel_Weight_PS
        global Oxi_Weight_PS
        global solver_type
        global oxi_injector_amount_temp
        global fuel_injector_amount_temp
        
        file.write(f"Fv:{Fv}\n")
        file.write(f"Qmc:{Qmc}\n")
        file.write(f"OPS:{Oxi_Weight_PS}\n")
        file.write(f"FPS:{Fuel_Weight_PS}\n")
        file.write(f"Me:{Me}\n")
        file.write(f"At:{At}\n")
        file.write(f"Dt:{Dt}\n")
        file.write(f"Ac:{Ac}\n")
        file.write(f"Dc:{Dc}\n")
        file.write(f"Ae:{Ae}\n")
        file.write(f"De:{De}\n")
        file.write(f"Lc1:{Lc1}\n")
        file.write(f"Lc2:{Lc2}\n")
        file.write(f"h:{h}\n")
        file.write(f"H:{H}\n")
        file.write(f"R2:{R2}\n")
        file.write(f"R1:{R1}\n")
        file.write(f"Oxidizer Injector Area:{A_oxi}\n")
        file.write(f"Oxidizer Injector Diameter:{D_oxi}\n")
        file.write(f"Fuel Injector Area:{A_fuel}\n")
        file.write(f"Fuel Injector Diameter:{D_fuel}\n")
        file.write(f"Oxidizer Injector Amount:{oxi_injector_amount_temp}\n")
        file.write(f"Fuel Injector Amount:{oxi_injector_amount_temp}\n")
        file.write(f"Fuel Mass Flow Rate:{Fuel_Weight_PS}\n")
        file.write(f"Oxidizer Mass Flow Rate:{Oxi_Weight_PS}\n")


# def new():
#     file_creation = tk.Toplevel(root)
#     file_creation.attributes('-topmost', True)
#     file_creation.title('New')
#     file_creation.geometry('300x100')
#     Label(file_creation, text='Path:').place(x=10, y=10)
#     Entry(file_creation, textvariable=path).place(x=70, y=10)
#     Button(file_creation, text='Path', command=selectPath).place(x=200, y=7)
#     Label(file_creation, text='New File:').place(x=10, y=35)
#     Entry(file_creation, textvariable=file_name).place(x=70, y=35)
#     Button(file_creation, text='Creat', command=create_file).place(x=200, y=32)

def export():
    global dirs
    file_creation = tk.Toplevel(root)
    file_creation.attributes('-topmost', True)
    file_creation.title('Export')
    file_creation.geometry('300x100')
    Label(file_creation, text='Path:').place(x=10, y=10)
    Entry(file_creation, textvariable=path).place(x=70, y=10)
    Button(file_creation, text='Path', command=selectPath).place(x=200, y=7)
    Label(file_creation, text='Export File:').place(x=10, y=35)
    Entry(file_creation, textvariable=file_name).place(x=70, y=35)
    Button(file_creation, text='New', command=create_file).place(x=200, y=32)
    Button(file_creation, text = "Export", command=export_data).place(x=125, y=56)


# overall setup zone
def conv_zone_init():
    global conv_zone
    conv_zone = conv_zone_temp.get()
    print(conv_zone)
def div_zone_init():
    global div_zone
    div_zone = div_zone_temp.get()
    print(div_zone)


def cooling_system_init():
    global cooling_system
    cooling_system = cooling_system_temp.get()
    print(cooling_system)


def propellant_init():
    global propellant
    global y
    global Isp
    global R
    global Tc
    global Lc_star
    global MR
    global O_density
    global F_density
    Propellant = Propellant_temp.get()
    output_text.insert(tk.END, "Propellants Initialized\n")
    print(Propellant)

    if (Propellant == 'LH2_LOX'):
        y = 1.4
        R = 594
        Isp = 391
        Tc = 3300
        Lc_star = 0.8
        MR = 6
        O_density = 1141
        F_density = 70.9
        y_entry.delete(0, tk.END)
        y_entry.insert(tk.END, y)
        R_entry.delete(0, tk.END)
        R_entry.insert(tk.END, R)
        Isp_entry.delete(0, tk.END)
        Isp_entry.insert(tk.END, Isp)
        Tc_entry.delete(0, tk.END)
        Tc_entry.insert(tk.END, Tc)
        Lc_star_entry.delete(0, tk.END)
        Lc_star_entry.insert(tk.END, Lc_star)
        MR_entry.delete(0, tk.END)
        MR_entry.insert(tk.END, MR)
        o_density_entry.delete(0, tk.END)
        o_density_entry.insert(tk.END, O_density)
        f_density_entry.delete(0, tk.END)
        f_density_entry.insert(tk.END, F_density)
        output_text.insert(tk.END, 'y Initialized\n')
        output_text.insert(tk.END, 'Isp Initialized\n')
        output_text.insert(tk.END, 'R Initialized\n')
        output_text.insert(tk.END, 'Tc Initialized\n')
        output_text.insert(tk.END, 'Lc* Initialized\n')
        output_text.insert(tk.END, 'MR Initialized\n')
        output_text.insert(tk.END, 'Oxidizer Density Initialized\n')
        output_text.insert(tk.END, 'Fuel Density Initialized\n')
    if (Propellant == 'RP1_LOX'):
        y = 1.25
        R = 379.6
        Isp = 301.5
        Tc = 3670
        Lc_star = 1.5
        MR = 2.56
        O_density = 1141
        F_density = 810
        y_entry.delete(0, tk.END)
        y_entry.insert(tk.END, y)
        R_entry.delete(0, tk.END)
        R_entry.insert(tk.END, R)
        Isp_entry.delete(0, tk.END)
        Isp_entry.insert(tk.END, Isp)
        Tc_entry.delete(0, tk.END)
        Tc_entry.insert(tk.END, Tc)
        Lc_star_entry.delete(0, tk.END)
        Lc_star_entry.insert(tk.END, Lc_star)
        MR_entry.delete(0, tk.END)
        MR_entry.insert(tk.END, MR)
        o_density_entry.delete(0, tk.END)
        o_density_entry.insert(tk.END, O_density)
        f_density_entry.delete(0, tk.END)
        f_density_entry.insert(tk.END, F_density)
        output_text.insert(tk.END, 'y Initialized\n')
        output_text.insert(tk.END, 'Isp Initialized\n')
        output_text.insert(tk.END, 'R Initialized\n')
        output_text.insert(tk.END, 'Tc Initialized\n')
        output_text.insert(tk.END, 'Lc* Initialized\n')
        output_text.insert(tk.END, 'MR Initialized\n')
        output_text.insert(tk.END, 'Oxidizer Density Initialized\n')
        output_text.insert(tk.END, 'Fuel Density Initialized\n')
    if (Propellant == 'CH4_LOX'):
        y = 1.23
        R = 311.36
        Isp = 350
        Tc = 3533
        Lc_star = 1.13
        MR = 3.3
        O_density = 1141
        F_density = 0.657
        y_entry.delete(0, tk.END)
        y_entry.insert(tk.END, y)
        R_entry.delete(0, tk.END)
        R_entry.insert(tk.END, R)
        Isp_entry.delete(0, tk.END)
        Isp_entry.insert(tk.END, Isp)
        Tc_entry.delete(0, tk.END)
        Tc_entry.insert(tk.END, Tc)
        Lc_star_entry.delete(0, tk.END)
        Lc_star_entry.delete(0, tk.END)
        Lc_star_entry.insert(tk.END, Lc_star)
        MR_entry.delete(0, tk.END)
        MR_entry.insert(tk.END, MR)
        o_density_entry.delete(0, tk.END)
        o_density_entry.insert(tk.END, O_density)
        f_density_entry.delete(0, tk.END)
        f_density_entry.insert(tk.END, F_density)
        output_text.insert(tk.END, 'y Initialized\n')
        output_text.insert(tk.END, 'Isp Initialized\n')
        output_text.insert(tk.END, 'R Initialized\n')
        output_text.insert(tk.END, 'Tc Initialized\n')
        output_text.insert(tk.END, 'Lc* Initialized\n')
        output_text.insert(tk.END, 'MR Initialized\n')
        output_text.insert(tk.END, 'Oxidizer Density Initialized\n')
        output_text.insert(tk.END, 'Fuel Density Initialized\n')


def y_init():
    global y
    y = y_temp.get()
    output_text.insert(tk.END, 'y Initialized\n')
    print(y)


def Isp_init():
    global Isp
    Isp = Isp_temp.get()
    output_text.insert(tk.END, 'Isp Initialized\n')
    print(Isp)


def R_init():
    global R
    R = R_temp.get()
    output_text.insert(tk.END, 'R Initialized\n')
    print(R)


def Tc_init():
    global Tc
    Tc = Tc_temp.get()
    output_text.insert(tk.END, 'Tc Initialized\n')
    print(Tc)


def MR_init():
    global MR
    MR = MR_temp.get()
    output_text.insert(tk.END, 'MR Initialized\n')
    print(y)


def Lc_star_init():
    global Lc_star
    Lc_star = Lc_star_temp.get()
    output_text.insert(tk.END, 'Lc* Initialized\n')
    print(Lc_star)


def overall_setup():
    global y_entry
    global Isp_entry
    global R_entry
    global Tc_entry
    global MR_entry
    global Lc_star_entry
    global o_density_entry
    global f_density_entry
    for widget in right_frame.winfo_children():
        widget.grid_forget()
    Label(right_frame, text='Nozzle Setup').grid(row=0, column=0)
    Label(right_frame, text='Convergent').grid(row=2, column=0)
    ttk.Combobox(right_frame, textvariable=conv_zone_temp, values=('Straight', 'Curve')).grid(row=2, column=1)
    Button(right_frame, text='Confirm', command=conv_zone_init).grid(row=2, column=2)
    Label(right_frame, text='Divergent').grid(row=3, column=0)
    ttk.Combobox(right_frame, textvariable=div_zone_temp, values=('Straight', 'Curve')).grid(row=3, column=1)
    Button(right_frame, text='Confirm', command=div_zone_init).grid(row=3, column=2)
    # Label(right_frame, text='Cooling System').grid(row=4, column=0)
    # ttk.Combobox(right_frame, textvariable=cooling_system_temp, values=('Heat Sink', 'Gas Film', 'Regenerate')).grid(
    #     row=4, column=1)
    # Button(right_frame, text='Confirm', command=cooling_system_init).grid(row=4, column=2)
    Label(right_frame, text='O-F Setup').grid(row=4, column=0)
    Label(right_frame, text='O-F').grid(row=5, column=0)
    ttk.Combobox(right_frame, textvariable=Propellant_temp, values=('LH2_LOX', 'RP1_LOX', 'CH4_LOX')).grid(row=5,
                                                                                                           column=1)
    Button(right_frame, text='Confirm', command=propellant_init).grid(row=5, column=2)
    Label(right_frame, text='y').grid(row=6, column=0)
    y_entry = Entry(right_frame, textvariable=y_temp)
    y_entry.grid(row=6, column=1)
    Button(right_frame, text='Confirm', command=y_init).grid(row=6, column=2)
    Label(right_frame, text='Isp').grid(row=7, column=0)
    Isp_entry = Entry(right_frame, textvariable=Isp_temp)
    Isp_entry.grid(row=7, column=1)
    Button(right_frame, text='Confirm', command=Isp_init).grid(row=7, column=2)
    Label(right_frame, text='R').grid(row=8, column=0)
    R_entry = Entry(right_frame, textvariable=R_temp)
    R_entry.grid(row=8, column=1)
    Button(right_frame, text='Confirm', command=R_init).grid(row=8, column=2)
    Label(right_frame, text='Tc').grid(row=9, column=0)
    Tc_entry = Entry(right_frame, textvariable=Tc_temp)
    Tc_entry.grid(row=9, column=1)
    Button(right_frame, text='Confirm', command=Tc_init).grid(row=9, column=2)
    Label(right_frame, text='MR').grid(row=10, column=0)
    MR_entry = Entry(right_frame, textvariable=MR_temp)
    MR_entry.grid(row=10, column=1)
    Button(right_frame, text='Confirm', command=MR_init).grid(row=10, column=2)
    Lc_star_entry = Entry(right_frame, textvariable=Lc_star_temp)
    Label(right_frame, text='Lc*').grid(row=11, column=0)
    Lc_star_entry.grid(row=11, column=1)
    Button(right_frame, text='Confirm', command=Lc_star_init).grid(row=11, column=2)


# place to initialize combustion chamber
def Fv_init():  # initiation of thrust
    global Qmc
    global Me
    global Pc
    global Fv

    global Fv_init
    global Qmc_init
    global Pc_init
    global Me_init

    global Fv_entry
    global Qmc_entry
    global Me_entry
    global Pc_entry
    global solver_type
    Fv = Fv_temp.get()

    output_text.insert(tk.END, "Fv Initialized\n")
    if solver_type == "Fv_Pc":
        Qmc = 0
        Me = 0
    if solver_type == "Fv_Me":
        Qmc = 0
        Pc = 0
    print(Fv)


def Qmc_init():
    global Qmc
    global Me
    global Pc
    global Fv
    global Fv_entry
    global Qmc_entry
    global Me_entry
    global Pc_entry
    global solver_type
    Qmc = Qmc_temp.get()

    output_text.insert(tk.END, "Qmc Initialized\n")
    if solver_type == "Qmc_Pc":
        Fv = 0
        Me = 0
    if solver_type == "Qmc_Me":
        Fv = 0
        Pc = 0
    print(Qmc)


def Pc_init():
    global Qmc
    global Me
    global Pc
    global Fv
    global Fv_entry
    global Qmc_entry
    global Me_entry
    global Pc_entry
    global solver_type
    Pc = Pc_temp.get()

    if solver_type == "Fv_Pc":
        Qmc = 0
        Me = 0
    if solver_type == "Qmc_Pc":
        Fv = 0
        Me = 0
    output_text.insert(tk.END, "Pc Initialized\n")
    print(Pc)


def Me_init():
    global Qmc
    global Me
    global Pc
    global Fv
    global Fv_entry
    global Qmc_entry
    global Me_entry
    global Pc_entry
    global solver_type
    Me = Me_temp.get()
    if solver_type == "Fv_Me":
        Qmc = 0
        Pc = 0
    if solver_type == "Qmc_Me":
        Fv = 0
        Pc = 0
    print(Me)

def Fv_Qmc_selected():
    global state_Fv_Qmc
    global state_Me_Pc
    global solver_type
    global Fv_status
    global Qmc_status
    global Me_status
    global Pc_status
    global Fv
    global Qmc
    global Pc
    global Me
    if state_Fv_Qmc.get() == 1:
        Fv_status = 1
        Qmc_status = 0
        output_text.insert(tk.END, "Fv Selected\n")
        if Fv_status == 1 and Pc_status == 1:
            solver_type = "Fv_Pc"
            Fv_entry.config(state="normal")
            Qmc_entry.delete(0, tk.END)
            Qmc_entry.insert(tk.END, "0")
            Qmc_entry.update_idletasks()
            Qmc_entry.config(state="readonly")
            Me_entry.delete(0, tk.END)
            Me_entry.insert(tk.END, "0")
            Me_entry.update_idletasks()
            Me_entry.config(state="readonly")
            Pc_entry.config(state="normal")
            output_text.insert(tk.END, "Fv_Pc\n")
        if Fv_status == 1 and Me_status == 1:
            solver_type = "Fv_Me"
            Fv_entry.config(state="normal")
            Qmc_entry.delete(0, tk.END)
            Qmc_entry.insert(tk.END, "0")
            Qmc_entry.update_idletasks()
            Qmc_entry.config(state="readonly")
            Pc_entry.config(state="normal")
            Pc_entry.delete(0, tk.END)
            Pc_entry.insert(tk.END, "0")
            Pc_entry.update_idletasks()
            Pc_entry.config(state="readonly")
            output_text.insert(tk.END, "Fv_Me\n")
    if state_Fv_Qmc.get() == 2:
        Fv_status = 0
        Qmc_status = 1
        output_text.insert(tk.END, "Qmc Selected\n")
        if Qmc_status == 1 and Pc_status == 1:
            solver_type = "Qmc_Pc"
            Fv_entry.delete(0, tk.END)
            Fv_entry.insert(tk.END, "0")
            Fv_entry.update_idletasks()
            Fv_entry.config(state="readonly")
            Qmc_entry.config(state="normal")
            Me_entry.delete(0, tk.END)
            Me_entry.insert(tk.END, "0")
            Me_entry.update_idletasks()
            Me_entry.config(state="readonly")
            Pc_entry.config(state="normal")
            output_text.insert(tk.END, "Qmc_Pc\n")
        if Qmc_status == 1 and Me_status == 1:
            solver_type = "Qmc_Me"
            Fv_entry.delete(0, tk.END)
            Fv_entry.insert(tk.END, "0")
            Fv_entry.update_idletasks()
            Fv_entry.config(state="readonly")
            Qmc_entry.config(state="normal")
            Me_entry.config(state="normal")
            Pc_entry.delete(0, tk.END)
            Pc_entry.insert(tk.END, "0")
            Pc_entry.update_idletasks()
            Pc_entry.config(state="readonly")
            output_text.insert(tk.END, "Qmc_Me\n")
def Me_Pc_selected():
    global state_Fv_Qmc
    global state_Me_Pc
    global solver_type
    global Fv_status
    global Qmc_status
    global Me_status
    global Pc_status
    global Fv
    global Qmc
    global Pc
    global Me
    if state_Me_Pc.get() == 1:
        Me_status = 1
        Pc_status = 0
        output_text.insert(tk.END, "Me Selected\n")
        if Fv_status == 1 and Me_status == 1:
            solver_type = "Fv_Me"
            Fv_entry.config(state="normal")
            Qmc_entry.delete(0, tk.END)
            Qmc_entry.insert(tk.END, "0")
            Qmc_entry.update_idletasks()
            Qmc_entry.config(state="readonly")
            Me_entry.config(state="normal")
            Pc_entry.delete(0, tk.END)
            Pc_entry.insert(tk.END, "0")
            Pc_entry.update_idletasks()
            Pc_entry.config(state="readonly")
            output_text.insert(tk.END, "Fv_Me\n")
        if Qmc_status == 1 and Me_status == 1:
            solver_type = "Qmc_Me"
            Fv_entry.delete(0, tk.END)
            Fv_entry.insert(tk.END, "0")
            Fv_entry.update_idletasks()
            Fv_entry.config(state="readonly")
            Qmc_entry.config(state="normal")
            Me_entry.config(state="normal")
            Pc_entry.delete(0, tk.END)
            Pc_entry.insert(tk.END, "0")
            Pc_entry.update_idletasks()
            Pc_entry.config(state="readonly")
            output_text.insert(tk.END, "Qmc_Me\n")
    elif state_Me_Pc.get() == 2:
        Me_status = 0
        Pc_status = 1
        output_text.insert(tk.END, "Pc Selected\n")
        if Fv_status == 1 and Pc_status == 1:
            solver_type = "Fv_Pc"
            Fv_entry.config(state="normal")
            Qmc_entry.delete(0, tk.END)
            Qmc_entry.insert(tk.END, "0")
            Qmc_entry.update_idletasks()
            Qmc_entry.config(state="readonly")
            Me_entry.delete(0, tk.END)
            Me_entry.insert(tk.END, "0")
            Me_entry.update_idletasks()
            Me_entry.config(state="readonly")
            Pc_entry.config(state="normal")
            output_text.insert(tk.END, "Fv_Pc\n")
        if Qmc_status == 1 and Pc_status == 1:
            solver_type = "Qmc_Pc"
            Fv_entry.delete(0, tk.END)
            Fv_entry.insert(tk.END, "0")
            Fv_entry.update_idletasks()
            Fv_entry.config(state="readonly")
            Qmc_entry.config(state="normal")
            Me_entry.delete(0, tk.END)
            Me_entry.insert(tk.END, "0")
            Me_entry.update_idletasks()
            Me_entry.config(state="readonly")
            Pc_entry.config(state="normal")
            output_text.insert(tk.END, "Qmc_Pc\n")
def combustion_chamber():
    global Fv_entry
    global Qmc_entry
    global Me_entry
    global Pc_entry
    global state_Fv_Qmc
    global state_Me_Pc
    global solver_type
    global Fv_status
    global Qmc_status
    global Me_status
    global Pc_status
    global Fv
    global Pc
    global Qmc
    global Me
    state_Fv_Qmc = IntVar()
    state_Me_Pc = IntVar()

    for widget in right_frame.winfo_children():
        widget.grid_forget()
    if state_Fv_Qmc == 1 and state_Me_Pc == 1:
        Qmc_entry.config(state="readonly")
        Me_entry.config(state="readonly")
    tk.Radiobutton(right_frame, text="Fv", variable=state_Fv_Qmc, value=1).grid(row=1, column=1)
    tk.Radiobutton(right_frame, text="Qmc", variable=state_Fv_Qmc, value=2).grid(row=1, column=2)
    tk.Button(right_frame, text="Confirm", command=Fv_Qmc_selected).grid(row=1, column=3)
    tk.Radiobutton(right_frame, text="Me", variable=state_Me_Pc, value=1).grid(row=2, column=1)
    tk.Radiobutton(right_frame, text="Pc", variable=state_Me_Pc, value=2).grid(row=2, column=2)
    tk.Button(right_frame, text="Confirm", command=Me_Pc_selected).grid(row=2, column=3)
    Label(right_frame, text='Fv (Max Thrust)').grid(row=3, column=1)
    Fv_entry = Entry(right_frame, textvariable=Fv_temp)
    Fv_entry.grid(row=3, column=2)
    Button(right_frame, text='Confirm', command=Fv_init).grid(row=3, column=3)
    Label(right_frame, text='Qmc (mass flow rate)').grid(row=4, column=1)
    Qmc_entry = Entry(right_frame, textvariable=Qmc_temp)
    Qmc_entry.grid(row=4, column=2)
    Button(right_frame, text='Confirm', command=Qmc_init).grid(row=4, column=3)
    Label(right_frame, text='Me (Exit Mach Number)').grid(row=5, column=1)
    Me_entry = Entry(right_frame, textvariable=Me_temp)
    Me_entry.grid(row=5, column=2)
    Button(right_frame, text='Confirm', command=Me_init).grid(row=5, column=3)
    Label(right_frame, text='Pc (Combustion Pressure)').grid(row=6, column=1)
    Pc_entry = Entry(right_frame, textvariable=Pc_temp)
    Pc_entry.grid(row=6, column=2)
    Button(right_frame, text='Confirm', command=Pc_init).grid(row=6, column=3)

    Fv_entry.config(state="readonly")
    Qmc_entry.config(state="readonly")
    Me_entry.config(state="readonly")
    Pc_entry.config(state="readonly")

    if solver_type == "Fv_Pc":
        Fv_entry.config(state = "normal")
        Pc_entry.config(state = "normal")
    if solver_type == "Fv_Me":
        Fv_entry.config(state="normal")
        Me_entry.config(state="normal")
    if solver_type == "Qmc_Me":
        Qmc_entry.config(state="normal")
        Me_entry.config(state="normal")
    if solver_type == "Qmc_Pc":
        Qmc_entry.config(state="normal")
        Pc_entry.config(state="normal")


# place to initialize nozzle
def p_init():
    global p
    p = p_temp.get()
    output_text.insert(tk.END, 'p Initialized')
    print(p)


def k_init():
    global k
    k = k_temp.get()
    output_text.insert(tk.END, 'k Initialized\n')
    print(k)


def div_angle_init():
    global div_angle
    div_angle = div_angle_temp.get()
    output_text.insert(tk.END, 'Divergent Angle Initialized')
    print(div_angle)


def conv_angle_init():
    global conv_angle
    conv_angle = conv_angle_temp.get()
    output_text.insert(tk.END, 'Convergent Angle Initialized')
    print(conv_angle)


def nozzle():
    for widget in right_frame.winfo_children():
        widget.grid_forget()
    # 4 cases
    if (conv_zone == 'Straight' and div_zone == 'Straight'):
        Label(right_frame, text='Convergent Angle').grid(row=0, column=0)
        conv_angle_entry = Entry(right_frame, textvariable=conv_angle_temp).grid(row=0, column=1)
        Button(right_frame, text='Confirm', command=conv_angle_init).grid(row=0, column=2)
        Label(right_frame, text='Divergent Angle').grid(row=1, column=0)
        div_angle_entry = Entry(right_frame, textvariable=div_angle_temp).grid(row=1, column=1)
        Button(right_frame, text='Confirm', command=div_angle_init).grid(row=1, column=2)
    if (conv_zone == 'Curve' and div_zone == 'Straight'):
        Label(right_frame, text='p').grid(row=0, column=0)
        p_entry = Entry(right_frame, textvariable=p_temp).grid(row=0, column=1)
        Button(right_frame, text='Confirm', command=p_init).grid(row=0, column=2)
        Label(right_frame, text='k').grid(row=1, column=0)
        k_entry = Entry(right_frame, textvariable=k_temp).grid(row=1, column=1)
        Button(right_frame, text='Confirm', command=k_init).grid(row=1, column=2)
        Label(right_frame, text='Divergent Angle').grid(row=2, column=0)
        div_angle_entry = Entry(right_frame, textvariable=div_angle_temp).grid(row=2, column=1)
        Button(right_frame, text='Confirm', command=div_angle_init).grid(row=2, column=2)
    if conv_zone == 'Straight' and div_zone == 'Curve':
        output_text.insert(tk.END, 'Nozzle Configuration Is Not Supported\n')


# place to initialize injector
def Cd_oxi_init():
    global Cd_oxi
    Cd_oxi = Cd_oxi_temp.get()
    output_text.insert(tk.END, 'Oxidizer Cd Initialized\n')
    print(Cd_oxi)


def Cd_fuel_init():
    global Cd_fuel
    Cd_fuel = Cd_fuel_temp.get()
    output_text.insert(tk.END, 'Fuel Cd Initialized\n')
    print(Cd_fuel)


def rough_oxi_init():
    global rough_oxi
    rough_oxi = rough_oxi_temp.get()
    output_text.insert(tk.END, 'Oxidizer Density Initialized\n')
    print(rough_oxi)


def rough_fuel_init():
    global rough_fuel
    rough_fuel = rough_fuel_temp.get()
    output_text.insert(tk.END, 'Fuel Density Initialized\n')
    print(rough_fuel)


def Pp_init():
    global Pp
    Pp = Pp_temp.get()
    output_text.insert(tk.END, 'Injection Pressure Initialized\n')
    print(Pp)


def oxi_injector_amount_init():
    global oxi_injector_amount
    oxi_injector_amount = oxi_injector_amount_temp.get()
    output_text.insert(tk.END, 'Oxidizer Amount Initialized Initialized\n')
    print(oxi_injector_amount)


def fuel_injector_amount_init():
    global fuel_injector_amount
    fuel_injector_amount = fuel_injector_amount_temp.get()
    output_text.insert(tk.END, 'Fuel Injector Amount Initialized\n')
    print(fuel_injector_amount)


def injector():
    global o_density_entry
    global f_density_entry
    for widget in right_frame.winfo_children():
        widget.grid_forget()
    Label(right_frame, text='Oxidizer Cd').grid(row=1, column=1)
    Entry(right_frame, textvariable=Cd_oxi_temp).grid(row=1, column=2)
    Button(right_frame, text='Confirm', command=Cd_oxi_init).grid(row=1, column=3)
    Label(right_frame, text='Fuel Cd').grid(row=2, column=1)
    Entry(right_frame, textvariable=Cd_fuel_temp).grid(row=2, column=2)
    Button(right_frame, text='Confirm', command=Cd_fuel_init).grid(row=2, column=3)
    Label(right_frame, text='Oxidizer Density').grid(row=3, column=1)
    o_density_entry = Entry(right_frame, textvariable=rough_oxi_temp)
    o_density_entry.grid(row=3, column=2)
    Button(right_frame, text='Confirm', command=rough_oxi_init).grid(row=3, column=3)
    Label(right_frame, text='Fuel Density').grid(row=4, column=1)
    f_density_entry = Entry(right_frame, textvariable=rough_fuel_temp)
    f_density_entry.grid(row=4, column=2)
    Button(right_frame, text='Confirm', command=rough_fuel_init).grid(row=4, column=3)
    Label(right_frame, text='Inject Pressure').grid(row=5, column=1)
    Entry(right_frame, textvariable=Pp_temp).grid(row=5, column=2)
    Button(right_frame, text='Confirm', command=Pp_init).grid(row=5, column=3)
    Label(right_frame, text='# of Oxidizer Injectors').grid(row=6, column=1)
    Entry(right_frame, textvariable=oxi_injector_amount_temp).grid(row=6, column=2)
    Button(right_frame, text='Confirm', command=oxi_injector_amount_init).grid(row=6, column=3)
    Label(right_frame, text='# of Fuel Injectors').grid(row=7, column=1)
    Entry(right_frame, textvariable=fuel_injector_amount_temp).grid(row=7, column=2)
    Button(right_frame, text='Confirm', command=fuel_injector_amount_init).grid(row=7, column=3)


# place to initialize cooling system
def cooling_system():
    for widget in right_frame.winfo_children():
        widget.grid_forget()
    pass


# place to initialize  result page
def results():
    global Qmc
    global Fv
    global Pc
    global Me
    global At
    global Dt
    global Ac
    global Dc
    global Ae
    global De
    global ee
    global ec
    global Lc2
    global Lc1
    global h
    global H
    global Y
    global R2
    global R1
    global A_oxi
    global D_oxi
    global A_fuel
    global D_fuel
    global Fuel_Weight_PS
    global Oxi_Weight_PS
    global solver_type
    global oxi_injector_amount_temp
    global fuel_injector_amount_temp
    for widget in right_frame.winfo_children():
        widget.grid_forget()
    result_text = tk.Text(right_frame)
    result_text.config(height = 300)

    global run_click_num
    run_click_num += 1
    result_text.grid(row=0, column=0, sticky=tk.NS)
    result_text.insert(tk.END, f"Fv:{Fv}\n")
    result_text.insert(tk.END, f"Qmc:{Qmc}\n")
    result_text.insert(tk.END, f"OPS:{Oxi_Weight_PS}\n")
    result_text.insert(tk.END, f"FPS:{Fuel_Weight_PS}\n")
    result_text.insert(tk.END, f"Me:{Me}\n")
    result_text.insert(tk.END, f"At:{At}\n")
    result_text.insert(tk.END, f"Dt:{Dt}\n")
    result_text.insert(tk.END, f"Ac:{Ac}\n")
    result_text.insert(tk.END, f"Dc:{Dc}\n")
    result_text.insert(tk.END, f"Ae:{Ae}\n")
    result_text.insert(tk.END, f"De:{De}\n")
    result_text.insert(tk.END, f"Lc1:{Lc1}\n")
    result_text.insert(tk.END, f"Lc2:{Lc2}\n")
    result_text.insert(tk.END, f"h:{h}\n")
    result_text.insert(tk.END, f"H:{H}\n")
    result_text.insert(tk.END, f"R2:{R2}\n")
    result_text.insert(tk.END, f"R1:{R1}\n")
    result_text.insert(tk.END, f"Oxidizer Injector Area:{A_oxi}\n")
    result_text.insert(tk.END, f"Oxidizer Injector Diameter:{D_oxi}\n")
    result_text.insert(tk.END, f"Fuel Injector Area:{A_fuel}\n")
    result_text.insert(tk.END, f"Fuel Injector Diameter:{D_fuel}\n")
    result_text.insert(tk.END, f"Oxidizer Injector Amount:{oxi_injector_amount_temp}\n")
    result_text.insert(tk.END, f"Fuel Injector Amount:{oxi_injector_amount_temp}\n")
    result_text.insert(tk.END, f"Fuel Mass Flow Rate:{Fuel_Weight_PS}\n")
    result_text.insert(tk.END, f"Oxidizer Mass Flow Rate:{Oxi_Weight_PS}\n")


# when pressed run, start solving
def solvers():
    global run_click_num
    run_click_num += 1
    global Qmc
    global Fv
    global Pc
    global Me
    global At
    global Dt
    global Ac
    global Dc
    global Ae
    global De
    global ee
    global ec
    global Lc2
    global Lc1
    global h
    global H
    global Y
    global R2
    global R1
    global A_oxi
    global D_oxi
    global A_fuel
    global D_fuel
    global Fuel_Weight_PS
    global Oxi_Weight_PS
    global solver_type
    global oxi_injector_amount_temp
    global fuel_injector_amount_temp
    if solver_type == "Fv_Pc":
        Me = math.sqrt(((2 * (math.pow((Pe / Pc), -(y - 1) / y))) - 1) / (y - 1))
        ve = Me * a
        Qmc = Fv / (ve * nc * nn)
        At = Qmc * math.sqrt(R * Tc) / (Pc * math.sqrt(y * (2 / (y + 1)) ** ((y + 1) / (y - 1))))
        Dt = math.sqrt(4 * At / Pi)
        ec = 8 * (Dt * 100) ** (-0.6) + 1.25
        Ac = At * ec
        Dc = Dt * math.sqrt(ec)
        Ae = At * (1 / Me) * ((2 / (y + 1)) * (1 + (y - 1) / 2 * Me ** 2)) ** ((y + 1) / (2 * (y - 1)))
        De = math.sqrt(4 * Ae / Pi)
        ee = Ae / At
        Fuel_Weight_PS = Qmc / (1 + MR)
        Oxi_Weight_PS = Fuel_Weight_PS * MR
        Qmc_entry.delete(0, tk.END)
        Qmc_entry.insert(tk.END, Qmc)
        Me_entry.delete(0, tk.END)
        Me_entry.insert(tk.END, Me)
    if solver_type == "Fv_Me":
        Pc = Pe / pow(((pow(Me, 2) * (y + 1)) / 2) + 1, -(-(y - 1) / y))
        ve = Me * a
        Qmc = Fv / (ve * nc * nn)
        At = Qmc * math.sqrt(R * Tc) / (Pc * math.sqrt(y * (2 / (y + 1)) ** ((y + 1) / (y - 1))))
        Dt = math.sqrt(4 * At / Pi)
        ec = 8 * (Dt * 100) ** -0.6 + 1.25
        Ac = At * ec
        Dc = Dt * math.sqrt(ec)
        Ae = At * (1 / Me) * ((2 / (y + 1)) * (1 + (y - 1) / 2 * Me ** 2)) ** ((y + 1) / (2 * (y - 1)))
        De = math.sqrt(4 * Ae / Pi)
        ee = Ae / At
        Fuel_Weight_PS = Qmc / (1 + MR)
        Oxi_Weight_PS = Fuel_Weight_PS * MR
        Qmc_entry.delete(0, tk.END)
        Qmc_entry.insert(tk.END, Qmc)
        Pc_entry.delete(0, tk.END)
        Pc_entry.insert(tk.END, Pc)
    if solver_type == "Qmc_Pc":
        Me = math.sqrt(((2 * (math.pow((Pe / Pc), -(y - 1) / y))) - 1) / (y - 1))
        ve = Me * a
        Fv = Qmc * (ve * nc * nn)
        At = Qmc * math.sqrt(R * Tc) / (Pc * math.sqrt(y * (2 / (y + 1)) ** ((y + 1) / (y - 1))))
        Dt = math.sqrt(4 * At / Pi)
        ec = 8 * (Dt * 100) ** -0.6 + 1.25
        Ac = At * ec
        Dc = Dt * math.sqrt(ec)
        Ae = At * (1 / Me) * ((2 / (y + 1)) * (1 + (y - 1) / 2 * Me ** 2)) ** ((y + 1) / (2 * (y - 1)))
        De = math.sqrt(4 * Ae / Pi)
        ee = Ae / At
        Fuel_Weight_PS = Qmc / (1 + MR)
        Oxi_Weight_PS = Fuel_Weight_PS * MR
        Fv_entry.delete(0, tk.END)
        Fv_entry.insert(tk.END, Fv)
        Me_entry.delete(0, tk.END)
        Me_entry.insert(tk.END, Me)
    if solver_type == "Qmc_Me":
        Pc = Pe / pow(((pow(Me, 2) * (y + 1)) / 2) + 1, -(-(y - 1) / y))
        ve = Me * a
        Fv = Qmc * (ve * nc * nn)
        At = Qmc * math.sqrt(R * Tc) / (Pc * math.sqrt(y * (2 / (y + 1)) ** ((y + 1) / (y - 1))))
        Dt = math.sqrt(4 * At / Pi)
        ec = 8 * (Dt * 100) ** -0.6 + 1.25
        Ac = At * ec
        Dc = Dt * math.sqrt(ec)
        Ae = At * (1 / Me) * ((2 / (y + 1)) * (1 + (y - 1) / 2 * Me ** 2)) ** ((y + 1) / (2 * (y - 1)))
        De = math.sqrt(4 * Ae / Pi)
        ee = Ae / At
        Fuel_Weight_PS = Qmc / (1 + MR)
        Oxi_Weight_PS = Fuel_Weight_PS * MR
        Fv_entry.delete(0, tk.END)
        Fv_entry.insert(tk.END, Fv)
        Pc_entry.delete(0, tk.END)
        Pc_entry.insert(tk.END, Pc)
    # nozzle solver
    if conv_zone == 'Curve' and div_zone == 'Straight':
        # for temporary
        Lc2 = (Dt / 2) * math.sqrt(((k + p * math.sqrt(ec)) ** 2) - ((p - 1) * math.sqrt(ec) + 1 + k) ** 2)
        h = Lc2 * (k / (k + p * math.sqrt(ec)))
        H = Lc2 - h
        Y = k * (Dt / 2) + (Dt / 2) - math.sqrt(k ** 2 * (Dt / 2) ** 2 - h ** 2)
        R2 = (H ** 2 + ((Dc / 2) - Y) ** 2) / (2 * ((Dc / 2) - Y))
        R1 = (h ** 2 + (Y - (Dt / 2)) ** 2) / (2 * (Y - (Dt / 2)))
        # fix here
        Rc = Dc/2
        Rt = Dt/2
        R2_volume = 3.14*(-math.asin(H/abs(R2))*R2**2*(R2-Rc)-H*math.sqrt(R2**2-H**2)*(R2-Rc)-(H**3/3)+H*(2*R2**2-2*Rc*R2+Rc**2))
        R1_volume = 3.14*(-math.asin(h/abs(R1))*R1**2*(R1+Rt)-h*math.sqrt(R1**2-h**2)*(R1+Rt)-(h**3/3)+h*(2*R1**2+2*Rt*R1+Rt**2))
        nozzle_volume = R2_volume+R1_volume
        Lc1 = (Lc_star * At - nozzle_volume) / (Pi * (Dc / 2) ** 2)
    if conv_zone == 'Straight' and div_zone == 'Straight':
        Lc2 = ((Dc - Dt) / 2) / math.tan(conv_angle * Pi / 180)
        nozzle_volume = (Dc / 2) * math.tan(((Pi / 2) - conv_angle) * Pi / 180) * (1 / 3) * Pi * (Dc / 2) ** 2 - (
                1 / 3) * Pi * (Dt / 2) ** 2 * ((Dt / 2) * math.tan(((Pi / 2) - conv_angle) - Lc2))
        Lc1 = (Lc_star * At - nozzle_volume) / (Pi * (Dc / 2) ** 2)
    # injector solver
    if Cd_oxi != 0 and Cd_fuel != 0 and rough_oxi != 0 and rough_fuel != 0 and Pp != 0:
        A_oxi = (Oxi_Weight_PS / 4) / (Cd_oxi * math.sqrt(2 * rough_oxi * (Pp - Pc)))
        D_oxi = 2 * math.sqrt(A_oxi / Pi)
        A_fuel = (Fuel_Weight_PS) / (Cd_fuel * math.sqrt(2 * rough_fuel * (Pp - Pc)))
        D_fuel = 2 * math.sqrt(A_fuel / Pi)
        print(f"D_oxi: {D_oxi}")
        print(f"D_fuel: {D_fuel}")


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='File', menu=filemenu),
# # open = filemenu.add_command(label='Open', command=open),
# new = filemenu.add_command(label='New', command=new),
# # save = filemenu.add_command(label='Save', command=save)
menubar.add_cascade(label='Run', command=solvers)
menubar.add_cascade(label='Export', command=export)
root.config(menu=menubar)

# initiate frames
pw = tk.PanedWindow(root, orient='vertical', sashrelief='sunken')
pw.pack(fill='both', expand=1)
separator = ttk.Separator(root).pack(fill='x', padx=5)
pw_1 = tk.PanedWindow(pw, orient='horizontal', sashrelief='sunken')
pw_2 = tk.PanedWindow(pw, orient='vertical', sashrelief='sunken')
left_frame, right_frame, bottom_frame = ttk.Frame(pw_1, width=100, relief='sunken'), \
    ttk.Frame(pw_1, height=280, relief='sunken'), \
    ttk.Frame(pw_2, relief='sunken')
pw.add(pw_1), pw.add(pw_2), pw_1.add(left_frame), pw_1.add(right_frame), pw_2.add(bottom_frame)

# IO box
output_text = tk.Text(bottom_frame)
output_text.pack(fill=tk.BOTH, expand=1)

output_text_scrollbar = tk.Scrollbar(output_text)
output_text.config(yscrollcommand=output_text_scrollbar.set)
output_text_scrollbar.config(command=output_text.yview)
output_text_scrollbar.pack(side="right", fill="y")

ttk.Button(left_frame, text="Overall Setup", command=overall_setup).pack(fill=tk.X)
ttk.Button(left_frame, text="Combustion Chamber", command=combustion_chamber).pack(fill=tk.X)
ttk.Button(left_frame, text="Nozzle", command=nozzle).pack(fill=tk.X)
ttk.Button(left_frame, text="Injector", command=injector).pack(fill=tk.X)
# ttk.Button(left_frame, text="Cooling System", command=cooling_system).pack(fill=tk.X)
# ttk.Button(left_frame, text="Cooling System", command = cooling_system).pack(fill = tk.X)
ttk.Button(left_frame, text="Results", command=results).pack(fill=tk.X)
o_density_entry = Entry(right_frame, textvariable=rough_oxi_temp)
f_density_entry = Entry(right_frame, textvariable=rough_fuel_temp)

root.resizable(False, False)
root.mainloop()
