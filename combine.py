import streamlit as st
import pandas as pd
import datetime
import uuid
import json
import os
from PIL import Image
from anti2 import DECISION_TREE  # Importing the decision tree from anti2.py
import base64

# Ilova konfiguratsiyasi
st.set_page_config(
    page_title="Manfaatlar to'qnashuvi deklaratsiyasi",
    page_icon="🇺🇿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Davlat saytlariga o'xshash interfeys dizaynini sozlash
def set_custom_style():
    # CSS stillarini qo'shish
    st.markdown("""
    <style>
        .stApp {
        background-color: #F8F8F8; /* Qaymoq rang, o‘zgartirish uchun boshqa hex kod qo‘shing */
    }
        .sidebar-logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 300px;        /* Kenglik */
            height: auto;        /* Balandlik mos ravishda */
            border-radius: 15px;
        }
        
        /* Asosiy ranglar */
        :root {
            --main-color: #0065BD;
            --secondary-color: #003366;
            --accent-color: #E50000;
            --light-color: #F5F5F5;
            --header-color: #022F54;
            --border-color: #CCCCCC;
        }
        
        /* Asosiy dizayn */
        .main {
            background-color: white;
            padding: 10px;
        }
        
        /* Header */
        .css-18e3th9 {
            padding-top: 0;
        }
        
        .header {
            background-color: var(--header-color);
            color: white;
            padding: 20px;
            border-radius: 0;
            text-align: center;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .header-title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin: 0;
        }
        
        .header-logo {
            height: 60px;
            margin-right: 20px;
        }
        [data-testid="stSidebar"] {
            background-color: #FFFFFF; /* bu yerda rangni o'zgartiring */
            font-size: 24px;       /* Yozuvni kattalashtiradi */
            font-weight: bold;
            border-right: 4px solid #0065bd;
        }
        /* Formalar */
        .form-container {
            border: 1px solid var(--border-color);
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .section-title {
            color: var(--main-color);
            border-bottom: 2px solid var(--main-color);
            padding-bottom: 5px;
            margin-bottom: 15px;
            font-weight: bold;
        }
        
        /* Tugmalar */
        div.stButton > button {
            background-color: #0065bd;  /* yashil fon */
            color: white;               /* oq yozuv */
            border: 2px solid 	#90EE90 !important;               /* border olib tashlandi */
            padding: 10px 24px;
            border-radius: 8px;         /* yumaloq burchak */
            font-size: 16px;
        }
        
        .stButton>button:hover {
        border-color: #FF0000 !important;
        background-color: #003087 !important;  /* Havo rang fon */
        color: white !important;              /* Oq matn */
        border-radius: 12px !important;       /* Dumaloq shakl */
        transform: scale(1.05);               /* Kattalashadi */
        transition: all 0.3s ease-in-out;     /* Silliq effekt */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Soya qo'shish */
}
        /* Inputlar */
        .stTextInput>div>div>input, 
        .stSelectbox>div, 
        .stTextArea>div>div>textarea {
            border-radius: 4px;
            border: 1px solid var(--border-color);
        }
        
        /* Progress */
        .stProgress>div>div>div {
            background-color: white !important; /* Oq rang */
            height: 8px !important; /* Balandligini oshirish */
            border: 1px solid #0065BD !important; /* Ko'k chiziq bilan chegaralash */
            box-shadow: 0 0 5px rgba(255, 255, 255, 0.7) !important; 
        }
        
        /* Sidebar */
        .css-1d391kg {
            background-color: var(--light-color);
        }
        
        .sidebar-nav {
            margin-bottom: 10px;
            padding: 10px;
            background-color: white;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
        }
        
        .sidebar-nav:hover {
            background-color: var(--light-color);
            color: var(--main-color);
        }
        
        .sidebar-icon {
            margin-right: 10px;
            color: var(--main-color);
        }
        
        .sidebar-active {
            background-color: var(--main-color);
            color: white;
        }
        
        .sidebar-active .sidebar-icon {
            color: white;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 20px;
            background-color: var(--header-color);
            color: white;
            margin-top: 30px;
            border-radius: 4px;
            font-size: 14px;
        }
        
        /* Admin panel */
        .metric-container {
            background-color: white;
            border-radius: 4px;
            padding: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .metric-value {
            font-size: 24px;
            font-weight: bold;
            color: var(--main-color);
        }
        
        .metric-label {
            color: gray;
            font-size: 14px;
        }
        
        .table-container {
            background-color: white;
            border-radius: 4px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        
        /* Xabar boxlari */
        .info-box {
            background-color: #E6F3FF;
            border-left: 5px solid var(--main-color);
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }
        
        .warning-box {
            background-color: #FFF9E6;
            border-left: 5px solid #FFB400;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }
        
        .success-box {
            background-color: #E6FFE6;
            border-left: 5px solid #00A300;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }
        
        .error-box {
            background-color: #FFE6E6;
            border-left: 5px solid var(--accent-color);
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }
        
        /* Tablitsa */
        .styled-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15px;
            font-size: 14px;
        }
        
        .styled-table thead tr {
            background-color: var(--main-color);
            color: white;
            text-align: left;
        }
        
        .styled-table th,
        .styled-table td {
            padding: 12px 15px;
            border-bottom: 1px solid #E0E0E0;
        }
        
        .styled-table tbody tr:nth-of-type(even) {
            background-color: #F8F8F8;
        }
        
        .styled-table tbody tr:hover {
            background-color: #EEEEFF;
        }
        
        /* Navbar */
        .navbar {
            display: flex;
            background-color: var(--main-color);
            padding: 10px 20px;
            color: white;
            margin-bottom: 20px;
            border-radius: 4px;
            align-items: center;
        }
        
        .navbar-item {
            padding: 8px 15px;
            margin-right: 10px;
            cursor: pointer;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        
        .navbar-item:hover {
            background-color: rgba(255, 255, 255, 0.2);
        }
        
        .navbar-active {
            background-color: rgba(255, 255, 255, 0.3);
            font-weight: bold;
        }
        
        /* Buttons */
        .primary-button {
            background-color: var(--main-color);
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }
        
        .secondary-button {
            background-color: white;
            color: var(--main-color);
            padding: 8px 16px;
            border: 1px solid var(--main-color);
            border-radius: 4px;
            cursor: pointer;
        }
        
        .danger-button {
            background-color: var(--accent-color);
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .sidebar-title {
        font-size: 36px;           /* Yozuv o'lchami */
        font-weight: bold;         /* Qalin font */
        color: #000000;            /* Yozuvning rangi (qora rangga yaqin) */
        text-align: left;        /* O'rtaga tekislash */
        margin-top: 10px;          /* Yuqoridan biroz bo'shliq */
        }
        .sidebar-title:hover {
        color: #000000;            /* Sichqoncha ustiga olib borganda ko'k rangga o'zgaradi */
        }
        
        /* Mobil moslashtirish */
        @media screen and (max-width: 768px) {
            .header {
                flex-direction: column;
            }
            
            .header-logo {
                margin-right: 0;
                margin-bottom: 10px;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar-ga "Xizmatlar" yozuvini qo'shish
st.sidebar.markdown("""
    <div class="sidebar-title">
        Xizmatlar
    </div>
""", unsafe_allow_html=True)

# Davlat gerbi yoki logotipni ko'rsatish

def get_base64_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def show_logo():
    gerb_base64 = get_base64_image("logo2.png")  # ← Fayl nomi

    # CSS
    st.markdown("""
    <style>
    .header-content {
        display: flex;             /* Elementlarni yonma-yon joylashtirish */
        align-items: center;       /* Vertikal markazlashtirish */
        gap: 5px;                  /* Elementlar orasidagi bo'shliq */
        justify-content: center
    }
    .header-logo {
        width: 80px;               /* Rasmning kengligi */
        height: 80px;              /* Rasmning balandligi */
        object-fit: contain;       /* Rasmning asl shaklini saqlash */
        border-radius: 0;          /* Dumaloqlikni olib tashlash */
    }
    .kun-text {
        font-size: 48px;           /* "TO'QNASHUV" uchun kattaroq font */
        font-weight: bold;         /* Qalin font */
        color: #1C2526;            /* Rasmdagi qora rangga yaqin */
        margin-right: 5px;         /* Nuqta bilan bo'shliq */
    }
    .dot {
        font-size: 48px;           /* Nuqta o'lchami */
        font-weight: bold;         /* Qalin nuqta */
        color: #1C2526;            /* Rasmdagi qora rangga yaqin */
        margin-right: 5px;         /* Dumaloq element bilan bo'shliq */
    }
    .uz-circle {
        background-color: #003087; /* Dumaloq elementning ko'k rangi (rasmdagi kabi) */
        color: white;              /* Matn oq rangda */
        font-size: 48px;           /* "UZ" uchun kichikroq font */
        font-weight: bold;         /* Qalin font */
        border-radius: 50%;        /* To'liq dumaloq shakl */
        width: 70px;               /* Dumaloq elementning kengligi */
        height: 70px;              /* Dumaloq elementning balandligi */
        display: flex;             /* Matnni markazlashtirish uchun */
        align-items: center;       /* Vertikal markazlashtirish */
        justify-content: center;   /* Gorizontal markazlashtirish */
    }
    </style>
    """, unsafe_allow_html=True)

    # HTML orqali logotipni chiqarish ("KUN.UZ" o'rniga "TO'QNASHUV.UZ")
    st.markdown(f"""
        <div class="header-content">
            <img src="data:image/png;base64,{gerb_base64}" class="header-logo">
            <span class="kun-text">TO'QNASHUV</span>
            <span class="dot">.</span>
            <div class="uz-circle">UZ</div>
        </div>
    """, unsafe_allow_html=True)


# Ma'lumotlar saqlash funksiyalari
def load_data():
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Deklaratsiyalar
    if not os.path.exists("data/declarations.json"):
        with open("data/declarations.json", "w") as f:
            json.dump([], f)
    
    with open("data/declarations.json", "r") as f:
        return json.load(f)

def save_declaration(declaration):
    declarations = load_data()
    declarations.append(declaration)
    with open("data/declarations.json", "w") as f:
        json.dump(declarations, f)

# Admin foydalanuvchilar ro'yxati (real holatda xavfsizlikni yaxshilash kerak)
ADMINS = {
    "kadrlar": "password123",
    "xavfsizlik": "password123"
}

# Sessiya holatini boshqarish
def init_session():
    if "page" not in st.session_state:
        st.session_state.page = "main"
    if "form_stage" not in st.session_state:
        st.session_state.form_stage = 1
    if "form_data" not in st.session_state:
        st.session_state.form_data = {}
    if "admin_view" not in st.session_state:
        st.session_state.admin_view = None
    if "admin_type" not in st.session_state:
        st.session_state.admin_type = None
    if "relatives" not in st.session_state:
        st.session_state.relatives = []
    if "legal_entities" not in st.session_state:
        st.session_state.legal_entities = []
    if "relative_legal_entities" not in st.session_state:
        st.session_state.relative_legal_entities = []
    if "lang" not in st.session_state:
        st.session_state.lang = "uz"
    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False
    # anti3.py uchun state qo'shish
    if "conflict_page" not in st.session_state:
        st.session_state.conflict_page = "welcome"
    if "conflict_current_node" not in st.session_state:
        st.session_state.conflict_current_node = "start"
    if "conflict_path" not in st.session_state:
        st.session_state.conflict_path = []

init_session()

# Navigatsiya funksiyalari
def navigate_to(page):
    st.session_state.page = page
    st.session_state.button_clicked = False

def next_stage():
    st.session_state.form_stage += 1
    st.session_state.button_clicked = False

def prev_stage():
    st.session_state.form_stage -= 1
    st.session_state.button_clicked = False

def reset_form():
    st.session_state.form_stage = 1
    st.session_state.form_data = {}
    st.session_state.relatives = []
    st.session_state.legal_entities = []
    st.session_state.relative_legal_entities = []
    st.session_state.button_clicked = False

# Dizaynni sozlash
set_custom_style()

#################################
# anti3.py dan funksiyalarni import qilish
#################################

# Daraxtni yuklash
@st.cache_data
def load_decision_tree():
    # To'g'ridan-to'g'ri o'rnatilgan daraxtni qaytarish
    return DECISION_TREE
  
def show_welcome_page():
    st.title("Manfaatlar to'qnashuvini aniqlash dasturi")
    if st.button("Boshlash", key="start_button", use_container_width=True):
        st.session_state.conflict_page = "quiz"
        st.rerun() 
        
    st.markdown("---")
  
def show_node(node_id, tree):
    # Agar node_id dict bo'lsa, bu natija objekti
    if isinstance(node_id, dict):
        return show_result(node_id)
    
    # Tugunni olish
    node = tree.get(node_id)
    if not node:
        st.error(f"Xatolik: Tugun {node_id} topilmadi")
        return
    
    # Progress ko'rsatish
    if node_id != "start":
        progress_value = min(len(node_id.split('.')) * 0.1, 1.0)
        st.progress(progress_value)
    
    # Savolni ko'rsatish
    st.markdown(f"## {node['question']}")
    
    # Javob tugmalarni yaratish
    for option in node["options"]:
        if st.button(option, key=f"{node_id}_{option}", use_container_width=True):
            # Javobga ko'ra keyingi tugun yoki natijani aniqlash
            next_item = node["next"][option]
            st.session_state.conflict_current_node = next_item
            st.session_state.conflict_path.append({
                "question": node["question"],
                "answer": option
            })
            st.rerun()

# Natijani ko'rsatish
def show_result(result):
    # Natijani ko'rsatish
    st.markdown(f"# {result['title']}")
    
    # Vaziyat tahlili
    if "analysis" in result:
        st.markdown("## Vaziyat tahlili:")
        st.markdown(result["analysis"])
    
    # Tavsiyalar
    if "recommendations" in result:
        st.markdown("## Tavsiyalar:")
        for i, rec in enumerate(result['recommendations'], 1):
            st.markdown(f"{i}. {rec}")
    
    # Qonuniy asos
    if "legal_basis" in result:
        st.markdown("## Qonuniy asos:")
        for basis in result['legal_basis']:
            st.markdown(f"- {basis}")
    
    
    # So'rovlar yo'lini ko'rsatish
    if len(st.session_state.conflict_path) > 0:
        st.markdown("---")
        st.markdown("### Sizning javoblaringiz:")
        for i, item in enumerate(st.session_state.conflict_path, 1):
            st.markdown(f"**{i}. {item['question']}** - *{item['answer']}*")
    
    # Natijani eksport qilish tugmasi
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Natijani saqlash", key="export_result", use_container_width=True):
            export_result(result)
    
    with col2:
        if st.button("🏠 Bosh sahifaga qaytish", use_container_width=True):
            st.session_state.conflict_page = "welcome"
            st.session_state.conflict_current_node = "start"
            st.session_state.conflict_path = []
            st.rerun()

# Natijani eksport qilish funksiyasi
def export_result(result):
    # Natija matnini tayyorlash
    result_text = f"# {result['title']}\n\n"
    
    if "analysis" in result:
        result_text += "## Vaziyat tahlili:\n"
        result_text += f"{result['analysis']}\n\n"
    
    if "recommendations" in result:
        result_text += "## Tavsiyalar:\n"
        for i, rec in enumerate(result['recommendations'], 1):
            result_text += f"{i}. {rec}\n"
        result_text += "\n"
    
    if "legal_basis" in result:
        result_text += "## Qonuniy asos:\n"
        for basis in result['legal_basis']:
            result_text += f"- {basis}\n"
        result_text += "\n"
    
    if "steps" in result:
        result_text += "## Keyingi qadamlar:\n"
        for i, step in enumerate(result['steps'], 1):
            result_text += f"{i}. {step}\n"
    
    # So'rovlar yo'lini qo'shish
    if len(st.session_state.conflict_path) > 0:
        result_text += "\n---\n### Sizning javoblaringiz:\n"
        for i, item in enumerate(st.session_state.conflict_path, 1):
            result_text += f"{i}. {item['question']} - {item['answer']}\n"
    
    # Natijani yuklab olish imkonini berish
    st.download_button(
        label="📥 Yuklab olish",
        data=result_text,
        file_name="manfaatlar_toqnashuvi_natijasi.txt",
        mime="text/plain",
    )

# Savol-javob qismini ko'rsatish
def show_quiz_page():
    # Sarlavha va tavsif
    st.title("Manfaatlar to'qnashuvini aniqlash tizimi")
    # Joriy tugunni ko'rsatish
    tree = load_decision_tree()
    current_node = st.session_state.conflict_current_node
    show_node(current_node, tree)

# Manfaatlar to'qnashuvi dasturini ko'rsatish
def show_conflict_of_interest_tool():
    st.markdown("""
    <style>
    button:hover {
        background-color: #0065BD !important;  /* Yashil fon */
        color: white !important;              /* Oq matn */
        border-radius: 12px !important;       /* Dumaloq shakl */
        transform: scale(1.05);               /* Kattalashadi */
        transition: all 0.3s ease-in-out;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sahifani ko'rsatish
    if st.session_state.conflict_page == "welcome":
        show_welcome_page()
    elif st.session_state.conflict_page == "quiz":
        show_quiz_page()

#################################
# Asosiy dasturni davom ettirish
#################################

# Yuqori panel (Header)
show_logo()

# Til tanlash
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

with col4:
    lang_options = {
        "uz": "UZ",
        "ru": "RU",
        "en": "ENG"
    }
    selected_lang = st.selectbox("", 
                               options=list(lang_options.keys()),
                               format_func=lambda x: lang_options[x],
                               index=list(lang_options.keys()).index(st.session_state.lang))
    
    if selected_lang != st.session_state.lang:
        st.session_state.lang = selected_lang
        st.rerun()

# Navbar
st.markdown("""
<div class="navbar">
    <div class="navbar-item navbar-active" onclick="window.location.href='#'">Bosh sahifa</div>
    <div class="navbar-item" onclick="window.location.href='#'">Normativ hujjatlar</div>
    <div class="navbar-item" onclick="window.location.href='#'">Hisobotlar</div>
    <div class="navbar-item" onclick="window.location.href='#'">Bog'lanish</div>
</div>
""", unsafe_allow_html=True)

# Sidebar (Yon panel)
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h3 style="color: #003366;">           </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigatsiya elementlari - TO'G'RILANGAN
    def sidebar_item(icon, text, page_name, active=False):
        active_class = "sidebar-active" if active else ""
        
        # Faqat Streamlit tugmasini ishlatamiz
        if st.button(f"{icon} {text}", key=f"sidebar_{page_name}", 
                     on_click=navigate_to, args=(page_name,),
                     use_container_width=True):
            pass  # Harakat navigate_to funksiyasiga berildi
    
    # Navigatsiya elementlari
    sidebar_item("📝", "Deklaratsiya to'ldirish", "main", st.session_state.page == "main")
    
    # Manfaatlar to'qnashuvi tugmasini qo'shamiz
    if st.button("🔍 Manfaatlar to'qnashuvi", key="sidebar_conflict", use_container_width=True):
        navigate_to("conflict_tool")
        # Manfaatlar to'qnashuvi dasturi uchun boshlang'ich qiymatlarni o'rnatish
        st.session_state.conflict_page = "welcome"
        st.session_state.conflict_current_node = "start"
        st.session_state.conflict_path = []
    
    sidebar_item("ℹ️", "Ma'lumot va yordam", "help", st.session_state.page == "help")
    sidebar_item("📞", "Bog'lanish", "contact", st.session_state.page == "contact")
    sidebar_item("👤", "Admin kirish", "admin_login", st.session_state.page == "admin_login")
    
    st.markdown("""
    <div style="margin-top: 50px; padding: 10px; background-color: #f0f0f0; border-radius: 5px;">
        <p style="font-size: 14px; color: #666;">O'zbekiston Respublikasi<br>Korrupsiyaga qarshi kurashish agentligi</p>
        <p style="font-size: 12px; color: #888;">Tel: +998 71 123 45 67<br>E-mail: info@anticorruption.uz</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="footer" style="margin-top: 20px; font-size: 12px;">
        © 2025 Manfaatlar to'qnashuvi tizimi<br>
        <small>Barcha huquqlar himoyalangan</small>
    </div>
    """, unsafe_allow_html=True)

# Ma'lumot va yordam sahifasi
def show_help_page():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Ma'lumot va yordam</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 20px;">
        <h3 style="color: #003366;">Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya nima?</h3>
        <p>
            Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya - bu xodimning o'z lavozim yoki xizmat 
            majburiyatlarini bajarishiga ta'sir ko'rsatishi mumkin bo'lgan shaxsiy manfaatlarini oshkor qilish 
            maqsadida to'ldiriladigan rasmiy hujjat.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h3 style="color: #003366;">Kimlar to'ldirishi kerak?</h3>
        <p>
            Davlat organlarida va mahalliy davlat hokimiyati organlarida, davlat muassasalarida, davlat unitar 
            korxonalarida, davlat maqsadli jamg'armalarida, shuningdek ustav fondida (ustav kapitalida) davlat 
            ulushi 50 foiz miqdorda va undan ortiq bo'lgan aksiyadorlik jamiyatlarida mehnat faoliyatini amalga 
            oshirayotgan xodimlar.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h3 style="color: #003366;">Qanday to'ldirish kerak?</h3>
        <p>
            Deklaratsiya 5 bosqichdan iborat:
        </p>
        <ol>
            <li>Xodim haqida asosiy ma'lumotlar</li>
            <li>ID va shaxsiy ma'lumotlar</li>
            <li>Yaqin qarindoshlar ma'lumotlari</li>
            <li>Yuridik shaxslar ma'lumotlari</li>
            <li>Manfaatlar to'qnashuvi tavsifi</li>
        </ol>
        <p>
            Har bir bosqichda barcha majburiy maydonlarni to'ldiring. Agar ma'lumot to'liq bo'lmasa, 
            keyingi bosqichga o'tish imkoni bo'lmaydi.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="margin-top: 30px; padding: 15px; background-color: #E6F3FF; border-left: 5px solid #0065BD; border-radius: 4px;">
            <h4 style="margin-top: 0; color: #0065BD;">Muhim eslatma</h4>
            <p style="margin-bottom: 0;">
                O'zbekiston Respublikasining "Manfaatlar to'qnashuvi to'g'risida"gi Qonuniga muvofiq, 
                manfaatlar to'qnashuvi to'g'risidagi ma'lumotlarni oshkor qilmaslik yoki buzib ko'rsatish, 
                shuningdek xodim tomonidan manfaatlar to'qnashuvini tartibga solish choralarini ko'rmaganligi
                tegishli javobgarlikka sabab bo'lishi mumkin.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Bog'lanish sahifasi - TO'G'RILANGAN
def show_contact_page():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Bog'lanish</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Asosiy aloqa ma'lumotlari
    st.markdown("""
    <div style="margin-top: 30px; display: flex; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; min-width: 300px; padding: 20px; background-color: #F5F5F5; border-radius: 5px;">
            <h3 style="color: #003366;">Aloqa ma'lumotlari</h3>
            <p><strong>Tel:</strong> +998 71 123 45 67</p>
            <p><strong>Email:</strong> info@anticorruption.uz</p>
            <p><strong>Manzil:</strong> Toshkent shahri, Mustaqillik maydoni, 5-uy</p>
            <p><strong>Ish vaqti:</strong> Dushanbadan jumaga, 9:00 - 18:00</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Ishonch telefoni
    st.markdown("""
        <div style="flex: 1; min-width: 300px; padding: 20px; background-color: #F5F5F5; border-radius: 5px;">
            <h3 style="color: #003366;">Ishonch telefoni</h3>
            <p style="font-size: 24px; font-weight: bold; color: #0065BD;">+998 71 200-06-00</p>
            <p>Manfaatlar to'qnashuvi masalalari bo'yicha maslahat olish</p>
            <p><strong>Ishonch telefoni ish vaqti:</strong><br>Har kuni, 9:00 - 18:00</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Murojaat qoldirish formasi
    st.markdown("""
    <div style="margin-top: 30px; padding: 20px; background-color: #F5F5F5; border-radius: 5px;">
        <h3 style="color: #003366;">Murojaat qoldirish</h3>
        <p>Quyidagi formani to'ldirish orqali savol va murojaatlaringizni qoldirishingiz mumkin:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Form elementlarini Streamlit komponentlari bilan almashtirish
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input("F.I.O. *", placeholder="F.I.O.")
    
    with col2:
        st.text_input("Telefon *", placeholder="Telefon raqami")
    
    st.text_input("Email", placeholder="Email manzili")
    st.text_area("Murojaat matni *", placeholder="Murojaat matnini kiriting...", height=120)
    
    # Yuborish tugmasi
    if st.button("Yuborish", key="send_btn", type="primary"):
        if not st.session_state.button_clicked:
            st.session_state.button_clicked = True
            st.success("Murojaatingiz muvaffaqiyatli yuborildi!")
            
# Admin kirish sahifasi
def show_admin_login():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Admin kirish</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="padding: 30px; background-color: #F5F5F5; border-radius: 5px; margin: 30px 0;">
            <h3 style="color: #003366; text-align: center; margin-bottom: 20px;">Tizimga kirish</h3>
        """, unsafe_allow_html=True)
        
        admin_username = st.text_input("Login", placeholder="Foydalanuvchi nomi")
        admin_password = st.text_input("Parol", type="password", placeholder="Parol")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            # Button tugmalari bilan ishlash - TO'G'RILANGAN
            if st.button("Kirish", key="login_button", use_container_width=True):
                if not st.session_state.button_clicked:
                    st.session_state.button_clicked = True
                    if admin_username in ADMINS and ADMINS[admin_username] == admin_password:
                        st.session_state.admin_type = admin_username
                        navigate_to("admin_panel")
                    else:
                        st.error("Noto'g'ri login yoki parol")
        
        st.markdown("""
        </div>
        """, unsafe_allow_html=True)

# Deklaratsiya to'ldirish - Bosqich 1: Kirish qismi
def show_form_stage1():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya</h2>
        <p style="color: #666;">O'zbekiston Respublikasining "Manfaatlar to'qnashuvi to'g'risida"gi Qonunining 9-moddasiga muvofiq</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-top: 20px;">
        <h3 style="color: #003366;">1-bosqich: Xodim ma'lumotlari</h3>
    """, unsafe_allow_html=True)
    
    st.progress(1/5, "20%")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        full_name = st.text_input("To'liq ismingiz (F.I.O.)", 
                                  value=st.session_state.form_data.get("full_name", ""),
                                  placeholder="Familiya Ism Otasining ismi")
        position = st.text_input("Lavozimingiz", 
                               value=st.session_state.form_data.get("position", ""),
                               placeholder="Lavozimingizni kiriting")
    
    with col2:
        declaration_type = st.selectbox("Deklaratsiya turi",
                                      options=["Yillik", "Ishga qabul qilinayotganda", "Boshqa ishga o'tkazilayotganda"],
                                      index=0 if "declaration_type" not in st.session_state.form_data else 
                                      ["Yillik", "Ishga qabul qilinayotganda", "Boshqa ishga o'tkazilayotganda"].index(st.session_state.form_data["declaration_type"]))
    
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #E6F3FF; border-left: 5px solid #0065BD; border-radius: 4px;">
        <h4 style="margin-top: 0; color: #0065BD;">Muhim eslatma</h4>
        <p style="margin-bottom: 0;">
            Barcha ma'lumotlar to'g'ri va to'liq kiritilishi shart. Noto'g'ri ma'lumotlar kiritilganligi uchun javobgarlik belgilanadi.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col4:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("Davom etish", key="continue_btn1", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                if not full_name or not position:
                    st.error("Barcha majburiy maydonlarni to'ldiring!")
                else:
                    # Ma'lumotlarni saqlash
                    st.session_state.form_data["full_name"] = full_name
                    st.session_state.form_data["position"] = position
                    st.session_state.form_data["declaration_type"] = declaration_type
                    next_stage()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

# Deklaratsiya to'ldirish - Bosqich 2: Xodim ma'lumotlari
def show_form_stage2():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya</h2>
        <p style="color: #666;">O'zbekiston Respublikasining "Manfaatlar to'qnashuvi to'g'risida"gi Qonunining 9-moddasiga muvofiq</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-top: 20px;">
        <h3 style="color: #003366;">2-bosqich: Shaxsiy ma'lumotlar</h3>
    """, unsafe_allow_html=True)
    
    st.progress(2/5, "40%")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        id_info = st.text_input("ID-karta/biometrik pasport ma'lumotlari (seriya, raqam, berilgan sana)",
                               value=st.session_state.form_data.get("id_info", ""),
                               placeholder="Misol: AC 1234567, 01.01.2020")
        jshshir = st.text_input("JSHSHIR (Jismoniy shaxsning shaxsiy identifikatsiya raqami)",
                              value=st.session_state.form_data.get("jshshir", ""),
                              placeholder="14 raqamli identifikatsiya raqami")
    
    with col2:
        has_decision_authority = st.radio("Davlat organi/tashkilotida qaror qabul qilish vakolatiga egamisiz?",
                                        options=["Ha", "Yo'q"],
                                        index=0 if st.session_state.form_data.get("has_decision_authority", "") == "Ha" else 1)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("◀️ Orqaga", key="back_btn2", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                prev_stage()
    
    with col4:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("Davom etish ▶️", key="continue_btn2", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                if not id_info or not jshshir:
                    st.error("Barcha majburiy maydonlarni to'ldiring!")
                else:
                    # Ma'lumotlarni saqlash
                    st.session_state.form_data["id_info"] = id_info
                    st.session_state.form_data["jshshir"] = jshshir
                    st.session_state.form_data["has_decision_authority"] = has_decision_authority
                    next_stage()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

# Deklaratsiya to'ldirish - Bosqich 3: Yaqin qarindoshlar - O'ZGARTIRILGAN
def show_form_stage3():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya</h2>
        <p style="color: #666;">O'zbekiston Respublikasining "Manfaatlar to'qnashuvi to'g'risida"gi Qonunining 9-moddasiga muvofiq</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-top: 20px;">
        <h3 style="color: #003366;">3-bosqich: Yaqin qarindoshlar ma'lumotlari</h3>
    """, unsafe_allow_html=True)
    
    st.progress(3/5, "60%")
    
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #E6F3FF; border-left: 5px solid #0065BD; border-radius: 4px;">
        <h4 style="margin-top: 0; color: #0065BD;">Yaqin qarindoshlar kimlar?</h4>
        <p style="margin-bottom: 0;">
            Yaqin qarindoshlar - ota-onalar, aka-ukalar, opa-singillar, o'g'illar, qizlar, er-xotinlar, shuningdek er-xotinlarning ota-onalari, aka-ukalari, opa-singillari va farzandlari.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Button tugmalari bilan ishlash - TO'G'RILANGAN
    if st.button("+ Yaqin qarindosh qo'shish", key="add_relative", type="primary"):
        if not st.session_state.button_clicked:
            st.session_state.button_clicked = True
            st.session_state.relatives.append({})
            st.rerun()
    
    if len(st.session_state.relatives) > 0:
        for i, relative in enumerate(st.session_state.relatives):
            st.markdown(f"""
            <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px; position: relative;">
                <h4 style="margin-top: 0; color: #003366;">Qarindosh #{i+1}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([3, 1, 1])
            with col3:
                # Button tugmalari bilan ishlash - TO'G'RILANGAN
                if st.button("❌ O'chirish", key=f"del_relative_{i}", use_container_width=True):
                    if not st.session_state.button_clicked:
                        st.session_state.button_clicked = True
                        st.session_state.relatives.pop(i)
                        st.rerun()
            
            # Qarindoshlik darajasini tanlash uchun selectbox
            relative["relation_type"] = st.selectbox("Qarindoshlik darajasi", 
                                               options=["Tanlang...", "Otasi", "Onasi", "Akasi", "Ukasi", "Opasi", "Singlisi", "Turmush o'rtog'i", "O'g'li", "Qizi", "Boshqa"],
                                               key=f"relative_relation_type_{i}",
                                               index=0 if not relative.get("relation_type") else ["Tanlang...", "Otasi", "Onasi", "Akasi", "Ukasi", "Opasi", "Singlisi", "Turmush o'rtog'i", "O'g'li", "Qizi", "Boshqa"].index(relative.get("relation_type")))
            
            # Agar "Boshqa" tanlansa, boshqa qarindoshlik turini kiritish uchun text input
            if relative["relation_type"] == "Boshqa":
                relative["other_relation"] = st.text_input("Qarindoshlik darajasini kiriting", 
                                                     key=f"relative_other_relation_{i}",
                                                     value=relative.get("other_relation", ""),
                                                     placeholder="Masalan: Qaynota, Qaynona, Qaynegachi, va h.k.")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                relative["full_name"] = st.text_input("F.I.O.", 
                                                    key=f"relative_name_{i}",
                                                    value=relative.get("full_name", ""),
                                                    placeholder="Familiya Ism Otasining ismi")
                relative["id_info"] = st.text_input("ID-karta/biometrik pasport ma'lumotlari", 
                                                  key=f"relative_id_{i}",
                                                  value=relative.get("id_info", ""),
                                                  placeholder="Misol: AC 1234567, 01.01.2020")
            
            with col2:
                relative["jshshir"] = st.text_input("JSHSHIR", 
                                                  key=f"relative_jshshir_{i}",
                                                  value=relative.get("jshshir", ""),
                                                  placeholder="14 raqamli identifikatsiya raqami")
                relative["works_in_gov"] = st.radio("Bu qarindoshingiz davlat organida ishlaydi?", 
                                                 options=["Ha", "Yo'q"],
                                                 key=f"relative_works_{i}",
                                                 index=0 if relative.get("works_in_gov", "") == "Ha" else 1)
                
                relative["has_work_relation"] = st.radio("Qarindoshingiz bilan ishga oid aloqalar bor?", 
                                                     options=["Ha", "Yo'q"],
                                                     key=f"relative_relation_{i}",
                                                     index=0 if relative.get("has_work_relation", "") == "Ha" else 1)
    else:
        st.info("Yaqin qarindoshlar qo'shilmagan. Agar qarindoshlaringiz bo'lsa, '+ Yaqin qarindosh qo'shish' tugmasini bosing.")
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("◀️ Orqaga", key="back_btn3", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                prev_stage()
    
    with col4:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("Davom etish ▶️", key="continue_btn3", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                # Agar qarindosh qo'shilgan bo'lsa, barcha majburiy maydonlar to'liq ekanligini tekshirish
                error_found = False
                if len(st.session_state.relatives) > 0:
                    for i, relative in enumerate(st.session_state.relatives):
                        if not relative.get("full_name") or not relative.get("id_info") or relative.get("relation_type") == "Tanlang...":
                            st.error(f"Qarindosh #{i+1} uchun barcha majburiy maydonlarni to'ldiring!")
                            error_found = True
                            break
                        
                        # Agar "Boshqa" tanlangan bo'lsa, boshqa qarindoshlik turini kiritganini tekshirish
                        if relative.get("relation_type") == "Boshqa" and not relative.get("other_relation"):
                            st.error(f"Qarindosh #{i+1} uchun boshqa qarindoshlik darajasini kiriting!")
                            error_found = True
                            break
                
                if not error_found:
                    next_stage()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

# Deklaratsiya to'ldirish - Bosqich 4: Yuridik shaxslar
def show_form_stage4():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya</h2>
        <p style="color: #666;">O'zbekiston Respublikasining "Manfaatlar to'qnashuvi to'g'risida"gi Qonunining 9-moddasiga muvofiq</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-top: 20px;">
        <h3 style="color: #003366;">4-bosqich: Yuridik shaxslar ma'lumotlari</h3>
    """, unsafe_allow_html=True)
    
    st.progress(4/5, "80%")
    
    st.subheader("Xodim aloqador bo'lgan yuridik shaxslar")
    
    # Button tugmalari bilan ishlash - TO'G'RILANGAN
    if st.button("+ Yuridik shaxs qo'shish", key="add_entity", type="primary"):
        if not st.session_state.button_clicked:
            st.session_state.button_clicked = True
            st.session_state.legal_entities.append({})
            st.rerun()
    
    if len(st.session_state.legal_entities) > 0:
        for i, entity in enumerate(st.session_state.legal_entities):
            st.markdown(f"""
            <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px; position: relative;">
                <h4 style="margin-top: 0; color: #003366;">Yuridik shaxs #{i+1}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([3, 1, 1])
            with col3:
                # Button tugmalari bilan ishlash - TO'G'RILANGAN
                if st.button("❌ O'chirish", key=f"del_entity_{i}", use_container_width=True):
                    if not st.session_state.button_clicked:
                        st.session_state.button_clicked = True
                        st.session_state.legal_entities.pop(i)
                        st.rerun()
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                entity["name"] = st.text_input("Yuridik shaxs nomi", 
                                             key=f"rel_entity_name_{i}",
                                             value=entity.get("name", ""),
                                             placeholder="Yuridik shaxs nomi")
            
            with col2:
                entity["stir"] = st.text_input("STIR", 
                                             key=f"rel_entity_stir_{i}",
                                             value=entity.get("stir", ""),
                                             placeholder="Soliq to'lovchining identifikatsiya raqami")
                entity["has_contract"] = st.radio("Bu yuridik shaxs davlat organi bilan shartnomaviy munosabatda?", 
                                               options=["Ha", "Yo'q"],
                                               key=f"rel_entity_contract_{i}",
                                               index=0 if entity.get("has_contract", "") == "Ha" else 1)
    else:
        st.info("Qarindoshlaringizga aloqador yuridik shaxslar qo'shilmagan. Agar shunday shaxslar bo'lsa, '+ Qarindoshning yuridik shaxsini qo'shish' tugmasini bosing.")
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("◀️ Orqaga", key="back_btn4", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                prev_stage()
    
    with col4:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("Davom etish ▶️", key="continue_btn4", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                error_found = False
                # Agar yuridik shaxs qo'shilgan bo'lsa, barcha maydonlar to'liq ekanligini tekshirish
                for i, entity in enumerate(st.session_state.legal_entities):
                    if not entity.get("name") or not entity.get("stir"):
                        st.error(f"Yuridik shaxs #{i+1} uchun barcha majburiy maydonlarni to'ldiring!")
                        error_found = True
                        break
                
                for i, entity in enumerate(st.session_state.relative_legal_entities):
                    if not entity.get("name") or not entity.get("stir"):
                        st.error(f"Qarindoshning yuridik shaxsi #{i+1} uchun barcha majburiy maydonlarni to'ldiring!")
                        error_found = True
                        break
                
                if not error_found:
                    next_stage()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

def show_form_stage5():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya</h2>
        <p style="color: #666;">O'zbekiston Respublikasining "Manfaatlar to'qnashuvi to'g'risida"gi Qonunining 9-moddasiga muvofiq</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-top: 20px;">
        <h3 style="color: #003366;">5-bosqich: Manfaatlar to'qnashuvi ta'rifi</h3>
    """, unsafe_allow_html=True)
    
    st.progress(5/5, "100%")
    
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #E6F3FF; border-left: 5px solid #0065BD; border-radius: 4px;">
        <h4 style="margin-top: 0; color: #0065BD;">Manfaatlar to'qnashuvi nima?</h4>
        <p style="margin-bottom: 0;">
            Manfaatlar to'qnashuvi — shaxsning shaxsiy (bevosita yoki bilvosita) manfaatdorligi uning o'z lavozim yoki xizmat majburiyatlarini lozim darajada bajarishiga ta'sir ko'rsatayotgan yoxud ta'sir ko'rsatishi mumkin bo'lgan hamda shaxsiy manfaatdorlik bilan fuqarolarning, tashkilotlarning, jamiyatning yoki davlatning huquqlari, qonuniy manfaatlari o'rtasida qarama-qarshilik yuzaga kelayotgan (mavjud manfaatlar to'qnashuvi) yoki yuzaga kelishi mumkin bo'lgan (ehtimoliy manfaatlar to'qnashuvi) vaziyat.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        conflict_type = st.selectbox("Ehtimoliy manfaatlar to'qnashuvi turi",
                                   options=["Moliyaviy manfaatlar", "Qarindoshlik munosabatlari", 
                                           "Qo'shimcha ish", "Sovg'alar va boshqa foydalar", "Boshqa"],
                                   index=0 if "conflict_type" not in st.session_state.form_data else 
                                   ["Moliyaviy manfaatlar", "Qarindoshlik munosabatlari", 
                                    "Qo'shimcha ish", "Sovg'alar va boshqa foydalar", "Boshqa"].index(st.session_state.form_data["conflict_type"]))
    
    conflict_description = st.text_area("Ehtimoliy manfaatlar to'qnashuvini tasvirlash",
                                      value=st.session_state.form_data.get("conflict_description", ""),
                                      placeholder="Ehtimoliy manfaatlar to'qnashuvi holatini batafsil tasvirlang...",
                                      height=150)
    
    additional_info = st.text_area("Qo'shimcha ma'lumotlar",
                                 value=st.session_state.form_data.get("additional_info", ""),
                                 placeholder="Qo'shimcha ma'lumotlarni kiriting (ixtiyoriy)...",
                                 height=100)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("◀️ Orqaga", key="back_btn5", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                prev_stage()
    
    with col4:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("Davom etish ▶️", key="continue_btn5", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                if not conflict_description:
                    st.error("Manfaatlar to'qnashuvi tavsifini to'ldiring!")
                else:
                    # Ma'lumotlarni saqlash
                    st.session_state.form_data["conflict_type"] = conflict_type
                    st.session_state.form_data["conflict_description"] = conflict_description
                    st.session_state.form_data["additional_info"] = additional_info
                    next_stage()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

# Deklaratsiya to'ldirish - Bosqich 6: Tasdiqlash - O'ZGARTIRILGAN
def show_form_stage6():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya</h2>
        <p style="color: #666;">O'zbekiston Respublikasining "Manfaatlar to'qnashuvi to'g'risida"gi Qonunining 9-moddasiga muvofiq</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-top: 20px;">
        <h3 style="color: #003366;">6-bosqich: Ma'lumotlarni tekshirish va tasdiqlash</h3>
    """, unsafe_allow_html=True)
    
    st.info("Kiritgan ma'lumotlaringizni tekshirib chiqing. Tasdiqlagandan so'ng o'zgartirish kiritish imkoni bo'lmaydi.")
    
    # Xodim ma'lumotlari
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Xodim ma'lumotlari</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write(f"**F.I.O.:** {st.session_state.form_data.get('full_name', '')}")
        st.write(f"**Lavozim:** {st.session_state.form_data.get('position', '')}")
        st.write(f"**Deklaratsiya turi:** {st.session_state.form_data.get('declaration_type', '')}")
    with col2:
        st.write(f"**ID ma'lumotlari:** {st.session_state.form_data.get('id_info', '')}")
        st.write(f"**JSHSHIR:** {st.session_state.form_data.get('jshshir', '')}")
        st.write(f"**Qaror qabul qilish vakolati:** {st.session_state.form_data.get('has_decision_authority', '')}")
    
    # Yaqin qarindoshlar
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Yaqin qarindoshlar</h4>
    </div>
    """, unsafe_allow_html=True)
    
    if len(st.session_state.relatives) > 0:
        for i, relative in enumerate(st.session_state.relatives):
            st.write(f"**Qarindosh #{i+1}**")
            # Qarindoshlik darajasini ko'rsatish
            relation_display = relative.get("relation_type", "")
            if relation_display == "Boshqa":
                relation_display = f"Boshqa: {relative.get('other_relation', '')}"
            st.write(f"**Qarindoshlik darajasi:** {relation_display}")
            st.write(f"F.I.O.: {relative.get('full_name', '')}")
            st.write(f"ID: {relative.get('id_info', '')}, JSHSHIR: {relative.get('jshshir', '')}")
            st.write(f"Davlat organida ishlaydi: {relative.get('works_in_gov', '')}")
            st.write(f"Ishga oid aloqalar: {relative.get('has_work_relation', '')}")
            st.markdown("---")
    else:
        st.write("Yaqin qarindoshlar qo'shilmagan.")
    
    # Yuridik shaxslar
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Yuridik shaxslar</h4>
    </div>
    """, unsafe_allow_html=True)
    
    if len(st.session_state.legal_entities) > 0:
        st.write("**Xodimga aloqador yuridik shaxslar:**")
        for i, entity in enumerate(st.session_state.legal_entities):
            st.write(f"#{i+1}: {entity.get('name', '')}, STIR: {entity.get('stir', '')}")
            st.write(f"Davlat bilan shartnoma: {entity.get('has_contract', '')}")
            st.markdown("---")
    else:
        st.write("Xodimga aloqador yuridik shaxslar qo'shilmagan.")
    
    if len(st.session_state.relative_legal_entities) > 0:
        st.write("**Qarindoshlarga aloqador yuridik shaxslar:**")
        for i, entity in enumerate(st.session_state.relative_legal_entities):
            st.write(f"#{i+1}: {entity.get('name', '')}, STIR: {entity.get('stir', '')}")
            st.write(f"Davlat bilan shartnoma: {entity.get('has_contract', '')}")
            st.markdown("---")
    else:
        st.write("Qarindoshlarga aloqador yuridik shaxslar qo'shilmagan.")
    
    # Manfaatlar to'qnashuvi
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Manfaatlar to'qnashuvi ma'lumotlari</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"**To'qnashuv turi:** {st.session_state.form_data.get('conflict_type', '')}")
    st.write(f"**Ta'rifi:** {st.session_state.form_data.get('conflict_description', '')}")
    if st.session_state.form_data.get('additional_info', ''):
        st.write(f"**Qo'shimcha ma'lumot:** {st.session_state.form_data.get('additional_info', '')}")
    
    # Tasdiqlash checkboxi
    st.markdown("""
    <div style="margin-top: 30px; padding: 15px; background-color: #FFF9E6; border-left: 5px solid #FFB400; border-radius: 4px;">
        <h4 style="margin-top: 0; color: #FFB400;">Diqqat!</h4>
        <p style="margin-bottom: 0;">
            Mazkur deklaratsiyada ko'rsatilgan ma'lumotlarning to'g'riligini tasdiqlayman va noto'g'ri ma'lumotlar kiritganlik uchun tegishli javobgarlikni o'z zimmamga olaman.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    confirm = st.checkbox("Men kiritilgan ma'lumotlarning to'g'riligini tasdiqlayman")
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("◀️ Orqaga", key="back_btn6", use_container_width=True):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                prev_stage()
    
    with col4:
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("Yuborish", key="submit_btn", disabled=not confirm, use_container_width=True, type="primary"):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                # Deklaratsiyani saqlash
                declaration_id = str(uuid.uuid4())
                now = datetime.datetime.now()
                registry_number = f"{now.year}-{now.month}-{declaration_id[:8]}"
                
                declaration = {
                    "id": declaration_id,
                    "registry_number": registry_number,
                    "submission_date": now.strftime("%Y-%m-%d %H:%M:%S"),
                    "status": "Yangi",
                    "employee_data": st.session_state.form_data,
                    "relatives": st.session_state.relatives,
                    "legal_entities": st.session_state.legal_entities,
                    "relative_legal_entities": st.session_state.relative_legal_entities,
                    "has_potential_conflict": (
                        st.session_state.form_data.get("has_decision_authority") == "Ha" or
                        any(rel.get("works_in_gov") == "Ha" for rel in st.session_state.relatives) or
                        any(rel.get("has_work_relation") == "Ha" for rel in st.session_state.relatives) or
                        any(entity.get("has_contract") == "Ha" for entity in st.session_state.legal_entities) or
                        any(entity.get("has_contract") == "Ha" for entity in st.session_state.relative_legal_entities)
                    )
                }
                
                save_declaration(declaration)
                
                # Natija sahifasiga o'tish
                st.session_state.form_data["declaration_id"] = declaration_id
                st.session_state.form_data["registry_number"] = registry_number
                next_stage()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

# Deklaratsiya to'ldirish - Bosqich 7: Natija
def show_form_stage7():
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">Ehtimoliy manfaatlar to'qnashuvi to'g'risidagi deklaratsiya</h2>
        <p style="color: #666;">O'zbekiston Respublikasining "Manfaatlar to'qnashuvi to'g'risida"gi Qonunining 9-moddasiga muvofiq</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-top: 20px; text-align: center;">
        <div style="text-align: center; margin: 30px 0 50px 0;">
            <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#00A300" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <h3 style="color: #00A300; margin-top: 15px;">Deklaratsiya muvaffaqiyatli qabul qilindi!</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Ma'lumotlar jadvalini ko'rsatish
    registry_number = st.session_state.form_data.get('registry_number', '')
    current_date = datetime.datetime.now().strftime('%d.%m.%Y')
    
    st.markdown(f"""
        <div style="display: inline-block; text-align: left; padding: 20px; background-color: #F5F5F5; border-radius: 5px; margin-top: 15px;">
            <table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="padding: 8px; width: 200px; font-weight: bold; color: #003366;">Reyestr raqami:</td>
                    <td style="padding: 8px;">{registry_number}</td>
                </tr>
                <tr>
                    <td style="padding: 8px; font-weight: bold; color: #003366;">Qabul qilingan sana:</td>
                    <td style="padding: 8px;">{current_date}</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="margin-top: 40px; padding: 15px; background-color: #E6F3FF; border-left: 5px solid #0065BD; border-radius: 4px; text-align: left;">
            <h4 style="margin-top: 0; color: #0065BD;">Keyingi qadamlar</h4>
            <p style="margin-bottom: 0;">
                Deklaratsiyangiz Kadrlar bo'limi va Shaxsiy xavfsizlik bo'limi tomonidan ko'rib chiqiladi. 
                Natijalar va qo'shimcha ma'lumotlar uchun ish joyingizdagi kadrlar bo'limiga murojaat qilishingiz mumkin.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Bosh sahifaga qaytish tugmasi
    col1, col2 = st.columns([1, 1])
    with col2:
        if st.button("🏠 Bosh sahifaga qaytish", key="home_btn", use_container_width=True, type="primary"):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                navigate_to("main")
                reset_form()
                st.rerun()

# Admin panel - Kadrlar bo'limi
def show_hr_admin_panel():
    declarations = load_data()
    
    # Statistika
    st.markdown("""
    <div style="margin-top: 20px; padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h3 style="color: #003366; margin-top: 0;">Statistika</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 20px;">
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{len(declarations)}</div>
            <div class="metric-label">Barcha deklaratsiyalar</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        new_declarations = sum(1 for d in declarations if d["status"] == "Yangi")
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{new_declarations}</div>
            <div class="metric-label">Yangi deklaratsiyalar</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        potential_conflicts = sum(1 for d in declarations if d["has_potential_conflict"])
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{potential_conflicts}</div>
            <div class="metric-label">Potensial to'qnashuvlar</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Jadval
    st.markdown("""
    <div style="margin-top: 20px; padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h3 style="color: #003366; margin-top: 0;">Deklaratsiyalar ro'yxati</h3>
    """, unsafe_allow_html=True)
    
    if not declarations:
        st.info("Deklaratsiyalar mavjud emas")
    else:
        # Jadval uchun ma'lumotlarni tayyorlash
        data = []
        for d in declarations:
            data.append({
                "ID": d["id"],
                "F.I.O.": d["employee_data"]["full_name"],
                "Lavozim": d["employee_data"]["position"],
                "Sana": d["submission_date"],
                "Turi": d["employee_data"]["declaration_type"],
                "Holati": d["status"],
                "Potensial to'qnashuv": "✅" if d["has_potential_conflict"] else "❌"
            })
        
        df = pd.DataFrame(data)
        
        # Filtrlash
        st.markdown("""
        <h4 style="color: #003366; margin-top: 20px;">Filtrlash</h4>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_status = st.selectbox("Holati bo'yicha", options=["Barcha", "Yangi", "Ko'rib chiqilgan", "Tasdiqlangan"])
        
        with col2:
            filter_type = st.selectbox("Turi bo'yicha", options=["Barcha", "Yillik", "Ishga qabul qilinayotganda", "Boshqa ishga o'tkazilayotganda"])
        
        with col3:
            filter_conflict = st.selectbox("To'qnashuv bo'yicha", options=["Barcha", "Potensial to'qnashuv bor", "To'qnashuv yo'q"])
        
        # Filterlash
        filtered_df = df.copy()
        
        if filter_status != "Barcha":
            filtered_df = filtered_df[filtered_df["Holati"] == filter_status]
            
        if filter_type != "Barcha":
            filtered_df = filtered_df[filtered_df["Turi"] == filter_type]
            
        if filter_conflict != "Barcha":
            if filter_conflict == "Potensial to'qnashuv bor":
                filtered_df = filtered_df[filtered_df["Potensial to'qnashuv"] == "✅"]
            else:
                filtered_df = filtered_df[filtered_df["Potensial to'qnashuv"] == "❌"]
        
        # Jadvalni ko'rsatish
        st.dataframe(filtered_df, use_container_width=True)
        
        # Deklaratsiyani ko'rish
        st.markdown("""
        <h4 style="color: #003366; margin-top: 20px;">Deklaratsiyani ko'rish</h4>
        """, unsafe_allow_html=True)
        
        selected_id = st.selectbox("Deklaratsiyani tanlang", options=filtered_df["ID"], format_func=lambda x: filtered_df[filtered_df["ID"] == x]["F.I.O."].iloc[0])
        
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("Deklaratsiyani ko'rish", key="view_declaration", type="primary"):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                # Tanlangan deklaratsiyani topish
                selected_declaration = next((d for d in declarations if d["id"] == selected_id), None)
                
                if selected_declaration:
                    st.session_state.selected_declaration = selected_declaration
                    st.session_state.admin_view = "view_declaration"
                    st.rerun()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True) 

# Admin panel - Shaxsiy xavfsizlik bo'limi
def show_security_admin_panel():
    declarations = load_data()
    
    # Statistika
    st.markdown("""
    <div style="margin-top: 20px; padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h3 style="color: #003366; margin-top: 0;">Statistika</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 20px;">
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        potential_conflicts = sum(1 for d in declarations if d["has_potential_conflict"])
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{potential_conflicts}</div>
            <div class="metric-label">Potensial to'qnashuvlar</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        new_conflicts = sum(1 for d in declarations if d["has_potential_conflict"] and d["status"] == "Yangi")
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{new_conflicts}</div>
            <div class="metric-label">Ko'rib chiqilmagan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        resolved_conflicts = sum(1 for d in declarations if d["has_potential_conflict"] and d["status"] == "Tasdiqlangan")
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{resolved_conflicts}</div>
            <div class="metric-label">Hal qilingan</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Potensial to'qnashuvlar jadvali
    st.markdown("""
    <div style="margin-top: 20px; padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h3 style="color: #003366; margin-top: 0;">Potensial manfaatlar to'qnashuvlari</h3>
    """, unsafe_allow_html=True)
    
    # Faqat potensial to'qnashuvli deklaratsiyalarni olish
    conflict_declarations = [d for d in declarations if d["has_potential_conflict"]]
    
    if not conflict_declarations:
        st.info("Potensial to'qnashuvlar mavjud emas")
    else:
        # Jadval uchun ma'lumotlarni tayyorlash
        data = []
        for d in conflict_declarations:
            data.append({
                "ID": d["id"],
                "F.I.O.": d["employee_data"]["full_name"],
                "Lavozim": d["employee_data"]["position"],
                "To'qnashuv turi": d["employee_data"]["conflict_type"],
                "Sana": d["submission_date"],
                "Holati": d["status"]
            })
        
        df = pd.DataFrame(data)
        
        # Filtrlash
        st.markdown("""
        <h4 style="color: #003366; margin-top: 20px;">Filtrlash</h4>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            filter_status = st.selectbox("Holati bo'yicha", options=["Barcha", "Yangi", "Ko'rib chiqilgan", "Tasdiqlangan"])
        
        with col2:
            filter_type = st.selectbox("To'qnashuv turi bo'yicha", 
                                     options=["Barcha", "Moliyaviy manfaatlar", "Qarindoshlik munosabatlari", 
                                             "Qo'shimcha ish", "Sovg'alar va boshqa foydalar", "Boshqa"])
        
        # Filterlash
        filtered_df = df.copy()
        
        if filter_status != "Barcha":
            filtered_df = filtered_df[filtered_df["Holati"] == filter_status]
            
        if filter_type != "Barcha":
            filtered_df = filtered_df[filtered_df["To'qnashuv turi"] == filter_type]
        
        # Jadvalni ko'rsatish
        st.dataframe(filtered_df, use_container_width=True)
        
        # Deklaratsiyani ko'rish
        st.markdown("""
        <h4 style="color: #003366; margin-top: 20px;">To'qnashuvni ko'rish</h4>
        """, unsafe_allow_html=True)
        
        selected_id = st.selectbox("To'qnashuvni tanlang", options=filtered_df["ID"], format_func=lambda x: filtered_df[filtered_df["ID"] == x]["F.I.O."].iloc[0])
        
        # Button tugmalari bilan ishlash - TO'G'RILANGAN
        if st.button("To'qnashuvni ko'rish", key="view_conflict", type="primary"):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                # Tanlangan deklaratsiyani topish
                selected_declaration = next((d for d in declarations if d["id"] == selected_id), None)
                
                if selected_declaration:
                    st.session_state.selected_declaration = selected_declaration
                    st.session_state.admin_view = "view_conflict"
                    st.rerun()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

# Admin panel - Deklaratsiya ko'rish (Kadrlar bo'limi uchun) - O'ZGARTIRILGAN
# Deklaratsiyani ko'rish
def show_declaration_view(declaration):
    st.markdown(f"""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">
            Deklaratsiya №{declaration['registry_number']}
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Xodim ma'lumotlari
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Xodim ma'lumotlari</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write(f"**F.I.O.:** {declaration['employee_data']['full_name']}")
        st.write(f"**Lavozim:** {declaration['employee_data']['position']}")
        st.write(f"**Deklaratsiya turi:** {declaration['employee_data']['declaration_type']}")
    with col2:
        st.write(f"**ID ma'lumotlari:** {declaration['employee_data']['id_info']}")
        st.write(f"**JSHSHIR:** {declaration['employee_data']['jshshir']}")
        st.write(f"**Qaror qabul qilish vakolati:** {declaration['employee_data']['has_decision_authority']}")
        
        # Agar qaror qabul qilish vakolati mavjud bo'lsa, xavf sifatida belgilash
        if declaration['employee_data']['has_decision_authority'] == "Ha":
            st.warning("⚠️ **Xavf**: Xodim qaror qabul qilish vakolatiga ega!")
    
    # Yaqin qarindoshlar
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Yaqin qarindoshlar</h4>
    </div>
    """, unsafe_allow_html=True)
    
    if len(declaration['relatives']) > 0:
        for i, relative in enumerate(declaration['relatives']):
            st.write(f"**Qarindosh #{i+1}**")
            
            # Qarindoshlik darajasi ko'rsatish
            relation_display = relative.get("relation_type", "")
            if relation_display == "Boshqa":
                relation_display = f"Boshqa: {relative.get('other_relation', '')}"
            if relation_display:
                st.write(f"**Qarindoshlik darajasi:** {relation_display}")
                
            st.write(f"F.I.O.: {relative.get('full_name', '')}")
            st.write(f"ID: {relative.get('id_info', '')}, JSHSHIR: {relative.get('jshshir', '')}")
            st.write(f"Davlat organida ishlaydi: {relative.get('works_in_gov', '')}")
            st.write(f"Ishga oid aloqalar: {relative.get('has_work_relation', '')}")
            
            # Qarindoshlar bilan bog'liq xavflarni ko'rsatish
            if relative.get('works_in_gov') == "Ha":
                st.warning(f"⚠️ **Xavf**: {relative.get('full_name', '')} davlat organida ishlaydi!")
            
            if relative.get('has_work_relation') == "Ha":
                st.warning(f"⚠️ **Xavf**: {relative.get('full_name', '')} bilan ishga oid aloqalar mavjud!")
                
            st.markdown("---")
    else:
        st.write("Yaqin qarindoshlar qo'shilmagan.")
    
    # Yuridik shaxslar
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Yuridik shaxslar</h4>
    </div>
    """, unsafe_allow_html=True)
    
    if len(declaration['legal_entities']) > 0:
        st.write("**Xodimga aloqador yuridik shaxslar:**")
        for i, entity in enumerate(declaration['legal_entities']):
            st.write(f"#{i+1}: {entity.get('name', '')}, STIR: {entity.get('stir', '')}")
            st.write(f"Davlat bilan shartnoma: {entity.get('has_contract', '')}")
            
            # Yuridik shaxslar bilan bog'liq xavflarni ko'rsatish
            if entity.get('has_contract') == "Ha":
                st.warning(f"⚠️ **Xavf**: {entity.get('name', '')} davlat bilan shartnomaviy munosabatda!")
                
            st.markdown("---")
    else:
        st.write("Xodimga aloqador yuridik shaxslar qo'shilmagan.")
    
    if len(declaration['relative_legal_entities']) > 0:
        st.write("**Qarindoshlarga aloqador yuridik shaxslar:**")
        for i, entity in enumerate(declaration['relative_legal_entities']):
            st.write(f"#{i+1}: {entity.get('name', '')}, STIR: {entity.get('stir', '')}")
            st.write(f"Davlat bilan shartnoma: {entity.get('has_contract', '')}")
            
            # Qarindoshning yuridik shaxslari bilan bog'liq xavflarni ko'rsatish
            if entity.get('has_contract') == "Ha":
                st.warning(f"⚠️ **Xavf**: Qarindoshga aloqador {entity.get('name', '')} davlat bilan shartnomaviy munosabatda!")
                
            st.markdown("---")
    else:
        st.write("Qarindoshlarga aloqador yuridik shaxslar qo'shilmagan.")
    
    # Manfaatlar to'qnashuvi
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Manfaatlar to'qnashuvi ma'lumotlari</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"**To'qnashuv turi:** {declaration['employee_data']['conflict_type']}")
    st.write(f"**Ta'rifi:** {declaration['employee_data']['conflict_description']}")
    if declaration['employee_data'].get('additional_info', ''):
        st.write(f"**Qo'shimcha ma'lumot:** {declaration['employee_data']['additional_info']}")
    
    # Potensial to'qnashuv haqida ogohlantirish
    if declaration['has_potential_conflict']:
        # Xavf sabablarini aniqlash
        reasons = []
        # Xodimning qaror qabul qilish vakolati
        if declaration['employee_data']['has_decision_authority'] == "Ha":
            reasons.append(f"Xodim ({declaration['employee_data']['full_name']}) qaror qabul qilish vakolatiga ega.")
        
        # Qarindoshlar bilan bog'liq xavflar
        for i, relative in enumerate(declaration['relatives']):
            relation_display = relative.get('relation_type', '')
            if relation_display == "Boshqa":
                relation_display = relative.get('other_relation', '')
                
            if relative.get('works_in_gov') == "Ha":
                relation_info = f"{relation_display} " if relation_display else ""
                reasons.append(f"Qarindosh {relation_info}{relative.get('full_name', 'Nomalum')} davlat organida ishlaydi.")
                
            if relative.get('has_work_relation') == "Ha":
                relation_info = f"{relation_display} " if relation_display else ""
                reasons.append(f"Qarindosh {relation_info}{relative.get('full_name', 'Nomalum')} bilan ishga oid aloqalar mavjud.")
        
        # Yuridik shaxslar bilan bog'liq xavflar
        for i, entity in enumerate(declaration['legal_entities']):
            if entity.get('has_contract') == "Ha":
                reasons.append(f"Xodimga aloqador yuridik shaxs {entity.get('name', 'Nomalum')} davlat bilan shartnomaviy munosabatda.")
        
        for i, entity in enumerate(declaration['relative_legal_entities']):
            if entity.get('has_contract') == "Ha":
                reasons.append(f"Qarindoshga aloqador yuridik shaxs {entity.get('name', 'Nomalum')} davlat bilan shartnomaviy munosabatda.")
        
        # Xavf sabablari ro'yxatini ko'rsatish
        reasons_html = "<ul>" + "".join([f"<li>{reason}</li>" for reason in reasons]) + "</ul>" if reasons else "<p>Sabablar aniqlanmadi.</p>"
        
        st.markdown(f"""
        <div style="margin-top: 30px; padding: 15px; background-color: #FFF9E6; border-left: 5px solid #FFB400; border-radius: 4px;">
            <h4 style="margin-top: 0; color: #FFB400;">Diqqat! Potensial manfaatlar to'qnashuvi aniqlandi</h4>
            <p style="margin-bottom: 10px;">
                Ushbu deklaratsiyada potensial manfaatlar to'qnashuvi belgilari aniqlandi. Deklaratsiyani ko'rib chiqish uchun
                shaxsiy xavfsizlik bo'limiga yo'naltirish tavsiya etiladi.
            </p>
            <h5 style="margin-top: 10px; color: #FFB400;">Potensial xavf sabablari:</h5>
            {reasons_html}
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Shaxsiy xavfsizlik bo'limiga yo'naltirish", key=f"forward_{declaration['id']}", type="primary"):
                if not st.session_state.button_clicked:
                    st.session_state.button_clicked = True
                    declarations = load_data()
                    for d in declarations:
                        if d['id'] == declaration['id']:
                            d['status'] = "Ko'rib chiqilgan"
                            break
                    with open("data/declarations.json", "w") as f:
                        json.dump(declarations, f)
                    st.success("Deklaratsiya shaxsiy xavfsizlik bo'limiga yo'naltirildi!")
                    st.session_state.button_clicked = False
                    st.rerun()
        with col2:
            if st.button("Orqaga qaytish", key=f"back_{declaration['id']}"):
                if not st.session_state.button_clicked:
                    st.session_state.button_clicked = True
                    st.session_state.admin_view = None
                    st.rerun()
    else:
        st.markdown("""
        <div style="margin-top: 30px; padding: 15px; background-color: #E6FFE6; border-left: 5px solid #00A300; border-radius: 4px;">
            <h4 style="margin-top: 0; color: #00A300;">Ma'lumot</h4>
            <p style="margin-bottom: 0;">
                Ushbu deklaratsiyada potensial manfaatlar to'qnashuvi belgilari aniqlanmadi.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("Orqaga qaytish", key=f"back_{declaration['id']}"):
                if not st.session_state.button_clicked:
                    st.session_state.button_clicked = True
                    st.session_state.admin_view = None
                    st.rerun()

# Admin panel - To'qnashuv ko'rish (Shaxsiy xavfsizlik bo'limi uchun) - O'ZGARTIRILGAN
def show_conflict_view():
    declaration = st.session_state.selected_declaration
    
    st.markdown(f"""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">
            Manfaatlar to'qnashuvi: {declaration['employee_data']['full_name']} (№{declaration['registry_number']})
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 20px; padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        status_color = {
            "Yangi": "🔵",
            "Ko'rib chiqilgan": "🟠",
            "Tasdiqlangan": "🟢",
            "Rad etilgan": "🔴"
        }
        st.write(f"**Holati:** {status_color.get(declaration['status'], '')} {declaration['status']}")
    
    with col2:
        st.write(f"**Reyestr raqami:** {declaration['registry_number']}")
    
    with col3:
        st.write(f"**Sana:** {declaration['submission_date']}")
    
    st.divider()
    
    # Xodim asosiy ma'lumotlari
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Xodim ma'lumotlari</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**F.I.O.:** {declaration['employee_data']['full_name']}")
        st.write(f"**Lavozim:** {declaration['employee_data']['position']}")
    
    with col2:
        st.write(f"**Qaror qabul qilish vakolati:** {declaration['employee_data']['has_decision_authority']}")
        
        if declaration['employee_data']['has_decision_authority'] == "Ha":
            st.warning("⚠️ **Xavf**: Xodim qaror qabul qilish vakolatiga ega!")
    
    # To'qnashuv sabablari
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #FFF9E6; border-left: 5px solid #FFB400; border-radius: 4px;">
        <h4 style="margin-top: 0; color: #FFB400;">Potensial to'qnashuv sabablari</h4>
    </div>
    """, unsafe_allow_html=True)
    
    found_causes = False
    
    # Qarindoshlik munosabatlari tekshirish
    relative_conflicts = []
    for rel in declaration['relatives']:
        # Qarindoshlik darajasini olish
        relation_display = rel.get('relation_type', '')
        if relation_display == "Boshqa":
            relation_display = rel.get('other_relation', '')
            
        relation_info = f"{relation_display} " if relation_display else ""
            
        if rel['works_in_gov'] == "Ha":
            relative_conflicts.append(f"{relation_info}{rel['full_name']} - davlat organida ishlaydi")
        if rel['has_work_relation'] == "Ha":
            relative_conflicts.append(f"{relation_info}{rel['full_name']} - xodim bilan ishga oid aloqalar mavjud")
    
    if relative_conflicts:
        found_causes = True
        st.write("**Qarindoshlik munosabatlari:**")
        for conflict in relative_conflicts:
            st.warning(f"⚠️ {conflict}")
    
    # Yuridik shaxslar tekshirish
    entity_conflicts = []
    for entity in declaration['legal_entities']:
        if entity['has_contract'] == "Ha":
            entity_conflicts.append(f"{entity['name']} - davlat bilan shartnomaviy munosabatda")
    
    for entity in declaration['relative_legal_entities']:
        if entity['has_contract'] == "Ha":
            entity_conflicts.append(f"{entity['name']} - qarindosh orqali davlat bilan shartnomaviy munosabatda")
    
    if entity_conflicts:
        found_causes = True
        st.write("**Yuridik shaxslar bilan bog'liqlik:**")
        for conflict in entity_conflicts:
            st.warning(f"⚠️ {conflict}")
    
    # Xodimning qaror qabul qilish vakolati
    if declaration['employee_data']['has_decision_authority'] == "Ha":
        found_causes = True
        st.write("**Vakolatlar bo'yicha:**")
        st.warning(f"⚠️ Xodim qaror qabul qilish vakolatiga ega")
    
    # Agar to'qnashuv belgilari aniqlanmagan bo'lsa
    if not found_causes:
        st.info("⚠️ Avtomatik tekshiruvda aniq to'qnashuv belgilari aniqlanmadi, lekin xodim tomonidan deklaratsiyada manfaatlar to'qnashuvi ko'rsatilgan.")
    
    # Manfaatlar to'qnashuvi tavsifi
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Manfaatlar to'qnashuvi tavsifi</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"**To'qnashuv turi:** {declaration['employee_data']['conflict_type']}")
    conflict_description = st.text_area("Ta'rifi", value=declaration['employee_data']['conflict_description'], disabled=True, height=150)
    
    if declaration['employee_data'].get('additional_info', ''):
        st.write("**Qo'shimcha ma'lumot:**")
        st.text_area("", value=declaration['employee_data']['additional_info'], disabled=True, height=100)
    
    # Qaror qabul qilish
    st.markdown("""
    <div style="margin-top: 20px; padding: 15px; background-color: #F5F5F5; border-radius: 5px;">
        <h4 style="margin-top: 0; color: #003366;">Qaror qabul qilish</h4>
    </div>
    """, unsafe_allow_html=True)
    
    decision = st.radio("To'qnashuv bo'yicha qaror:", options=[
        "Manfaatlar to'qnashuvi mavjud",
        "Manfaatlar to'qnashuvi mavjud emas",
        "Qo'shimcha tekshiruv talab etiladi"
    ])
    
    # To'qnashuv bo'yicha ko'riladigan choralarni taklif qilish
    measure_suggestions = ""
    if decision == "Manfaatlar to'qnashuvi mavjud":
        if declaration['employee_data']['has_decision_authority'] == "Ha":
            measure_suggestions += "- Xodimning qaror qabul qilish vakolatlarini cheklash\n"
        
        if relative_conflicts:
            measure_suggestions += "- Yaqin qarindoshlar bilan ishga oid aloqalarni cheklash\n"
        
        if entity_conflicts:
            measure_suggestions += "- Yuridik shaxslar bilan bog'liq masalalarda xodimning ishtirokini cheklash\n"
        
        measure_suggestions += "- Manfaatlar to'qnashuvi mavjudligi to'g'risida boshqa xodimlarni xabardor qilish\n"
        measure_suggestions += "- Manfaatlar to'qnashuvi mavjud bo'lgan masalalarda xodimning ishtirokini taqiqlash\n"
        measure_suggestions += "- Belgilangan tartibda monitoring o'tkazib borish\n"
    
    measures = st.text_area("Ko'riladigan choralar:", 
                          value=measure_suggestions,
                          placeholder="Manfaatlar to'qnashuvini bartaraf etish bo'yicha choralarni kiriting...",
                          height=150)
    
    # Qarorni saqlash
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Qarorni saqlash", key="save_decision", type="primary"):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                # Deklaratsiya holatini yangilash
                declarations = load_data()
                for d in declarations:
                    if d["id"] == declaration["id"]:
                        if decision == "Manfaatlar to'qnashuvi mavjud":
                            d["status"] = "Tasdiqlangan"
                        elif decision == "Manfaatlar to'qnashuvi mavjud emas":
                            d["status"] = "Rad etilgan"
                        else:
                            d["status"] = "Ko'rib chiqilgan"
                        
                        # Qo'shimcha ma'lumotlar qo'shish
                        if not "security_decision" in d:
                            d["security_decision"] = {}
                        
                        d["security_decision"]["decision"] = decision
                        d["security_decision"]["measures"] = measures
                        d["security_decision"]["decision_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open("data/declarations.json", "w") as f:
                            json.dump(declarations, f)
                
                        st.success("Qaror muvaffaqiyatli saqlandi!")
                        st.session_state.admin_view = None
                        st.rerun()
    
    with col2:
        # Ortga qaytish
        if st.button("Ortga qaytish", key="back_btn_conflict"):
            if not st.session_state.button_clicked:
                st.session_state.button_clicked = True
                st.session_state.admin_view = None
                st.rerun()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)
    
def show_admin_panel():
    # Admin turi bo'yicha sahifa sarlavhasi
    admin_title = "Kadrlar bo'limi" if st.session_state.admin_type == "kadrlar" else "Shaxsiy xavfsizlik bo'limi"
    
    st.markdown(f"""
    <div style="padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h2 style="color: #0065BD; border-bottom: 2px solid #0065BD; padding-bottom: 10px;">
            {admin_title}
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Admin turini tekshirish va tegishli funksiyaga yo'naltirish
    if st.session_state.admin_view == "view_declaration":
        # Deklaratsiya ko'rish - Kadrlar bo'limi uchun
        show_declaration_view(st.session_state.selected_declaration)
    elif st.session_state.admin_view == "view_conflict":
        # To'qnashuv ko'rish - Shaxsiy xavfsizlik bo'limi uchun
        show_conflict_view()
    elif st.session_state.admin_type == "kadrlar":
        # Kadrlar bo'limi uchun
        show_hr_admin_panel()
    elif st.session_state.admin_type == "xavfsizlik":
        # Shaxsiy xavfsizlik bo'limi uchun
        show_security_admin_panel()
    else:
        # Nomalum admin turi uchun
        st.error("Admin turi aniqlanmadi!")

# Asosiy ilovani ko'rsatish
def main():
    if st.session_state.page == "main":
        # Deklaratsiya to'ldirish bosqichlari
        if st.session_state.form_stage == 1:
            show_form_stage1()
        elif st.session_state.form_stage == 2:
            show_form_stage2()
        elif st.session_state.form_stage == 3:
            show_form_stage3()
        elif st.session_state.form_stage == 4:
            show_form_stage4()
        elif st.session_state.form_stage == 5:
            show_form_stage5()
        elif st.session_state.form_stage == 6:
            show_form_stage6()
        elif st.session_state.form_stage == 7:
            show_form_stage7()
    elif st.session_state.page == "conflict_tool":
        # Manfaatlar to'qnashuvi dasturini ko'rsatish
        show_conflict_of_interest_tool()
    elif st.session_state.page == "help":
        show_help_page()
    elif st.session_state.page == "contact":
        show_contact_page()
    elif st.session_state.page == "admin_login":
        show_admin_login()
    elif st.session_state.page == "admin_panel":
        show_admin_panel()

# Har safar sahifa yuklanganda, tugma bosilganligi holatini tozalash
st.session_state.button_clicked = False

if __name__ == "__main__":
    main()
                                             
            
            