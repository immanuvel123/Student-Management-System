import sqlite3 as sq
import streamlit as st
con=sq.connect('management.db')
cus=con.cursor()
admin={'admin':'Admin@123'}
if 'logged' not in st.session_state:
    st.session_state.logged=False
def login():
    u_name=st.text_input('User Name')
    p_word=st.text_input('Password', type='password')
    lg=st.button('Login', type='primary')
    if lg:
        if u_name in admin and p_word==admin[u_name]:
            st.session_state.logged=True
            st.rerun()
def inse():
    name=st.text_input('Name')
    ph=st.number_input('Phone', min_value=0)
    db=st.date_input('DOB')
    g=st.radio('Gender',['Mail','Femail'])
    ad=st.text_area('Address')
    po= st.file_uploader('Photo', type=['jpg', 'png', 'svg'])
    z=st.button('Add', type='primary')
    if z:
        ins="insert into student (sname, phno, dob, gender, address, photo) values(?, ?, ?, ?, ?, ?)"
        im=po.read()
        cus.execute(ins,(name,ph,db,g,ad, im))
        con.commit()
        st.success('Student Details added Successfully')
        st.balloons()
def remv():
    sid=st.number_input('Id', min_value=0)
    re=st.button('Remove',type='primary')
    if re:
        rem="delete from student where sid=?"
        cus.execute(rem,(sid,))
        con.commit()
        st.success('Student Details Removed Successfully')
        st.balloons()
def disp():
    di="select * from student"
    data=cus.execute(di).fetchall()
    head=['SID','NAME','PHONE','DOB','GENDER','ADDRESS','PHOTO']
    cols=st.columns(7)
    for col_n, col in zip(head,cols):
        col.markdown(col_n)
    for row in data:
        c1, c2, c3, c4, c5, c6, c7=st.columns(7)
        c1.write(row[0])
        c2.write(row[1])
        c3.write(row[2])
        c4.write(row[3])
        c5.write(row[4])
        c6.write(row[5])
        c7.image(row[6])
def upd():
    um=['Name','Phone','DOB','Gender','Address','Photo']
    ud=st.selectbox('Chose to Change',um)
    if ud=='Name':
        sid = st.number_input('Id', min_value=0)
        name = st.text_input('Name')
        b=st.button('Update',type='primary')
        if b:
            uq="update student set sname=? where sid=?"
            cus.execute(uq,(name,sid))
            con.commit()
            st.success('Updated Successfully')
            st.balloons()
    elif ud=='Phone':
        sid = st.number_input('Id', min_value=0)
        age = st.number_input('phon',min_value=0)
        b=st.button('Update', type='primary')
        if b:
            uq = "update student set phno=? where sid=?"
            cus.execute(uq, (age, sid))
            con.commit()
            st.success('Updated Successfully')
            st.balloons()
    elif ud=='DOB':
        sid = st.number_input('Id', min_value=0)
        pn = st.date_input('Dob')
        b=st.button('Update', type='primary')
        if b:
            uq = "update student set dob=? where sid=?"
            cus.execute(uq, (pn, sid))
            con.commit()
            st.success('Updated Successfully')
            st.balloons()
    elif ud=='Gender':
        sid = st.number_input('Id', min_value=0)
        po=st.radio('Gender',['Male','Female'])
        b=st.button('Update',type='primary')
        if b:
            uq="update student set gender=? where sid=?"
            cus.execute(uq,(po,sid))
            con.commit()
            st.success('Updated Successfully')
            st.balloons()
    elif ud=='Address':
        sid = st.number_input('Id', min_value=0)
        ad = st.text_area('Address')
        b=st.button('Update', type='primary')
        if b:
            uq = "update student set address=? where sid=?"
            cus.execute(uq, (ad, sid))
            con.commit()
            st.success('Updated Successfully')
            st.balloons()
    elif ud=='Photo':
        sid = st.number_input('Id', min_value=0)
        ph = st.file_uploader('Photo', type=['jpg', 'png', 'svg'])
        b = st.button('Update', type='primary')
        if b:
            uq = "update student set photo=? where sid=?"
            im = ph.read()
            cus.execute(uq, (im, sid))
            con.commit()
            st.success('Updated Successfully')
            st.balloons()
if st.session_state.logged:
    menu=['Add Student','Display Student','Remove Student','Update Student']
    op=st.radio('Chose the Option', menu)
    if op=='Add Student':
        inse()
    elif op=='Display Student':
        disp()
    elif op=='Remove Student':
        remv()
    elif op=='Update Student':
        upd()
else:
    login()

