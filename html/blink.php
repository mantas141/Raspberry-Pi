<!DOCTYPE HTML>
<HTML>
<head>
<?php 
if (isset($_POST['RedON']))
{
	exec('sudo python /home/pythongpiotest/blink.py');
}
?>
<title></title>
</head>
<body>
<form method="post">
<<button name="RedON">Red On</button>
</body>
</HTML>