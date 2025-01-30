import requests

# API'nin URL'si
api_url = "http://185.240.104.121:8000/send_sms/{}/{}"

# Numara ve SMS sayısı
number = "5551234567"  # Gerçek bir telefon numarası girin
sms_count = 3  # Gönderilecek SMS sayısı

# URL'yi dinamik olarak oluştur
url = api_url.format(number, sms_count)

try:
    # API'ye GET isteği gönder
    response = requests.get(url)
    
    # İstek başarılıysa sonuçları yazdır
    if response.status_code == 200:
        print("SMS Gönderim Sonuçları:", response.json())
    else:
        print(f"API Hatası: {response.status_code}")
except requests.exceptions.RequestException as e:
    # İstek sırasında oluşabilecek hataları yakala
    print(f"Hata oluştu: {e}")
