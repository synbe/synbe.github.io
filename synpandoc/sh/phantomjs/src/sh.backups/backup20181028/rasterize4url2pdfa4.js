var page = require('webpage').create(),
	system = require('system'),
        url = system.args[1];// 注意分号
        
page.paperSize = {
    format: 'A4',
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
      var  outputpdf =  './src/pdf/' + page.title + '_a4' + '.pdf';
      var rurl = page.url;
        console.log('URL: ' + rurl);
       console.log('保存为:' + outputpdf);
    window.setTimeout(function () 
    {
        page.render(outputpdf, {format: 'pdf', quality: '100'});
        phantom.exit();
    }, 1000+500);    

}); 
