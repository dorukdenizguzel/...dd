import discord
from discord.ext import commands
import requests
import pyttsx3


def speak(text):
    """Aldığı metni pyttsx3 kullanarak seslendirir."""
    engine = pyttsx3.init()

    engine.setProperty('rate', 150) 
    engine.say(text)
    engine.runAndWait()


intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot başarıyla bağlandı! Giriş yapılan hesap: {bot.user.name}')

@bot.command()
async def start(ctx):
    """!start komutuna karşılama mesajı verir."""
    welcome_msg = "Merhaba! Ben ilginç bilgiler veren botunuzum. Eğlenmeye hazır mısınız?"
    await ctx.send(welcome_msg)

@bot.command()
async def fact(ctx):
    """!fact komutuyla API'den rastgele bir bilgi çeker, kullanıcıya gönderir ve seslendirir."""
    api_url = "https://uselessfacts.jsph.pl/random.json"
    
    try:
        response = requests.get(api_url)
        
        
        print("API Yanıtı:", response.json())
        
        
        if response.status_code == 200:
            data = response.json()
            fact_text = data.get("text", "Bilgi bulunamadı.")
            
            await ctx.send(f" **İlginç Bilgi:** {fact_text}")
        
            speak(fact_text)
            
        else:
            await ctx.send(" API sunucusuna bağlanırken bir sorun oluştu. Lütfen daha sonra tekrar deneyin.")
            
    except Exception as e:
        print(f"Hata oluştu: {e}")
        await ctx.send(" Bir hata meydana geldi, bilgi alınamadı.")



bot.run('MOCK_TOKEN_BURAYA')
