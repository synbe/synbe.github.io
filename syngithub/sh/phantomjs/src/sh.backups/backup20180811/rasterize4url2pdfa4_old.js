var page = require('webpage').create(),
	system = require('system'),
        url = system.args[1];// 注意分号
	
//设置viewportSize宽度和高度
//更改页码宽度和高度，只对响应式网页有效:width:595 600 680 768 800 1024 
// // 当你设定的分辨率是72像素/英寸时，A4纸的尺寸的图像的像素是595×842，
// // // 当你设定的分辨率是150像素/英寸时，A4纸的尺寸的图像的像素是1240×1754，
// 	view_width = '1240',//如微信,宽度太小，增加宽度后,但却不合适手机(iphone6s)阅读，建议:400
// 	view_height = '1754',
// 	view_size = view_width + view_height,
// 	paper_width = '210mm',
// 	paper_heigth = '297mm';
// 	
// //   paperSize纸张大小:A4
// If no paperSize is defined, the size is defined by the web page.
page.paperSize = {
  format:'A4',//210mmX297mm
};
	
// page.viewportSize = { width: view_width, height: view_height };  


page.evaluate(function()
    {
        window.scrollTo(0,10000);
    });
page.open(url, function (status) 
{
    if (status != "success") 
    {
        console.log('FAIL to load the address');
        phantom.exit();
    }
      var date = Date.now();
      var  outputpdf =  './src/pdf/' + page.title + '.pdf';
      var rurl = page.url;
        console.log('URL: ' + rurl);
       console.log('保存为:' + outputpdf);
    window.setTimeout(function () 
    {
        page.render(outputpdf, {format: 'pdf', quality: '100'});
        phantom.exit();
    }, 1000+500);    

}); 


// page.paperSize = {
//   format:'A4',//210mmX297mm
// };
