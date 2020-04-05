var page = require('webpage').create(),
	system = require('system'),
        url = system.args[1];//声明变量后，注意分号;结尾！！！！
	
//设置viewportSize宽度和高度
//更改页码宽度和高度，只对响应式网页有效:width:595 600 680 768 800 1024 
// // 当你设定的分辨率是72像素/英寸时，A4纸的尺寸的图像的像素是595×842，
// // // 当你设定的分辨率是150像素/英寸时，A4纸的尺寸的图像的像素是1240×1754，
page.viewportSize = { width: 795, height: 1024};  

page.paperSize = {
    margin: "1cm",
    /* default header/footer for pages that don't have custom overwrites (see below) */
//     header: {
// 	height: "1cm",
// 	contents: phantom.callback(function(pageNum, numPages) {
// 	    if (pageNum == 1) {
// 		return "";
// 	    }
// 	    return "<h1>Header <span style='float:right'>" + pageNum + " / " + numPages + "</span></h1>";
// 	})
//     },
    footer: {
	height: "1cm",
	contents: phantom.callback(function(pageNum, numPages) {
	    if (pageNum == numPages) {
		return "";
	    }
	    return "<h5>synbe.com <span style='float:right'>" + pageNum + " / " + numPages + "</span></h5>";
	})
    }
};

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
      var date = Date.now();
//       var  outputpdf =  './src/pdf/' + page.title + '.pdf';
      var  outputjpg =  './src/jpg/' + page.title + '.jpg';
//       var  outputpng =  './src/png/' + page.title + '.png';
      var rurl = page.url;
        console.log('URL:' + rurl);
//         console.log('保存为:' + outputpdf);
	 console.log('保存为:' + outputjpg);
// 	 console.log('保存为:' + outputpng);
    window.setTimeout(function () 
    {
//        page.render(outputpdf, {format: 'pdf', quality: '100'});
	page.render(outputjpg, {format: 'jpg', quality: '100'});
// 	page.render(outputpng, {format: 'png', quality: '100'});
        phantom.exit();
    }, 10000);    

}); 
