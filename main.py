import tkinter as tk

from utils.cost import expaction,max_p_worst

def on_botton_click():
    
    
    
    E = expaction(float(textbox1.get()),int(textbox2.get()),float(textbox3.get()),option.get())
    label4.config(text="期望抽卡次数："+str(E))

    p_worst = max_p_worst(float(textbox1.get()),int(textbox2.get()),float(textbox3.get()),option.get())
    label5.config(text="(大)保底发生概率："+str(p_worst))
    
def main():
    global window
    window = tk.Tk()
    window.title("抽卡次数期望计算")
    
    
    global textbox1 
    global textbox2
    global textbox3
    global option
    global label4
    global label5
    
    
    label1 = tk.Label(window, text="请输入头奖概率：")
    label1.grid(row=0, column=0)

    textbox1 = tk.Entry(window)
    textbox1.insert(0,"0.007")
    textbox1.grid(row=0, column=1)
    
    label2 = tk.Label(window, text="选择卡池类型：")
    label2.grid(row=1, column=0)
    
    option = tk.StringVar()
    option.set("mi")
    
    radiobutton1 = tk.Radiobutton(window, text="大小保底", variable=option, value="mi")
    radiobutton1.grid(row=1, column=1)
    
    radiobutton2 = tk.Radiobutton(window, text="单保底", variable=option, value="single")
    radiobutton2.grid(row=1, column=2)
    
    radiobutton3 = tk.Radiobutton(window, text="无保底", variable=option, value="none")
    radiobutton3.grid(row=1, column=3)
    
    label2 = tk.Label(window, text="请输入(小)保底次数：")
    label2.grid(row=2, column=0)
    
    textbox2 = tk.Entry(window)
    textbox2.insert(0,"80")
    textbox2.grid(row=2, column=1)
    
    label3 = tk.Label(window, text="请输入小保底概率：")
    label3.grid(row=3, column=0)
    
    textbox3 = tk.Entry(window)
    textbox3.insert(0,"0.5")
    textbox3.grid(row=3, column=1)
    
    button = tk.Button(window, text="计算", command=on_botton_click)
    button.grid(row=4, column=1)
    
    label4 = tk.Label(window, text="期望抽卡次数：")
    label4.grid(row=5,column=0)

    label5 = tk.Label(window,text="(大)保底发生概率：")   
    label5.grid(row=6,column=0)
    
    tk.mainloop()
    
    
    
if __name__ == '__main__':
    main()
    