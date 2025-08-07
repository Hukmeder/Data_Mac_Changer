import random

def generate_mac():
    first_octet = "02"  # Locally administered
    mac = [first_octet]
    for _ in range(5):
        mac.append("%02X" % random.randint(0x00, 0xFF))
    return ":".join(mac).upper()

def generate_unique_macs(count=2):
    macs = set()
    while len(macs) < count:
        mac = generate_mac()
        macs.add(mac)
    return list(macs)

# MAC adreslerini üret
macs = generate_unique_macs(2)

# Hata kontrolü
print("Toplam MAC sayısı:", len(macs))
print("MAC listesi:", macs)

# Ekrana yazdır
if len(macs) >= 2:
    print("MAC 1 (örneğin LAN):  ", macs[0])
    print("MAC 2 (örneğin Wi-Fi):", macs[1])
else:
    print("Yeterli sayıda MAC üretilemedi.")
