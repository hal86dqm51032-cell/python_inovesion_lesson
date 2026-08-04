import streamlit as st

# ── ページ設定 ──────────────────────────────────────
st.set_page_config(page_title="電卓", page_icon="🧮", layout="centered")

# ── カスタムCSS ─────────────────────────────────────
st.markdown("""
<style>
/* 背景・全体 */
[data-testid="stAppViewContainer"] {
    background: #1a1a2e;
}
[data-testid="stHeader"] { background: transparent; }

/* 電卓本体 */
.calc-wrapper {
    max-width: 360px;
    margin: 40px auto 0;
    background: #16213e;
    border-radius: 28px;
    padding: 28px 24px 32px;
    box-shadow: 0 30px 80px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.05);
}

/* ディスプレイ */
.calc-display {
    background: #0f3460;
    border-radius: 16px;
    padding: 20px 24px 14px;
    margin-bottom: 24px;
    text-align: right;
    min-height: 100px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    box-shadow: inset 0 4px 12px rgba(0,0,0,0.4);
}
.calc-expression {
    color: #a0b4c8;
    font-size: 15px;
    font-family: 'Courier New', monospace;
    min-height: 22px;
    margin-bottom: 4px;
    letter-spacing: 0.5px;
}
.calc-result {
    color: #e2e8f0;
    font-size: 42px;
    font-family: 'Courier New', monospace;
    font-weight: 300;
    letter-spacing: 1px;
    line-height: 1.1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

/* ボタングリッド */
.btn-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}

/* ボタン共通 */
.calc-btn {
    border: none;
    border-radius: 14px;
    font-size: 20px;
    font-weight: 500;
    height: 68px;
    cursor: pointer;
    transition: all 0.1s ease;
    font-family: 'Courier New', monospace;
}
.calc-btn:active { transform: scale(0.94); }

/* ボタン種類別 */
.btn-num {
    background: #1e3a5f;
    color: #e2e8f0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
.btn-num:hover { background: #264d7a; }

.btn-op {
    background: #e94560;
    color: #fff;
    box-shadow: 0 4px 12px rgba(233,69,96,0.4);
}
.btn-op:hover { background: #ff5c74; }

.btn-func {
    background: #0f3460;
    color: #7ec8e3;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
.btn-func:hover { background: #1a4a80; }

.btn-eq {
    background: linear-gradient(135deg, #e94560, #c0392b);
    color: #fff;
    box-shadow: 0 4px 16px rgba(233,69,96,0.5);
    font-size: 24px;
}
.btn-eq:hover { background: linear-gradient(135deg, #ff5c74, #e74c3c); }

.btn-zero {
    grid-column: span 2;
}

/* タイトル */
.calc-title {
    text-align: center;
    color: #7ec8e3;
    font-size: 14px;
    letter-spacing: 4px;
    font-family: 'Courier New', monospace;
    margin-bottom: 6px;
    opacity: 0.7;
    text-transform: uppercase;
}

/* Streamlitのデフォルト要素を非表示 */
.stButton button {
    display: none;
}
div[data-testid="column"] { gap: 0; }
</style>
""", unsafe_allow_html=True)

# ── セッション状態の初期化 ───────────────────────────
if "display" not in st.session_state:
    st.session_state.display = "0"       # 表示中の数値
if "expression" not in st.session_state:
    st.session_state.expression = ""     # 式の履歴
if "prev_num" not in st.session_state:
    st.session_state.prev_num = None     # 前の数値
if "operator" not in st.session_state:
    st.session_state.operator = None     # 演算子
if "new_input" not in st.session_state:
    st.session_state.new_input = True    # 新しい入力か

# ── 計算ロジック ────────────────────────────────────
def calculate(a, op, b):
    if op == "+": return a + b
    if op == "−": return a - b
    if op == "×": return a * b
    if op == "÷":
        if b == 0:
            return "ERROR"
        return a / b
    return b

def format_num(n):
    """数値を見やすく整形"""
    if isinstance(n, str):
        return n
    if n == int(n):
        return str(int(n))
    return f"{n:.8g}"

def press_num(digit):
    if st.session_state.new_input:
        st.session_state.display = str(digit)
        st.session_state.new_input = False
    else:
        if st.session_state.display == "0":
            st.session_state.display = str(digit)
        else:
            if len(st.session_state.display) < 12:
                st.session_state.display += str(digit)

def press_dot():
    if st.session_state.new_input:
        st.session_state.display = "0."
        st.session_state.new_input = False
    elif "." not in st.session_state.display:
        st.session_state.display += "."

def press_op(op):
    current = float(st.session_state.display)
    if st.session_state.prev_num is not None and not st.session_state.new_input:
        result = calculate(st.session_state.prev_num, st.session_state.operator, current)
        if result == "ERROR":
            st.session_state.display = "ERROR"
            st.session_state.expression = ""
            st.session_state.prev_num = None
            st.session_state.operator = None
            st.session_state.new_input = True
            return
        st.session_state.prev_num = result
        st.session_state.display = format_num(result)
    else:
        st.session_state.prev_num = current
    st.session_state.operator = op
    st.session_state.expression = f"{format_num(st.session_state.prev_num)} {op}"
    st.session_state.new_input = True

def press_eq():
    if st.session_state.prev_num is None or st.session_state.operator is None:
        return
    current = float(st.session_state.display)
    result = calculate(st.session_state.prev_num, st.session_state.operator, current)
    expr = f"{format_num(st.session_state.prev_num)} {st.session_state.operator} {format_num(current)} ="
    st.session_state.expression = expr
    if result == "ERROR":
        st.session_state.display = "ERROR"
    else:
        st.session_state.display = format_num(result)
    st.session_state.prev_num = None
    st.session_state.operator = None
    st.session_state.new_input = True

def press_clear():
    st.session_state.display = "0"
    st.session_state.expression = ""
    st.session_state.prev_num = None
    st.session_state.operator = None
    st.session_state.new_input = True

def press_sign():
    if st.session_state.display not in ("0", "ERROR"):
        if st.session_state.display.startswith("-"):
            st.session_state.display = st.session_state.display[1:]
        else:
            st.session_state.display = "-" + st.session_state.display

def press_percent():
    try:
        val = float(st.session_state.display)
        st.session_state.display = format_num(val / 100)
    except:
        pass

def press_backspace():
    d = st.session_state.display
    if d not in ("0", "ERROR") and len(d) > 1:
        st.session_state.display = d[:-1]
    else:
        st.session_state.display = "0"

# ── ボタン定義 ──────────────────────────────────────
# (label, action, style, span)
BUTTONS = [
    [("AC",  press_clear,   "func", 1),
     ("+/-", press_sign,    "func", 1),
     ("%",   press_percent, "func", 1),
     ("÷",   lambda: press_op("÷"), "op", 1)],

    [("7",   lambda: press_num(7), "num", 1),
     ("8",   lambda: press_num(8), "num", 1),
     ("9",   lambda: press_num(9), "num", 1),
     ("×",   lambda: press_op("×"), "op", 1)],

    [("4",   lambda: press_num(4), "num", 1),
     ("5",   lambda: press_num(5), "num", 1),
     ("6",   lambda: press_num(6), "num", 1),
     ("−",   lambda: press_op("−"), "op", 1)],

    [("1",   lambda: press_num(1), "num", 1),
     ("2",   lambda: press_num(2), "num", 1),
     ("3",   lambda: press_num(3), "num", 1),
     ("+",   lambda: press_op("+"), "op", 1)],

    [("⌫",   press_backspace,"func", 1),
     ("0",   lambda: press_num(0), "num", 1),
     (".",   press_dot,     "num", 1),
     ("=",   press_eq,      "eq",  1)],
]

# ── UI描画 ─────────────────────────────────────────
st.markdown('<div class="calc-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="calc-title">🧮 Calculator</div>', unsafe_allow_html=True)

# ディスプレイ
expr_html = st.session_state.expression if st.session_state.expression else "&nbsp;"
st.markdown(f"""
<div class="calc-display">
    <div class="calc-expression">{expr_html}</div>
    <div class="calc-result">{st.session_state.display}</div>
</div>
""", unsafe_allow_html=True)

# ボタン
for row in BUTTONS:
    cols = st.columns([b[3] for b in row])
    for col, (label, action, style, _) in zip(cols, row):
        with col:
            if st.button(label, key=f"btn_{label}_{id(action)}"):
                action()
                st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
