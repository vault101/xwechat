<!DOCTYPE HTML>
<html>
<head>
<title>{{ title }}</title> 
<link href="/static/css/style.css" rel="stylesheet" type="text/css" media="all"/> 
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"> 
<meta name="keywords" content="wechat searcher" /> 
<link href='/static/css/googlefont.css' rel='stylesheet' type='text/css'> 
</head>
<body> 
<div class="search">
	<i></i>
	<div class="s-bar">
	   <form>
		<input type="text" value="type something for search" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'type something for search';}">
		<input type="submit"  value="搜索"/>
	  </form>
	</div>
	<p>{{ description }}</p>
</div> 
<div class="copyright">
	 <p>by <a href="http://xlzd.me" target="_blank">xlzd</a></p>
</div>	
</body>
</html>