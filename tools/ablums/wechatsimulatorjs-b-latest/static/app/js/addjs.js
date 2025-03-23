// addjs.js
function saveChatContainerScreenshot() {
    const chatContainer = document.getElementById('saveimagearea');
    
    html2canvas(chatContainer).then(function(canvas) {
      const image = canvas.toDataURL('image/jpeg');
      const link = document.createElement('a');
      link.download = 'screenshot.jpg';
      link.href = image;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    });
  }
  
  // 确保在页面加载完成后注册事件监听器
  document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('saveImageButton').addEventListener('click', saveChatContainerScreenshot);
  });

  
// 清除所有 localStorage 数据
function clearAllData() {
  localStorage.clear();
  location.reload();
}