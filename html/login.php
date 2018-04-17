<!DOCTYPE HTML>
<HTML>
<head>
	<title>Users logged in</title>
	<style>
		body {background-color: lightgrey;}
		h1 {color: black;}
		h3 {color: darkblue;}
	</style>
</head>
<body>
<p><a href="index.html"> <img src="back.png" alt="Back" style="width:13px;height:13px;"> <a href="index.html">Home page</a></p>

<?php echo "<p> Users that are currently logged in to my Raspberry PI</p>";?>
<?php system(who) ?>
</body>
</HTML>