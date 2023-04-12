import pandas as pd
import numpy as np
import streamlit as st
import math

st.write("# ◆割り勘システム◆")

count_user = st.number_input("割り勘する人数を入力してください：",2,10,2,step=1)
count_item = st.number_input("割り勘する品目数を入力してください：",2,10,2,step=1)

def warikan(count_user,count_item):

    user = {}
    users = []
    for i in range(count_user):
        user_name = st.text_area("ユーザー"+str(i+1)+"の名前を入力してください：")
        user[user_name] = 0
        users.append(user_name)

    item_info = []
    for j in range(count_item):
        price = st.number_input("品目"+str(j+1)+"の金額を入力してください：",0,100000000,0,step=1)
        item_user = st.multiselect('対象者を選んでください',users,users,key=j+1)
        item_info.append([price,item_user])

    for k in range(len(item_info)):
        for l in item_info[k][1]:
            user[l]= user[l]+(item_info[k][0]/len(item_info[k][1]))

    for m, n in user.items():
        user[m] = math.ceil(n)

    return(user)

kekka = warikan(count_user,count_item)

st.write("## ◆内訳◆")
for o, p in kekka.items():
    st.write("###",o,":",str(p)+"円")
    
st.write("※小数点切り上げ")
