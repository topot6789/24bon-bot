from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from aiogram.types import FSInputFile


dp=Dispatcher()
# ───────────────── MAIN MENU ─────────────────

MAIN_MENU_TEXT = (
    "🌟 Menú de Respuesta Rápida de 24BON - Explicaciones\n\n"
    "💰 Depósitos/Recargas: Para consultar tus depósitos, retrasos o problemas con los pagos.\n\n"
    "💸 Retiros/Retiros: Para consultar el estado de tus retiros, retrasos o problemas con las transferencias bancarias.\n\n"
    "🎁 Bonos/Promociones: Para reclamar o consultar sobre recompensas, promociones y eventos.\n\n"
    "🔑 Inicio de sesión/Problemas con la cuenta: Para obtener ayuda con el inicio de sesión, la contraseña o el acceso a la cuenta.\n\n"
    "📱 Descarga de la app/Soporte técnico: Para instalar la app de 24BON o solucionar problemas técnicos.\n\n"
    "🤝 Colaboración comercial/Consulta con agentes: Para oportunidades de colaboración y detalles del programa de agentes.\n\n"
    "❓ Otros: Para cualquier inquietud no mencionada anteriormente."
)
BONUS_CODE=os.getenv("Bonus_Code")


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Bono especial de la comunidad de Telegram 🎁", callback_data="special_bonus")],
        [InlineKeyboardButton(text="💰 Depósito / Recarga", callback_data="deposit")],
        [InlineKeyboardButton(text="💸 Retiro / Cobro", callback_data="withdraw")],
        [InlineKeyboardButton(text="📱 Descargar la app GRATIS", callback_data="app_download")],
        [InlineKeyboardButton(text="😲 Saldo no acreditado", callback_data="balance_missing")],
        [InlineKeyboardButton(text="🎁 Bonos y promociones", callback_data="bonus")],
        [InlineKeyboardButton(text="🔑 Problemas de acceso / Cuenta", callback_data="login")],
        [InlineKeyboardButton(text="🤝 Alianza comercial / Agente", callback_data="agent")],
        [InlineKeyboardButton(text="❓ Otros", callback_data="others")],
    ])

def back_to_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Volver al menú principal", callback_data="back_main")]
    ])

# ───────────────── ENTRY POINT ─────────────────

async def start(message: types.Message):
    await message.edit_text(
        MAIN_MENU_TEXT,
        reply_markup=main_menu()
    )

# ───────────────── CALLBACK ROUTER ─────────────────

async def handle_callback(call: types.CallbackQuery):

    # 🔙 Back to main menu
    if call.data == "back_main":
        await call.message.edit_text(
            MAIN_MENU_TEXT,
            reply_markup=main_menu()
        )
        return

    # 🎁 Special Bonus
    if call.data == "special_bonus":
        kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Página oficial de descarga del sitio web", url="https://www.24bon.com/download")],
        [InlineKeyboardButton(text="⬅️ Volver a las bonificaciones", callback_data="back_main")],
        ])
        await call.message.edit_text(
        "Hola familia 👋 ¡Buenas noticias de la familia 24BON! 💖\n\n"
        "Solo descarga la app de 24BON y realiza un depósito de ₱200 para recibir un código de bono adicional:\n\n"
        f"{BONUS_CODE}\n\n"
        "👉 ¡No pierdas esta oportunidad 🚀! Descarga ahora, deposita hoy y reclama tu recompensa exclusiva.",
            reply_markup=kb
        )


    # 💰 Deposit
    elif call.data == "deposit":
        kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="¿CÓMO DEPOSITAR?", callback_data="how_to_deposit")],
        [InlineKeyboardButton(text="⬅️ Volver a las bonificaciones", callback_data="back_main")],
    ])
        await call.message.edit_text(
        "Depósito / Recarga\n\n"
        "Hola familia 👋 Los depósitos normalmente se acreditan en un plazo de 10 minutos.\n\n"
        "Si hay algún retraso, generalmente se debe a un problema del banco. "
        "No te preocupes — tus fondos están 100% seguros y no se perderán. 💖\n\n"
        "👉 Si tu depósito no se ha acreditado después de 10 minutos, por favor envíanos el comprobante de pago "
        "para que podamos ayudarte de inmediato. 🚀",
            reply_markup=kb
        )
    elif call.data == "how_to_deposit":
        await how_to_deposit(call)

    # 💸 Withdraw
    elif call.data == "withdraw":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="¿CÓMO RETIRAR DINERO?", callback_data="how_to_withdraw")],
            [InlineKeyboardButton(text="PROBLEMAS RELACIONADOS CON LA VINCULACIÓN DE LA CUENTA DE RETIRO", callback_data="binding_issues")],
            [InlineKeyboardButton(text="⬅️ Volver a las bonificaciones", callback_data="back_main")],
        ])
        await call.message.edit_text(
            "Para consultas sobre depósitos o retiros, por favor envíanos tu nombre de usuario y una breve descripción del problema para que podamos ayudarte más rápido.\n\n"
            "👉 Nuestro equipo de soporte te guiará paso a paso.\n\n"
            "Hola familia 👋 Normalmente, la revisión de los retiros se completa en un plazo de 10 minutos.\n"
            "Una vez aprobado, la transferencia bancaria también suele acreditarse dentro de 10 minutos.\n\n"
            "⏳ Si tarda más de lo esperado, las posibles razones son:\n"
            "Nuestro equipo de Control de Riesgos está realizando una segunda revisión, lo cual puede tomar de 2 a 10 horas.\n"
            "Si ya fue aprobado pero no se acreditó en 10 minutos, se debe al tiempo de procesamiento del banco.\n\n"
            "Por favor, no te preocupes — tus fondos están 100% seguros y llegarán pronto. 💖 Te pedimos amablemente que esperes con paciencia.",
            reply_markup=kb
        )

    elif call.data == "how_to_withdraw":
        await how_to_withdraw(call)

    elif call.data == "binding_issues":
        await binding_issues(call)

    # 📱 App Download
    elif call.data == "app_download":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Página oficial de descarga del sitio web", url="https://www.24bon.com/download")],
            [InlineKeyboardButton(text="⬅️ Volver a las bonificaciones", callback_data="back_main")]
    ])
        await call.message.edit_text(
            "Hola familia 👋 ¡Gracias por descargar la app de 24BON!\n\n"
            "Recibirás un bono de 5ARGinmediatamente. 🎁\n\n"
            "⚠️ Recordatorio: si no realizas un depósito, no será posible retirar.\n\n"
            "👉 Recomendamos encarecidamente realizar al menos un depósito primero para activar los retiros, "
            "y luego disfrutar de su bono gratuito.\n\n"
            "Comienza ahora, deposita una vez y maximiza tus recompensas con la familia 24BON. 🚀💖",
            reply_markup=kb
        )

    # 😲 Balance Missing
    elif call.data == "balance_missing":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="GUÍA DE EQUILIBRIO DE RETIRADA", callback_data="recall_guide")],
            [InlineKeyboardButton(text="⬅️ Volver al menú principal", callback_data="back_main")],
    ])
        await call.message.edit_text(
            "💳 Saldo desaparecido repentinamente\n\n"
            "Hola familia 👋 No hay de qué preocuparse 💖 A veces esto ocurre debido a un problema técnico del proveedor del juego.\n\n"
            "Normalmente, tu saldo volverá a tu billetera entre 5 minutos y 3 horas después de que finalice el mantenimiento.\n\n"
            "👉 Si tus fondos no han regresado después de este tiempo, por favor proporciona tu nombre de usuario o ID y nuestro equipo de CSR te asistirá de inmediato para solucionarlo. 🚀",
            reply_markup=kb
        )
    elif call.data == "recall_guide":
        await recall_guide(call)

    # 🎁 Bonuses
    elif call.data == "bonus":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🥚🎁 120% de Bono en tu Primer Depósito", callback_data="bonus_120_deposit")],
            [InlineKeyboardButton(text="👑 Beneficios VIP Exclusivos", callback_data="bonus_vip")],
            [InlineKeyboardButton(text="🌧 Lluvia Diaria de Sobres Rojos", callback_data="bonus_red_envelope")],
            [InlineKeyboardButton(text="💸 Cashback Diario según tu Volumen de Apuestas", callback_data="bonus_cashback")],
            [InlineKeyboardButton(text="📅 Check-in Diario de 7 Días", callback_data="bonus_checkin")],
            [InlineKeyboardButton(text="🥚 Huevo Dorado por Pérdidas", callback_data="bonus_golden_egg")],
            [InlineKeyboardButton(text="🎡 Ruleta de la Suerte", callback_data="bonus_spin")],
            [InlineKeyboardButton(text="💸 Invita y Gana Dinero", callback_data="bonus_referral")],
            [InlineKeyboardButton(text="⬅️ Volver al menú principal", callback_data="back_main")]
    ])
        await call.message.edit_text(
            "🎁 120% de Bono en tu Primer Depósito\n\n"
            "👑 Beneficios VIP Exclusivos\n\n"
            "🌧 Lluvia Diaria de Sobres Rojos\n\n"
            "💸 Cashback Diario según tu Volumen de Apuestas\n\n"
            "📅 Check-in Diario de 7 Días\n\n"
            "🥚 Huevo Dorado por Pérdidas\n\n"
            "🎡 Ruleta de la Suerte\n\n"
            "💸 Invita y Gana Dinero\n\n", 
            reply_markup=kb
        )

    elif call.data == "bonus_120_deposit":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])
        await call.message.edit_text(
            "🎁 120% de Bono en tu Primer Depósito\n\n"

            "📌 Detalles de la Promoción\n"
            "• Participantes: Todos los miembros recién registrados.\n"
            "• Bono de Depósito: Desde el primer hasta el quinto depósito, "
            "puedes obtener un bono acumulado de hasta **120%**, "
            "con un límite máximo de **$50,000**.\n\n"

            "━━━━━━━━━━━━━━━\n"
            "💰 Desglose del Bono por Depósito\n\n"

            "1️⃣ Primer depósito\n"
            "• Depósito mínimo: ≥ $5,000\n"
            "• Bono: 15%\n\n"

            "2️⃣ Segundo depósito\n"
            "• Depósito mínimo: ≥ $5,000\n"
            "• Bono: 20%\n\n"

            "3️⃣ Tercer depósito\n"
            "• Depósito mínimo: ≥ $5,000\n"
            "• Bono: 25%\n\n"

            "4️⃣ Cuarto depósito\n"
            "• Depósito mínimo: ≥ $5,000\n"
            "• Bono: 30%\n\n"

            "5️⃣ Quinto depósito\n"
            "• Depósito mínimo: ≥ $5,000\n"
            "• Bono: 30%\n\n"

            "━━━━━━━━━━━━━━━\n"
            "🚀 Cómo Participar\n\n"
            "1️⃣ Inicia sesión en tu cuenta y haz clic en **Recarga**.\n"
            "2️⃣ Ingresa el monto a depositar (mínimo ≥ $5,000).\n"
            "3️⃣ Selecciona esta promoción y completa el depósito.\n"
            "4️⃣ El bono se acreditará automáticamente en tu cuenta.\n\n"

            "✨ Todo en uno. Todo en 24BON.",
            reply_markup=kb
        )

    elif call.data == "bonus_vip":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])
        
        await call.message.edit_text(
            "👑 Beneficios VIP Exclusivos\n\n"

            "📌 Bono por Ascenso de Nivel VIP\n"
            "Cumple con los requisitos de depósito y volumen de apuesta para subir de nivel "
            "y desbloquear bonos exclusivos.\n\n"

            "━━━━━━━━━━━━━━━\n"
            "🏆 Bonos por Nivel VIP\n\n"

            "VIP 0  | Depósito: ARS$ 0 | Apuesta: ARS$ 0 | Bono: ARS$ 0 | Rollover: 0x\n"
            "VIP 1  | Depósito: ARS$ 5,000 | Apuesta: ARS$ 50,000 | Bono: ARS$ 0 | 1x\n"
            "VIP 2  | Depósito: ARS$ 50,000 | Apuesta: ARS$ 250,000 | Bono: ARS$ 1,000 | 1x\n"
            "VIP 3  | Depósito: ARS$ 250,000 | Apuesta: ARS$ 1,000,000 | Bono: ARS$ 5,000 | 1x\n"
            "VIP 4  | Depósito: ARS$ 750,000 | Apuesta: ARS$ 3,000,000 | Bono: ARS$ 10,000 | 1x\n"
            "VIP 5  | Depósito: ARS$ 2,000,000 | Apuesta: ARS$ 8,000,000 | Bono: ARS$ 20,000 | 1x\n"
            "VIP 6  | Depósito: ARS$ 4,500,000 | Apuesta: ARS$ 17,500,000 | Bono: ARS$ 50,000 | 1x\n"
            "VIP 7  | Depósito: ARS$ 10,000,000 | Apuesta: ARS$ 37,500,000 | Bono: ARS$ 125,000 | 1x\n"
            "VIP 8  | Depósito: ARS$ 25,000,000 | Apuesta: ARS$ 100,000,000 | Bono: ARS$ 250,000 | 1x\n\n"

            "━━━━━━━━━━━━━━━\n"
            "💸 Cashback y Salario Semanal\n"
            "Disfruta beneficios continuos según tu actividad de la semana anterior.\n\n"

            "VIP 0  | Cashback: 0% | Depósito semanal: ARS$ 0 | Bono: ARS$ 0 | 0x\n"
            "VIP 1  | Cashback: 0.10% | Depósito: ARS$ 12,500 | Bono: ARS$ 150 | 3x\n"
            "VIP 2  | Cashback: 0.10% | Depósito: ARS$ 25,000 | Bono: ARS$ 250 | 3x\n"
            "VIP 3  | Cashback: 0.10% | Depósito: ARS$ 37,500 | Bono: ARS$ 550 | 3x\n"
            "VIP 4  | Cashback: 0.20% | Depósito: ARS$ 50,000 | Bono: ARS$ 850 | 3x\n"
            "VIP 5  | Cashback: 0.20% | Depósito: ARS$ 62,500 | Bono: ARS$ 1,350 | 3x\n"
            "VIP 6  | Cashback: 0.20% | Depósito: ARS$ 75,000 | Bono: ARS$ 1,850 | 3x\n"
            "VIP 7  | Cashback: 0.30% | Depósito: ARS$ 125,000 | Bono: ARS$ 3,350 | 3x\n"
            "VIP 8  | Cashback: 0.30% | Depósito: ARS$ 250,000 | Bono: ARS$ 4,350 | 3x\n\n"

            "✨ Sube de nivel, gana más beneficios y disfruta recompensas exclusivas.\n"
            "✨ Todo en uno. Todo en 24BON.",
            reply_markup=kb
        )

    elif call.data == "bonus_red_envelope":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])
 
        await call.message.edit_text(
            "🌧 Lluvia Diaria de Sobres Rojos\n\n"

            "📌 Detalles de la Promoción\n"
            "• Participantes: Todos los miembros VIP de 24BON.\n"
            "• Mecánica: Al realizar un depósito diario de **ARS$5,000**, "
            "podrás participar en el sorteo de efectivo hasta **8 veces al día**.\n"
            "• Cuanto mayor sea tu nivel VIP, mayores serán tus recompensas.\n"
            "• Los premios son **dinero real** y pueden reclamarse directamente.\n\n"

            "━━━━━━━━━━━━━━━\n"
            "💰 Recompensas por Nivel VIP\n\n"

            "VIP 0 – VIP 1 → **ARS$50 – ARS$388**\n"
            "VIP 2 – VIP 3 → **ARS$50 – ARS$1,388**\n"
            "VIP 4 – VIP 6 → **ARS$50 – ARS$2,388**\n"
            "VIP 7 – VIP 8 → **ARS$50 – ARS$3,888**\n\n"

            "━━━━━━━━━━━━━━━\n"
            "⏰ Horarios del Evento\n"
            "Disponible **8 veces al día**:\n\n"

            "🕚 11:00 – 11:30\n"
            "🕐 13:00 – 13:30\n"
            "🕒 15:00 – 15:30\n"
            "🕔 17:00 – 17:30\n"
            "🕖 19:00 – 19:30\n"
            "🕘 21:00 – 21:30\n"
            "🕚 23:00 – 23:30\n"
            "🌙 01:00 – 01:30\n\n"

            "🔥 ¡Deposita, participa y gana premios en efectivo todos los días!\n\n"
            "✨ Todo en uno. Todo en 24BON.",
            reply_markup=kb
        )

    elif call.data == "bonus_cashback":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "👑 Recompensas por Subir de Nivel VIP\n\n"

            "📌 Detalles de la Promoción\n"
            "1️⃣ Todos los miembros VIP pueden participar en esta promoción.\n"
            "2️⃣ Cuando un usuario alcanza el nivel VIP correspondiente, "
            "recibirá una recompensa única (one-time reward).\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 Recompensas por Nivel VIP (Única vez)\n\n"

            "VIP 1:\n"
            "• Depósito acumulado: $100\n"
            "• Volumen de apuesta válido: 500+\n"
            "• Recompensa: $3\n\n"

            "VIP 2:\n"
            "• Depósito acumulado: $500\n"
            "• Volumen de apuesta válido: 2,500+\n"
            "• Recompensa: $10\n\n"

            "VIP 3:\n"
            "• Depósito acumulado: ARG$1,000\n"
            "• Volumen de apuesta válido: 5,000+\n"
            "• Recompensa: ARG$18\n\n"

            "VIP 4:\n"
            "• Depósito acumulado: ARG$3,000\n"
            "• Volumen de apuesta válido: 15,000+\n"
            "• Recompensa: ARG$48\n\n"

            "VIP 5:\n"
            "• Depósito acumulado: ARG$5,000\n"
            "• Volumen de apuesta válido: 25,000+\n"
            "• Recompensa: ARG$68\n\n"

            "VIP 6:\n"
            "• Depósito acumulado: ARG$10,000\n"
            "• Volumen de apuesta válido: 50,000+\n"
            "• Recompensa: ARG$108\n\n"

            "VIP 7:\n"
            "• Depósito acumulado: ARG$20,000\n"
            "• Volumen de apuesta válido: 150,000+\n"
            "• Recompensa: ARG$288\n\n"

            "VIP 8:\n"
            "• Depósito acumulado: ARG$50,000\n"
            "• Volumen de apuesta válido: 250,000+\n"
            "• Recompensa: ARG$588\n\n"

            "VIP 9:\n"
            "• Depósito acumulado: ARG$100,000\n"
            "• Volumen de apuesta válido: 500,000+\n"
            "• Recompensa: ARG$988\n\n"

            "VIP 10:\n"
            "• Depósito acumulado: ARG$300,000\n"
            "• Volumen de apuesta válido: 1,500,000+\n"
            "• Recompensa: ARG$1,188\n\n"

            "VIP 11:\n"
            "• Depósito acumulado: ARG$500,000\n"
            "• Volumen de apuesta válido: 2,500,000+\n"
            "• Recompensa: ARG$2,588\n\n"

            "VIP 12:\n"
            "• Depósito acumulado: ARG$1,000,000\n"
            "• Volumen de apuesta válido: 5,000,000+\n"
            "• Recompensa: ARG$3,588\n\n"

            "VIP 13:\n"
            "• Depósito acumulado: ARG$3,000,000\n"
            "• Volumen de apuesta válido: 15,000,000+\n"
            "• Recompensa: ARG$4,688\n\n"

            "VIP 14:\n"
            "• Depósito acumulado: ARG$5,000,000\n"
            "• Volumen de apuesta válido: 25,000,000+\n"
            "• Recompensa: ARG$9,888\n\n"

            "VIP 15:\n"
            "• Depósito acumulado: ARG$10,000,000\n"
            "• Volumen de apuesta válido: 50,000,000+\n"
            "• Recompensa: ARG$25,888\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📅 Recompensas VIP Semanales\n"
            "• Todos los miembros VIP pueden participar.\n"
            "• Las recompensas se entregan el lunes de la semana siguiente "
            "tras cumplir los requisitos.\n\n"

            "Ejemplos de recompensas semanales:\n"
            "VIP 1 → ARG$3\n"
            "VIP 3 → ARG$11\n"
            "VIP 7 → ARG$77\n"
            "VIP 10 → ARG$177\n"
            "VIP 15 → ARG$7,777\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🗓 Recompensas VIP Mensuales\n"
            "• Todos los miembros VIP son elegibles.\n"
            "• Las recompensas se entregan el día 3 del mes siguiente.\n\n"

            "Ejemplos de recompensas mensuales:\n"
            "VIP 1 → ARG$6\n"
            "VIP 5 → ARG$54\n"
            "VIP 10 → ARG$354\n"
            "VIP 15 → ARG$15,554",
            reply_markup=kb
        )

    elif call.data == "bonus_checkin":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "📅 Check-in Diario de 7 Días\n\n"

            "📌 Recompensas por Check-in Diario\n"
            "• Participantes: Todos los miembros VIP desde VIP0 hasta VIP8.\n"
            "• Completa tu check-in diario y cumple con el depósito mínimo para recibir bonos en efectivo.\n"
            "• El check-in debe ser **continuo**; si se interrumpe, el progreso volverá al Día 1.\n\n"

            "━━━━━━━━━━━━━━━\n"
            "💰 Recompensas por Nivel VIP\n\n"

            "VIP 0 → Día 1–6: ARS$50 | Día 7: ARS$100 | Depósito: ARS$1,500 | Rollover: 10x\n"
            "VIP 1 → Día 1–6: ARS$100 | Día 7: ARS$200 | Depósito: ARS$3,000 | Rollover: 10x\n"
            "VIP 2 → Día 1–6: ARS$150 | Día 7: ARS$300 | Depósito: ARS$4,500 | Rollover: 10x\n"
            "VIP 3 → Día 1–6: ARS$200 | Día 7: ARS$400 | Depósito: ARS$6,000 | Rollover: 10x\n"
            "VIP 4 → Día 1–6: ARS$250 | Día 7: ARS$500 | Depósito: ARS$7,500 | Rollover: 10x\n"
            "VIP 5 → Día 1–6: ARS$300 | Día 7: ARS$600 | Depósito: ARS$9,000 | Rollover: 10x\n"
            "VIP 6 → Día 1–6: ARS$350 | Día 7: ARS$700 | Depósito: ARS$10,500 | Rollover: 10x\n"
            "VIP 7 → Día 1–6: ARS$400 | Día 7: ARS$800 | Depósito: ARS$12,000 | Rollover: 10x\n"
            "VIP 8 → Día 1–6: ARS$450 | Día 7: ARS$900 | Depósito: ARS$13,500 | Rollover: 10x\n\n"

            "━━━━━━━━━━━━━━━\n"
            "🚀 Cómo Reclamar\n\n"
            "1️⃣ Inicia sesión en tu cuenta.\n"
            "2️⃣ Ve a la página de **Check-in Diario**.\n"
            "3️⃣ Completa el depósito mínimo del día y haz clic para reclamar.\n\n"

            "✅ El bono se acreditará automáticamente.\n"
            "⚠️ Recuerda que deberás cumplir con el requisito de apuesta de **10x** antes de retirar.\n\n"

            "🔥 ¡Mantén tu racha activa y gana recompensas cada semana!\n\n"
            "✨ Todo en uno. Todo en 24BON.",
            reply_markup=kb
        )

    elif call.data == "bonus_golden_egg":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "🥚 Huevo Dorado por Pérdidas\n\n"

            "📌 Detalles de la Promoción\n"
            "• Participantes: Todos los miembros VIP de la plataforma.\n\n"

            "🎯 Mecánica:\n"
            "Cuando tu **pérdida neta diaria** alcance o supere los **ARS$10,000**, "
            "el sistema te otorgará una oportunidad para romper un **Huevo Dorado**.\n\n"

            "💰 Después de romperlo, podrás recibir una **recompensa en efectivo aleatoria**.\n"
            "✅ El premio es **dinero real** y se acreditará directamente en tu cuenta.\n\n"

            "━━━━━━━━━━━━━━━\n"
            "🍀 ¡Convierte un día difícil en una nueva oportunidad de ganar!\n\n"

            "✨ Todo en uno. Todo en 24BON.",
            reply_markup=kb
        )

    elif call.data == "bonus_spin":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "🎡 Ruleta de la Suerte\n\n"

            "📌 Detalles de la Promoción\n"
            "• Participantes: Todos los miembros VIP de la plataforma.\n\n"

            "🎯 Mecánica:\n"
            "Cuando tu **depósito acumulado diario** alcance los **ARS$5,000**, "
            "recibirás **1 oportunidad** para girar la Ruleta de la Suerte.\n\n"

            "💰 Después de girarla, podrás obtener una **recompensa en efectivo aleatoria**.\n"
            "✅ El premio es **dinero real** y puede reclamarse directamente.\n\n"

            "━━━━━━━━━━━━━━━\n"
            "🔥 ¡Deposita, gira y descubre tu premio al instante!\n\n"

            "✨ Todo en uno. Todo en 24BON.",
            reply_markup=kb
        )

    elif call.data == "bonus_referral":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "🤝 Recompensas por Invitar Amigos\n\n"

            "📌 Bono por Referidos\n"
            "• El invitador recibirá **$1,500 en efectivo** sin requisito de apuesta (**0x rollover**), "
            "disponible para retiro inmediato.\n\n"

            "📋 Requisitos para el amigo invitado:\n"
            "✅ Depósito mínimo de **$5,000**.\n"
            "✅ Generar **$15,000 en apuestas válidas**.\n"
            "✅ Completar la verificación telefónica y vincular sus datos de retiro.\n\n"

            "👥 Ejemplo de recompensa:\n"
            "• Invita a **1 amigo** → Depósito ≥ $5,000 → Ganas **+$1,500**\n\n"

            "━━━━━━━━━━━━━━━\n"
            "💰 Comisión por Depósitos de Amigos\n"
            "Gana hasta **1% de comisión** por cada depósito realizado por tus referidos.\n\n"

            "$5,000 → $50\n"
            "$10,000 → $100\n"
            "$15,000 → $150\n"
            "$30,000 → $300\n"
            "$50,000 → $500\n"
            "$200,000 → $2,000\n"
            "$500,000 → $5,000\n"
            "$1,000,000 → $10,000\n\n"

            "━━━━━━━━━━━━━━━\n"
            "🏆 Comisión por Apuestas de Amigos\n"
            "¡Fortalece tu equipo y conviértete en un verdadero líder!\n"
            "Obtén comisiones de hasta **0.3%** según tu nivel:\n\n"

            "Nivel 1 (Directos) → 0.3%\n"
            "Nivel 2 → 0.1%\n"
            "Nivel 3 → 0.05%\n\n"

            "🔥 Cuantos más amigos invites, mayores serán tus ganancias.\n\n"

            "✨ Todo en uno. Todo en 24BON.",
            reply_markup=kb
        )


    # 🔑 Login
    elif call.data == "login":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔒 Olvidé mi contraseña", callback_data="login_forgot_pw")],
            [InlineKeyboardButton(text="☎️ Número de teléfono incorrecto / perdido", callback_data="login_lost_phone")],
            [InlineKeyboardButton(text="📱 SMS / OTP no recibido", callback_data="login_no_otp")],
            [InlineKeyboardButton(text="🚫 Cuenta bloqueada - Solución", callback_data="login_locked")],
            [InlineKeyboardButton(text="◀️ Volver al menú principal", callback_data="back_main")]
    ])
        await call.message.edit_text(
            "🔑 Inicio de sesión / Problemas de cuenta\n\n"
            "🔒 Olvidé mi contraseña\n"
            "👉 El jugador no recuerda su contraseña y necesita ayuda para restablecerla.\n\n"
            "☎️ Número de teléfono incorrecto / perdido\n"
            "👉 El jugador cambió o perdió su número de teléfono y no puede iniciar sesión.\n\n"
            "📱 SMS / OTP no recibido\n"
            "👉 El jugador no recibió el código necesario para iniciar sesión.\n\n"
            "🚫 Cuenta bloqueada\n"
            "👉 La cuenta del jugador está bloqueada debido a múltiples intentos fallidos o por motivos de seguridad.\n\n"
            "📊 ¿Por qué aumentó mi requisito de apuesta?\n"
            "👉 El jugador quiere saber por qué aumentó su requisito de apuesta/rotación.\n\n"
            "❓ Otros problemas de inicio de sesión\n"
            "👉 Para cualquier otro problema de acceso no mencionado arriba.",
            reply_markup=kb
        )

    elif call.data == "login_forgot_pw":
        await login_forgot_pw(call)

    elif call.data == "login_no_otp":
        await login_no_otp(call)

    elif call.data == "login_locked":
        await login_locked(call)

    # 🤝 Agent
    elif call.data == "agent":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Canal oficial de agentes", url="https://t.me/Official_24BON")],
            [InlineKeyboardButton(text="⬅️ Volver al menú principal", callback_data="back_main")],
    ])

        await call.message.edit_text(
            "🤝 Consulta sobre asociación comercial / Agente\n\n"
            "Hola familia 👋 ¡Gracias por tu interés en colaborar con 24BON! 💖\n\n"
            "Actualmente, solo trabajamos con jugadores que tengan algo de experiencia en promoción online.\n"
            "Si tu consulta no está relacionada con agentes o asociaciones, por favor contacta con nuestro equipo de Atención al Cliente (CSR) para una solución más rápida y efectiva.\n\n"
            "Para poder entender mejor tu perfil, por favor compártenos:\n"
            " 1️⃣ Tu experiencia en promoción (por ejemplo: redes sociales, grupos comunitarios, marketing offline)\n"
            " 2️⃣ Qué tipo de colaboración o apoyo estás buscando por parte de nosotros\n\n"
            "Una vez recibamos tu información, nuestro equipo la revisará y te orientará sobre cómo comenzar a ganar como agente oficial 🚀",
            reply_markup=kb
        )

    # ❓ Others
    elif call.data == "others":
        text = (
            "Hola familia. 👋 Si tienes alguna otra duda, contacta con atención al cliente.\n\n"
            "👉 Para agilizar nuestra respuesta, por favor, proporciona tu ID de miembro\n"
            "No te preocupes, nuestro equipo atenderá tu solicitud con prioridad y te ayudará de inmediato. 💖"
        )

        photo_path = os.path.join(os.path.dirname(__file__), "images", "support.jpg")
        await call.answer()  # stop loading

        if os.path.exists(photo_path):
            await call.message.answer_photo(
                photo=FSInputFile(photo_path),
                caption=text,
                parse_mode="HTML",
            )
        else:
            await call.message.answer(text)

    else:
        await call.answer("Esta opción estará disponible pronto 🚀", show_alert=True)


@dp.callback_query(F.data == "how_to_deposit")
async def how_to_deposit(call: types.CallbackQuery):
    text = (
        "Cómo hacer un depósito en 24BON\n\n"
        "1. Abre la app de 24BON.\n"
        "2. En la página principal, toca \"Depósito\".\n"
        "3. Elige tu método de pago.\n"
        "4. Selecciona un canal de pago disponible.\n"
        "5. Ingresa el monto que deseas depositar.\n"
        "6. (Opcional) Selecciona una promoción si hay disponible y toca \"Siguiente\".\n"
        "7. Espera a que aparezcan las instrucciones de pago.\n"
        "8. Realiza el pago usando tu app bancaria.\n"
        "9. Espera el mensaje de \"Pago exitoso\".\n"
        "10. Toca \"Listo\" — tu saldo se actualizará automáticamente.\n\n"
        "📢 No olvides unirte al canal oficial de Telegram para promociones y novedades:\n"
        "👉 https://t.me/Official_24BON\n\n"
        "✨ Todo en uno. Todo en 24BON."
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️Atrás", callback_data="deposit")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "how_to_withdraw")
async def how_to_withdraw(call: types.CallbackQuery):
    text = (
        "💸 Cómo retirar en 24BON\n\n"
        "Paso 1. Abre la app de 24BON → Retiro.\n"
        "Paso 2. Selecciona el banco.\n\n"
        "📌 Si es tu primer retiro:\n"
        "• Nombre completo (debe coincidir con el nombre registrado en el banco; no se podrá modificar después de enviarlo).\n"
        "• Número de cuenta bancaria (formato correcto).\n\n"
        "Paso 3. Crea una contraseña de transacción (6 caracteres, SOLO letras y números; debe ser diferente a la contraseña de inicio de sesión).\n"
        "Paso 4. Ingresa el monto (mín: 100 ARG| máx: 50,000 ARG).\n"
        "Paso 5. Verifica los datos → Retirar / Confirmar.\n"
        "Paso 6. Si se solicita OTP/PIN, ingrésalo.\n"
        "Paso 7. Espera el estado: Procesando → Exitoso.\n"
        "Paso 8. Revisa el saldo en tu app bancaria.\n\n"
        "⚠️ Recordatorios:\n"
        "• ✅ El nombre completo debe coincidir exactamente con el registrado en la Identificación Oficial (INE/IFE).\n"
        "• ✅ El número de cuenta bancaria debe ser correcto y exacto, ya que ahí se enviará el retiro.\n"
        "• ✅ La contraseña de transacción debe tener 6 caracteres usando solo letras y números.\n"
        "• 🔒 La contraseña de la cuenta y la contraseña de transacción deben ser diferentes.\n"
        "• 🔒 Solo se permite un banco por cuenta 24BON para evitar errores de retiro.\n"
        "• ❌ No ingreses el número de teléfono como nombre completo, ya que causará problemas en el retiro.\n"
        "• ✔️ El OTP es válido solo por unos minutos; ingrésalo de inmediato antes de que expire.\n\n"
        "📢 Únete a Telegram para promociones y actualizaciones:\n"
        "👉 https://t.me/Official_24BON\n\n"
        "✨ Todo en uno. Todo en 24BON. ✨"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️Atrás", callback_data="withdraw")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "binding_issues")
async def binding_issues(call: types.CallbackQuery):
    text = (
        "💳 How to link a Bank in 24BON\n\n"
        "⚠️ Hello 24BON family!\n\n"
        "1. Open the 24BON app → go to \"Withdraw\".\n"
        "2. Press the \"+\" button.\n"
        "3. Fill in the required details:\n"
        "Full name of the beneficiary • must be exactly the same as in your Bank (see example/guide image below)\n"
        "• ⚠️ Once submitted, it cannot be modified or edited in your current Bank.\n"
        "• ✅ The full name must exactly match the one registered in the Bank.\n"
        "• ✅ Must not exceed 30 characters and must not contain special characters such as periods.\n"
        "• ❌ Do not enter your phone number as the full name, as it will cause withdrawal issues.\n"
        "• Type of Bank: select your bank.\n"
        "• Account number: bank account number (CLABE, 18 digits).\n\n"
        "👉 Example:\n"
        "CORRECT: ✅ 123456789012345678\n"
        "INCORRECT: ❌ 12345678901234567\n\n"
        "• Transaction password\n"
        "👉 Enter 6 characters using ONLY letters and numbers. Special characters are not allowed.\n"
        "⚠️ The login password and transaction password cannot be the same; make sure they are different.\n"
        "✅ This is required for added security: even if someone gains access to your account, they won’t be able to withdraw easily.\n\n"
        "4. Tap \"Submit\" to link it successfully.\n\n"
        "✅ A confirmation message will appear when the linking is successful.\n\n"
        "⚠️ STRICTLY ONE BANK PER 24BON ACCOUNT TO AVOID ERRORS AND FAILURES. ⚠️\n\n"
        "📌 Tip: always verify the full name and account number before submitting to avoid future errors.\n\n"
        "✨ All in one. All in 24BON. ✨"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️Atrás", callback_data="withdraw")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "recall_guide")
async def recall_guide(call: types.CallbackQuery):
    guide = (
        "¡Hola familia 24BON!\n"
        "¿Tu saldo desapareció después de jugar a un juego? 😟 No te preocupes — ¡tus fondos están completamente seguros!\n\n"
        "Para recuperar tu saldo, solo sigue estos sencillos pasos:\n"
        "1️⃣ Ve a la sección de Retiros\n"
        "2️⃣ Toca la opción \"Recuperar saldo\"\n"
        "3️⃣ ¡Tus fondos volverán inmediatamente a tu billetera!\n\n"
        "No hay nada de qué preocuparse — todos tus fondos están protegidos con nosotros.\n\n"
        "Si tienes alguna pregunta o necesitas ayuda, no dudes en contactar a nuestro equipo de Atención al Cliente. ¡Siempre estamos listos para ayudarte!\n\n"
        "🙏 ¡Gracias por tu continuo apoyo!\n"
        "✨ Todo en uno. Todo en 24BON. ✨"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️Atrás", callback_data="balance_missing")],
    ])

    await call.message.edit_text(guide, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "login_forgot_pw")
async def login_forgot_pw(call: types.CallbackQuery):
    text = (
        "Olvidé mi contraseña\n\n"
        "Hola familia 👋 Puedes restablecer tu contraseña haciendo clic en “Olvidé mi contraseña” en la página de inicio de sesión.\n\n"
        "Sigue los pasos y volverás a acceder en segundos."
    )
    await call.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️Atrás", callback_data="login")]]))
    await call.answer()

@dp.callback_query(F.data == "login_no_otp")
async def login_no_otp(call: types.CallbackQuery):
    text = (
        "SMS / OTP no recibido\n\n"
        "Hola familia 👋 A veces el retraso del SMS/OTP se debe a problemas de red o del operador.\n\n"
        "Por favor espera unos minutos y vuelve a solicitarlo.\n"
        "¿Aún no lo recibes? Contacta con Atención al Cliente para recibir ayuda."
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Contacte con el servicio de atención al cliente ahora",
            url="https://direct.lc.chat/19443792/"          # ← change this link anytime
        )],
        [InlineKeyboardButton(text="⬅️Atrás", callback_data="login")]
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "login_locked")
async def login_locked(call: types.CallbackQuery):
    text = (
        "🚫 Cuenta bloqueada - Solución\n\n"
        "Hola familia 👋 Tu cuenta puede estar bloqueada por varias razones:\n"
        "• Múltiples intentos de inicio de sesión incorrectos\n"
        "• Protección de seguridad\n"
        "• Incumplimiento de las normas de la plataforma\n\n"
        "No te preocupes — ¡tus fondos están 100% seguros!\n"
        "👉 Solo envíanos tu nombre de usuario o ID de miembro y la desbloquearemos en minutos."
    )    
    await call.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️Atrás", callback_data="login")]]))
    await call.answer()
