# código CSS chamado de QSS (Qt CSS)

STYLE_SHEET = """
QMainWindow { background-color: #020617; }
#Sidebar { background-color: #0f172a; border-right: 1px solid #1e293b; }
#Header { background-color: #020617; border-bottom: 1px solid #1e293b; }

#Title { color: #f8fafc; font-size: 26px; font-weight: bold; }
#Subtitle { color: #94a3b8; font-size: 15px; line-height: 1.6; }
#Formula { color: #60a5fa; font-family: 'Consolas'; font-size: 16px; background: #1e293b; padding: 15px; border-radius: 8px; border: 1px solid #334155; }

QLineEdit {
    background-color: #020617; color: #f8fafc; border: 1px solid #334155;
    border-radius: 8px; padding: 12px; font-size: 14px;
}
QLineEdit:focus { border: 1px solid #3b82f6; }

QPushButton#MenuBtn {
    text-align: left; padding: 14px; background: transparent; border: none;
    color: #94a3b8; font-size: 14px; border-radius: 6px;
}
QPushButton#MenuBtn:hover { background-color: #1e293b; color: #3b82f6; }
QPushButton#MenuBtn:checked { background-color: #2563eb; color: white; font-weight: bold; }

QPushButton#ActionBtn {
    background-color: #3b82f6; color: white; font-weight: bold; border-radius: 8px; padding: 14px; border: none;
}
QPushButton#ActionBtn:hover { background-color: #2563eb; }

#ResultCard { background: #111827; border: 1px dashed #3b82f6; border-radius: 10px; padding: 20px; }
"""
