<?php
include_once __DIR__ . "/../../configuration/config.php";

$location = $GLOBALS["absolutePath"] . "pages/search_page.php";
session_start();
$_SESSION["login"] = $_GET["login"];
echo($_SESSION["login"]);
session_write_close();
header("Location: $location");
exit();
?>