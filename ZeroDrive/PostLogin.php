<html>
 <body>
  <head>
   <title>
    MDRIVE ACCESS
   </title>
   <style>
    h2{text-align: center;}
    
    .container{
	text-align: center;
	padding-top: 10px;
	padding-bottom: 10px;
    }

    p{text-align: center;}

    body{font-family: Arial, Helvetica, sans-serif;}

    a{text-align: center;}

    button {
	background-color: #3377FF;
	color: white;
	padding: 14px 20px;
	margin: 8px 0;
	border: none;
	cursor: pointer;
	width: 50%;
    }
    button:hover {
	opacity: 0.8;

    }

   </style>

  </head>
  <h2>Click the RE-ZIP button and wait until you are notified that it is ready to download! </h2>

  <form method="post">
	<div class="container">
	   <button type="submit" value="RE-ZIP" name="RE-ZIP">RE-ZIP the MDrive </button> 
	</div>
  </form>

  <p>
  	<br>
	 <a href="Downloadables/mdrive.zip" title="This is a link to the zipped m-drive">Download the MDrive zip folder</a> 
	<br>
  </p>
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
		echo"<p>The MDrive Folder has successfully been zipped! You may now click the MDrive download link!</p>";
		echo"<br>";
		
	}

?>
