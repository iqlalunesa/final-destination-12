import os

INDEX_HTML_PATH = './webapp/index.html'
IMAGES_FOLDER = './webapp/images'

def get_existing_images_from_html(html):
    """Cari semua path gambar yang sudah ada di index.html"""
    existing = []
    start = 0
    while True:
        start = html.find('images/', start)
        if start == -1:
            break
        end = html.find('"', start)
        existing.append(html[start:end])
        start = end
    return set(existing)

def generate_article_tag(img_name):
    """Buat tag <article> untuk satu gambar"""
    img_path = f'images/{img_name}'
    return f'''    <article class="thumb">
        <a href="{img_path}" class="image"><img src="{img_path}" alt="" /></a>
        <h2>{img_name}</h2>
    </article>\n'''

def update_index_html():
    if not os.path.exists(INDEX_HTML_PATH):
        print("index.html tidak ditemukan.")
        return

    with open(INDEX_HTML_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # Ambil gambar-gambar yang sudah ada
    existing_images = get_existing_images_from_html(html)

    # Ambil semua file gambar dari folder
    valid_ext = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    all_images = sorted([
        f for f in os.listdir(IMAGES_FOLDER)
        if f.lower().endswith(valid_ext)
    ])

    # Filter gambar yang belum ada di HTML
    new_articles = ''
    for img in all_images:
        if f'images/{img}' not in existing_images:
            new_articles += generate_article_tag(img)

    if not new_articles:
        print("Tidak ada gambar baru yang perlu ditambahkan.")
        return

    # Sisipkan sebelum </div> penutup dari id="main"
    insert_pos = html.find('</div>', html.find('<div id="main">'))
    if insert_pos == -1:
        print("Tag </div> penutup untuk #main tidak ditemukan.")
        return

    updated_html = html[:insert_pos] + new_articles + html[insert_pos:]

    with open(INDEX_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print(f"{len(new_articles.strip().splitlines()) // 5} gambar baru ditambahkan ke index.html.")

# Jalankan
if __name__ == '__main__':
    update_index_html()
