print("🔍 WEBSITE URL CHECKER")
url = input("\nenter a website URL")

if url.startswith("https://"):
    print("🔐 This website uses HTTPS (secure)")
elif url.startswith("HTTP://"):
    print("👀 this website uses HTTP (not secure)")
