import os
from pathlib import Path
from datetime import datetime

def create_index_html():
    blog_dir = Path.cwd() / 'blog' / 'posts'
    html_files = list(blog_dir.rglob('*.html'))
    
    posts = []
    for html_file in html_files:
        parts = html_file.relative_to(blog_dir).parts
        if len(parts) >= 3 and all(p.isdigit() for p in parts[:3]):
            date = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
            url = '/' + str(html_file.relative_to(Path.cwd())).replace('\\', '/')
            posts.append({
                'date': date,
                'url': url,
                'title': html_file.stem.replace('_', ' ').title()
            })
    
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Index</title>
    <style>
        body {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: system-ui, -apple-system, sans-serif;
            line-height: 1.6;
        }
        .post {
            margin-bottom: 1em;
        }
        .post-date {
            color: #666;
            font-size: 0.9em;
        }
        a {
            color: #3182ce;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>
"""
    
    for post in posts:
        date_str = post['date'].strftime('%B %d, %Y')
        html += f"""    <div class="post">
        <span class="post-date">{date_str}</span>
        <a href="{post['url']}">{post['title']}</a>
    </div>
"""
    
    html += """</body>
</html>"""
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Created index.html with {len(posts)} posts")

if __name__ == "__main__":
    create_index_html()