var page = require('webpage').create(),
	system = require('system'),
        url = system.args[1];//声明变量后，注意分号;结尾！！！！
	
//设置viewportSize宽度和高度
//更改页码宽度和高度，只对响应式网页有效:width:595 600 680 768 800 1024 
// // 当你设定的分辨率是72像素/英寸时，A4纸的尺寸的图像的像素是595×842，
// // // 当你设定的分辨率是150像素/英寸时，A4纸的尺寸的图像的像素是1240×1754，
page.viewportSize = { width:595, height: 1024 };  

page.evaluate(function()
    {
        window.scrollTo(0,100000);
    });
page.evaluate(function() {
    document.body.bgColor = 'white';
});
page.open(url, function (status) 
{
    if (status != "success") 
    {
        console.log('FAIL to load the address');
        phantom.exit();
    }
      var  outputpdf =  './src/pdf/' + page.title + '.pdf';
      
      var rurl = page.url;
        console.log('URL: ' + rurl);
       console.log('保存为:' + outputpdf);
    window.setTimeout(function () 
    {
        page.render(outputpdf, {format: 'pdf', quality: '100'});
        phantom.exit();
    }, 10000);    

}); 

