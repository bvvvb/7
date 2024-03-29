from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1223059443407781918/0y2c2Ud8H4W_qKZ1MGYdDWktB9dObor2EI12KZg2K73JMLVPVNA4piIuST8tOF7Wt0og", content="hi sir iam abd")
response = webhook.execute()