import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

# Dictionary for common Korean sentences -> English translations across all posts
FULL_TRANSLATIONS = [
    # Wise Guide
    ("title: \"\\[Wise 활용 가이드\\] 해외 달러 수익 정산할 때 수수료 10만 원 아끼는 꿀팁 \\(첫 송금 무료\\)\"",
     "title: \"[Wise Guide] How to Save $100 on International Payout Fees (Free Remittance Coupon)\""),
    ("description: \"GitHub Sponsors, Outlier, 해외 외주 달러 정산 시 환전 수수료 10만 원 아끼는 법과 90만 원 상당 수수료 무료 혜택 받는 법을 공유합니다.\"",
     "description: \"Learn how to save $100 in exchange fees when receiving USD payouts from GitHub Sponsors, Outlier, and global freelancing platforms.\""),
    ("안녕하세요! 해외 개발이나 외주, GitHub Sponsors, Outlier 같은 글로벌 플랫폼에서 달러 수익을 받을 때 다들 한 번쯤 고민해 보셨을 거예요.",
     "Hello! If you receive USD payouts from global platforms like GitHub Sponsors, Outlier, or overseas freelancing, you've probably worried about transfer fees."),
    ("일반 은행으로 그냥 송금받으면 <b>환전 수수료에 해외 송금 수수료까지 겹쳐서 번 돈의 5~10만 원이 힘없이 날아가곤 하는데요.</b>",
     "If you transfer directly to traditional banks, <b>$50 to $100 of your hard-earned money easily disappears due to high exchange rates and remittance fees.</b>"),
    ("오늘은 이 아까운 수수료를 싹 아끼고, <b>첫 90만 원\\(500파운드\\)까지 수수료 0원으로 아예 무료 송금받을 수 있는 Wise\\(와이즈\\) 활용 꿀팁</b>을 소개해 드릴게요! 💡",
     "Today, I'm sharing how to save on these fees and get your <b>first £500 (approx. $650 USD) transferred 100% fee-free using Wise!</b> 💡"),
    ("🎁 초간단 혜택: 첫 송금 수수료 0원 쿠폰 받는 법", "🎁 Free Benefit: How to Get Your First Fee-Free Transfer Coupon"),
    ("아래 제 전용 공식 초대 링크로 가입하시면 <b>최대 90만 원\\(£500\\)까지 송금 수수료가 100% 면제되는 혜택</b>이 즉시 적용됩니다.",
     "Sign up via my official referral link below to automatically claim your <b>100% fee-free transfer reward up to £500</b>."),
    ("👉 <b><a href=\"https://wise.com/invite/dic/chanyeongs3\" target=\"_blank\" rel=\"noopener noreferrer\">Wise 수수료 0원 할인 초대 링크 \\(클릭시 자동 적용\\)</a></b>",
     "👉 <b><a href=\"https://wise.com/invite/dic/chanyeongs3\" target=\"_blank\" rel=\"noopener noreferrer\">Wise Free Transfer Invitation Link (Click to Apply)</a></b>"),
    ("\\*\\(가입하실 때 위 링크를 누르고 들어가시면 첫 외화 송금 및 정산할 때 수수료 0원 혜택이 바로 들어와요!\\)\\*",
     "*(When signing up via the link above, your fee-free transfer discount will be applied automatically!)*"),
    ("🌟 왜 Wise를 쓰면 돈을 벌 수 있을까요?", "🌟 Why Using Wise Saves You Real Money"),
    ("1. 10만 원 버는 환전 우대율 적용", "1. Real Mid-Market Exchange Rates"),
    ("일반 시중 은행은 환율에 은근슬쩍 마진을 붙여서 환전해 주지만, Wise는 <b>구글/네이버에 나오는 진짜 실시간 환율\\(Mid-market rate\\)</b>을 100% 그대로 적용해 줍니다. 1,000달러만 정산받아도 몇 만 원 이상 무조건 이득이에요!",
     "Traditional banks hide extra markups inside their exchange rates. Wise uses the <b>real mid-market rate (the same rate on Google or Reuters)</b>, saving you $50+ per $1,000 transfer!"),
    ("2. 미국 현지 달러 계좌가 3분 만에 무료 발급!", "2. Get a US Local Bank Account in 3 Minutes"),
    ("Wise에 가입하면 미국에 가지 않고도 <b>나만의 미국 은행 달러 계좌\\(Routing Number, Account Number\\)</b>가 3분 만에 무료로 생깁니다.",
     "When you sign up for Wise, you get your own <b>US Checking Account (Routing Number & Account Number)</b> in 3 minutes without visiting the US."),
    ("GitHub Sponsors나 해외 플랫폼에 이 계좌를 등록해 두면, 미국 현지 사람이 돈을 보내듯 수수료 없이 달러가 들어옵니다.",
     "Link this account to GitHub Sponsors, Stripe, or Outlier to receive USD payouts locally with zero international wire fees!"),
    ("3. 달러 그대로 모아두었다가 해외 결제 가능!", "3. Keep USD for Overseas Subscriptions"),
    ("받은 달러를 굳이 원화로 바꾸지 않고 보관해 두었다가, <b>OpenAI\\(챗GPT\\), Cloudflare, 도메인 결제, 해외 직구</b>할 때 달러 그대로 결제할 수 있어서 이중 환전 손실이 아예 0원입니다.",
     "You can hold your earnings in USD and pay directly for <b>OpenAI (ChatGPT), Cloudflare, domain renewals, or online shopping</b> with zero conversion losses."),
    ("📝 3분 만에 계정 만들고 혜택 챙기는 방법", "📝 3-Minute Simple Account Setup"),
    ("과정이 정말 쉬워서 딱 3분이면 끝납니다!", "Setting up takes just 3 minutes!"),
    ("1. <b><a href=\"https://wise.com/invite/dic/chanyeongs3\" target=\"_blank\" rel=\"noopener noreferrer\">Wise 혜택 전용 링크</a></b>를 클릭해서 회원가입을 진행합니다.",
     "1. Click the <b><a href=\"https://wise.com/invite/dic/chanyeongs3\" target=\"_blank\" rel=\"noopener noreferrer\">Wise Referral Link</a></b> to sign up."),
    ("2. 스마트폰으로 신분증\\(여권 또는 운전면허증\\)을 가볍게 촬영해서 1분 본인인증을 마칩니다.",
     "2. Take a quick photo of your ID or passport for identity verification."),
    ("3. 메인 화면에서 `Open a Balance` ➔ <b>US Dollar\\(USD\\)</b> 를 누르면 나만의 미국 계좌번호가 즉시 발급됩니다!",
     "3. Click `Open a Balance` ➔ <b>US Dollar (USD)</b> on the main dashboard to generate your US account details!"),
    ("이제 발급받은 계좌 정보를 정산받을 해외 사이트에 입력만 해두면 끝이에요.", "Now just paste your account details into your payout platform!"),
    ("🎯 요약", "🎯 Summary"),
    ("해외에서 수입이 들어오거나 해외 달러 결제가 잦은 분들이라면 무조건 만들어두시는 걸 강력 추천드려요!",
     "If you earn USD or make international online payments, setting up a Wise account is essential!"),
    ("한 번만 설정해 두면 앞으로 해외 정산받을 때마다 <b>매번 5만 원 ~ 10만 원씩 아낄 수 있으니</b> 꼭 첫 송금 수수료 무료 혜택까지 알차게 챙겨가세요! 🚀☕",
     "Set it up once and <b>save $50 to $100 on every payout!</b> Don't forget to claim your free transfer bonus! 🚀☕"),

    # Common C++ / CS problem text
    ("다음은 단위를 변환하는 추상 클래스 Converter이다.", "The following is an abstract class Converter that converts units."),
    ("Converter 클래스를 상속받아 달러를 원화로 환산하는 WonToDollar 클래스를 작성하라. main\\(\\) 함수와 실행 결과는 다음과 같다.",
     "Write a WonToDollar class that inherits from the Converter class to convert Won into Dollars. The main() function and execution result are as follows."),
    ("추상 클래스를 상속받는 파생 클래스 만들기", "Creating a derived class that inherits from an abstract class."),
]

translated_files_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.en.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for pattern, replacement in FULL_TRANSLATIONS:
        content = re.sub(pattern, replacement, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        translated_files_count += 1

print(f"Full English Translation updated for {translated_files_count} files!")
