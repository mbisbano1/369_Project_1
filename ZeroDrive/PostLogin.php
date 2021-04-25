<html>
 <body>
  <head>
   <title>
    MDRIVE ACCESS
   </title>
  </head>
  <p>Click the RE-ZIP button and wait until you are notified that it is ready to download! </p>
  <form method="post">
   <input type="submit" value="RE-ZIP" name="RE-ZIP"> 
  </form>
  <br>
  <a href="Downloadables/mdrive.zip" title="This is a link to the zipped m-drive">Download the MDrive zip folder</a> 
  <br>	

 </body>
</html>

<?php
	if(isset($_POST['RE-ZIP']))
	{
		
		//echo"Hold on while we zip!<br>";
		$mDriveZip = shell_exec("sudo python3 /var/www/html/MiddleGround.py");
		//echo"<pre>$mDriveZip</pre>";
		echo"<br>";
		echo"The MDrive Folder has successfully been zipped! You may now click the MDrive download link!";
		echo"<br>";
		
	}

?>
