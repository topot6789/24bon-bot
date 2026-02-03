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
            "Recibirás un bono de 5MXN inmediatamente. 🎁\n\n"
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
            [InlineKeyboardButton(text="🥚 Golden Egg for Losses", callback_data="bonus_golden_egg")],
            [InlineKeyboardButton(text="🤝 INVITE", callback_data="bonus_invite")],
            [InlineKeyboardButton(text="💰 DEPOSITS", callback_data="bonus_deposits")],
            [InlineKeyboardButton(text="👑 Exclusive VIP Benefits", callback_data="bonus_vip")],
            [InlineKeyboardButton(text="🎁 Daily Red Envelope Rain", callback_data="bonus_red_envelope")],
            [InlineKeyboardButton(text="📅 7-Day Daily Check-In", callback_data="bonus_checkin_7day")],
            [InlineKeyboardButton(text="📈 Daily Cumulative Recharge Reward", callback_data="bonus_cumulative_recharge")],
            [InlineKeyboardButton(text="🧑‍🤝‍🧑 Invite Friends to Get Support", callback_data="bonus_invite_support")],
            [InlineKeyboardButton(text="🎡 Lucky Spin Wheel", callback_data="bonus_lucky_spin")],
            [InlineKeyboardButton(text="💸 Daily Cashback Based on Betting", callback_data="bonus_daily_cashback")],
            [InlineKeyboardButton(text="⬅️ Volver al menú principal", callback_data="back_main")],
    ])
        await call.message.edit_text(
            "🎁 Bonos y promociones\n\n\n"
            "🥚 Huevo Dorado por Pérdidas\n\n"
            "🤝 INVITAR\n\n"
            "💰 DEPÓSITOS\n\n"
            "👑 Beneficios VIP Exclusivos\n\n"
            "🎁 Lluvia Diaria de Sobres Rojos\n\n"
            "📅 Registro Diario de 7 Días\n\n"
            "📈 Recompensa por Recarga Diaria Acumulada\n\n"
            "🧑‍🤝‍🧑 Invita Amigos y Obtén Apoyo\n\n"
            "🎡 Ruleta de la Suerte\n\n"
            "💸 Cashback Diario por Apuestas\n\n",
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
            "1️⃣ Participantes:\n"
            "Todos los miembros VIP de la plataforma.\n\n"

            "2️⃣ Contenido de la Promoción:\n"
            "Cuando la pérdida diaria de un usuario alcance los $100 MXN, "
            "el usuario recibirá un Huevo Dorado.\n"
            "Al romper el Huevo Dorado, el usuario podrá obtener una recompensa "
            "en efectivo aleatoria.\n\n"

            "3️⃣ Recompensa del Huevo Dorado:\n"
            "La recompensa es dinero real y puede reclamarse directamente.\n\n",
            reply_markup=kb
        )

    elif call.data == "bonus_invite":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])
        
        await call.message.edit_text(
            "🤝 Programa de Comisiones y Recompensas por Invitación de Agentes\n\n"

            "Invita a tus amigos y desbloquea 4 niveles de recompensas.\n"
            "Únete al Programa Oficial de Agentes de 24BON y genera ingresos "
            "desde la comodidad de tu hogar.\n"
            "Promociona libremente y gana hasta $1,000,000+ en comisiones mensuales.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📌 Descripción del Programa\n"
            "Todos los miembros de 24BON pueden registrarse como agentes.\n"
            "Tu cuenta de agente es la misma que tu cuenta de jugador.\n\n"

            "📊 ¿Cómo funciona?\n"
            "1️⃣ Comparte tu enlace de referido\n"
            "2️⃣ Invita a tus amigos a registrarse, depositar y apostar\n"
            "3️⃣ Ganas comisiones — ganen o pierdan, si tu equipo juega, tú cobras\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "✅ ¿Qué es un Usuario Calificado?\n"
            "Un usuario calificado es un jugador referido que:\n"
            "• Se registra a través de tu enlace de referido\n"
            "• Realiza un depósito inicial de al menos $100\n\n"
            "⚠️ Solo los usuarios calificados cuentan para las recompensas de agente.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Plan 1: Bono Instantáneo por Invitación\n"
            "Cuando tu usuario invitado deposita $100:\n"
            "👉 Recibes inmediatamente $77 como bono de invitación\n\n"
            "📍 Ejemplo:\n"
            "El usuario invitado deposita $100 → Recibes $77 al instante\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 Plan 2: Bonos por Metas\n"
            "Desbloquea recompensas según el número total de usuarios calificados invitados:\n\n"
            "5 usuarios → Bono de $100 (8x apuesta)\n"
            "10 usuarios → Bono de $300 (8x apuesta)\n"
            "20 usuarios → Bono de $500 (8x apuesta)\n"
            "50 usuarios → Bono de $1,000 (8x apuesta)\n"
            "100 usuarios → Bono de $3,000 (8x apuesta)\n"
            "200 usuarios → Bono de $5,000 (8x apuesta)\n"
            "300 usuarios → Bono de $10,000 (8x apuesta)\n"
            "500 usuarios → Bono de $20,000 (8x apuesta)\n"
            "1,000 usuarios → Bono de $50,000 (8x apuesta)\n"
            "5,000 usuarios → Bono de $250,000 (8x apuesta)\n"
            "10,000 usuarios → Bono de $500,000 (8x apuesta)\n"
            "50,000 usuarios → Bono de $1,000,000 (8x apuesta)\n"
            "100,000 usuarios → Bono de $9,000,000 (8x apuesta)\n\n"
            "📍 Ejemplo:\n"
            "Invita a 100 jugadores → Recibe un bono único de $3,000\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🏦 Plan 3: Comisión por Depósitos\n"
            "Gana una comisión del 1% sobre el total de los depósitos diarios "
            "de tus usuarios invitados — ¡sin límite!\n\n"
            "📍 Condición:\n"
            "Depósito del referido ≥ $50 → Comisión del 1% (1x apuesta)\n\n"
            "📍 Ejemplo:\n"
            "El usuario invitado deposita $10,000 → Ganas $100\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎮 Plan 4: Cashback por Apuestas\n"
            "Gana cashback multinivel según el volumen total de apuestas "
            "de tus usuarios invitados:\n\n"
            "Nivel 1 → 0.3% cashback (1x apuesta)\n"
            "Nivel 2 → 0.1% cashback (1x apuesta)\n"
            "Nivel 3 → 0.05% cashback (1x apuesta)\n\n"
            "📍 Cuanto más apueste tu equipo, mayores serán tus ingresos pasivos — sin límite.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 ¿Cómo Empezar?\n"
            "1️⃣ Comparte tu enlace de referido en:\n"
            "Facebook • YouTube • Telegram • Instagram • Messenger • WhatsApp y más\n"
            "2️⃣ Los jugadores que se registren con tu enlace quedarán vinculados automáticamente a tu cuenta\n"
            "3️⃣ Las comisiones se acreditan en tu cuenta — retira cuando quieras",
            reply_markup=kb
        )

    elif call.data == "bonus_deposits":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])
 
        await call.message.edit_text(
            "💰 Bono por Depósitos Acumulados\n\n"

            "📌 Detalles de la Promoción\n"
            "1️⃣ Participantes:\n"
            "Todos los miembros recién registrados.\n\n"

            "2️⃣ Bono por Depósito:\n"
            "Desde el primer hasta el quinto depósito, los miembros pueden "
            "disfrutar de un bono acumulado de hasta el 125%, con un bono máximo "
            "de MXN $50,000.\n\n"

            "3️⃣ Requisitos de Retiro:\n"
            "El bono es válido únicamente para juegos electrónicos.\n"
            "Debe completarse un requisito de apuesta de 6× a 10×.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📊 Desglose del Bono por Depósito\n\n"
            "1️⃣ Primer Depósito:\n"
            "• Depósito mínimo: ≥ MXN $100\n"
            "• Bono: 15%\n"
            "• Requisito de apuesta: 6×\n\n"

            "2️⃣ Segundo Depósito:\n"
            "• Depósito mínimo: ≥ MXN $100\n"
            "• Bono: 20%\n"
            "• Requisito de apuesta: 6×\n\n"

            "3️⃣ Tercer Depósito:\n"
            "• Depósito mínimo: ≥ MXN $100\n"
            "• Bono: 25%\n"
            "• Requisito de apuesta: 10×\n\n"

            "4️⃣ Cuarto Depósito:\n"
            "• Depósito mínimo: ≥ MXN $100\n"
            "• Bono: 30%\n"
            "• Requisito de apuesta: 10×\n\n"

            "5️⃣ Quinto Depósito:\n"
            "• Depósito mínimo: ≥ MXN $100\n"
            "• Bono: 35%\n"
            "• Requisito de apuesta: 10×\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 Cómo Participar\n"
            "1️⃣ Inicia sesión en tu cuenta y haz clic en *Recarga*\n"
            "2️⃣ Ingresa el monto de recarga (mínimo ≥ MXN $100)\n"
            "3️⃣ Selecciona esta promoción y completa el depósito\n"
            "4️⃣ El bono se acreditará automáticamente en tu cuenta",
            reply_markup=kb
        )

    elif call.data == "bonus_vip":
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
            "• Depósito acumulado: MXN $100\n"
            "• Volumen de apuesta válido: 500+\n"
            "• Recompensa: MXN $3\n\n"

            "VIP 2:\n"
            "• Depósito acumulado: MXN $500\n"
            "• Volumen de apuesta válido: 2,500+\n"
            "• Recompensa: MXN $10\n\n"

            "VIP 3:\n"
            "• Depósito acumulado: MXN $1,000\n"
            "• Volumen de apuesta válido: 5,000+\n"
            "• Recompensa: MXN $18\n\n"

            "VIP 4:\n"
            "• Depósito acumulado: MXN $3,000\n"
            "• Volumen de apuesta válido: 15,000+\n"
            "• Recompensa: MXN $48\n\n"

            "VIP 5:\n"
            "• Depósito acumulado: MXN $5,000\n"
            "• Volumen de apuesta válido: 25,000+\n"
            "• Recompensa: MXN $68\n\n"

            "VIP 6:\n"
            "• Depósito acumulado: MXN $10,000\n"
            "• Volumen de apuesta válido: 50,000+\n"
            "• Recompensa: MXN $108\n\n"

            "VIP 7:\n"
            "• Depósito acumulado: MXN $20,000\n"
            "• Volumen de apuesta válido: 150,000+\n"
            "• Recompensa: MXN $288\n\n"

            "VIP 8:\n"
            "• Depósito acumulado: MXN $50,000\n"
            "• Volumen de apuesta válido: 250,000+\n"
            "• Recompensa: MXN $588\n\n"

            "VIP 9:\n"
            "• Depósito acumulado: MXN $100,000\n"
            "• Volumen de apuesta válido: 500,000+\n"
            "• Recompensa: MXN $988\n\n"

            "VIP 10:\n"
            "• Depósito acumulado: MXN $300,000\n"
            "• Volumen de apuesta válido: 1,500,000+\n"
            "• Recompensa: MXN $1,188\n\n"

            "VIP 11:\n"
            "• Depósito acumulado: MXN $500,000\n"
            "• Volumen de apuesta válido: 2,500,000+\n"
            "• Recompensa: MXN $2,588\n\n"

            "VIP 12:\n"
            "• Depósito acumulado: MXN $1,000,000\n"
            "• Volumen de apuesta válido: 5,000,000+\n"
            "• Recompensa: MXN $3,588\n\n"

            "VIP 13:\n"
            "• Depósito acumulado: MXN $3,000,000\n"
            "• Volumen de apuesta válido: 15,000,000+\n"
            "• Recompensa: MXN $4,688\n\n"

            "VIP 14:\n"
            "• Depósito acumulado: MXN $5,000,000\n"
            "• Volumen de apuesta válido: 25,000,000+\n"
            "• Recompensa: MXN $9,888\n\n"

            "VIP 15:\n"
            "• Depósito acumulado: MXN $10,000,000\n"
            "• Volumen de apuesta válido: 50,000,000+\n"
            "• Recompensa: MXN $25,888\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📅 Recompensas VIP Semanales\n"
            "• Todos los miembros VIP pueden participar.\n"
            "• Las recompensas se entregan el lunes de la semana siguiente "
            "tras cumplir los requisitos.\n\n"

            "Ejemplos de recompensas semanales:\n"
            "VIP 1 → MXN $3\n"
            "VIP 3 → MXN $11\n"
            "VIP 7 → MXN $77\n"
            "VIP 10 → MXN $177\n"
            "VIP 15 → MXN $7,777\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🗓 Recompensas VIP Mensuales\n"
            "• Todos los miembros VIP son elegibles.\n"
            "• Las recompensas se entregan el día 3 del mes siguiente.\n\n"

            "Ejemplos de recompensas mensuales:\n"
            "VIP 1 → MXN $6\n"
            "VIP 5 → MXN $54\n"
            "VIP 10 → MXN $354\n"
            "VIP 15 → MXN $15,554",
            reply_markup=kb
        )

    elif call.data == "bonus_red_envelope":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "🎁 Lluvia Diaria de Sobres Rojos\n\n"

            "📌 Detalles de la Promoción\n"
            "1️⃣ Participantes:\n"
            "Todos los miembros VIP de 24BON.\n\n"

            "2️⃣ Condición para Participar:\n"
            "Realiza un depósito mayor a MXN $100 por día y podrás "
            "reclamar Sobres Rojos durante 8 diferentes horarios diarios.\n\n"

            "3️⃣ Recompensas:\n"
            "Las recompensas son dinero real y pueden reclamarse directamente.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Recompensa por Sobre Rojo según Nivel VIP (MXN)\n\n"
            "VIP 0 - VIP 1:\n"
            "• MXN $1.7 - $7.7\n\n"

            "VIP 2 - VIP 3:\n"
            "• MXN $2.7 - $37\n\n"

            "VIP 4 - VIP 6:\n"
            "• MXN $6.7 - $77\n\n"

            "VIP 7 - VIP 10:\n"
            "• MXN $13.7 - $577\n\n"

            "VIP 11 - VIP 13:\n"
            "• MXN $27.7 - $1,377\n\n"

            "VIP 14 - VIP 15:\n"
            "• MXN $177.7 - $3,777\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "⏰ Horarios de la Lluvia de Sobres Rojos\n"
            "(Horario de México)\n\n"
            "🕚 11:00 - 11:30\n"
            "🕐 13:00 - 13:30\n"
            "🕒 15:00 - 15:30\n"
            "🕔 17:00 - 17:30\n"
            "🕖 19:00 - 19:30\n"
            "🕘 21:00 - 21:30\n"
            "🕚 23:00 - 23:30\n"
            "🕐 01:00 - 01:30\n\n"

            "⚠️ Nota:\n"
            "Cada sesión tiene una cantidad limitada de Sobres Rojos. "
            "Se recomienda ingresar puntualmente para no perder la oportunidad.",
            reply_markup=kb
        )

    elif call.data == "bonus_checkin_7day":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "📅 Registro Diario de 7 Días\n\n"

            "📌 Detalles de la Promoción\n"
            "1️⃣ Participantes:\n"
            "Todos los miembros VIP pueden participar.\n\n"
            "2️⃣ Recompensa:\n"
            "Los jugadores que inicien sesión diariamente y completen el registro "
            "pueden recibir recompensas en efectivo.\n\n"
            "3️⃣ Condición Importante:\n"
            "El registro debe ser continuo. Si se omite un día, el progreso se reinicia.\n\n"
            "4️⃣ Nivel VIP:\n"
            "Las recompensas varían según el nivel VIP. "
            "A mayor nivel VIP, mayor recompensa.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Recompensas de Registro (VIP 1 – VIP 4)\n\n"
            "Día 1 → Depósito mín. MXN $100 → Recompensa MXN $3\n"
            "Día 2 → Sin depósito → Recompensa MXN $3\n"
            "Día 3 → Depósito mín. MXN $100 → Recompensa MXN $3\n"
            "Día 4 → Sin depósito → Recompensa MXN $3\n"
            "Día 5 → Depósito mín. MXN $100 → Recompensa MXN $3\n"
            "Día 6 → Sin depósito → Recompensa MXN $3\n"
            "Día 7 → Depósito mín. MXN $200 → Recompensa MXN $10\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Recompensas de Registro (VIP 5 – VIP 8)\n\n"
            "Día 1 → Depósito mín. MXN $200 → Recompensa MXN $4\n"
            "Día 2 → Sin depósito → Recompensa MXN $4\n"
            "Día 3 → Depósito mín. MXN $200 → Recompensa MXN $4\n"
            "Día 4 → Sin depósito → Recompensa MXN $4\n"
            "Día 5 → Depósito mín. MXN $200 → Recompensa MXN $4\n"
            "Día 6 → Sin depósito → Recompensa MXN $4\n"
            "Día 7 → Depósito mín. MXN $300 → Recompensa MXN $15\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Recompensas de Registro (VIP 9 – VIP 12)\n\n"
            "Día 1 → Depósito mín. MXN $300 → Recompensa MXN $5\n"
            "Día 2 → Sin depósito → Recompensa MXN $5\n"
            "Día 3 → Depósito mín. MXN $300 → Recompensa MXN $5\n"
            "Día 4 → Sin depósito → Recompensa MXN $5\n"
            "Día 5 → Depósito mín. MXN $300 → Recompensa MXN $5\n"
            "Día 6 → Sin depósito → Recompensa MXN $5\n"
            "Día 7 → Depósito mín. MXN $400 → Recompensa MXN $20\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Recompensas de Registro (VIP 13 – VIP 15)\n\n"
            "Día 1 → Depósito mín. MXN $400 → Recompensa MXN $6\n"
            "Día 2 → Sin depósito → Recompensa MXN $6\n"
            "Día 3 → Depósito mín. MXN $400 → Recompensa MXN $6\n"
            "Día 4 → Sin depósito → Recompensa MXN $6\n"
            "Día 5 → Depósito mín. MXN $400 → Recompensa MXN $6\n"
            "Día 6 → Sin depósito → Recompensa MXN $6\n"
            "Día 7 → Depósito mín. MXN $500 → Recompensa MXN $30\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 Cómo Reclamar\n"
            "1️⃣ Inicia sesión en tu cuenta → Ve a la página principal de 24BON\n"
            "2️⃣ Haz clic en el ícono de *Registro Diario* en la esquina inferior derecha\n"
            "3️⃣ El bono se acreditará automáticamente tras completar el registro\n\n"

            "⏰ Reinicio del Registro:\n"
            "El ciclo de registro diario se reinicia todos los días a las 10:00 "
            "(hora de México).\n\n"
            "⚠️ Nota Importante:\n"
            "El registro debe ser continuo. Si se pierde un día, el progreso se reiniciará.",
            reply_markup=kb
        )

    elif call.data == "bonus_cumulative_recharge":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "📈 Recompensa por Recarga Diaria Acumulada\n\n"

            "📌 Detalles de la Promoción\n"
            "1️⃣ Elegibilidad:\n"
            "Solo los usuarios cuya recarga diaria acumulada sea "
            "igual o superior a MXN $1,000 pueden participar en esta promoción.\n\n"

            "2️⃣ Mecánica de la Promoción:\n"
            "Cuando la recarga diaria acumulada alcanza un nivel específico, "
            "el usuario completa la tarea y recibe una recompensa en efectivo.\n\n"
            "⚠️ Todas las recompensas están sujetas a un requisito de apuesta "
            "de 3× antes de poder retirar.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Recompensas por Recarga Diaria Acumulada\n\n"
            "• ≥ MXN $1,000 → Recompensa MXN $30 (3× apuesta)\n"
            "• ≥ MXN $10,000 → Recompensa MXN $500 (3× apuesta)\n"
            "• ≥ MXN $50,000 → Recompensa MXN $4,000 (3× apuesta)\n"
            "• ≥ MXN $150,000 → Recompensa MXN $15,000 (3× apuesta)\n"
            "• ≥ MXN $500,000 → Recompensa MXN $50,000 (3× apuesta)\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 Cómo Recibir la Recompensa\n"
            "1️⃣ Cuanto mayor sea tu monto de recarga diaria, mayor será la recompensa.\n"
            "2️⃣ El periodo de liquidación de la promoción es de las 10:00 "
            "a las 09:59 del día siguiente (hora de México).\n"
            "3️⃣ Las recompensas se acreditarán automáticamente una vez "
            "finalizado el periodo de liquidación.",
            reply_markup=kb
        )

    elif call.data == "bonus_invite_support":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "🧑‍🤝‍🧑 Invita Amigos y Obtén Apoyo\n\n"

            "📌 Detalles de la Promoción\n"
            "1️⃣ Participantes:\n"
            "Todos los usuarios recién registrados pueden participar.\n\n"

            "2️⃣ Cupón Inicial:\n"
            "El sistema te otorgará un cupón con un monto aleatorio al participar.\n\n"

            "3️⃣ Invitación de Amigos:\n"
            "Por cada amigo que invites y que complete el registro y realice un "
            "depósito de MXN $100, recibirás una *Caja de Apoyo*.\n\n"

            "4️⃣ Recompensa de la Caja de Apoyo:\n"
            "Al abrir la Caja de Apoyo, recibirás aleatoriamente entre "
            "MXN $1 y MXN $5.\n\n"

            "5️⃣ Recompensa Acumulada:\n"
            "Cuando el monto acumulado de cupones alcance MXN $100, "
            "recibirás una recompensa en efectivo de MXN $100.\n\n"

            "6️⃣ Beneficio Adicional:\n"
            "Al participar en esta promoción, también puedes disfrutar "
            "simultáneamente del *Bono por Invitar Amigos de MXN $77*.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "⚠️ Nota:\n"
            "Las recompensas se otorgan de forma aleatoria y están sujetas "
            "a las reglas de la plataforma.",
            reply_markup=kb
        )

    elif call.data == "bonus_lucky_spin":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "🎡 Ruleta de la Suerte\n\n"

            "📌 Detalles de la Promoción\n"
            "1️⃣ Participantes:\n"
            "Todos los miembros VIP de la plataforma pueden participar.\n\n"

            "2️⃣ Mecánica de la Promoción:\n"
            "Cuando la recarga diaria acumulada del usuario alcance "
            "MXN $100, el usuario recibirá una oportunidad para girar "
            "la Ruleta de la Suerte.\n\n"
            "Después de girar la ruleta, el usuario podrá obtener "
            "una recompensa en efectivo aleatoria.\n\n"

            "3️⃣ Recompensas de la Ruleta:\n"
            "Las recompensas son dinero real y pueden reclamarse directamente.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "⚠️ Nota:\n"
            "Cada giro está sujeto a las reglas de la plataforma y "
            "la cantidad de oportunidades depende del cumplimiento "
            "de las condiciones diarias.",
            reply_markup=kb
        )

    elif call.data == "bonus_daily_cashback":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Volver a Bonos", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Menú principal", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "💸 Cashback Diario por Apuestas\n\n"

            "📌 Detalles de la Promoción\n"
            "1️⃣ Participantes:\n"
            "Todos los miembros VIP pueden participar en esta promoción.\n\n"

            "2️⃣ Contenido de la Promoción:\n"
            "Los miembros VIP que realicen apuestas en juegos designados "
            "pueden recibir cashback en tiempo real de hasta el 1.0%.\n\n"

            "3️⃣ Juegos Aplicables:\n"
            "Válido únicamente para juegos de tragamonedas y juegos de pesca.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📊 Porcentaje de Cashback por Nivel VIP\n\n"
            "VIP 1  → 0.20%\n"
            "VIP 2  → 0.20%\n"
            "VIP 3  → 0.20%\n"
            "VIP 4  → 0.20%\n"
            "VIP 5  → 0.20%\n"
            "VIP 6  → 0.20%\n"
            "VIP 7  → 0.30%\n"
            "VIP 8  → 0.30%\n"
            "VIP 9  → 0.40%\n"
            "VIP 10 → 0.50%\n"
            "VIP 11 → 0.60%\n"
            "VIP 12 → 0.70%\n"
            "VIP 13 → 0.80%\n"
            "VIP 14 → 0.90%\n"
            "VIP 15 → 1.00%\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 Cómo Participar\n"
            "• Todos los miembros VIP que jueguen tragamonedas o juegos de pesca "
            "tendrán su monto de apuesta válido calculado automáticamente por el sistema.\n"
            "• El cashback se generará dentro de los 15 minutos posteriores a la apuesta.\n"
            "• El cashback puede reclamarse manualmente desde la página de Cashback.\n"
            "• Si no se reclama manualmente, el sistema acreditará automáticamente "
            "el cashback a las 14:00 (hora de México).\n\n"

            "⚠️ Nota:\n"
            "El cashback se calcula únicamente sobre apuestas válidas "
            "y está sujeto a las reglas de la plataforma.",
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
        "Paso 4. Ingresa el monto (mín: 100 MXN | máx: 50,000 MXN).\n"
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