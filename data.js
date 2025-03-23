let entries = [
  {
    "id": "mk851lqbxea",
    "title": "编程爱好者",
    "author": "xun",
    "content": "编程爱好者编程神器----vscode。\n\n![编程爱好者](./assets/coder.png)",
    "tags": [
      "爱好",
      "编程"
    ],
    "date": "2025-03-22",
    "creattimestamp": "2025-03-22 21:03:34",
    "edittimestamp": "2025-03-23 13:43:31",
    "isFavorite": true,
    "comments": [
      {
        "id": "s4sfxby9mjs",
        "commentauthor": "xun",
        "time": "2025-03-23 11:59:03",
        "text": "[[欢迎来到synbe的博客|inithomepage]]"
      }
    ]
  },
  {
    "id": "koacagurdb",
    "title": "代码高亮",
    "author": "xun",
    "content": "#### 代码高亮显示\n\n需声明语言种类，如python\n\n\\`\\`\\`python\n\n\n```python\nclass CodeBlockExtension(markdown.extensions.Extension):\n    def extendMarkdown(self, md):\n        md.registerExtension(self)\n        md.preprocessors.register(CodeBlockPreprocessor(md), 'code_block', 25)\n```",
    "tags": [
      "代码",
      "编程",
      "学习",
      "python"
    ],
    "date": "2025-03-21",
    "creattimestamp": "2025-03-21 22:00:35",
    "edittimestamp": "2025-03-23 01:50:54",
    "isFavorite": false,
    "comments": [
      {
        "id": "q6za4r1ltri",
        "commentauthor": "xun",
        "time": "2025-03-23 01:49:44",
        "text": "代码高亮\n\n已经声明语言种类python\n\n\\`\\`\\`python\n\n\n```python\nclass CodeBlockExtension(markdown.extensions.Extension):\n    def extendMarkdown(self, md):\n        md.registerExtension(self)\n        md.preprocessors.register(CodeBlockPreprocessor(md), 'code_block', 25)\n```"
      },
      {
        "id": "bn5qu9d5mq",
        "commentauthor": "xun",
        "time": "2025-03-23 01:48:45",
        "text": "未声明语言种类python，无法渲染\n\n\\`\\`\\`(未声明python)\n\n```\nclass CodeBlockExtension(markdown.extensions.Extension):\n    def extendMarkdown(self, md):\n        md.registerExtension(self)\n        md.preprocessors.register(CodeBlockPreprocessor(md), 'code_block', 25)\n```"
      },
      {
        "id": "0mu9e3c20p1",
        "commentauthor": "2025-03-23 11:58:53",
        "time": "2025-03-23 01:49:44",
        "text": "[[欢迎来到synbe的博客|inithomepage]]"
      }
    ]
  },
  {
    "id": "inithomepage",
    "title": "欢迎来到synbe的博客",
    "author": "xun",
    "content": "我是一名业余[[编程爱好者|mk851lqbxea]]。\n\n这是本人写的一个静态日志管理系统，纯js，不依赖后端服务器，欢迎批评改进！\n\n具备以下功能和特性：\n\n### 功能\n- 日历展示：展示当前月份的日历，可切换月份，点击日期显示该日日志，无日志时可创建新日志。\n- 日志管理：支持创建、编辑、删除、收藏、复制链接等操作，能按日期筛选日志。\n- 搜索功能：可根据关键词搜索日志标题和内容。\n- 评论管理：支持对日志添加、编辑和删除评论。\n- 标签管理：展示标签云，可按标签筛选日志。\n- 插入图片：支持一次性插入本地多张图片，图片将压缩到2M以下并转换成base64编码，同时支持markdown语法插入图片。\n- 插入链接：支持[[插入内部日志链接|ohkclt6r75t]]。\n- 数据导出：支持将日志数据导出为 JSON 文件，日志数据保存为json。默认读取根目录下./data.js中的json数据并渲染处理。\n\n### 特性\n- 响应式设计：页面布局在不同屏幕尺寸下自适应，768px 以下屏幕采用单栏布局。\n- 代码高亮：使用 Highlight.js 对代码块进行[[代码高亮]]显示。\n- Markdown 解析：使用 marked 解析日志和评论中的 Markdown 内容。\n- 用户交互：按钮、标签等元素有交互效果，如悬停变色、显示操作按钮等。\n\n### 使用\n\n- 编辑、提交日志后，导出数据，自动生成并下载data.js文件，放到根目录下（./data.js）即可，\n- 纯静态，无需后端服务器，可本地部署，也可在github上静态部署。\n\n### 注意\n\n- 刷新页面前，务必先导出数据！\n\n### 联系\n\n- 邮箱：421103218@qq.com\n\n---\n\n\n![](./assets/home.png)",
    "tags": [
      "首页",
      "编程",
      "博客"
    ],
    "isFavorite": true,
    "comments": [
      {
        "id": "c4lpodnzurh",
        "commentauthor": "synbe",
        "time": "2025-03-23 13:37:32",
        "text": "#### 如何插入其他日志链接？\n\n```\n在日志和评论中也使用\\[\\[日志标题|日志id\\]\\]或者 \\[\\[日志标题\\[\\[格式来插入其他日志的链接。\n\n例如：\\[\\[日志标题|日123\\]\\]，这里的 `123` 就是目标日志的 id。\n```\n例：\n\n[[编程爱好者|mk851lqbxea]] \n\n或者 \n\n[[代码高亮]]"
      },
      {
        "id": "cgh2gad769l",
        "commentauthorr": "xun",
        "time": "2025-03-23 13:37:25",
        "text": "#### 插入图片\n\n支持一次性插入本地多张图片，图片将压缩到2M以下并转换成base64编码，同时支持markdown语法插入图片。\n\n\n\n![](./assets/001.png)\n\n点击图片放大！",
        "commentauthor": "synbe"
      },
      {
        "id": "ep22716b1wv",
        "commentauthor": "synbe",
        "time": "2025-03-23 13:35:59",
        "text": "#### 代码高亮显示\n\n需声明语言种类，如python\n\n\\`\\`\\`python\n\n\n```python\nclass CodeBlockExtension(markdown.extensions.Extension):\n    def extendMarkdown(self, md):\n        md.registerExtension(self)\n        md.preprocessors.register(CodeBlockPreprocessor(md), 'code_block', 25)\n```"
      }
    ],
    "date": "2025-03-17",
    "creattimestamp": "2025-03-17 22:33:03",
    "edittimestamp": "2025-03-23 15:14:27"
  },
  {
    "id": "ohkclt6r75t",
    "author": "synbe",
    "title": "插入内部日志链接",
    "content": "## 如何插入其他日志链接？\n\n```\n在日志和评论中也使用\\[\\[日志标题|日志id\\]\\]或者 \\[\\[日志标题\\[\\[格式来插入其他日志的链接。\n\n```\n例：\n\n[[编程爱好者|mk851lqbxea]] \n\n或者 \n\n[[代码高亮]]",
    "tags": [
      "编程",
      "博客"
    ],
    "date": "2025-03-17",
    "creattimestamp": "2025-03-23 13:30:21",
    "edittimestamp": "2025-03-23 13:31:11",
    "isFavorite": false,
    "comments": []
  }
]