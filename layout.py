import pip
pip.main(['install', '-r', 'requirement.txt'])

import streamlit as st
from textblob import TextBlob
from enhance_note_backend import *

# Tạo giao diện cho người dùng nhập ghi chú
st.set_page_config(layout="wide")  # Thiết lập giao diện toàn màn hình
st.title("NoteGen AI")

# Sử dụng Session State để lưu trữ nội dung note
if 'note' not in st.session_state:
    st.session_state['note'] = ""

# Bố cục trang: điều chỉnh cột để cột 2 rộng hơn và giảm khoảng trống
col1, col2 = st.columns([3.5, 1.5])  # Mở rộng cả hai cột để giảm khoảng trống

# Cột 1: chứa text area và prompt
with col1:
    # Tạo một text area để người dùng nhập note ban đầu, nội dung là từ session_state
    note = st.text_area("Take note here:", value=st.session_state['note'], height=300)

    # Tạo một text input để người dùng nhập prompt chỉnh sửa ghi chú
    prompt = st.text_input("Take prompt to enhance note:")

    # Nút để thực hiện chỉnh sửa
    if st.button("Enhance note"):
        if note and prompt:
            # Giả lập xử lý chỉnh sửa với prompt
            edited_note = prompt_enhance_note(prompt, note)

            # Hiển thị ghi chú đã chỉnh sửa
            st.subheader("After enhance note by prompt:")
            st.write(edited_note)
        else:
            st.error("Please take your note and prompt to execute enhancing note!")

# Cột 2: Hiển thị số lượng từ và kiểm tra lỗi chính tả
with col2:
    st.subheader("Information about note")

    # Đếm số lượng từ
    word_count = len(note.split())
    st.write(f"Word count: {word_count}")

    # Kiểm tra lỗi chính tả với TextBlob
    spelling_mistakes = checkNumber_of_Spelling(note)

    st.write(f"Spelling mistakes: {spelling_mistakes}")

    # Tạo nút "Sửa chính tả" với màu cyan
    fix_spelling_button = st.markdown("""
        <style>
        .stButton > button {
            background-color: #00FFFF;
            color: black;
        }
        </style>""", unsafe_allow_html=True)

    if st.button("Correct spells"):
        corrected_note = show_spells_error(note)

        # Cập nhật lại ghi chú đã sửa vào session state
        # st.session_state['note'] = corrected_note
        if corrected_note == "":
            st.write("No spelling mistakes")
        else:
            st.subheader("After check spelling:")
            st.write(corrected_note)
