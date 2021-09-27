from flask import Flask, render_template
from gen import*

app=Flask(__name__) 

def get_list(n):
     lst = []
     for i in range(9):
          p = n
          lst.append(n)

     return lst

@app.route("/") 
def index(): 

     
     easy_16_lst = []
     easy_32_lst = []
     strong_16_lst = []
     strong_32_lst = []
     strong_lst = []
     hash_lst =[]
     
     for i in range(9):
          easy_16_lst.append(gen_easy_16())
          easy_32_lst.append(gen_easy_32())
          strong_16_lst.append(gen_strong_16())
          strong_32_lst.append(gen_strong_32())
          strong_lst.append(gen_strong())

          num = random.random()
          hash_lst.append(hash(str(num)))

     # print(easy_16_lst)

     return  render_template('index.html', easy_16_lst=easy_16_lst, easy_32_lst=easy_32_lst, strong_16_lst=strong_16_lst,strong_32_lst=strong_32_lst, strong_lst=strong_lst, hash_lst=hash_lst)

if __name__=="__main__": 
    app.run(debug=True) 
