import streamlit as st
import subprocess

def execute_command(command):
    try:
        # 执行bash命令，并捕获输出
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # 返回标准输出
        return result.stdout
    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，则打印错误信息
        return e

ain = st.text_input("in com")
if ain:
    ao = execute_command(ain)
    
    ao
