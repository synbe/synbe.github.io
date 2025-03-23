// 编辑器初始化
document.addEventListener('DOMContentLoaded', function() {
    let isMarkdownMode = false;
    
    // 初始化富文本编辑器
    tinymce.init({
        selector: '#richEditor',
        language: 'zh_CN',
        height: 500,
        plugins: [
            'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
            'searchreplace', 'visualblocks', 'code', 'fullscreen',
            'insertdatetime', 'media', 'table', 'help', 'wordcount', 'codesample'
        ],
        toolbar: 'undo redo | formatselect fontselect fontsizeselect forecolor bold italic backcolor link image media table codesample | alignleft aligncenter alignright alignjustify bullist numlist outdent indent | removeformat code help',
        toolbar_mode: 'wrap',
        toolbar_sticky: true,
        menubar: 'file edit view insert format tools table help',
        content_style: 'body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; font-size: 14px; }',
        font_formats: `
            微软雅黑=Microsoft YaHei,Helvetica Neue,PingFang SC,sans-serif;
            苹果苹方=PingFang SC,Microsoft YaHei,sans-serif;
            宋体=simsun,serif;
            黑体=SimHei,sans-serif;
            Arial=arial,helvetica,sans-serif;
            Arial Black=arial black,avant garde;
            Times New Roman=times new roman,times;
            Courier New=courier new,courier;
            Verdana=verdana,geneva;
        `,
        fontsize_formats: '12px 14px 16px 18px 24px 36px 48px',
        images_upload_handler: handleImageUpload
    });

    // 初始化 Markdown 编辑器
    const markdownEditor = document.getElementById('markdownEditor');
    const markdownPreview = document.getElementById('markdownPreview');

    // 添加实时预览功能
    markdownEditor.addEventListener('input', function() {
        const markdown = this.value;
        const html = marked.parse(markdown);
        markdownPreview.innerHTML = html;
        
        // 保存光标位置
        const cursorPosition = this.selectionStart;
        this.value = markdown;
        this.setSelectionRange(cursorPosition, cursorPosition);
    });

    // 添加 Markdown 切换按钮事件监听
    const markdownToggle = document.getElementById('markdownToggle');
    markdownToggle.addEventListener('click', function() {
        isMarkdownMode = !isMarkdownMode;
        this.classList.toggle('active', isMarkdownMode);
        toggleEditorMode(tinymce.get('richEditor'), isMarkdownMode);
    });
});

// 切换编辑器模式
function toggleEditorMode(editor, isMarkdown) {
    const richEditorContainer = document.getElementById('richEditorContainer');
    const markdownEditorContainer = document.getElementById('markdownEditorContainer');
    const markdownEditor = document.getElementById('markdownEditor');
    const turndownService = new TurndownService({
        headingStyle: 'atx',
        codeBlockStyle: 'fenced'
    });

    if (isMarkdown) {
        // 转换为 Markdown
        const html = editor.getContent();
        const markdown = turndownService.turndown(html);
        
        // 隐藏富文本编辑器，显示 Markdown 编辑器
        richEditorContainer.style.display = 'none';
        markdownEditorContainer.style.display = 'block';
        markdownEditor.value = markdown;
        
        // 初始化预览
        markdownPreview.innerHTML = marked.parse(markdown);
        
        // 设置焦点并移动光标到末尾
        markdownEditor.focus();
        markdownEditor.setSelectionRange(markdown.length, markdown.length);
        
        showToast('已切换到 Markdown 模式');
    } else {
        // 转换回 HTML
        const markdown = markdownEditor.value;
        const html = marked.parse(markdown);
        
        // 隐藏 Markdown 编辑器，显示富文本编辑器
        markdownEditorContainer.style.display = 'none';
        richEditorContainer.style.display = 'block';
        editor.setContent(html);
        
        // 设置焦点到富文本编辑器
        editor.focus();
        
        showToast('已切换到富文本模式');
    }
}

// 修改样式定义
const style = document.createElement('style');
style.textContent = `
    /* Markdown 按钮激活状态样式 */
    button[aria-label="Markdown"][aria-pressed="true"],
    button[title="Markdown"][aria-pressed="true"],
    button[data-mce-name="markdown"][aria-pressed="true"],
    .tox .tox-tbtn.tox-tbtn--enabled[aria-label="Markdown"],
    .tox .tox-tbtn.tox-tbtn--active[aria-label="Markdown"] {
        background-color: #fff8dc !important;
        border-color: #deb887 !important;
        color: #000 !important;
    }

    /* 悬停状态 */
    button[aria-label="Markdown"][aria-pressed="true"]:hover,
    button[title="Markdown"][aria-pressed="true"]:hover,
    button[data-mce-name="markdown"][aria-pressed="true"]:hover,
    .tox .tox-tbtn.tox-tbtn--enabled[aria-label="Markdown"]:hover,
    .tox .tox-tbtn.tox-tbtn--active[aria-label="Markdown"]:hover {
        background-color: #ffe4b5 !important;
        border-color: #deb887 !important;
        color: #000 !important;
    }
`;
document.head.appendChild(style);

// 图片上传处理
function handleImageUpload(blobInfo, progress) {
    return new Promise((resolve, reject) => {
        try {
            const base64 = blobInfo.base64();
            resolve('data:' + blobInfo.blob().type + ';base64,' + base64);
        } catch (error) {
            reject('图片上传失败: ' + error.message);
        }
    });
}

// 保存为 HTML
function saveAsHtml() {
    const editor = tinymce.get('richEditor');
    const markdownEditor = document.getElementById('markdownEditor');
    const isMarkdownMode = markdownEditor.style.display !== 'none';

    let content;
    if (isMarkdownMode) {
        // 如果是 Markdown 模式，转换为 HTML
        content = marked.parse(markdownEditor.value);
    } else {
        content = editor.getContent();
    }

    // 添加基本的 HTML 结构
    const htmlContent = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>导出内容</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            line-height: 1.6;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    ${content}
</body>
</html>`;

    const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'content.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    showToast('HTML文件保存成功');
}

// 保存为 PDF
async function saveAsPdf() {
    const editor = tinymce.get('richEditor');
    const markdownEditor = document.getElementById('markdownEditor');
    const isMarkdownMode = markdownEditor.style.display !== 'none';

    try {
        showToast('正在生成PDF...');
        
        // 创建临时容器
        const tempDiv = document.createElement('div');
        if (isMarkdownMode) {
            tempDiv.innerHTML = marked.parse(markdownEditor.value);
        } else {
            tempDiv.innerHTML = editor.getContent();
        }

        // 设置打印样式
        tempDiv.style.cssText = `
            padding: 40px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            font-size: 14px;
            line-height: 1.6;
            color: #333;
            background: white;
            width: 800px;
            margin: 20px auto;
        `;
        document.body.appendChild(tempDiv);

        // 等待图片加载
        await new Promise(resolve => setTimeout(resolve, 500));

        const canvas = await html2canvas(tempDiv, {
            scale: 2,
            useCORS: true,
            logging: false,
            allowTaint: true,
            backgroundColor: '#ffffff',
            windowWidth: 800,
            windowHeight: tempDiv.offsetHeight
        });
        
        document.body.removeChild(tempDiv);

        // 创建 PDF
        const { jsPDF } = window.jspdf;
        const pdf = new jsPDF({
            unit: 'pt',
            format: 'a4',
            orientation: 'portrait'
        });

        // 计算页面尺寸
        const pageWidth = pdf.internal.pageSize.getWidth();
        const pageHeight = pdf.internal.pageSize.getHeight();
        const imgWidth = pageWidth;
        const imgHeight = (canvas.height * imgWidth) / canvas.width;

        // 分页处理
        let heightLeft = imgHeight;
        let position = 0;
        pdf.addImage(canvas, 'PNG', 0, position, imgWidth, imgHeight);
        heightLeft -= pageHeight;

        while (heightLeft >= 0) {
            position = heightLeft - imgHeight;
            pdf.addPage();
            pdf.addImage(canvas, 'PNG', 0, position, imgWidth, imgHeight);
            heightLeft -= pageHeight;
        }

        pdf.save('content.pdf');
        showToast('PDF文件保存成功');
    } catch (error) {
        console.error('PDF生成错误:', error);
        showToast('PDF生成失败: ' + error.message, 'error');
    }
}

// 保存为图片
async function saveAsImage() {
    const editor = tinymce.get('richEditor');
    const markdownEditor = document.getElementById('markdownEditor');
    const isMarkdownMode = markdownEditor.style.display !== 'none';

    try {
        showToast('正在生成图片...');
        
        // 创建临时容器
        const tempDiv = document.createElement('div');
        if (isMarkdownMode) {
            tempDiv.innerHTML = marked.parse(markdownEditor.value);
        } else {
            tempDiv.innerHTML = editor.getContent();
        }

        tempDiv.style.cssText = `
            padding: 20px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            font-size: 14px;
            line-height: 1.6;
            color: #333;
            background: white;
            width: 800px;
            margin: 20px auto;
        `;
        document.body.appendChild(tempDiv);

        // 等待图片加载
        await new Promise(resolve => setTimeout(resolve, 500));

        const canvas = await html2canvas(tempDiv, {
            scale: 2,
            useCORS: true,
            logging: false,
            allowTaint: true,
            backgroundColor: '#ffffff',
            windowWidth: 800,
            windowHeight: tempDiv.offsetHeight
        });
        
        document.body.removeChild(tempDiv);

        // 保存图片
        const link = document.createElement('a');
        link.download = 'content.png';
        link.href = canvas.toDataURL('image/png', 1.0);
        link.click();
        
        showToast('图片保存成功');
    } catch (error) {
        console.error('图片生成错误:', error);
        showToast('图片生成失败: ' + error.message, 'error');
    }
}

// 复制内容
async function copyContent() {
    const editor = tinymce.get('richEditor');
    const markdownEditor = document.getElementById('markdownEditor');
    const isMarkdownMode = markdownEditor.style.display !== 'none';

    try {
        const content = isMarkdownMode ? markdownEditor.value : editor.getContent();
        await navigator.clipboard.writeText(content);
        showToast('内容已复制到剪贴板');
    } catch (error) {
        console.error('复制错误:', error);
        showToast('复制失败: ' + error.message, 'error');
    }
}

// Toast 提示
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => toast.classList.add('show'), 10);
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => document.body.removeChild(toast), 300);
    }, 3000);
}

// 导出为 PDF
async function exportToPDF() {
    const editor = tinymce.get('editor');
    if (!editor) return;

    try {
        showToast('正在生成PDF...');
        
        // 创建临时容器
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = editor.getContent();
        tempDiv.style.cssText = `
            padding: 40px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            font-size: 14px;
            line-height: 1.6;
            color: #333;
            background: white;
            width: 800px;
            margin: 20px auto;
        `;
        document.body.appendChild(tempDiv);

        // 等待内容渲染
        await new Promise(resolve => setTimeout(resolve, 500));

        // 生成 PDF
        const canvas = await html2canvas(tempDiv, {
            scale: 2,
            useCORS: true,
            logging: true, // 开启日志以便调试
            allowTaint: true,
            backgroundColor: '#ffffff',
            removeContainer: false,
            windowWidth: 800,
            windowHeight: tempDiv.offsetHeight
        });
        
        document.body.removeChild(tempDiv);

        const { jsPDF } = window.jspdf;
        const pdf = new jsPDF({
            unit: 'pt',
            format: 'a4',
            orientation: 'portrait'
        });

        const imgData = canvas.toDataURL('image/jpeg', 1.0);
        const pageWidth = pdf.internal.pageSize.getWidth();
        const pageHeight = pdf.internal.pageSize.getHeight();
        const imgWidth = pageWidth;
        const imgHeight = (canvas.height * imgWidth) / canvas.width;

        let heightLeft = imgHeight;
        let position = 0;
        let page = 1;

        pdf.addImage(imgData, 'JPEG', 0, position, imgWidth, imgHeight);
        heightLeft -= pageHeight;

        while (heightLeft >= 0) {
            position = heightLeft - imgHeight;
            pdf.addPage();
            pdf.addImage(imgData, 'JPEG', 0, position, imgWidth, imgHeight);
            heightLeft -= pageHeight;
            page++;
        }

        pdf.save('content.pdf');
        showToast('PDF导出成功');
    } catch (error) {
        console.error('PDF导出错误:', error);
        showToast('PDF导出失败: ' + error.message, 'error');
    }
}

// 导出为图片
async function exportToImage() {
    const editor = tinymce.get('editor');
    if (!editor) return;

    try {
        showToast('正在生成图片...');
        
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = editor.getContent();
        tempDiv.style.cssText = `
            padding: 20px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            font-size: 14px;
            line-height: 1.6;
            color: #333;
            background: white;
            width: 800px;
            margin: 20px auto;
        `;
        document.body.appendChild(tempDiv);

        // 等待内容渲染
        await new Promise(resolve => setTimeout(resolve, 500));

        const canvas = await html2canvas(tempDiv, {
            scale: 2,
            useCORS: true,
            logging: true,
            allowTaint: true,
            backgroundColor: '#ffffff',
            removeContainer: false,
            windowWidth: 800,
            windowHeight: tempDiv.offsetHeight
        });
        
        document.body.removeChild(tempDiv);

        // 保存图片
        const link = document.createElement('a');
        link.download = 'content.png';
        link.href = canvas.toDataURL('image/png', 1.0);
        link.click();
        
        showToast('图片导出成功');
    } catch (error) {
        console.error('图片导出错误:', error);
        showToast('图片导出失败: ' + error.message, 'error');
    }
} 