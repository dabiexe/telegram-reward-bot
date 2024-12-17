---

# Telegram Reward Bot

The Telegram Reward Bot is a Python script designed to engage users by rewarding them with virtual currency (Naira) upon activation of their accounts and claiming of custom codes. This README will guide you through the setup process and usage of the bot, providing detailed instructions at every step.

## Getting Started

To begin using the Telegram Reward Bot, follow these steps:

1. **Obtain a Telegram Bot Token**: Before running the script, you'll need to create a Telegram bot and obtain its token from the BotFather. Start by opening the Telegram app and searching for BotFather. Initiate a chat with BotFather and use the `/newbot` command to create a new bot. Follow the prompts to set a name and username for your bot, and BotFather will provide you with a unique API token. Ensure you keep this token secure and do not share it with anyone else.

2. **Clone the Repository**: Next, clone the repository containing the Telegram Reward Bot script to your local machine. Use the following command in your terminal:

   ```bash
   git clone https://github.com/dabiexe/telegram-reward-bot.git
   ```



3. **Navigate to the Project Directory**: Once the repository is cloned, navigate to the project directory using the `cd` command:

   ```bash
   cd telegram-reward-bot
   ```

4. **Replace Bot Token in the Script**: Open the `bot.py` script in a text editor of your choice. Locate the `TOKEN` variable at the beginning of the script and replace `"YOUR_BOT_TOKEN_HERE"` with the Telegram bot token obtained from BotFather in step 1.

5. **Optional: Set Admin Chat ID (if needed)**: If you wish to enable the admin chat ID functionality for withdrawal notifications, replace `None` in the `ADMIN_CHAT_ID` variable with the chat ID of your admin chat. This step is optional but can be useful for receiving notifications about withdrawal requests.

6. **Define Activation Code and Claim Codes**: Customize the `activation_code` variable with your desired activation code, and add any custom claim codes along with their corresponding worth to the `claim_codes` dictionary.

7. **Run the Script**: With the necessary configurations in place, you're ready to run the script. Execute the following command in your terminal:

   ```bash
   python bot.py
   ```

   This command will start the Telegram Reward Bot and begin listening for incoming messages.

## Usage

The Telegram Reward Bot provides several commands and functionalities for users:

- **Activation**: Users can activate their accounts by sending the activation code defined in the script (`activation_code`). Once activated, users gain access to claim rewards and check their account balance.

- **Claim Rewards**: Users can claim rewards by entering specific claim codes defined in the script (`claim_codes`). Each claim code corresponds to a certain amount of virtual currency (Naira) that is credited to the user's account upon successful redemption.

- **Check Balance**: Users can check their account balance at any time by using the `/balance` command. This command provides users with their current balance in Naira.

- **Withdrawal**: Users with a balance of at least 15,000 Naira can request a withdrawal by using the `/withdraw` command. Withdrawal requests are submitted to the admin chat (if configured) for approval. Once approved, the user's balance is reset to zero, and the withdrawal is processed.

## License

This project is licensed under the MIT License. For more information, refer to the `LICENSE` file included in the repository.

## Acknowledgments

Special thanks to the developers of the `pyTelegramBotAPI` library for providing an intuitive interface for building Telegram bots.

---
