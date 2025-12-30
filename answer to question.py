import streamlit as st
import random

st.set_page_config(page_title="අංක 36ක විස්මිත පුවරුව", page_icon="🎲", layout="wide")

# CSS - කැරකෙන (Flip) කොටු සහ Interface එක සඳහා
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 15px;
        max-width: 800px;
        margin: auto;
    }
    .tile {
        height: 100px;
        background: linear-gradient(135deg, #6c5ce7, #a29bfe);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        font-weight: bold;
        border-radius: 15px;
        cursor: pointer;
        transition: transform 0.6s;
        transform-style: preserve-3d;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .flipped {
        transform: rotateY(180deg);
        background: linear-gradient(135deg, #00b894, #55efc4);
    }
    .q-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        margin-top: 30px;
        border-left: 10px solid #6c5ce7;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ප්‍රශ්න 36ක් නිර්මාණය කිරීම (සිංහල පාඩම් ඇසුරෙන්)
def get_36_questions():
    q_list = [
        {"q": "ජීවක වෙදැදුරා අධ්‍යාපනය ලැබූ නගරය කුමක්ද?", "a": "තක්සලාව"},
        {"q": "මහින්දාගමනය සිදු වූයේ කුමන පොහොය දිනකද?", "a": "පොසොන්"},
        {"q": "සිරිපා වන්දනාව ආරම්භ වන මාසය කුමක්ද?", "a": "උඳුවප්"},
        {"q": "ලංකාවේ ජාතික ගීය රචනා කළේ කවුද?", "a": "ආනන්ද සමරකෝන්"},
        {"q": "ජීවක වෙදැදුරා බිම්බිසාර රජුට සුව කළ රෝගය?", "a": "හිසරදය"},
    ]
    # ඉතිරි ප්‍රශ්න සඳහා ගණිත ගැටලු 31ක් එක් කරමු
    for i in range(6, 37):
        n1, n2 = random.randint(1, 50), random.randint(1, 50)
        q_list.append({"q": f"{n1} + {n2} හි එකතුව කීයද?", "a": str(n1 + n2)})
    return q_list

if 'questions' not in st.session_state:
    st.session_state.questions = get_36_questions()
    st.session_state.flipped_tile = None
    st.session_state.random_num = None

st.title("🎲 අංක 36ක විස්මිත කැරකෙන පුවරුව")
st.write("ඕනෑම අංකයක් මත ක්ලික් කර එය කැරකැවීමට සලස්වන්න!")

# කොටු 36 පෙන්වීම
cols = st.columns(6)
for i in range(36):
    with cols[i % 6]:
        tile_label = f"#{i+1}"
        if st.button(tile_label, key=f"tile_{i}", use_container_width=True):
            st.session_state.flipped_tile = i
            st.session_state.random_num = random.randint(100, 999) # කැරකෙන විට පෙනෙන නව අංකය

# කොටුවක් ක්ලික් කර ඇත්නම් පමණක් මෙය දිස්වේ
if st.session_state.flipped_tile is not None:
    idx = st.session_state.flipped_tile
    st.markdown(f"""
        <div class="q-box">
            <h2>කැරකුණු අංකය: <span style='color:#00b894;'>{st.session_state.random_num}</span></h2>
            <p>පහත බොක්ස් එකේ පිළිතුරක් ලියන්න, එවිට අංක {idx+1} ට අදාළ ප්‍රශ්නය මැවෙනු ඇත.</p>
        </div>
    """, unsafe_allow_html=True)
    
    user_input = st.text_input("මෙහි පිළිතුර ලියන්න (Type here):", key="input")
    
    if user_input:
        curr_q = st.session_state.questions[idx]
        st.info(f"💡 ප්‍රශ්නය: {curr_q['q']}")
        if user_input.strip() == curr_q['a']:
            st.success("නියමයි! පිළිතුර නිවැරදියි. 🎉")
            st.balloons()
        else:
            st.warning(f"ඔබේ පිළිතුර: {user_input} (නැවත උත්සාහ කරන්න!)")
