import pandas as pd
import numpy as np
import streamlit as st
import math

st.write("# ◆割り勘システム◆")
st.write("")
st.write("")

#割り勘対象ユーザー入力フォーム
with st.form("user_input_form", clear_on_submit=True):
  
  if 'name_list' not in st.session_state:
    st.session_state["name_list"] = []

  st.write("#### 割り勘ユーザー入力")
  
  name = st.text_input('割り勘する人を一人ずつ入力し、「追加」を押してください').strip()

  seg1,seg2,seg3 = st.columns(3)

  add_button1 = seg1.form_submit_button("追加")
  reset_button1 = seg3.form_submit_button("やり直す")

  #追加(重複する名前でエラーを出す)
  if add_button1:
    st.session_state["name_list"].append(name) 
  
  #やり直し
  if reset_button1:
    st.session_state["name_list"] = []

  #ユーザーリスト
  users = st.session_state["name_list"] 
  st.write("割り勘メンバー：",*users)
  


#金額入力フォーム

if "item_price_users" not in st.session_state:
   st.session_state["item_price_users"] = []


with st.form("money_input_form",clear_on_submit=True):

  st.write("#### 金額入力")

  item = st.text_input('品物名').strip()   
  price = st.number_input('品物の金額を入力してください',0,100000000,0,step=1)
  item_user = st.multiselect('対象者を選んでください',users,users)

  #ボタン
  seg4,seg5,seg6 = st.columns(3)
  add_button2 = seg4.form_submit_button("追加")
  reset_button2 = seg6.form_submit_button("やり直す")

  if add_button2:
     st.session_state["item_price_users"].append([item,price,item_user])

  #やり直し
  if reset_button2:
    st.session_state["item_price_users"] = []

  for i in st.session_state["item_price_users"]:
     st.write(i[0],":",str(i[1]),"、対象者：",*i[2])




kaimono = st.session_state["item_price_users"]

meisai = {}
for user in users:
    meisai[user] = [] 

for a in range(len(kaimono)):
  for b in kaimono[a][2]:
      meisai[b].append([kaimono[a][0],kaimono[a][1]/len(kaimono[a][2])])

#精算
finish_button = st.button("精算")

if finish_button:
  
  kingaku = {}
  for i,j in meisai.items():
    kingaku[i] = 0
    for k in range(len(j)):
      kingaku[i] += j[k][1]
  
  for i,j in zip(kingaku.keys(),kingaku.values()):
    st.write("### ",i,":",str(j),"円")
  
  st.write("")
  st.write("------------------内訳-------------------")
  for i in users:
    st.write("### ",i)
    for j in meisai[i]:
      st.write(j[0],":",str(j[1]),"円")