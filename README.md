# Hash Cracker Programı

Bu Python programı, verilen bir hash değerini deneme-yanılma yöntemiyle çözmeye çalışan bir hash kırıcıdır. Program, belirtilen bir kelime listesi dosyasını kullanarak şifreyi çözmeyi dener.

## Özellikler

- MD5, SHA1, SHA256 gibi farklı hash algoritmalarını destekler.
- Şifre tahminlerini bir kelime listesi dosyasından okur.
- Şifre başarıyla çözüldüğünde süreyi ve sonucu gösterir.
- Eksik veya yanlış argümanlar için hata mesajları görüntüler.

## Gereksinimler

- Python 3.6 veya üzeri
- `settings.py` dosyasında tanımlı yardımcı fonksiyonlar (ör. `print_`, `colored`, `get_time`, `text_types`)

## Kurulum

1. Bu projeyi bilgisayarınıza indirin veya klonlayın.
2. Python 3.6+ yüklü olduğundan emin olun.
3. Şifre denemeleri için bir `wordlist.txt` dosyası oluşturun veya mevcut bir dosyayı kullanın.

## Kullanım

Programı çalıştırmak için şu adımları izleyin:

1. Terminal veya komut satırında şu komutu çalıştırın:

   ```bash
   python cracker.py <hash_to_crack> <hash_type> <wordlist_file>
   ```

   - `<hash_to_crack>`: Çözmek istediğiniz hash değeri.
   - `<hash_type>`: Kullanılacak hash algoritması (ör. `md5`, `sha1`, `sha256`).
   - `<wordlist_file>`: Şifre denemelerini içeren dosyanın yolu.

### Örnek

MD5 hash değerini çözmek için şu komut kullanılabilir:

```bash
python cracker.py 35eda9c1dbed8e8db1fe6bbca915753e md5 wordlist.txt
```

Bu örnekte:

- `35eda9c1dbed8e8db1fe6bbca915753e` hash değeri `bytistan` kelimesine karşılık gelir.
- `md5` hash algoritması kullanılır.
- `wordlist.txt` dosyası şifre tahminlerini içerir.

### Örnek Kelime Listesi (wordlist.txt)

Kelime listesi dosyası şu şekilde görünebilir:

```
password
bytistan
123456
admin
```

## Hata Mesajları

- **The file {wordlist_file} was not found.**
  - Belirtilen kelime listesi dosyası bulunamadığında görüntülenir.
- **{hash_type} is not supported. Please choose a valid hash algorithm.**
  - Desteklenmeyen bir hash algoritması seçildiğinde görüntülenir.
- **Password not found.**
  - Tüm tahminler denenmesine rağmen eşleşme bulunamadığında görüntülenir.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
