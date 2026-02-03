from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from aiogram.types import FSInputFile


dp=Dispatcher()
# ───────────────── MAIN MENU ─────────────────

MAIN_MENU_TEXT = (
        "🌟 24BON Quick Reply Menu - Explanations\n\n\n"
        "💰 Deposit / Top-up - For checking your deposits, delays, or payment concerns.\n\n"
        "💸 Withdrawal / Cash out - For withdrawal status, delays, or bank transfer issues.\n\n"
        "🎁 Bonuses / Promotions - For claiming or asking about rewards, promos, and events.\n\n"
        "🔑 Login / Account Issue - For help with login, password, or account access.\n\n"
        "📱 App Download / Technical Support - For installing the 24BON app or fixing technical problems.\n\n"
        "🤝 Business Partnership / Agent Inquiry - For partnership opportunities and agent program details.\n\n"
        "❓ Others - For any concerns not listed above.\n\n")
BONUS_CODE=os.getenv("Bonus_Code")


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Telegram Community Special Bonus 🎁", callback_data="special_bonus")],
        [InlineKeyboardButton(text="💰 Deposit / Top-up", callback_data="deposit")],
        [InlineKeyboardButton(text="💸 Withdrawal / Cash out", callback_data="withdraw")],
        [InlineKeyboardButton(text="📱 App Download FREE", callback_data="app_download")],
        [InlineKeyboardButton(text="😲 Balance Missing", callback_data="balance_missing")],
        [InlineKeyboardButton(text="🎁 Bonuses / Promotions", callback_data="bonus")],
        [InlineKeyboardButton(text="🔑 Login / Account Issue", callback_data="login")],
        [InlineKeyboardButton(text="🤝 Business Partnership / Agent", callback_data="agent")],
        [InlineKeyboardButton(text="❓ Others", callback_data="others")],
    ])

def back_to_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Back to Main Menu", callback_data="back_main")]
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
        [InlineKeyboardButton(text="Official App Download web page", url="https://www.24bon.com/download")],
        [InlineKeyboardButton(text="⬅️ Back to Main Menu", callback_data="back_main")],
        ])
        await call.message.edit_text(
            "Hello fam 👋 Good news from the 24BON Family! 💖\n\n"
            "Just download the 24BON App and make a deposit of ₹200, and you'll receive an extra bonus code:\n\n"
            f"{BONUS_CODE}\n\n"
            "👉 Don't miss this chance  🚀— download now, deposit today, and claim your exclusive reward!",
            reply_markup=kb
        )


    # 💰 Deposit
    elif call.data == "deposit":
        kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="HOW TO DEPOSIT?", callback_data="how_to_deposit")],
        [InlineKeyboardButton(text="⬅️ Back to Main Menu", callback_data="back_main")],
    ])
        await call.message.edit_text(
            "Deposit / Top-up\n\n"
            "Hello fam 👋  Deposits normally arrive within 10 minutes.\n\n"
            "If there's any delay, it's usually because of the bank side issue,"
            "but don't worry — your funds are 100% safe and will not be lost. 💖\n\n"
            "👉 If your deposit hasn't arrived after 10 minutes, please send us your payment proof/receipt "
            "so we can assist you right away. 🚀",
            reply_markup=kb
        )
    elif call.data == "how_to_deposit":
        await how_to_deposit(call)

    # 💸 Withdraw
    elif call.data == "withdraw":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="HOW TO WITHDRAW?", callback_data="how_to_withdraw")],
            [InlineKeyboardButton(text="BINDING WITHDRAWAL ACCOUNT ISSUES", callback_data="binding_issues")],
            [InlineKeyboardButton(text="⬅️ Back to Main Menu", callback_data="back_main")],
        ])
        await call.message.edit_text(
            "For deposit or withdrawal concerns, please send us your username and briefly describe the issue so we can assist you faster.\n\n"
            "👉 Our support team will guide you step by step.\n\n"
            "Hello fam 👋 Normally, withdrawal review takes within 10 minutes.\n"
            "Once approved, the bank transfer also arrives within 10 minutes.\n\n"
            "⏳ If it takes longer, possible reasons are:\n"
            "Our Risk Control Team is doing a second review, which may take 2-10 hours.\n"
            "If already approved but not credited within 10 minutes, it is due to the bank's processing time.\n\n"
            "Please don't worry — your funds are 100% safe and will arrive soon. 💖 Kindly wait patiently.",
            reply_markup=kb
        )

    elif call.data == "how_to_withdraw":
        await how_to_withdraw(call)

    elif call.data == "binding_issues":
        await binding_issues(call)

    # 📱 App Download
    elif call.data == "app_download":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Official App Download web page", url="https://www.24bon.com/download")],
            [InlineKeyboardButton(text="⬅️ Back to Main Menu", callback_data="back_main")]
    ])
        await call.message.edit_text(
            "Hello fam 👋 Thank you for downloading the 24BON App!\n\n"
            "You'll receive ₹5 bonus right away. 🎁\n\n"
            "⚠️ Reminder: If you don't make a deposit, withdrawals are not possible.\n\n"
            "👉 We strongly recommend making at least one deposit first to activate withdrawals, "
            "then enjoy your free bonus and spins.\n\n"
            "Start now, deposit once, and maximize your rewards with the 24BON Family! 🚀💖",
            reply_markup=kb
        )

    # 😲 Balance Missing
    elif call.data == "balance_missing":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="RECALL BALANCE", callback_data="recall_guide")],
            [InlineKeyboardButton(text="⬅️ Back to Main Menu", callback_data="back_main")],
    ])
        await call.message.edit_text(
            "💳 Balance Suddenly Missing\n\n"
            "Hello fam 👋 No need to worry 💖 Sometimes this happens because of the game provider's technical issue.\n\n"
            "Usually, your balance will return to your wallet within 5 minutes to 3 hours after the maintenance ends.\n\n"
            "👉 If your funds have not returned after this time, please provide your member name/ID and our CSR team will assist you right away to resolve it. 🚀",
            reply_markup=kb
        )
    elif call.data == "recall_guide":
        await recall_guide(call)

    # 🎁 Bonuses
    elif call.data == "bonus":
        kb=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🤝 Refer and Earn", callback_data="bonus_invite")],
        [InlineKeyboardButton(text="💰 Bonus on Deposit", callback_data="bonus_deposits")],
        [InlineKeyboardButton(text="🎁 Red Envelope: Money Rain Every Day!", callback_data="bonus_red_envelope")],
        [InlineKeyboardButton(text="📅 7-Day Check-In: Log In Daily - Win Bigger Rewards!", callback_data="bonus_checkin_7day")],
        [InlineKeyboardButton(text="📈 Cumulative Deposit Rewards", callback_data="bonus_cumulative_recharge")],
        [InlineKeyboardButton(text="💸 Daily Cashback: Win or Lose, Get Cashback!", callback_data="bonus_daily_cashback")],
        [InlineKeyboardButton(text="👑 VIP Privileges: Royal Status & Exclusive Rewards", callback_data="bonus_vip")],
        [InlineKeyboardButton(text="⬅️ Back to Main Menu", callback_data="back_main")],
    ])
        await call.message.edit_text(
            "🎁 Bonus and Promotions \n\n\n"
            "🤝 Refer and Earn\n\n"
            "💰 Bonus on Deposit\n\n"
            "🎁 Red Envelope: Money Rain Every Day!\n\n"
            "📈 Cumulative Deposit Rewards\n\n"
            "💸 Daily Cashback: Win or Lose, Get Cashback!\n\n"
            "👑 VIP Privileges: Royal Status & Exclusive Rewards\n\n",
            reply_markup=kb
        )

    elif call.data == "bonus_invite":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Back to Bonus Menu", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Main Menu", callback_data="back_main")],
    ])
        await call.message.edit_text(
            "🤝 Rewards for Referring Friends\n\n"

            "🎉 Referral Bonus\n"
            "1️⃣ Inviter Reward:\n"
            "• The inviter receives ₹77 cash with NO wagering requirement (0x rollover).\n"
            "• The reward can be withdrawn immediately.\n\n"

            "2️⃣ Invited Friend Bonus:\n"
            "• The invited friend receives a ₹17 bonus with an 8x wagering requirement.\n"
            "• Minimum deposit required: ₹200.\n"
            "• The invited friend must generate at least ₹300 in valid bets.\n"
            "• Phone verification and withdrawal details must be completed.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📊 Referral Rewards (Per Friend)\n"
            "• 1 invited friend (₹200+ deposit):\n"
            "  → You receive ₹77 | Friend receives ₹17\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 Achievement Rewards (0x Rollover)\n"
            "Invite more friends to unlock bigger rewards!\n"
            "All achievement rewards have NO wagering requirement.\n\n"

            "• 5 friends  → ₹40\n"
            "• 10 friends → ₹90\n"
            "• 20 friends → ₹190\n"
            "• 50 friends → ₹400\n"
            "• 100 friends → ₹1,000\n"
            "• 200 friends → ₹2,200\n"
            "• 500 friends → ₹6,000\n"
            "• 1,000 friends → ₹13,000\n"
            "• 5,000 friends → ₹100,000\n"
            "• 10,000 friends → ₹500,000\n"
            "• 50,000 friends → ₹1,000,000\n"
            "• 100,000 friends → ₹9,000,000\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Commission on Friends’ Deposits\n"
            "Earn up to 1% commission on every recharge made by your invited friends.\n\n"
            "Examples:\n"
            "• Friend deposits ₹200 → You earn ₹2.0\n"
            "• Friend deposits ₹500 → You earn ₹5\n"
            "• Friend deposits ₹2,000 → You earn ₹20\n"
            "• Friend deposits ₹5,000 → You earn ₹50\n"
            "• Friend deposits ₹10,000 → You earn ₹100\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "👑 Commission on Friends’ Bets\n"
            "Build your team and become the BOSS!\n"
            "Earn multi-level betting commissions based on your level:\n\n"
            "• Level 1 (Direct): 0.3%\n"
            "• Level 2: 0.1%\n"
            "• Level 3: 0.05%\n\n"

            "📌 Note:\n"
            "Commissions are calculated automatically based on valid deposits and bets.\n\n"
            "✨ All in One. All in 24BON. ✨",
            reply_markup=kb
        )

    elif call.data == "bonus_deposits":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Back to Bonus Menu", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Main Menu", callback_data="back_main")],
    ])
        
        await call.message.edit_text(
            "💰 Deposit Bonus (1st to 5th Deposit)\n\n"

            "📌 Promotion Details\n"
            "1️⃣ Eligibility:\n"
            "All newly registered members are eligible to participate.\n\n"

            "2️⃣ Deposit Bonus:\n"
            "From the first to the fifth deposit, members can enjoy a total cumulative "
            "bonus of up to 66%, with a maximum bonus cap of ₹50,000 INR.\n\n"

            "3️⃣ Withdrawal Conditions:\n"
            "• The bonus is valid only for electronic games (Slots).\n"
            "• A 3x wagering (betting volume) requirement must be completed before withdrawal.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📊 Deposit Bonus Breakdown\n\n"
            "• First Deposit  (≥ ₹200) → 8% Bonus\n"
            "• Second Deposit (≥ ₹200) → 11% Bonus\n"
            "• Third Deposit  (≥ ₹200) → 13% Bonus\n"
            "• Fourth Deposit (≥ ₹200) → 16% Bonus\n"
            "• Fifth Deposit  (≥ ₹200) → 18% Bonus\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 How to Participate\n"
            "1️⃣ Log in to your account and click Recharge (Deposit).\n"
            "2️⃣ Enter the deposit amount (minimum ₹200 INR).\n"
            "3️⃣ Select this promotion and complete the deposit process.\n"
            "4️⃣ The bonus will be credited automatically to your account.\n\n"

            "📌 Note:\n"
            "Bonuses are subject to the stated wagering requirements before withdrawal.\n\n"
            "✨ All in One. All in 24BON. ✨",
            reply_markup=kb
        )

    elif call.data == "bonus_red_envelope":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Back to Bonus Menu", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Main Menu", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "🎁 Cash Lucky Draw\n\n"

            "📌 Promotion Details\n"
            "1️⃣ Eligibility:\n"
            "All VIP members of 24BON are eligible to participate.\n\n"

            "2️⃣ Promotion Details:\n"
            "By making a daily deposit of ₹200, you can participate in the Cash Lucky Draw "
            "up to 8 times per day.\n"
            "The higher your VIP level, the bigger the cash reward you can receive.\n\n"

            "3️⃣ Rewards:\n"
            "All rewards are real cash and can be claimed directly.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 VIP Level Rewards (Per Draw)\n\n"
            "• VIP 0 - VIP 1  → ₹1.8 - ₹8.8\n"
            "• VIP 2 - VIP 3  → ₹2.8 - ₹38\n"
            "• VIP 4 - VIP 6  → ₹6.8 - ₹88\n"
            "• VIP 7 - VIP 10 → ₹13.8 - ₹588\n"
            "• VIP 11 - VIP 13 → ₹28.8 - ₹1,888\n"
            "• VIP 14 - VIP 15 → ₹188.8 - ₹3,888\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "⏰ Event Schedule (8 Sessions Daily)\n"
            "• 11:00 - 11:30\n"
            "• 13:00 - 13:30\n"
            "• 15:00 - 15:30\n"
            "• 17:00 - 17:30\n"
            "• 19:00 - 19:30\n"
            "• 21:00 - 21:30\n"
            "• 23:00 - 23:30\n"
            "• 01:00 - 01:30\n\n"

            "📌 Note:\n"
            "Each draw opportunity is granted based on the daily deposit requirement.\n\n"
            "✨ All in One. All in 24BON. ✨",
            reply_markup=kb
        )

    elif call.data == "bonus_checkin_7day":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Back to Bonus Menu", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Main Menu", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "📅 Daily VIP Check-In Rewards\n\n"

            "📌 Promotion Details\n"
            "1️⃣ Eligibility:\n"
            "All VIP members are eligible to participate.\n\n"

            "2️⃣ Promotion Rules:\n"
            "Players who log in daily and complete the check-in task can receive cash rewards.\n"
            "Check-ins must be continuous — if even one day is missed, progress will reset.\n"
            "Rewards vary by VIP level. Higher VIP levels receive bigger rewards.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🗓 Deposit Requirements by Day\n"
            "• Monday (Day 1): Deposit ₹200\n"
            "• Tuesday (Day 2): No deposit required\n"
            "• Wednesday (Day 3): Deposit ₹200\n"
            "• Thursday (Day 4): No deposit required\n"
            "• Friday (Day 5): Deposit ₹200\n"
            "• Saturday (Day 6): No deposit required\n"
            "• Sunday (Day 7): Deposit ₹200\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 VIP Check-In Rewards (₹ per day)\n\n"
            "VIP 1  → D1 ₹2 | D2 ₹2 | D3 ₹3 | D4 ₹3 | D5 ₹5 | D6 ₹5 | D7 ₹10\n"
            "VIP 2  → D1 ₹3 | D2 ₹3 | D3 ₹4 | D4 ₹4 | D5 ₹6 | D6 ₹6 | D7 ₹12\n"
            "VIP 3  → D1 ₹3 | D2 ₹4 | D3 ₹4 | D4 ₹5 | D5 ₹6 | D6 ₹6 | D7 ₹13\n"
            "VIP 4  → D1 ₹3 | D2 ₹4 | D3 ₹5 | D4 ₹5 | D5 ₹6 | D6 ₹7 | D7 ₹14\n"
            "VIP 5  → D1 ₹3 | D2 ₹4 | D3 ₹5 | D4 ₹5 | D5 ₹6 | D6 ₹8 | D7 ₹15\n"
            "VIP 6  → D1 ₹4 | D2 ₹5 | D3 ₹6 | D4 ₹7 | D5 ₹8 | D6 ₹10 | D7 ₹20\n"
            "VIP 7  → D1 ₹5 | D2 ₹6 | D3 ₹7 | D4 ₹8 | D5 ₹9 | D6 ₹10 | D7 ₹25\n"
            "VIP 8  → D1 ₹5 | D2 ₹6 | D3 ₹7 | D4 ₹8 | D5 ₹9 | D6 ₹10 | D7 ₹26\n"
            "VIP 9  → D1 ₹5 | D2 ₹6 | D3 ₹7 | D4 ₹8 | D5 ₹9 | D6 ₹10 | D7 ₹29\n"
            "VIP 10 → D1 ₹5 | D2 ₹6 | D3 ₹7 | D4 ₹8 | D5 ₹9 | D6 ₹10 | D7 ₹30\n"
            "VIP 11 → D1 ₹5 | D2 ₹6 | D3 ₹7 | D4 ₹8 | D5 ₹9 | D6 ₹10 | D7 ₹30\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 How to Claim\n"
            "1️⃣ Log in to your account → go to the 24BON homepage.\n"
            "2️⃣ Tap the Daily Sign-In icon at the bottom-right corner.\n"
            "3️⃣ After completing the check-in, rewards will be credited automatically.\n\n"

            "⚠️ Important:\n"
            "Check-ins must be continuous. Missing even one day will reset your progress.\n\n"
            "✨ All in One. All in 24BON. ✨",
            reply_markup=kb
        )

    elif call.data == "bonus_cumulative_recharge":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Back to Bonus Menu", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Main Menu", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "📈 Daily Total Deposit Rewards\n\n"

            "📌 Promotion Details\n"
            "1️⃣ Eligibility:\n"
            "Only users whose total daily deposit is equal to or greater than ₹1,000 INR "
            "are eligible to participate in this promotion.\n\n"

            "2️⃣ Promotion Rules:\n"
            "When your total daily deposit reaches a specific tier, "
            "you will complete the task and receive a cash reward.\n"
            "The higher the deposit amount, the larger the reward.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Daily Total Deposit Rewards\n\n"
            "• ≥ ₹1,000  → Cashback ₹30   (3× wagering)\n"
            "• ≥ ₹10,000 → Cashback ₹500  (3× wagering)\n"
            "• ≥ ₹50,000 → Cashback ₹4,000 (3× wagering)\n"
            "• ≥ ₹150,000 → Cashback ₹15,000 (3× wagering)\n"
            "• ≥ ₹500,000 → Cashback ₹50,000 (3× wagering)\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 How to Claim\n"
            "1️⃣ Rewards can be used on any game and are subject to a 3× wagering requirement.\n"
            "2️⃣ The promotion settlement period runs from 10:00 AM to 9:59 AM the following day.\n"
            "3️⃣ After settlement is completed, the system will automatically credit the reward.\n\n"

            "📌 Note:\n"
            "Only valid deposits made within the settlement period are counted.\n\n"
            "✨ All in One. All in 24BON. ✨",
            reply_markup=kb
        )

    elif call.data == "bonus_daily_cashback":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Back to Bonus Menu", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Main Menu", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "💸 Daily VIP Cashback\n\n"

            "📌 Promotion Details\n"
            "1️⃣ Eligibility:\n"
            "All VIP members are eligible to participate in this promotion.\n\n"

            "2️⃣ Promotion Details:\n"
            "VIP members who place bets on designated games can receive cashback "
            "(reimbursement) of up to 1.0%.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📊 Cashback Rates by VIP Level\n\n"
            "• VIP 1  → 0.10%\n"
            "• VIP 2  → 0.10%\n"
            "• VIP 3  → 0.10%\n"
            "• VIP 4  → 0.20%\n"
            "• VIP 5  → 0.20%\n"
            "• VIP 6  → 0.20%\n"
            "• VIP 7  → 0.30%\n"
            "• VIP 8  → 0.30%\n"
            "• VIP 9  → 0.30%\n"
            "• VIP 10 → 0.40%\n"
            "• VIP 11 → 0.40%\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 How to Participate\n"
            "• The system will automatically calculate the valid betting volume for all VIP users.\n"
            "• Cashback will be credited automatically on the next day after betting.\n\n"

            "📌 Note:\n"
            "Cashback is calculated based on valid bets placed on designated games.\n\n"
            "✨ All in One. All in 24BON. ✨",
            reply_markup=kb
        )

    elif call.data == "bonus_vip":
        kb=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Back to Bonus Menu", callback_data="bonus")],
            [InlineKeyboardButton(text="🏠 Main Menu", callback_data="back_main")],
    ])


        await call.message.edit_text(
            "👑 VIP Upgrade & Periodic Rewards\n\n"

            "📌 VIP Upgrade Rewards\n"
            "1️⃣ Eligibility:\n"
            "All VIP members can participate in this promotion.\n\n"

            "2️⃣ Upgrade Reward Rule:\n"
            "When a user reaches the corresponding VIP level, "
            "they will receive a one-time exclusive upgrade reward.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 VIP Upgrade Rewards\n\n"
            "VIP 1  → Deposit ₹100 | Valid Bet 0 → Reward ₹0\n"
            "VIP 2  → Deposit ₹2,000 | Valid Bet 20,000+ → Reward ₹25\n"
            "VIP 3  → Deposit ₹10,000 | Valid Bet 100,000+ → Reward ₹100\n"
            "VIP 4  → Deposit ₹20,000 | Valid Bet 200,000+ → Reward ₹200\n"
            "VIP 5  → Deposit ₹50,000 | Valid Bet 500,000+ → Reward ₹500\n"
            "VIP 6  → Deposit ₹150,000 | Valid Bet 1,500,000+ → Reward ₹900\n"
            "VIP 7  → Deposit ₹300,000 | Valid Bet 3,000,000+ → Reward ₹1,500\n"
            "VIP 8  → Deposit ₹600,000 | Valid Bet 6,000,000+ → Reward ₹2,000\n"
            "VIP 9  → Deposit ₹1,500,000 | Valid Bet 15,000,000+ → Reward ₹10,000\n"
            "VIP 10 → Deposit ₹5,000,000 | Valid Bet 50,000,000+ → Reward ₹50,000\n"
            "VIP 11 → Deposit ₹10,000,000 | Valid Bet 100,000,000+ → Reward ₹100,000\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "📆 VIP Weekly Rewards\n"
            "• All VIP members are eligible.\n"
            "• Rewards are issued every Monday of the following week once requirements are met.\n\n"

            "VIP 1  → Deposit ₹100 | Bet ₹100 → Reward ₹3\n"
            "VIP 2  → Deposit ₹200 | Bet ₹200 → Reward ₹15\n"
            "VIP 3  → Deposit ₹300 | Bet ₹300 → Reward ₹30\n"
            "VIP 4  → Deposit ₹400 | Bet ₹400 → Reward ₹40\n"
            "VIP 5  → Deposit ₹600 | Bet ₹600 → Reward ₹60\n"
            "VIP 6  → Deposit ₹1,000 | Bet ₹1,000 → Reward ₹100\n"
            "VIP 7  → Deposit ₹2,000 | Bet ₹2,000 → Reward ₹200\n"
            "VIP 8  → Deposit ₹4,000 | Bet ₹4,000 → Reward ₹400\n"
            "VIP 9  → Deposit ₹5,000 | Bet ₹5,000 → Reward ₹500\n"
            "VIP 10 → Deposit ₹5,000 | Bet ₹5,000 → Reward ₹500\n"
            "VIP 11 → Deposit ₹5,000 | Bet ₹5,000 → Reward ₹500\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n"
            "🗓 VIP Monthly Rewards\n"
            "• All VIP members are eligible.\n"
            "• Rewards are issued on the 3rd day of the following month.\n\n"

            "VIP 1  → Deposit ₹500 | Bet ₹500 → Reward ₹6\n"
            "VIP 2  → Deposit ₹1,000 | Bet ₹1,000 → Reward ₹30\n"
            "VIP 3  → Deposit ₹1,500 | Bet ₹1,500 → Reward ₹60\n"
            "VIP 4  → Deposit ₹2,000 | Bet ₹2,000 → Reward ₹80\n"
            "VIP 5  → Deposit ₹3,000 | Bet ₹3,000 → Reward ₹120\n"
            "VIP 6  → Deposit ₹5,000 | Bet ₹5,000 → Reward ₹200\n"
            "VIP 7  → Deposit ₹10,000 | Bet ₹10,000 → Reward ₹400\n"
            "VIP 8  → Deposit ₹20,000 | Bet ₹20,000 → Reward ₹800\n"
            "VIP 9  → Deposit ₹25,000 | Bet ₹25,000 → Reward ₹1,000\n"
            "VIP 10 → Deposit ₹25,000 | Bet ₹25,000 → Reward ₹1,000\n"
            "VIP 11 → Deposit ₹25,000 | Bet ₹25,000 → Reward ₹1,000\n\n"

            "📌 Note:\n"
            "VIP rewards are credited automatically once the corresponding requirements are met.\n\n"
            "✨ All in One. All in 24BON. ✨",
            reply_markup=kb
        )

    # 🔑 Login
    elif call.data == "login":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔒 Forgot Password", callback_data="login_forgot_pw")],
            [InlineKeyboardButton(text="☎️ Wrong / Lost Phone Number", callback_data="login_lost_phone")],
            [InlineKeyboardButton(text="📱 SMS / OTP Not Received", callback_data="login_no_otp")],
            [InlineKeyboardButton(text="🚫 Account Locked - Solution", callback_data="login_locked")],
            [InlineKeyboardButton(text="◀️ Back to Main Menu", callback_data="back_main")]
    ])
        await call.message.edit_text(
            "🔑Login / Account Issue\n\n"
            "🔒Forgot Password\n"
            "👉 Player cannot remember their password and needs reset help.\n\n"
            "☎️ Wrong / Lost Phone Number\n"
            "👉 Player changed/lost their phone number and cannot log in.\n\n"
            "📱 SMS / OTP Not Received\n"
            "👉 Player did not get the code needed for login.\n\n"
            "🚫 Account Locked\n"
            "👉 Player's account is blocked due to multiple failed attempts or security reasons.\n\n"
            "📊 Why Did My Turnover Increase?\n"
            "👉 Player wants to know why their wagering/turnover requirement went up.\n\n"
            "❓ Other Login Problems\n"
            "👉 For any login issue not listed above.",
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
            [InlineKeyboardButton(text="Official Agent Channel", url="https://t.me/Official_24BON")],
            [InlineKeyboardButton(text="⬅️ Back to Main Menu", callback_data="back_main")],
    ])

        await call.message.edit_text(
            "🤝 Business Partnership / Agent Inquiry\n\n"
            "Hello fam  👋 Thank you for your interest in partnering with 24BON! 💖\n\n"
            "We are only open to players with some online promotion experience.\n"
            "If you encounter any non-agent issues, please contact CSR for a faster and better solution.\n\n"
            "To help us understand better, could you please share:\n"
            " 1️⃣ Your promotion experience (e.g., social media, community groups, offline marketing)\n"
            " 2️⃣ What kind of collaboration or support you are looking for from us\n\n"
            "Once we receive your details, our team will review and guide you on how to start earning as our official 🚀",
            reply_markup=kb
        )

    # ❓ Others
    elif call.data == "others":
        text = (
            "Hello fam 👋 For other concerns, please ask <a href='https://direct.lc.chat/19443792/'>Customer service</a> for help\n\n"
            "👉 To speed up our response, kindly provide your member ID.\n"
            "Rest assured, our team will handle your request as a priority and assist you right away.💖"
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
        await call.answer("This option will be available soon 🚀", show_alert=True)


@dp.callback_query(F.data == "how_to_deposit")
async def how_to_deposit(call: types.CallbackQuery):
    text = (
            "How to Deposit on 24BON\n\n"
            "1. Open the 24BON app.\n"
            "2. On the home page, tap the wallet icon.\n"
            "3. Choose your preferred payment method (Paytm, PhonePe, or UPI).\n"
            "4. Select an available payment channel.\n"
            "5. Enter the amount you want to deposit.\n"
            "6. (Optional) Select a promotion if available, then tap 'Next'.\n"
            "7. Wait for the UPI QR code or payment instructions to appear.\n"
            "8. Complete the payment using Paytm, PhonePe, or any UPI-supported banking app\n"
            "(scan the QR code or copy the UPI details).\n"
            "9. Wait for the 'Payment Successful' confirmation.\n"
            "10. Tap 'Done' — your balance will be updated automatically.\n\n"
            "📢 Don't forget to join the official Telegram channel for promotions and updates:\n"
            "👉 https://t.me/Official_24BON\n\n"
            "✨ All in One. All in 24BON!\n"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️Back", callback_data="deposit")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "how_to_withdraw")
async def how_to_withdraw(call: types.CallbackQuery):
    text = (
        "💸 How to Withdraw on 24BON\n\n"
        "Step 1. Open the 24BON app → Withdraw.\n"
        "Step 2. Select Bank Transfer as your withdrawal method.\n\n"
        "📌 If this is your first withdrawal:\n"
        "• Full name (must exactly match the name registered with your bank/KYC; once submitted, it cannot be changed).\n"
        "• Bank account details (correct format required).\n\n"
        "Step 3. Create a transaction password "
        "(6 characters, letters and numbers ONLY; must be different from your login password).\n"
        "Step 4. Enter the withdrawal amount (min: ₹100 | max: ₹50,000).\n"
        "Step 5. Verify all details → Withdraw / Confirm.\n"
        "Step 6. If an OTP or PIN is requested, enter it.\n"
        "Step 7. Wait for the status: Processing → Successful.\n"
        "Step 8. Check the balance in your bank app.\n\n"
        "⚠️ Important Reminders:\n"
        "• ✅ The full name must exactly match your bank/KYC records.\n"
        "• ✅ Bank account details must be correct, as funds will be sent there.\n"
        "• ✅ The transaction password must be 6 characters using only letters and numbers.\n"
        "• 🔒 The login password and transaction password must be different.\n"
        "• 🔒 Only ONE bank account is allowed per 24BON account to avoid withdrawal errors.\n"
        "• ❌ Do NOT enter your phone number as your full name.\n"
        "• ✔️ OTPs are valid for only a few minutes — enter them immediately before they expire.\n\n"
        "📢 Join our official Telegram channel for promotions and updates:\n"
        "👉 https://t.me/Official_24BON\n\n"
        "✨ All in One. All in 24BON. ✨"
    )


    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️Back", callback_data="withdraw")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "binding_issues")
async def binding_issues(call: types.CallbackQuery):
    text = (
        "💳 How to Link a Bank in 24BON\n\n"
        "⚠️ Hello 24BON family!\n\n"
        "1. Open the 24BON app → go to 'Withdraw'\n\n"
        "2. Press the 'Add Card' button.\n"
        "3. Fill in the required details:\n\n"
        "• Beneficiary full name\n"
        "  - Must exactly match the name registered with your bank (KYC).\n"
        "  - ⚠️ Once submitted, it cannot be modified or edited.\n"
        "  - ✅ Must not exceed 30 characters.\n"
        "  - ✅ Must not contain special characters (such as dots or symbols).\n"
        "  - ❌ Do NOT enter your phone number as the full name, as it will cause withdrawal issues.\n\n"
        "• Withdrawal method\n"
        "  - Select Bank.\n\n"
        "• Bank Account Details\n"
        "  - Bank: Account Number + IFSC Code\n\n"
        "INCORRECT: ❌ 1234567890\n\n"
        "• Transaction password\n"
        "  - Enter 6 characters using ONLY letters and numbers.\n"
        "  - Special characters are not allowed.\n"
        "  - ⚠️ The login password and transaction password must be different.\n"
        "  - ✅ This adds extra security even if someone accesses your account.\n\n"
        "4. Tap 'Submit' to complete the linking.\n\n"
        "✅ A confirmation message will appear once the linking is successful.\n\n"
        "⚠️ STRICTLY ONE BANK ACCOUNT PER 24BON ACCOUNT\n"
        "to avoid withdrawal errors or failures.\n\n"
        "📌 Tip: Always double-check your full name and UPI ID / bank details "
        "before submitting to avoid future issues.\n\n"
        "✨ All in One. All in 24BON. ✨"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️Back", callback_data="withdraw")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "recall_guide")
async def recall_guide(call: types.CallbackQuery):
    guide = (
        "Hello 24BON family!\n"
        "Did your balance disappear after playing a game? 😟 Don't worry — your funds are completely safe!\n\n"
        "To recover your balance, simply follow these easy steps:\n"
        "1️⃣ Go to the Withdraw section\n"
        "2️⃣ Tap the \"Recover Balance\" option\n"
        "3️⃣ Your funds will be returned to your wallet immediately!\n\n"
        "There's nothing to worry about — all your funds are fully protected with us.\n\n"
        "If you have any questions or need assistance, feel free to contact our Customer Support team. We're always ready to help!\n\n"
        "🙏 Thank you for your continued support!\n"
        "✨ All in One. All in 24BON. ✨"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️Back", callback_data="balance_missing")],
    ])

    await call.message.edit_text(guide, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "login_forgot_pw")
async def login_forgot_pw(call: types.CallbackQuery):
    text = (
        "Forgot My Password\n\n"
        "Hello family 👋 You can reset your password by clicking "
        "“Forgot my password” on the login page.\n\n"
        "Follow the steps and you’ll be able to access your account again in seconds."
    )

    await call.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️Back", callback_data="login")]]))
    await call.answer()

@dp.callback_query(F.data == "login_no_otp")
async def login_no_otp(call: types.CallbackQuery):
    text = (
        "Forgot My Password\n\n"
        "Hello family 👋 You can reset your password by clicking "
        "“Forgot my password” on the login page.\n\n"
        "Follow the steps and you'll regain access in seconds."
)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Contact Customer Service",
            url="https://direct.lc.chat/19443792/"          # ← change this link anytime
        )],
        [InlineKeyboardButton(text="⬅️Back", callback_data="login")]
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "login_locked")
async def login_locked(call: types.CallbackQuery):
    text = (
        "🚫 Account Locked - Solution\n\n"
        "Hello family 👋 Your account may be locked for several reasons:\n"
        "• Multiple incorrect login attempts\n"
        "• Security protection\n"
        "• Violation of platform rules\n\n"
        "Don't worry — your funds are 100% safe!\n"
        "👉 Simply send us your username or member ID and we'll unlock it within minutes."
    )  
    await call.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️Back", callback_data="login")]]))
    await call.answer()