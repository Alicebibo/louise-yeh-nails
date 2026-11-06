# 產生發佈用 publish.html：圖片內嵌成 base64、拿掉外層 html/head/body
import re, base64
s = open('index.html', encoding='utf-8').read()
s = re.sub(r'"(works/[^"]+\.jpg)"', lambda m: '"data:image/jpeg;base64,' + base64.b64encode(open(m.group(1), 'rb').read()).decode() + '"', s)
s = re.sub(r'"(audio/[^"]+\.mp3)"', lambda m: '"data:audio/mpeg;base64,' + base64.b64encode(open(m.group(1), 'rb').read()).decode() + '"', s)
s = re.sub(r'<!doctype html>\s*<html[^>]*>\s*<head>\s*', '', s, flags=re.I)
s = re.sub(r'<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', '', s)
s = s.replace('</head>\n<body>\n', '').replace('</body>\n</html>', '')
s = s.replace('.reveal{opacity:0;transform:translateY(18px)', '.reveal{opacity:1;transform:translateY(18px)')
open('publish.html', 'w', encoding='utf-8').write(s)
print('publish.html', len(s))
