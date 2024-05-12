import telebot
import csv
import os

# Bot token
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Admin chat ID (optional)
ADMIN_CHAT_ID = None

# Activate account code
activation_code ="activatemyaccount"

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# Load user data from CSV file
user_data = {}
if os.path.exists('user_data.csv'):
    with open('user_data.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = int(row['ID'])
            user_data[user_id] = {
                'activated': row.get('Activated', False) == 'True',
                'claimed_codes': row.get('ClaimedCodes', '').split(','),
                'balance': int(row.get('Balance', 0))
            }

# Custom claim codes with their worth
claim_codes = {
    # Add your custom claim codes here
}

# Function to start the conversation
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id in user_data and user_data[user_id]['activated']:
        bot.reply_to(message, "Your account is already activated.")
    else:
        bot.reply_to(message, "Please send the activation code to proceed.")

# Function to handle activation code
@bot.message_handler(func=lambda message: message.text == activation_code)
def activate(message):
    user_id = message.from_user.id
    if user_id in user_data and user_data[user_id]['activated']:
        bot.reply_to(message, "Your account is already activated.")
    else:
        user_data[user_id] = {'activated': True, 'claimed_codes': [], 'balance': 0}
        save_to_csv()
        bot.reply_to(message, "Activation successful! You can now claim your reward by using the claim codes.")

# Function to handle custom claim codes
@bot.message_handler(func=lambda message: message.text in claim_codes.keys())
def handle_custom_claim_code(message):
    user_id = message.from_user.id
    code = message.text
    if user_id not in user_data or not user_data[user_id]['activated']:
        bot.reply_to(message, "Please activate your account first using the activation code.")
        return
    if code in user_data[user_id]['claimed_codes']:
        bot.reply_to(message, "You have already claimed the reward for this code.")
        return
    if code in claim_codes:
        worth = claim_codes[code]
        user_data[user_id]['claimed_codes'].append(code)
        user_data[user_id]['balance'] += worth
        save_to_csv()
        bot.reply_to(message, f"You have successfully claimed {worth} Naira using the code {code}! Use another code to claim another one.")
    else:
        bot.reply_to(message, "Invalid claim code.")

# Function to handle balance check
@bot.message_handler(commands=['balance'])
def balance(message):
    user_id = message.from_user.id
    if user_id not in user_data or not user_data[user_id]['activated']:
        bot.reply_to(message, "Please activate your account first using the activation code.")
        return
    if 'balance' in user_data[user_id]:
        bot.reply_to(message, f"Your current balance: {user_data[user_id]['balance']} Naira.")
    else:
        bot.reply_to(message, "You haven't claimed any rewards yet.")

# Function to handle withdrawal
@bot.message_handler(commands=['withdraw'])
def withdraw(message):
    user_id = message.from_user.id
    if user_id not in user_data or not user_data[user_id]['activated']:
        bot.reply_to(message, "Please activate your account first using the activation code.")
        return
    if 'balance' in user_data[user_id] and user_data[user_id]['balance'] >= 15000:
        if ADMIN_CHAT_ID:
            # Notify admin about withdrawal request
            admin_message = f"Withdrawal request received from {message.from_user.first_name} (ID: {user_id}) with available balance {user_data[user_id]['balance']} Naira."
            try:
                bot.send_message(ADMIN_CHAT_ID, admin_message)
            except telebot.apihelper.ApiException as e:
                print(f"Failed to notify admin: {e}")
        # Reset user's balance
        user_data[user_id]['balance'] = 0
        save_to_csv()
        bot.reply_to(message, "Withdrawal request has been submitted. Your balance has been reset to 0 Naira.")
    else:
        bot.reply_to(message, "You need at least 15,000 Naira in your balance to withdraw.")

# Function to save user data to CSV
def save_to_csv():
    headers = ['ID', 'Activated', 'ClaimedCodes', 'Balance']
    with open('user_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for user_id, data in user_data.items():
            writer.writerow({'ID': user_id, 'Activated': data['activated'], 'ClaimedCodes': ','.join(data['claimed_codes']), 'Balance': data['balance']})

# Start the bot
bot.polling()
