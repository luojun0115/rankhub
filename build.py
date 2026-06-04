import os
import sys
import markdown

sys.stdout.reconfigure(encoding='utf-8')

CONTENT_DIR = 'content'
OUTPUT_DIR = 'docs'
TEMPLATE_FILE = 'templates/base.html'

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, 'content'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, 'css'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, 'js'), exist_ok=True)

SECTIONS = [
    {'id': 'bilibili', 'emoji': '🎮', 'name': 'B站排行榜'},
    {'id': 'douyin', 'emoji': '🎵', 'name': '抖音排行榜'},
    {'id': 'wechat', 'emoji': '💬', 'name': '微信公众号排行榜'},
    {'id': 'xiaohongshu', 'emoji': '📕', 'name': '小红书排行榜'},
    {'id': 'ai-global', 'emoji': '🌍', 'name': '全球AI网站排行榜'},
    {'id': 'ai-china', 'emoji': '🇨🇳', 'name': '中国AI应用排行榜'},
]

MONTHLY_RANKS = {
    'bilibili': [
        ('2026年5月B站UP主排行榜', '更新于 2026-05-01', 'hot'),
        ('2026年4月B站UP主排行榜', '更新于 2026-04-01', None),
        ('2026年3月B站UP主排行榜', '更新于 2026-03-01', None),
    ],
    'douyin': [
        ('2026年5月抖音达人排行榜', '更新于 2026-05-01', 'new'),
        ('2026年4月抖音达人排行榜', '更新于 2026-04-01', None),
        ('2026年3月抖音达人排行榜', '更新于 2026-03-01', None),
    ],
    'wechat': [
        ('2026年5月微信公众号排行榜', '更新于 2026-05-01', 'rising'),
        ('2026年4月微信公众号排行榜', '更新于 2026-04-01', None),
        ('2026年3月微信公众号排行榜', '更新于 2026-03-01', None),
    ],
    'xiaohongshu': [
        ('2026年5月小红书博主排行榜', '更新于 2026-05-01', 'hot'),
        ('2026年4月小红书博主排行榜', '更新于 2026-04-01', None),
        ('2026年3月小红书博主排行榜', '更新于 2026-03-01', None),
    ],
    'ai-global': [
        ('2026年5月全球AI网站排行榜', '更新于 2026-05-01', None),
        ('2026年4月全球AI网站排行榜', '更新于 2026-04-01', None),
        ('2026年3月全球AI网站排行榜', '更新于 2026-03-01', None),
    ],
    'ai-china': [
        ('2026年5月中国AI应用排行榜', '更新于 2026-05-01', 'new'),
        ('2026年4月中国AI应用排行榜', '更新于 2026-04-01', None),
        ('2026年3月中国AI应用排行榜', '更新于 2026-03-01', None),
    ],
}

def read_template():
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def md_to_html(md_content):
    extensions = ['tables', 'fenced_code', 'codehilite', 'toc']
    html = markdown.markdown(md_content, extensions=extensions)
    return html

def extract_title(md_content):
    for line in md_content.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    return '未命名页面'

def generate_page(title, content, template, is_index=False):
    base = '' if is_index else '../'
    html = template.replace('{{ base }}', base)
    html = html.replace('{{ title }}', title)
    if not is_index:
        breadcrumb = '<nav class="breadcrumb"><a href="' + base + 'index.html">首页</a> / <span>' + title + '</span></nav>\n'
        content = '<div class="content-page">\n' + breadcrumb + content + '\n</div>'
    html = html.replace('{{ content }}', content)
    return html

def build_rank_item(title, meta, badge, rank_num, href):
    badge_map = {
        'hot': '<span class="rank-badge badge-hot">Hot</span>',
        'new': '<span class="rank-badge badge-new">New</span>',
        'rising': '<span class="rank-badge badge-rising">Rising</span>',
    }
    rank_class = 'rank-' + str(rank_num) if rank_num <= 3 else 'rank-other'
    rank_label = str(rank_num)
    badge_html = badge_map.get(badge, '')
    return (
        '<a href="' + href + '" class="rank-item">'
        '<div class="rank-number ' + rank_class + '">' + rank_label + '</div>'
        '<div class="rank-info">'
        '<div class="rank-title">' + title + '</div>'
        '<div class="rank-meta">' + meta + '</div>'
        '</div>'
        + badge_html +
        '</a>'
    )

def build_section(section):
    items_html = ''
    ranks = MONTHLY_RANKS[section['id']]
    for i, (title, meta, badge) in enumerate(ranks, 1):
        items_html += build_rank_item(title, meta, badge, i, 'content/' + section['id'] + '.html')

    return (
        '<div class="section" data-category="' + section['name'] + '">'
        '<div class="section-header">'
        '<div class="section-icon">' + section['emoji'] + '</div>'
        '<h2 class="section-title">' + section['name'] + '</h2>'
        '<a href="content/' + section['id'] + '.html" class="section-more">查看更多 →</a>'
        '</div>'
        '<div class="rank-list">' + items_html + '</div>'
        '</div>'
    )

def generate_index():
    template = read_template()

    sections_html = ''
    for section in SECTIONS:
        sections_html += build_section(section)

    index_content = (
        '<div class="hero">'
        '<p>发现热门内容，追踪行业趋势</p>'
        '<div class="hero-search">'
        '<span class="search-icon">🔍</span>'
        '<input type="text" class="hero-search-input" id="heroSearchInput" placeholder="搜索排行榜..." autocomplete="off">'
        '</div>'
        '</div>'
        '<div class="section-grid">' + sections_html + '</div>'
    )

    full_html = generate_page('排行榜中心', index_content, template, is_index=True)
    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(full_html)
    print('✓ 生成首页: docs/index.html')

def process_md_files():
    template = read_template()
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if not file.endswith('.md'):
                continue
            md_path = os.path.join(root, file)
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            title = extract_title(md_content)
            html_content = md_to_html(md_content)
            full_html = generate_page(title, html_content, template, is_index=False)
            relative_path = os.path.relpath(md_path, CONTENT_DIR)
            output_path = os.path.join(OUTPUT_DIR, 'content', relative_path.replace('.md', '.html'))
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
            print('✓ 转换: ' + md_path + ' -> ' + output_path)

def copy_static_files():
    import shutil
    if os.path.exists('content/css'):
        for file in os.listdir('content/css'):
            src = os.path.join('content/css', file)
            dst = os.path.join(OUTPUT_DIR, 'css', file)
            shutil.copy2(src, dst)
            print('✓ 复制: ' + src + ' -> ' + dst)
    if os.path.exists('content/js'):
        for file in os.listdir('content/js'):
            src = os.path.join('content/js', file)
            dst = os.path.join(OUTPUT_DIR, 'js', file)
            shutil.copy2(src, dst)
            print('✓ 复制: ' + src + ' -> ' + dst)
    if os.path.exists('content/images'):
        os.makedirs(os.path.join(OUTPUT_DIR, 'images'), exist_ok=True)
        for file in os.listdir('content/images'):
            src = os.path.join('content/images', file)
            dst = os.path.join(OUTPUT_DIR, 'images', file)
            shutil.copy2(src, dst)
            print('✓ 复制: ' + src + ' -> ' + dst)

if __name__ == '__main__':
    print('开始构建...')
    print('=' * 50)
    generate_index()
    process_md_files()
    copy_static_files()
    print('=' * 50)
    print('构建完成！')
    print('输出目录: ' + OUTPUT_DIR + '/')
