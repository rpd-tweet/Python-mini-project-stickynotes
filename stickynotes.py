import tkinter as tk

s=0
list=["root","root1","root2","root3","root4","root5"]

def fn():
 global s
 s+=1
 start()
def start():
 global s
 r=list[s]
 r=tk.Tk()
 r.geometry("250x350")
 r.title("sticky notes")
 entry=tk.Text(r,height=20,width=30).pack(side=tk.TOP)
 if s!=5:
  button=tk.Button(r,text="+",command=fn).pack(side=tk.BOTTOM)
 r.mainloop()
 

if __name__=="__main__":
 start()
 