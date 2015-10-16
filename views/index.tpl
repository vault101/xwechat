<!DOCTYPE HTML>
<html>
<head>
<title>{{ title }}</title> 
<link href="/static/css/style.css" rel="stylesheet" type="text/css" media="all"/> 
<link rel="Shortcut Icon" href="http://7xkpi6.com1.z0.glb.clouddn.com/avatar.jpg" />
<link rel="Bootmark" href="http://7xkpi6.com1.z0.glb.clouddn.com/avatar.jpg" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"> 
<meta name="keywords" content="wechat searcher" /> 
<link href='/static/css/googlefont.css' rel='stylesheet' type='text/css'> 
</head>
<body> 
<div class="search">
	<i></i>
	<div class="s-bar">
	   <form action="/search" method="get">
		<input type="text" name="key" value="type something for search" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'type something for search';}">
		<input type="submit" value="搜索" onclick="search()" />
	  </form>
	</div>
	<p>{{ description }}</p>
</div> 
<div class="copyright">
	 <p>by <a href="http://xlzd.me" target="_blank">xlzd</a></p>
</div>	
<script type="text/javascript" src="http://7xldek.com1.z0.glb.clouddn.com/@/html/js/jquery.min.js"></script>
<script type="text/javascript" src="/static/js/search.js"></script>
</body>
</html>