<html>
	<head>
		<title>Witam</title>
	</head>
			<body>
				<?php
				$usr=$_POST['username'];
				$psw=$_POST['password'];
				if($usr=='mike' and $psw=='gawlicki')
				{
					$command = escapeshellcmd('python3 /var/www/html/mail/checkmailONCE.py');
					$output = shell_exec($command);
    					echo $output;
					/*header('Content-Type: text/plain');
					$myfile = fopen("mail.txt", "r") or die("Unable to open file!");
					$fromS = strval(fgets($myfile,filesize("mail.txt")));
					$fromS1 = htmlentities($fromS);
					echo $fromS1;
					header('Content-Type: text/html');
					echo '<br>';
					while(!feof($myfile))
					{
						$msgS = strval(fgets($myfile,filesize("mail.txt")));
						echo $msgS;
						echo '<br>';
					}*/
				}
				?> 
				
			</body>
</html>
