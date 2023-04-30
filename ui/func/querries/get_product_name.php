<?php
include_once __DIR__ . "/../../configuration/config.php";
$id = $_GET["id"];
$url = $GLOBALS["apiUrl"] . "products/$id";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$html = curl_exec($ch);
curl_close($ch);
$json = json_decode($html, true);
echo ($json["title"]);
?>