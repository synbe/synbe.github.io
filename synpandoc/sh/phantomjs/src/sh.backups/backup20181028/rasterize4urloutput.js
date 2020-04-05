var page = require('webpage').create(),
	system = require('system'),
	fs = require('fs'),
   url = system.args[1];// 注意分号

page.open(url, function (status) 
{
    if (status != "success") 
    {
        console.log('FAIL to load the address');
        phantom.exit();
    }
      var date = Date.now();
      var output = './src/original.html';
      var rurl = page.url;
      var rcontent = page.content;
        // console.log('URL: ' + rurl);
        console.log('保存为:' + output);
        // console.log('body:' + rcontent);
        fs.write(output, rcontent, 'w');
        phantom.exit();
});