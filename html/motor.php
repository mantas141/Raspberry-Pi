<!DOCTYPE HTML>
<HTML>
<head>
<?php 
if (isset($_POST['MotorONc']))
{
	shell_exec('sudo python /home/pythongpiotest/motoronc.py write 20');
}
if (isset($_POST['MotorONcc']))
{
	shell_exec('sudo python /home/pythongpiotest/motoroncc.py');
}
if (isset($_POST['MotorOFF']))
{
	shell_exec('sudo python /home/pythongpiotest/motoroff.py');
}
if (isset($_POST['Speed0']))
{
	exec('sudo python /home/pythongpiotest/speed0.py');
}
if (isset($_POST['Speed20']))
{
	exec('sudo python /home/pythongpiotest/speed20.py');
}
if (isset($_POST['Speed60']))
{
	exec('sudo python /home/pythongpiotest/speed60.py');
}
if (isset($_POST['Speed100']))
{
	exec('sudo python /home/pythongpiotest/speed100.py');
}
?>
<title></title>
</head>
<body>
<form method="post">
<button name="MotorONc">Motor spins clockwise</button>
<button name="MotorONcc">Motor spins counterclockwise</button>
<button name="MotorOFF">Turn off the motor</button>
<button name="Speed20">Change the speed to 20</button>
</form>
</body>
</HTML>