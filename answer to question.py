import streamlit as st
import random

# පිටුවේ සැකසුම් සහ නම
st.set_page_config(page_title="විස්මිත අංක 36 පුවරුව", layout="wide")

# CSS - මෙහිදී තමයි සියලුම තාක්ෂණික අලංකාරයන් ඇතුළත් වෙන්නේ
st.markdown("""
    <style>
    /* පසුබිම් වර්ණය */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* කොටු වල හැඩය සහ ඇනිමේෂන් */
    .stButton > button {
        border: none;
        border-radius: 15px;
        height: 100px;
        width: 100%;
        background: linear-gradient(145deg, #6c5ce7, #a29bfe);
        color: white !important;
        font-size: 32px !important;
        font-weight: bold;
        box-shadow: 5px 5px 15px #bebebe, -5px -5px 15px #ffffff;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    /* මූසිකය ගෙනගිය විට වෙනස් වන ආකාරය */
    .stButton > button:hover {
        transform: rotateY(180deg) scale(1.05);
        background: linear-gradient(145deg, #00b894, #55efc4);
        box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }

    /* ප්‍රශ්න පෙන්වන පෙට්ටිය */
    .question-card {
        background: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;
        text-align: center;
        border-top: 10px solid #6c5ce7;
        margin-top: 30px;
        animation: fadeIn 1s;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .secret-num {
        font-size: 80px;
        color: #d63031;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 1-36 ප්‍රශ්න ගබඩාව
def get_special_question(n):
    # උදාහරණ කිහිපයක් (මෙයට ඔබට අවශ්‍ය ඕනෑම ප්‍රශ්නයක් දැමිය හැක)
    data = {
        1: "පළමුවන රජු ලෙස සලකන්නේ කවුද?",
        4: "16 හි වර්ගමූලය ($\sqrt{16}$) කීයද?",
        7: "සතියකට ඇති දින ගණන කීයද?",
        12: "අවුරුද්දකට ඇති මාස ගණන කීයද?",
        36: "6 වරක් 6 කීයද?"
    }
    if n in data:
        return data[n]
    return f"අංක {n} ට අදාළ රහස් ගණිත ගැටලුව: {n} x 2 කීයද?"

# Session State පවත්වා ගැනීම
if 'selected' not in st.session_state:
    st.session_state.selected = None
    st.session_state.code = None

st.markdown("<h1 style='text-align: center; color: #2d3436;'>🎯 අංක 36ක විස්මිත කැරකෙන පුවරුව</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>කොටුවක් මත මූසිකය ගෙන ගොස් එය කරකවන්න!</p>", unsafe_allow_html=True)

# Grid එක නිර්මාණය (කොටු 36)
cols = st.columns(6)
for i in range(1, 37):
    with cols[(i-1) % 6]:
        if st.button(f"{i}", key=f"t_{i}"):
            st.session_state.selected = i
            st.session_state.code = random.randint(100, 999)

# කොටුවක් තෝරාගත් පසු
if st.session_state.selected:
    st.markdown("---")
    
    # රහස් අංකය පෙන්වන කොටස
    st.markdown(f"""
        <div class="question-card">
            <h3>ඔබ අංක {st.session_state.selected} කොටුව කරකැවුවා!</h3>
            <p>පහත දැක්වෙන්නේ ඔබේ රහස් කේතයයි:</p>
            <div class="secret-num">{st.session_state.code}</div>
        </div>
    """, unsafe_allow_html=True)

    # කේතය ඇතුළත් කිරීමට
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        val = st.text_input("රහස් කේතය මෙහි ලියන්න:", key="secret_val")
        
        if val == str(st.session_state.code):
            q_text = get_special_question(st.session_state.selected)
            st.markdown(f"""
                <div class="question-card" style="border-top: 10px solid #00b894;">
                    <h2 style="color: #00b894;">💡 ප්‍රශ්නය:</h2>
                    <h1 style="font-size: 40px;">{q_text}</h1>
                </div>
            """, unsafe_allow_html=True)
            
            ans = st.text_input("ඔබේ පිළිතුර:", key="final_ans")
            if ans == str(st.session_state.selected):
                st.balloons()
                st.success("විශිෂ්ටයි! ඔබ ජයග්‍රහණය කළා.")
