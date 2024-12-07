document.addEventListener('DOMContentLoaded', function () {
    var markdownIt = window.markdownit();
    var textarea = document.getElementById('comment-textarea');
    var submitBtn = document.getElementById('submit-btn');
    var generateBtn = document.getElementById('generate-btn');
    var openBtn = document.getElementById('open-btn');
    var fileInput = document.getElementById('file-input');
    var commentsDisplay = document.getElementById('comments-display');


    // 格式化时间戳函数
    function getFormattedDate() {
        return new Date().toISOString().replace('T', ' ').substring(0, 19).replace(/-/g, '-').replace(/\.\d+Z$/, '');
    }

    // 添加新评论函数
    function addComment(markdownText) {
        var html = markdownIt.render(markdownText);
        var commentEl = document.createElement('div');
        // // 获取系统当前时间
        // var time = new Date().toLocaleString(); // 
        // 获取系统当前时间，并格式化为 'YYYY-MM-DD HH:mm:ss'
        var time = new Date()
            .toISOString() // 转换为 ISO 8601 格式
            .replace('T', ' ') // 替换 T 为 空格
            .substring(0, 19) // 截取到 'YYYY-MM-DDTHH:mm:ss' 的部分
            .replace(/-/g, '/') // 替换年月日的 - 为 /
            .replace('Z', ''); // 移除尾部的 Z（如果是 UTC 时间）

        commentEl.classList.add('comment');
        commentEl.innerHTML = `
            <div class="comment-content">
                <div class="comment-time">${time}</div>
                <div class="comment-content-x">${html}</div>
            </div>
            <button class="delete-btn">删除</button> <!-- 删除按钮 -->
        `;
        commentsDisplay.appendChild(commentEl);

        // 为每个新评论绑定删除事件
        var deleteBtn = commentEl.querySelector('.delete-btn');
        deleteBtn.addEventListener('click', function (event) {
            event.stopPropagation(); // 阻止事件冒泡
            if (confirm('确定要删除这条评论吗？')) {
                commentEl.remove();
            }
        });

        // 滚动到评论区域底部
        commentsDisplay.scrollTop = commentsDisplay.scrollHeight;
    }


    // 提交评论事件
    submitBtn.addEventListener('click', function () {
        var markdownText = textarea.value.trim();
        if (!markdownText) return;
        addComment(markdownText);
        textarea.value = '';
        //激活保存按钮
        // generateBtn.click();
    });

    // 快捷键Ctrl+Enter提交
    textarea.addEventListener('keydown', function (event) {
        if (event.ctrlKey && event.key === 'Enter') {
            event.preventDefault();
            submitBtn.click();
        }
    });

    // 保存HTML文件事件
    function generateHTML() {
        var commentsHTML = '';
        var comments = document.querySelectorAll('#comments-display .comment');
        comments.forEach(function (comment) {
            // 提取评论内容和时间
            var commentContent = comment.querySelector('.comment-content').innerHTML;
            commentsHTML += `<div class="comment">${commentContent}</div>`;
        });

        var html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AxunComments</title>
    <style>
        body {
            height: 100%;
            max-width: 900px;
            margin: 0 auto;
        }

        .flex-container {
            display: flex;
            flex-direction: column;
            height: 95vh;
            overflow: hidden;
            max-width: 800px;
            margin: 0.5em auto;
        }

        .flex-panel {
            overflow-y: auto;
            padding: 1px;
        }

        .display-panel {
            flex: 1;
            background: #f9f9f9;
            border-radius: 5px;
            margin-bottom: 0.5em;
        }

        .editor-panel {
            flex: 0 1 150px;
            display: flex;
            flex-direction: column;
            background: #e5e8e6;
            border-radius: 5px;
        }

        #comment-textarea {
            flex: 1;
            margin-bottom: 1px;
            border-radius: 5px;
        }

        #button-container1 {
            display: flex;
            /* justify-content: space-between; */
        }

        #button-container2 {
            text-align: right;
        }

        button {
            cursor: pointer;
            padding: 4px 12px;
            width: 8em;
            border: 0px;
            margin: 1px 2px 1px 0px;
            background: #fff;
            border-radius: 5px;
            color: #444648;
            margin: 1px;
        }

        button:hover {
            background: #f9f9f9;
        }

        .resize-bar {
            width: 100%;
            cursor: row-resize;
            height: 5px;
            background-color: #ddd;
        }


        .comment-time {
            margin-bottom: 5px;
            font-size: 0.9em;
            color: gray;
            border-bottom: 1px solid #e5e8e6;
            padding-bottom: 2px;

        }

        .comment {
            position: relative;
            padding: 10px;
            border: 1px solid #ddd;
            margin-bottom: 10px;
            border-radius: 5px;
        }

        .delete-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            cursor: pointer;
            color: #f9f8f8;
            padding: 0px;
            width: 3em;
            background: red;
        }

        .delete-btn:hover {
            background: rgb(97, 28, 28);
        }

        img {
            margin: 0 auto;
            display: block;
            width: 100%;
        }

        pre {
            background: #1d2826;
            color: #e6d8d8;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
        }

        .popup-container {
            position: fixed;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .popup-content {
            background-color: #fff;
            padding: 1em 2em;
            border-radius: 5px;
            width: 800px;
        }

        .close-btn {
            cursor: pointer;
            float: right;
            font-size: 25px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="comments">${commentsHTML}</div>
</body>
</html>`;

        var blob = new Blob([html], { type: 'text/html;charset=utf-8' });
        saveAs(blob, 'indexout001.html'); // 保存为 indexout001.html
    }

    // 保存PDF文件
    function generatePDF() {
        var doc = new jsPDF.jsPDF();
        var comments = document.querySelectorAll('#comments-display .comment');
        var yOffset = 20; // 开始绘制的Y坐标，留出一些页眉空间
        comments.forEach(function (comment, index) {
            var time = comment.querySelector('.comment-time').textContent;
            var content = comment.querySelector('p:not(.comment-time)').textContent;
            doc.text(time, 10, yOffset);
            doc.text(content, 10, yOffset + 10);
            yOffset += 20; // 每条评论间隔20单位
        });
        doc.save('indexout001.pdf');
    }

    // 绑定保存按钮事件
    generateBtn.addEventListener('click', function () {
        generateHTML();
        generatePDF();
    });


    // 打开按钮的点击事件
    openBtn.addEventListener('click', function () {
        // 显示文件选择对话框，让用户选择文件
        fileInput.click();
    });

    window.onload = function () {
        let fileInput = document.getElementById('file-input');
        // 设置文件输入的默认值，这里的'path/to/your/file.txt'应该替换为你想要默认选择的文件路径
        fileInput.value = './indexout.html';
    };

    // 文件选择输入变化事件
    fileInput.addEventListener('change', function (event) {
        var file = event.target.files[0]; // 获取用户选择的文件
        if (!file) return; // 如果没有选择文件，则退出

        // 确保文件类型是.html
        if (!file.name.endsWith('.html')) {
            alert('请选择一个HTML文件。');
            return;
        }

        var reader = new FileReader(); // 创建FileReader对象
        reader.onload = function (e) {
            // 当文件读取完毕后，执行此回调函数
            var fileContent = e.target.result;
            if (fileContent.includes('AxunComments')) {
                // 如果文件包含'AxunComments'，则执行内容提取操作
                extractComments(fileContent);
            } else {
                // 如果文件不包含'AxunComments'，弹出错误提示窗
                alert('所选文件不符合条件！');
            }
        };
        reader.onerror = function () {
            // 读取文件时发生错误
            alert('读取文件时发生错误。');
        };

        reader.readAsText(file); // 以文本形式读取文件内容
    });

    fileInput.addEventListener('change', function (event) {
        var file = event.target.files[0];
        if (!file) {
            return;
        }

        var reader = new FileReader();
        reader.onload = function (e) {
            var fileContent = e.target.result;

            // 使用正则表达式提取评论时间和内容
            var timeRegex = /<div class="comment-time">([\s\S]*?)<\/div>/gm;
            var contentRegex = /<div class="comment-content-x">([\s\S]*?)<\/div>/gm;

            var comments = [];
            var timeMatch;
            var contentMatch;

            // 循环提取所有匹配的评论时间和内容
            while ((timeMatch = timeRegex.exec(fileContent)) !== null) {
                // 在同一匹配位置提取内容
                contentMatch = contentRegex.exec(fileContent);
                if (contentMatch) {
                    comments.push({
                        time: timeMatch[1],
                        content: contentMatch[1]
                        // content: markdownIt.render(contentMatch[1]) // 使用markdown-it渲染内容
                    });
                }
            }

            // 清空显示区并显示所有评论
            commentsDisplay.innerHTML = '';
            comments.forEach(function (comment) {
                var commentEl = document.createElement('div');
                commentEl.classList.add('comment');
                commentEl.innerHTML = `
                    <div class="comment-content">
                        <div class="comment-time">${comment.time}</div>
                        <div class="comment-content-x">${comment.content}</div>
                    </div>
                `;
                commentsDisplay.appendChild(commentEl);
            });
        };
        reader.readAsText(file);
    });


});

document.addEventListener('DOMContentLoaded', function () {
    var insertImagesBtn = document.getElementById('insertimages-btn');
    var commentTextarea = document.getElementById('comment-textarea');
    var imagesInput = document.getElementById('images-input');

    // 设置 input 元素的 multiple 属性为 true，允许选择多个文件
    imagesInput.setAttribute('multiple', 'true');

    // 为“插入图片”按钮添加点击事件监听器
    insertImagesBtn.addEventListener('click', function () {
        imagesInput.click(); // 触发文件选择
    });

    // 为文件输入添加 change 事件监听器
    imagesInput.addEventListener('change', function (event) {
        var files = event.target.files; // 获取选中的文件列表
        var imagesPath = '';

        // 遍历所有选中的文件
        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            // 检查文件类型是否为 JPG、PNG 或 GIF
            if (file.type === 'image/jpeg' || file.type === 'image/png' || file.type === 'image/gif') {
                // 生成图片的 Markdown 链接
                imagesPath += '![](./images/' + file.name + ')\n';
            }
        }

        // 将生成的 Markdown 链接追加到 comment-textarea 中
        commentTextarea.value += imagesPath;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var openPopupBtn = document.getElementById('help-btn');
    var popupContainer = document.getElementById('help-container');
    var closeBtn = document.querySelector('.close-btn');

    // 打开弹窗
    openPopupBtn.addEventListener('click', function () {
        popupContainer.style.display = 'flex';
    });

    // 关闭弹窗
    closeBtn.addEventListener('click', function () {
        popupContainer.style.display = 'none';
    });

    // 点击弹窗外部区域关闭弹窗
    popupContainer.addEventListener('click', function (event) {
        if (event.target === popupContainer) {
            popupContainer.style.display = 'none';
        }
    });
});