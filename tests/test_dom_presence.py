import re
import sys
from pathlib import Path

base = Path(__file__).resolve().parents[1]
carrito = base / 'carrito.html'

if not carrito.exists():
    print(f"ERROR: archivo no encontrado: {carrito}")
    sys.exit(2)

text = carrito.read_text(encoding='utf-8')

required_ids = [
    'modal-pago',
    'resumen-items',
    'resumen-total',
    'form-pago',
    'correo',
    'btn-cancelar',
    'cerrar-modal'
]

missing = []
for idname in required_ids:
    # simple id attribute search
    if not re.search(r"id\s*=\s*['\"]" + re.escape(idname) + r"['\"]", text):
        missing.append(idname)

if missing:
    print('FAIL: faltan elementos esperados en carrito.html:')
    for m in missing:
        print(' -', m)
    sys.exit(1)

print('PASS: todos los ids requeridos están presentes en carrito.html')
sys.exit(0)
