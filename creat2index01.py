#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import random
import json
import hashlib
from datetime import datetime
from pathlib import Path

def generate_color_from_path(path):
    """根据目录路径生成确定性颜色"""
    # 使用MD5哈希确保相同路径得到相同颜色
    hash_obj = hashlib.md5(path.encode('utf-8'))
    # 取哈希值的前6个字符作为颜色
    color_hex = hash_obj.hexdigest()[:6]
    return f'#{color_hex}'

def generate_index():
    """
    生成albums目录的索引页面，只显示包含index.html的目录
    """
    try:
        # 获取当前时间
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 定义路径
        current_dir = Path(__file__).parent
        albums_dir = current_dir / "ablums"
        output_file = current_dir / "index.html"
        
        # 验证必要的目录
        if not albums_dir.exists():
            print(f"错误: albums目录不存在: {albums_dir}")
            return False
        
        # 获取albums目录结构（递归），只包含有index.html的目录
        albums_structure = get_valid_albums_structure(albums_dir, current_dir)
        
        # 为每个目录查找封面图片
        find_covers_for_structure(albums_structure, albums_dir, current_dir)
        
        # 为每个目录生成颜色
        assign_colors_to_structure(albums_structure)
        
        # 生成HTML内容
        html_content = generate_html(today, albums_structure, current_dir)
        
        # 写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"成功生成索引页面: {output_file}")
        print(f"有效目录数量: {count_directories(albums_structure)}")
        print(f"生成时间: {today}")
        
        return True
        
    except Exception as e:
        print(f"生成索引时出错: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return False

def assign_colors_to_structure(structure):
    """为目录结构中的每个目录分配颜色"""
    for item in structure:
        # 根据路径生成确定性颜色
        item['color'] = generate_color_from_path(item['path'])
        
        # 递归处理子目录
        if item['subdirs']:
            assign_colors_to_structure(item['subdirs'])

def get_valid_albums_structure(directory, base_dir):
    """递归获取目录结构，只返回包含index.html的目录"""
    structure = []
    
    for item in sorted(directory.iterdir()):
        if item.is_dir():
            # 检查是否有index.html
            has_index = (item / "index.html").exists()
            
            # 获取有效的子目录（递归）
            subdirs = get_valid_albums_structure(item, base_dir)
            
            # 计算相对路径（相对于base_dir）
            rel_path = item.relative_to(base_dir).as_posix()
            
            # 只有有index.html或有有效子目录的目录才包含在结构中
            if has_index or subdirs:
                structure.append({
                    'name': item.name,
                    'path': rel_path,
                    'has_index': has_index,
                    'subdirs': subdirs,
                    'has_subdirs': len(subdirs) > 0,
                    'cover': None,  # 稍后填充
                    'color': None   # 稍后分配
                })
    
    return structure

def find_covers_for_structure(structure, current_dir, base_dir):
    """为目录结构中的每个目录查找封面图片"""
    for item in structure:
        item_dir = base_dir / item['path']
        
        # 查找封面图片
        cover_path = find_cover_image(item_dir, base_dir)
        if cover_path:
            item['cover'] = cover_path
        
        # 递归处理子目录
        if item['subdirs']:
            find_covers_for_structure(item['subdirs'], item_dir, base_dir)

def find_cover_image(directory, base_dir):
    """查找目录中的封面图片"""
    # 支持的图片格式
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg']
    
    # 首先查找名为cover的图片（不区分大小写）
    for ext in image_extensions:
        for pattern in [f'cover{ext}', f'Cover{ext}', f'COVER{ext}']:
            cover_file = directory / pattern
            if cover_file.exists():
                # 计算相对于base_dir的相对路径
                return cover_file.relative_to(base_dir).as_posix()
    
    # 如果找不到cover，查找该目录下的所有图片
    image_files = []
    for ext in image_extensions:
        image_files.extend(directory.glob(f'*{ext}'))
        image_files.extend(directory.glob(f'*{ext.upper()}'))
    
    # 排除子目录中的图片
    image_files = [f for f in image_files if f.is_file()]
    
    # 随机选择一张图片
    if image_files:
        img = random.choice(image_files)
        return img.relative_to(base_dir).as_posix()
    
    return None

def count_directories(structure):
    """统计目录数量"""
    count = 0
    for item in structure:
        count += 1  # 当前目录
        count += count_directories(item['subdirs'])
    return count

def generate_html(today, structure, base_dir):
    """生成完整的HTML内容"""
    
    # 将结构转换为JSON用于JavaScript
    structure_json = json.dumps(structure, ensure_ascii=False)
    
    # 生成安全的目录结构HTML
    list_html = generate_list_html(structure, base_dir)
    grid_html = generate_grid_html(structure, base_dir)
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Index</title>
    {generate_css()}
</head>
<body>
    <div class="container">
        <header class="page-header">
            <div class="header-content">
                <h1>Index</h1>
                <p class="subtitle">包含index.html的目录浏览</p>
                
                <div class="info-bar">
                    <div class="info-left">
                        <div class="date-info">
                            <svg class="icon"><use href="#icon-calendar"></use></svg>
                            <span class="desktop-text">更新: {today}</span>
                            <span class="mobile-text">{today.split()[0]}</span>
                        </div>
                        <div class="count-info">
                            <svg class="icon"><use href="#icon-folder"></use></svg>
                            <span class="desktop-text">有效目录: <span id="dir-count">{count_directories(structure)}</span></span>
                            <span class="mobile-text"><span id="dir-count-mobile">{count_directories(structure)}</span> 个</span>
                        </div>
                    </div>
                    
                    <div class="info-right">
                        <div class="controls">
                            <div class="control-group">
                                <button class="control-btn" id="view-toggle" title="切换视图">
                                    <svg class="icon"><use href="#icon-list"></use></svg>
                                    <span class="control-label desktop-text">列表</span>
                                    <span class="control-label mobile-text">视图</span>
                                </button>
                            </div>
                            
                            <div class="control-group">
                                <button class="control-btn" id="theme-toggle" title="切换主题">
                                    <svg class="icon"><use href="#icon-moon"></use></svg>
                                    <span class="control-label desktop-text">深色</span>
                                    <span class="control-label mobile-text">主题</span>
                                </button>
                            </div>
                            
                            <div class="control-group">
                                <button class="control-btn" id="expand-toggle" title="展开/折叠所有">
                                    <svg class="icon"><use href="#icon-expand"></use></svg>
                                    <span class="control-label desktop-text">展开</span>
                                    <span class="control-label mobile-text">折叠</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
        </header>
        
        <main class="main-content">
            <div class="content-view list-view active" id="list-view">
                {list_html}
            </div>
            
            <div class="content-view grid-view" id="grid-view">
                {grid_html}
            </div>
        </main>
        
        <footer class="page-footer">
            <p>© {datetime.now().year} Index索引 • 最后更新: {today}</p>
            <div class="footer-info">
                <span class="desktop-text">点击目录跳转 • 空格键展开/折叠 • ESC返回上一级</span>
                <span class="mobile-text">点击跳转 • 手势操作</span>
            </div>
        </footer>
    </div>
    
    <!-- SVG图标定义 -->
    {generate_svg_icons()}
    
    <script>
        // 目录结构数据
        const albumsStructure = {structure_json};
        
        // 状态变量
        let currentView = 'list'; // 'list' 或 'grid'
        let currentTheme = 'dark'; // 'light', 'dark', 'auto'
        let isAllExpanded = false;
        
        // 初始化函数
        document.addEventListener('DOMContentLoaded', function() {{
            initControls();
            initKeyboardNavigation();
            updateStats();
            
            // 从本地存储恢复设置
            restoreSettings();
            
            // 更新移动端计数显示
            updateMobileStats();
        }});
        
        // 初始化控制功能
        function initControls() {{
            // 视图切换按钮
            const viewToggle = document.getElementById('view-toggle');
            viewToggle.addEventListener('click', function() {{
                toggleView();
            }});
            
            // 主题切换按钮
            const themeToggle = document.getElementById('theme-toggle');
            themeToggle.addEventListener('click', function() {{
                toggleTheme();
            }});
            
            // 展开/折叠切换按钮
            const expandToggle = document.getElementById('expand-toggle');
            expandToggle.addEventListener('click', function() {{
                toggleExpandAll();
            }});
            
            // 折叠/展开按钮事件委托
            document.addEventListener('click', function(e) {{
                if (e.target.closest('.toggle-btn')) {{
                    const toggleBtn = e.target.closest('.toggle-btn');
                    const item = toggleBtn.closest('.directory-item');
                    toggleDirectory(item);
                    e.stopPropagation(); // 防止触发目录跳转
                }}
                
                // 卡片视图子目录折叠/展开按钮
                if (e.target.closest('.subdir-toggle-btn')) {{
                    const toggleBtn = e.target.closest('.subdir-toggle-btn');
                    const cardItem = toggleBtn.closest('.card-item');
                    toggleCardSubdirs(cardItem);
                    e.stopPropagation();
                }}
            }});
            
            // 目录项点击跳转
            document.addEventListener('click', function(e) {{
                // 查找最近的目录项
                const directoryItem = e.target.closest('.directory-item');
                const cardContent = e.target.closest('.card-content');
                const cardCover = e.target.closest('.card-cover');
                const subdirItem = e.target.closest('.subdir-item');
                const subdirItemInList = e.target.closest('.directory-sublist .subdir-item');
                
                if (directoryItem && !e.target.closest('.toggle-btn') && !e.target.closest('.directory-actions')) {{
                    const hasIndex = directoryItem.getAttribute('data-has-index') === 'true';
                    if (hasIndex) {{
                        const path = directoryItem.getAttribute('data-path');
                        window.open('./' + path + '/index.html', '_blank');
                    }}
                }}
                
                // 卡片内容区域或封面区域点击跳转
                if ((cardContent || cardCover) && !e.target.closest('.subdir-item') && !e.target.closest('.subdir-toggle-btn')) {{
                    // 获取卡片元素
                    const cardItem = (cardContent || cardCover).closest('.card-item');
                    const hasIndex = cardItem.getAttribute('data-has-index') === 'true';
                    if (hasIndex) {{
                        const path = cardItem.getAttribute('data-path');
                        window.open('./' + path + '/index.html', '_blank');
                    }}
                }}
                
                // 卡片视图中的子目录点击
                if (subdirItem && !subdirItemInList) {{
                    const hasIndex = subdirItem.getAttribute('data-has-index') === 'true';
                    if (hasIndex) {{
                        const path = subdirItem.getAttribute('data-path');
                        window.open('./' + path + '/index.html', '_blank');
                    }}
                }}
            }});
        }}
        
        // 切换视图
        function toggleView() {{
            const viewToggle = document.getElementById('view-toggle');
            const viewIcon = viewToggle.querySelector('.icon use');
            const desktopLabel = viewToggle.querySelector('.control-label.desktop-text');
            const mobileLabel = viewToggle.querySelector('.control-label.mobile-text');
            
            if (currentView === 'list') {{
                currentView = 'grid';
                switchView('grid');
                viewIcon.setAttribute('href', '#icon-grid');
                desktopLabel.textContent = '卡片';
                mobileLabel.textContent = '卡片';
            }} else {{
                currentView = 'list';
                switchView('list');
                viewIcon.setAttribute('href', '#icon-list');
                desktopLabel.textContent = '列表';
                mobileLabel.textContent = '列表';
            }}
            localStorage.setItem('preferred-view', currentView);
        }}
        
        // 切换主题
        function toggleTheme() {{
            const themeToggle = document.getElementById('theme-toggle');
            const themeIcon = themeToggle.querySelector('.icon use');
            const desktopLabel = themeToggle.querySelector('.control-label.desktop-text');
            const mobileLabel = themeToggle.querySelector('.control-label.mobile-text');
            
            const themes = ['light', 'dark'];
            const icons = ['#icon-sun', '#icon-moon'];
            const desktopLabels = ['浅色', '深色'];
            const mobileLabels = ['浅色', '深色'];
            
            const currentIndex = themes.indexOf(currentTheme);
            const nextIndex = (currentIndex + 1) % themes.length;
            
            currentTheme = themes[nextIndex];
            switchTheme(currentTheme);
            
            themeIcon.setAttribute('href', icons[nextIndex]);
            desktopLabel.textContent = desktopLabels[nextIndex];
            mobileLabel.textContent = mobileLabels[nextIndex];
            
            localStorage.setItem('preferred-theme', currentTheme);
        }}
        
        // 切换展开/折叠所有
        function toggleExpandAll() {{
            const expandToggle = document.getElementById('expand-toggle');
            const expandIcon = expandToggle.querySelector('.icon use');
            const desktopLabel = expandToggle.querySelector('.control-label.desktop-text');
            const mobileLabel = expandToggle.querySelector('.control-label.mobile-text');
            
            if (isAllExpanded) {{
                collapseAll();
                expandIcon.setAttribute('href', '#icon-expand');
                desktopLabel.textContent = '展开';
                mobileLabel.textContent = '展开';
            }} else {{
                expandAll();
                expandIcon.setAttribute('href', '#icon-collapse');
                desktopLabel.textContent = '折叠';
                mobileLabel.textContent = '折叠';
            }}
            isAllExpanded = !isAllExpanded;
        }}
        
        // 切换视图
        function switchView(view) {{
            document.querySelectorAll('.content-view').forEach(el => el.classList.remove('active'));
            document.getElementById(view + '-view').classList.add('active');
            document.body.setAttribute('data-view', view);
        }}
        
        // 切换主题
        function switchTheme(theme) {{
            if (theme === 'auto') {{
                document.body.removeAttribute('data-theme');
            }} else {{
                document.body.setAttribute('data-theme', theme);
            }}
        }}
        
        // 展开所有目录
        function expandAll() {{
            document.querySelectorAll('.directory-item').forEach(item => {{
                item.classList.add('expanded');
                const sublist = item.querySelector('.directory-sublist');
                if (sublist) sublist.style.maxHeight = sublist.scrollHeight + 'px';
            }});
            
            // 展开所有卡片视图的子目录
            document.querySelectorAll('.card-item').forEach(item => {{
                item.classList.add('subdirs-expanded');
                const sublist = item.querySelector('.card-subdirs');
                if (sublist) sublist.style.maxHeight = sublist.scrollHeight + 'px';
            }});
            updateStats();
            updateMobileStats();
        }}
        
        // 折叠所有目录
        function collapseAll() {{
            document.querySelectorAll('.directory-item').forEach(item => {{
                item.classList.remove('expanded');
                const sublist = item.querySelector('.directory-sublist');
                if (sublist) sublist.style.maxHeight = '0';
            }});
            
            // 折叠所有卡片视图的子目录
            document.querySelectorAll('.card-item').forEach(item => {{
                item.classList.remove('subdirs-expanded');
                const sublist = item.querySelector('.card-subdirs');
                if (sublist) sublist.style.maxHeight = '0';
            }});
            updateStats();
            updateMobileStats();
        }}
        
        // 切换单个目录的展开状态
        function toggleDirectory(item) {{
            const isExpanded = item.classList.contains('expanded');
            const sublist = item.querySelector('.directory-sublist');
            
            if (isExpanded) {{
                item.classList.remove('expanded');
                if (sublist) sublist.style.maxHeight = '0';
            }} else {{
                item.classList.add('expanded');
                if (sublist) sublist.style.maxHeight = sublist.scrollHeight + 'px';
            }}
            updateStats();
            updateMobileStats();
        }}
        
        // 切换卡片视图子目录的展开状态
        function toggleCardSubdirs(cardItem) {{
            const isExpanded = cardItem.classList.contains('subdirs-expanded');
            const sublist = cardItem.querySelector('.card-subdirs');
            const toggleBtn = cardItem.querySelector('.subdir-toggle-btn');
            
            if (isExpanded) {{
                cardItem.classList.remove('subdirs-expanded');
                if (sublist) sublist.style.maxHeight = '0';
                if (toggleBtn) {{
                    toggleBtn.innerHTML = '<svg class="icon"><use href="#icon-chevron-right"></use></svg><span class="subdir-toggle-count">' + (cardItem.querySelector('.subdir-toggle-count')?.textContent || '') + '</span>';
                }}
            }} else {{
                cardItem.classList.add('subdirs-expanded');
                if (sublist) sublist.style.maxHeight = sublist.scrollHeight + 'px';
                if (toggleBtn) {{
                    toggleBtn.innerHTML = '<svg class="icon"><use href="#icon-collapse"></use></svg><span class="subdir-toggle-count">' + (cardItem.querySelector('.subdir-toggle-count')?.textContent || '') + '</span>';
                }}
            }}
        }}
        
        // 更新统计信息
        function updateStats() {{
            const expandedCount = document.querySelectorAll('.directory-item.expanded').length;
            const totalCount = document.querySelectorAll('.directory-item[data-has-subs="true"]').length;
            const allCount = document.querySelectorAll('.directory-item').length;
            document.getElementById('dir-count').textContent = allCount + ' (' + expandedCount + '/' + totalCount + ' 展开)';
        }}
        
        // 更新移动端统计信息
        function updateMobileStats() {{
            const expandedCount = document.querySelectorAll('.directory-item.expanded').length;
            const totalCount = document.querySelectorAll('.directory-item[data-has-subs="true"]').length;
            const allCount = document.querySelectorAll('.directory-item').length;
            document.getElementById('dir-count-mobile').textContent = allCount + ' (' + expandedCount + '/' + totalCount + ')';
        }}
        
        // 从本地存储恢复设置
        function restoreSettings() {{
            // 恢复视图设置
            const savedView = localStorage.getItem('preferred-view');
            if (savedView) {{
                currentView = savedView;
                switchView(savedView);
                const viewToggle = document.getElementById('view-toggle');
                const viewIcon = viewToggle.querySelector('.icon use');
                const desktopLabel = viewToggle.querySelector('.control-label.desktop-text');
                const mobileLabel = viewToggle.querySelector('.control-label.mobile-text');
                
                if (savedView === 'grid') {{
                    viewIcon.setAttribute('href', '#icon-grid');
                    desktopLabel.textContent = '卡片';
                    mobileLabel.textContent = '卡片';
                }} else {{
                    viewIcon.setAttribute('href', '#icon-list');
                    desktopLabel.textContent = '列表';
                    mobileLabel.textContent = '列表';
                }}
            }}
            
            // 恢复主题设置
            const savedTheme = localStorage.getItem('preferred-theme');
            if (savedTheme) {{
                currentTheme = savedTheme;
                switchTheme(savedTheme);
                const themeToggle = document.getElementById('theme-toggle');
                const themeIcon = themeToggle.querySelector('.icon use');
                const desktopLabel = themeToggle.querySelector('.control-label.desktop-text');
                const mobileLabel = themeToggle.querySelector('.control-label.mobile-text');
                
                const themes = ['light', 'dark'];
                const icons = ['#icon-sun', '#icon-moon'];
                const desktopLabels = ['浅色', '深色'];
                const mobileLabels = ['浅色', '深色'];
                
                const index = themes.indexOf(savedTheme);
                if (index !== -1) {{
                    themeIcon.setAttribute('href', icons[index]);
                    desktopLabel.textContent = desktopLabels[index];
                    mobileLabel.textContent = mobileLabels[index];
                }}
            }}
        }}
        
        // 键盘导航
        function initKeyboardNavigation() {{
            document.addEventListener('keydown', function(e) {{
                const activeElement = document.activeElement;
                const isInput = activeElement.tagName === 'INPUT' || activeElement.tagName === 'TEXTAREA';
                
                if (isInput) return;
                
                switch(e.key) {{
                    case 'ArrowRight':
                        e.preventDefault();
                        if (activeElement.closest('.directory-item')) {{
                            const item = activeElement.closest('.directory-item');
                            if (!item.classList.contains('expanded')) {{
                                toggleDirectory(item);
                            }}
                        }}
                        break;
                    case 'ArrowLeft':
                        e.preventDefault();
                        if (activeElement.closest('.directory-item')) {{
                            const item = activeElement.closest('.directory-item');
                            if (item.classList.contains('expanded')) {{
                                toggleDirectory(item);
                            }}
                        }}
                        break;
                    case ' ':
                        e.preventDefault();
                        if (activeElement.closest('.directory-item')) {{
                            const item = activeElement.closest('.directory-item');
                            toggleDirectory(item);
                        }}
                        break;
                    case 'Enter':
                        e.preventDefault();
                        // 回车键打开当前选中的目录
                        const activeItem = document.querySelector('.directory-item:focus');
                        if (activeItem) {{
                            const hasIndex = activeItem.getAttribute('data-has-index') === 'true';
                            if (hasIndex) {{
                                const path = activeItem.getAttribute('data-path');
                                window.open('./' + path + '/index.html', '_blank');
                            }}
                        }}
                        break;
                    case 'Escape':
                        // 折叠当前目录
                        const expandedItem = document.querySelector('.directory-item.expanded');
                        if (expandedItem) {{
                            toggleDirectory(expandedItem);
                        }}
                        break;
                }}
            }});
        }}
    </script>
</body>
</html>'''
    
    return html

def generate_list_html(structure, base_dir, level=0):
    """生成列表视图HTML"""
    if not structure:
        return '<div class="empty-message">没有找到包含index.html的目录</div>'
    
    html_parts = []
    
    if level == 0:
        html_parts.append('<div class="directory-list">')
    
    for item in structure:
        has_subs = item['has_subdirs']
        has_index = item['has_index']
        
        # 确保路径中的特殊字符被正确转义
        path_escaped = item['path'].replace('"', '&quot;')
        name_escaped = item['name'].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        
        html_parts.append(f'''
        <div class="directory-item" data-has-subs="{str(has_subs).lower()}" data-has-index="{str(has_index).lower()}" data-path="{path_escaped}" data-level="{level}" tabindex="0">
            <div class="directory-header">
                {generate_toggle_button(has_subs)}
                <div class="directory-content">
                    {generate_cover_preview(item) if item['cover'] else generate_cover_placeholder(item)}
                    <div class="directory-info">
                        <h3 class="directory-name">{name_escaped}</h3>
                        <p class="directory-path">/{path_escaped.replace('ablums/', '')}</p>
                    </div>
                </div>
                <div class="directory-actions">
                    {generate_status_indicator(item)}
                </div>
            </div>
        ''')
        
        if has_subs and item['subdirs']:
            html_parts.append(f'<div class="directory-sublist" style="max-height: 0;">')
            html_parts.append(generate_list_html(item['subdirs'], base_dir, level + 1))
            html_parts.append('</div>')
        
        html_parts.append('</div>')
    
    if level == 0:
        html_parts.append('</div>')
    
    return ''.join(html_parts)

def generate_grid_html(structure, base_dir):
    """生成网格（卡片）视图HTML"""
    if not structure:
        return '<div class="empty-message">没有找到包含index.html的目录</div>'
    
    html_parts = ['<div class="card-grid">']
    
    for item in structure:
        has_index = item['has_index']
        has_subs = item['has_subdirs']
        
        # 确保路径中的特殊字符被正确转义
        path_escaped = item['path'].replace('"', '&quot;')
        name_escaped = item['name'].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        
        html_parts.append(f'''
        <div class="card-item" data-has-subs="{str(has_subs).lower()}" data-has-index="{str(has_index).lower()}" data-path="{path_escaped}" tabindex="0">
            <div class="card-cover">
                {generate_cover_image_html(item)}
                <div class="card-overlay">
                    {generate_status_badge(item)}
                </div>
            </div>
            <div class="card-content">
                <div class="card-info">
                    <h3 class="card-title">{name_escaped}</h3>
                    <p class="card-path">./{path_escaped.replace('ablums/', '')}</p>
                    {generate_card_subdir_toggle(item) if has_subs else ''}
                </div>
            </div>
            {generate_grid_subdirs(item) if has_subs else ''}
        </div>
        ''')
    
    html_parts.append('</div>')
    return ''.join(html_parts)

def generate_toggle_button(has_subs):
    """生成折叠/展开按钮"""
    if not has_subs:
        return '<span class="toggle-btn empty"></span>'
    
    return '''
    <button class="toggle-btn" aria-label="展开/折叠">
        <svg class="icon"><use href="#icon-chevron-right"></use></svg>
    </button>
    '''

def generate_card_subdir_toggle(item):
    """生成卡片视图的子目录折叠/展开按钮"""
    if not item['has_subdirs']:
        return ''
    
    count = len(item['subdirs'])
    return f'''
    <button class="subdir-toggle-btn" aria-label="展开/折叠子目录">
        <svg class="icon"><use href="#icon-chevron-right"></use></svg>
        <span class="subdir-toggle-count">{count}</span>
    </button>
    '''

def generate_cover_preview(item):
    """生成封面预览"""
    if not item['cover']:
        return generate_cover_placeholder(item)
    
    return f'''
    <div class="cover-preview">
        <img src="./{item['cover']}" alt="封面" loading="lazy">
    </div>
    '''

def generate_cover_placeholder(item):
    """生成封面占位符"""
    color = item.get('color', '#4361ee')  # 默认颜色
    return f'''
    <div class="cover-placeholder" style="background-color: {color};">
        <svg class="icon"><use href="#icon-folder"></use></svg>
    </div>
    '''

def generate_cover_image_html(item):
    """生成封面图片HTML"""
    if item['cover']:
        # 确保路径正确
        cover_path = f"./{item['cover']}"
        return f'<img src="{cover_path}" alt="封面" loading="lazy">'
    else:
        # 使用占位符，使用目录的颜色
        color = item.get('color', '#4361ee')
        return f'''
        <div class="cover-placeholder" style="background-color: {color};">
            <svg class="icon"><use href="#icon-folder"></use></svg>
        </div>
        '''

def generate_status_indicator(item):
    """生成状态指示器"""
    if item['has_index']:
        return '<span class="status-indicator has-index" title="点击跳转到index.html"></span>'
    else:
        return '<span class="status-indicator no-index" title="无index.html"></span>'

def generate_status_badge(item):
    """生成状态徽章"""
    if item['has_index']:
        return '<span class="status-badge has-index"></span>'
    else:
        return '<span class="status-badge no-index"></span>'

def generate_subdir_count(item):
    """生成子目录数量显示"""
    if not item['has_subdirs']:
        return ''
    
    count = len(item['subdirs'])
    return f'<span class="subdir-count">{count}</span>'

def generate_grid_subdirs(item):
    """生成网格视图的子目录列表"""
    if not item['has_subdirs'] or not item['subdirs']:
        return ''
    
    html_parts = ['<div class="card-subdirs" style="max-height: 0;">']
    
    # 只显示前3个子目录
    for subdir in item['subdirs'][:3]:
        has_index = subdir['has_index']
        
        # 确保子目录路径正确转义
        subdir_path_escaped = subdir['path'].replace('"', '&quot;')
        subdir_name_escaped = subdir['name'].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        
        html_parts.append(f'''
        <div class="subdir-item" data-has-index="{str(has_index).lower()}" data-path="{subdir_path_escaped}" tabindex="0">
            <span class="subdir-icon">{generate_svg_icon('folder')}</span>
            <span class="subdir-name">{subdir_name_escaped}</span>
        </div>
        ''')
    
    # 如果还有更多子目录，显示"更多"
    if len(item['subdirs']) > 3:
        html_parts.append(f'''
        <div class="more-subdirs">
            还有 {len(item['subdirs']) - 3} 个...
        </div>
        ''')
    
    html_parts.append('</div>')
    return ''.join(html_parts)

def generate_svg_icon(icon_type):
    """生成SVG图标引用"""
    if icon_type == 'folder':
        return '<svg class="icon"><use href="#icon-folder"></use></svg>'
    return ''

def generate_svg_icons():
    """生成SVG图标定义"""
    return '''
    <svg style="display: none;">
        <defs>
            <!-- 文件夹图标 -->
            <symbol id="icon-folder" viewBox="0 0 24 24">
                <path d="M10,4H4C2.9,4,2,4.9,2,6v12c0,1.1,0.9,2,2,2h16c1.1,0,2-0.9,2-2V8c0-1.1-0.9-2-2-2h-8L10,4z" 
                        fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </symbol>
            
            <!-- 日历图标 -->
            <symbol id="icon-calendar" viewBox="0 0 24 24">
                <path d="M19,4h-1V2h-2v2H8V2H6v2H5C3.9,4,3,4.9,3,6v14c0,1.1,0.9,2,2,2h14c1.1,0,2-0.9,2-2V6C21,4.9,20.1,4,19,4z M19,20H5V10h14V20z"/>
            </symbol>
            
            <!-- 列表视图图标 -->
            <symbol id="icon-list" viewBox="0 0 24 24">
                <path d="M3,13h2v-2H3V13z M3,17h2v-2H3V17z M3,9h2V7H3V9z M7,13h14v-2H7V13z M7,17h14v-2H7V17z M7,7v2h14V7H7z"/>
            </symbol>
            
            <!-- 网格视图图标 -->
            <symbol id="icon-grid" viewBox="0 0 24 24">
                <path d="M4,8h4V4H4V8z M10,20h4v-4h-4V20z M4,20h4v-4H4V20z M4,14h4v-4H4V14z M10,14h4v-4h-4V14z M16,4v4h4V4H16z M10,8h4V4h-4V8z M16,14h4v-4h-4V14z M16,20h4v-4h-4V20z"/>
            </symbol>
            
            <!-- 太阳图标（浅色主题） -->
            <symbol id="icon-sun" viewBox="0 0 24 24">
                <path d="M12,9c1.65,0,3,1.35,3,3s-1.35,3-3,3s-3-1.35-3-3S10.35,9,12,9z M12,7c-2.76,0-5,2.24-5,5s2.24,5,5,5s5-2.24,5-5S14.76,7,12,7zM2,13h2c0.55,0,1-0.45,1-1s-0.45-1-1-1H2c-0.55,0-1,0.45-1,1S1.45,13,2,13z M20,13h2c0.55,0,1-0.45,1-1s-0.45-1-1-1h-2c-0.55,0-1,0.45-1,1S19.45,13,20,13z M11,2v2c0,0.55,0.45,1,1,1s1-0.45,1-1V2c0-0.55-0.45-1-1-1S11,1.45,11,2z M11,20v2c0,0.55,0.45,1,1,1s1-0.45,1-1v-2c0-0.55-0.45-1-1-1S11,19.45,11,20z M5.99,4.58c-0.39-0.39-1.03-0.39-1.41,0c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0s0.39-1.03,0-1.41L5.99,4.58z M18.36,16.95c-0.39-0.39-1.03-0.39-1.41,0c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0c0.39-0.39,0.39-1.03,0-1.41L18.36,16.95z M19.42,5.99c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06c-0.39,0.39-0.39,1.03,0,1.41s1.03,0.39,1.41,0L19.42,5.99z M7.05,18.36c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06c-0.39,0.39-0.39,1.03,0,1.41s1.03,0.39,1.41,0L7.05,18.36z"/>
            </symbol>
            
            <!-- 月亮图标（深色主题） -->
            <symbol id="icon-moon" viewBox="0 0 24 24">
                <path d="M12,3c-4.97,0-9,4.03-9,9s4.03,9,9,9s9-4.03,9-9c0-0.46-0.04-0.92-0.1-1.36c-0.98,1.37-2.58,2.26-4.4,2.26c-2.98,0-5.4-2.42-5.4-5.4c0-1.81,0.89-3.42,2.26-4.4C12.92,3.04,12.46,3,12,3L12,3z"/>
            </symbol>
            
            <!-- 自动主题图标 -->
            <symbol id="icon-auto" viewBox="0 0 24 24">
                <path d="M12,2C6.48,2,2,6.48,2,12s4.48,10,10,10s10-4.48,10-10S17.52,2,12,2z M12,20c-4.41,0-8-3.59-8-8s3.59-8,8-8s8,3.59,8,8S16.41,20,12,20z M12,19.5c-4.14,0-7.5-3.36-7.5-7.5c0-4.14,3.36-7.5,7.5-7.5V19.5z"/>
            </symbol>
            
            <!-- 展开图标 -->
            <symbol id="icon-expand" viewBox="0 0 24 24">
                <path d="M16.59,8.59L12,13.17L7.41,8.59L6,10l6,6l6-6L16.59,8.59z"/>
            </symbol>
            
            <!-- 折叠图标 -->
            <symbol id="icon-collapse" viewBox="0 0 24 24">
                <path d="M12,8l-6,6l1.41,1.41L12,10.83l4.59,4.58L18,14L12,8z"/>
            </symbol>
            
            <!-- 右箭头图标 -->
            <symbol id="icon-chevron-right" viewBox="0 0 24 24">
                <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
            </symbol>
        </defs>
    </svg>
    '''

def generate_css():
    """生成完整的CSS样式"""
    return '''
    <style>
        :root {
            --primary: #4361ee;
            --primary-light: #eef2ff;
            --primary-dark: #3a0ca3;
            --secondary: #7209b7;
            --accent: #f72585;
            --light: #f8f9fa;
            --dark: #2d3748;
            --gray: #718096;
            --gray-light: #e2e8f0;
            --gray-dark: #4a5568;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --border-radius: 5px;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* 浅色主题 */
        body[data-theme="light"] {
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --border-color: #e2e8f0;
            --card-bg: #ffffff;
            --hover-bg: #f1f5f9;
        }
        
        /* 深色主题 */
        body[data-theme="dark"] {
            --bg-primary: #1e293b;
            --bg-secondary: #0f172a;
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --border-color: #334155;
            --card-bg: #334155;
            --hover-bg: #2d3748;
        }
        
        /* 自动主题使用系统设置 */
        @media (prefers-color-scheme: dark) {
            body:not([data-theme]) {
                --bg-primary: #1e293b;
                --bg-secondary: #0f172a;
                --text-primary: #f1f5f9;
                --text-secondary: #cbd5e1;
                --border-color: #334155;
                --card-bg: #334155;
                --hover-bg: #2d3748;
            }
        }
        
        @media (prefers-color-scheme: light) {
            body:not([data-theme]) {
                --bg-primary: #ffffff;
                --bg-secondary: #f8fafc;
                --text-primary: #1e293b;
                --text-secondary: #64748b;
                --border-color: #e2e8f0;
                --card-bg: #ffffff;
                --hover-bg: #f1f5f9;
            }
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html {
            font-size: 16px;
            scroll-behavior: smooth;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-primary);
            background-color: var(--bg-secondary);
            transition: var(--transition);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }
        
        /* 头部样式 */
        .page-header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            border-radius: 0 0 var(--border-radius) var(--border-radius);
            padding: 1rem;
            margin: 0;
            box-shadow: var(--shadow-lg);
        }
        
        .header-content {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        h1 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            letter-spacing: -0.5px;
        }
        
        .subtitle {
            font-size: 1.1rem;
            opacity: 0.9;
            margin-bottom: 1.5rem;
        }
        
        /* 信息栏响应式布局 */
        .info-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: var(--border-radius);
            padding: 1rem;
            margin-bottom: 0.5rem;
            flex-wrap: wrap;
            gap: 1rem;
        }
        
        .info-left {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            flex-wrap: wrap;
        }
        
        .info-right {
            display: flex;
            align-items: center;
        }
        
        .date-info, .count-info {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.95rem;
        }
        
        .desktop-text {
            display: inline;
        }
        
        .mobile-text {
            display: none;
        }
        
        .icon {
            width: 1.25rem;
            height: 1.25rem;
            fill: currentColor;
            flex-shrink: 0;
        }
        
        /* 控制栏 */
        .controls {
            display: flex;
            gap: 0.75rem;
            flex-wrap: nowrap;
        }
        
        .control-group {
            display: flex;
        }
        
        .control-btn {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            border-radius: 5px;
            color: white;
            cursor: pointer;
            padding: 0.75rem 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            transition: var(--transition);
            min-width: 100px;
            white-space: nowrap;
        }
        
        .control-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }
        
        .control-label {
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        /* 主内容区 */
        .main-content {
            padding: 1rem 0;
        }
        
        .content-view {
            display: none;
        }
        
        .content-view.active {
            display: block;
            animation: fadeIn 0.3s ease-out;
        }
        
        .empty-message {
            text-align: center;
            padding: 3rem;
            color: var(--text-secondary);
            font-size: 1.2rem;
            background: var(--bg-primary);
            border-radius: var(--border-radius);
            border: 1px solid var(--border-color);
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* 响应式设计 - 中等屏幕 (平板) */
        @media (max-width: 1024px) {
            .container {
                padding: 0 1.25rem;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            .info-bar {
                padding: 0.75rem;
                gap: 0.75rem;
            }
            
            .info-left {
                gap: 1rem;
            }
            
            .controls {
                gap: 0.5rem;
            }
            
            .control-btn {
                min-width: 90px;
                padding: 0.5rem 0.75rem;
            }
        }
        
        /* 响应式设计 - 小屏幕 (平板竖屏/大手机) */
        @media (max-width: 768px) {
            .container {
                padding: 0 1rem;
            }
            
            .page-header {
                margin: 0 -1rem 1.5rem -1rem;
                padding: 1.5rem 1rem;
                border-radius: 0;
            }
            
            h1 {
                font-size: 1.75rem;
            }
            
            .subtitle {
                font-size: 1rem;
            }
            
            .info-bar {
                flex-direction: column;
                align-items: stretch;
                gap: 1rem;
                padding: 1rem;
            }
            
            .info-left {
                justify-content: space-between;
                gap: 0.5rem;
            }
            
            .date-info, .count-info {
                font-size: 0.9rem;
            }
            
            .controls {
                width: 100%;
                justify-content: space-between;
            }
            
            .control-group {
                flex: 1;
            }
            
            .control-btn {
                min-width: 0;
                width: 100%;
                padding: 0.75rem;
            }
            
            .desktop-text {
                display: none;
            }
            
            .mobile-text {
                display: inline;
            }
            
            /* 网格视图调整 */
            .card-grid {
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 0.75rem;
            }
        }
        
        /* 响应式设计 - 超小屏幕 (手机) */
        @media (max-width: 480px) {
            h1 {
                font-size: 1.5rem;
            }
            
            .subtitle {
                font-size: 0.9rem;
            }
            
            .info-bar {
                padding: 0.75rem;
                gap: 0.75rem;
            }
            
            .info-left {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
                width: 100%;
            }
            
            .date-info, .count-info {
                width: 100%;
                justify-content: space-between;
            }
            
            .controls {
                flex-direction: column;
                gap: 0.5rem;
            }
            
            .control-group {
                width: 100%;
            }
            
            .control-btn {
                padding: 0.5rem;
                justify-content: flex-start;
            }
            
            /* 列表视图调整 */
            .directory-header {
                padding: 0.75rem;
            }
            
            .directory-content {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }
            
            .cover-preview,
            .cover-placeholder {
                align-self: flex-start;
            }
            
            /* 网格视图调整 */
            .card-grid {
                grid-template-columns: 1fr;
                gap: 0.5rem;
            }
            
            .card-cover {
                height: 180px;
            }
        }
        
        /* 响应式设计 - 极小屏幕 (小手机) */
        @media (max-width: 360px) {
            .container {
                padding: 0 0.75rem;
            }
            
            .page-header {
                padding: 1rem 0.75rem;
            }
            
            .info-bar {
                padding: 0.5rem;
            }
            
            .control-btn {
                padding: 0.5rem 0.25rem;
            }
            
            .control-label {
                font-size: 0.85rem;
            }
            
            .card-cover {
                height: 150px;
            }
        }
        
        /* 列表视图样式 */
        .directory-list {
            background: var(--bg-primary);
            border-radius: var(--border-radius);
            border: 1px solid var(--border-color);
            overflow: hidden;
        }
        
        .directory-item {
            border-bottom: 1px solid var(--border-color);
            cursor: pointer;
            transition: var(--transition);
            outline: none;
        }
        
        .directory-item:hover,
        .directory-item:focus {
            background-color: var(--hover-bg);
        }
        
        .directory-item[data-has-index="true"]:hover,
        .directory-item[data-has-index="true"]:focus {
            box-shadow: inset 0 0 0 2px var(--primary);
        }
        
        .directory-item:last-child {
            border-bottom: none;
        }
        
        .directory-header {
            display: flex;
            align-items: center;
            padding: 1rem;
        }
        
        .toggle-btn {
            background: none;
            border: none;
            width: 2rem;
            height: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: var(--text-secondary);
            transition: var(--transition);
            margin-right: 0.5rem;
            border-radius: 5px;
            z-index: 10;
        }
        
        .toggle-btn:hover {
            background: var(--bg-secondary);
            color: var(--text-primary);
        }
        
        .toggle-btn.empty {
            visibility: hidden;
        }
        
        .directory-item.expanded .toggle-btn svg {
            transform: rotate(90deg);
        }
        
        .directory-content {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex: 1;
        }
        
        .cover-preview {
            width: 3rem;
            height: 3rem;
            border-radius: 5px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            flex-shrink: 0;
        }
        
        .cover-preview img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .cover-placeholder {
            width: 3rem;
            height: 3rem;
            border-radius: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            flex-shrink: 0;
        }
        
        .directory-info {
            flex: 1;
        }
        
        .directory-name {
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }
        
        .directory-path {
            font-size: 0.875rem;
            color: var(--text-secondary);
            font-family: 'Monaco', 'Consolas', monospace;
        }
        
        .directory-actions {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .status-indicator {
            width: 10px;
            height: 10px;
            border-radius: 5px;
            display: inline-block;
        }
        
        .status-indicator.has-index {
            background-color: var(--success);
            box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.3);
        }
        
        .status-indicator.no-index {
            background-color: var(--gray);
            box-shadow: 0 0 0 2px rgba(113, 128, 150, 0.3);
        }
        
        .directory-sublist {
            overflow: hidden;
            transition: max-height 0.3s ease-out;
            background-color: var(--bg-secondary);
        }
        
        .directory-item[data-level="1"] .directory-header {
            padding-left: 3rem;
        }
        
        .directory-item[data-level="2"] .directory-header {
            padding-left: 4.5rem;
        }
        
        .directory-item[data-level="3"] .directory-header {
            padding-left: 6rem;
        }
        
        /* 卡片视图样式 */
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }
        
        .card-item {
            background: var(--card-bg);
            border-radius: var(--border-radius);
            border: 1px solid var(--border-color);
            overflow: hidden;
            transition: var(--transition);
            cursor: pointer;
            outline: none;
        }
        
        .card-item:hover,
        .card-item:focus {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }
        
        .card-item[data-has-index="true"]:hover,
        .card-item[data-has-index="true"]:focus {
            border-color: var(--primary);
        }
        
        .card-cover {
            position: relative;
            overflow: hidden;
            height: 200px;
        }
        
        .card-cover img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }
        
        .card-item:hover .card-cover img {
            transform: scale(1.05);
        }
        
        .cover-placeholder {
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .card-grid .cover-placeholder {
            width: 100%;
        }
        .cover-placeholder .icon {
            width: 3rem;
            height: 3rem;
            color: white;
        }
        
        .card-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.7) 0%, transparent 50%);
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            padding: 1rem;
            opacity: 0;
            transition: var(--transition);
        }
        
        .card-item:hover .card-overlay {
            opacity: 1;
        }
        
        .subdir-count {
            background: rgba(255, 255, 255, 0.9);
            color: var(--dark);
            padding: 0.1rem 0.5rem;
            border-radius: 5px;
            font-size: 0.875rem;
        }
        
        .status-badge {
            padding: 0.25rem 0.75rem;
            border-radius: 5px;
            font-size: 0.875rem;
            font-weight: 500;
        }
        
        .status-badge.has-index {
            background-color: var(--success);
            color: white;
            border-radius: 5px;
            width: 2px;
        }
        
        .status-badge.no-index {
            background-color: var(--gray);
            color: white;
            border-radius: 50%;
            width: 0.2rem;
        }
        
        .card-content {
            padding: 1rem 1.25rem;
            position: relative;
        }
        
        .card-info {
            flex: 1;
        }
        
        .card-title {
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
            font-size: 1.1rem;
        }
        
        .card-path {
            font-size: 0.875rem;
            color: var(--text-secondary);
            font-family: 'Monaco', 'Consolas', monospace;
        }
        
        .subdir-toggle-btn {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: none;
            border: none;
            width: 1.5rem;
            height: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: var(--text-secondary);
            transition: var(--transition);
            border-radius: 5px;
            z-index: 10;
        }
        
        .subdir-toggle-btn:hover {
            background: var(--bg-secondary);
            color: var(--text-primary);
        }
        
        .card-item.subdirs-expanded .subdir-toggle-btn svg {
            transform: rotate(180deg);
        }
        
        .card-subdirs {
            overflow: hidden;
            transition: max-height 0.3s ease-out;
            border-top: 1px solid var(--border-color);
            padding: 0;
            background: var(--bg-secondary);
        }
        
        .card-item.subdirs-expanded .card-subdirs {
            padding: 1rem;
        }
        
        .subdir-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem;
            border-radius: 5px;
            transition: var(--transition);
            cursor: pointer;
            outline: none;
            margin-bottom: 0.25rem;
        }
        
        .subdir-item:last-child {
            margin-bottom: 0;
        }
        
        .subdir-item:hover {
            background: var(--bg-primary);
        }
        
        .subdir-item[data-has-index="true"]:hover {
            box-shadow: inset 0 0 0 1px var(--primary);
        }
        
        .subdir-icon {
            width: 1.25rem;
            height: 1.25rem;
            color: var(--text-secondary);
            flex-shrink: 0;
        }

        .subdir-toggle-count {
            font-size: 0.75rem;
            color: var(--text-secondary);
            margin-left: 0.25rem;
            font-weight: 500;
        }
        .subdir-name {
            flex: 1;
            font-size: 0.875rem;
            color: var(--text-secondary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        
        .more-subdirs {
            text-align: center;
            padding: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.875rem;
            font-style: italic;
        }
        
        /* 页脚 */
        .page-footer {
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
            color: var(--text-secondary);
            border-top: 1px solid var(--border-color);
        }
        
        .footer-info {
            margin-top: 1rem;
            font-size: 0.875rem;
            opacity: 0.7;
        }
    </style>
    '''
    
if __name__ == "__main__":
    print("开始生成索引页面...")
    if generate_index():
        print("索引页面生成成功！")
        sys.exit(0)
    else:
        print("索引页面生成失败！")
        sys.exit(1)