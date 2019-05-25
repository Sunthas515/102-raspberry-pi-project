<?php
$f = fopen("/sys/class/thermal/thermal_zome0/temp","r");
$temp = fgets($f);
echo 'IFB102 Module 3 Miniproject  - Webserver + CPU Temp <br>;
echo 'The temperature of the raspberry pi is '.round($temp/1000);
fclose($f);
?>
