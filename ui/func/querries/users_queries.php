<?php
$url = "http://107.179.38.11/api/users/";
$method = $_POST["method"];

function main(){
    global $method;

    switch($method){
        case "POST":
            PostQuery();
            break;
        case "GET":
            GetQuery();
            break;
    }
}

function PostQuery(){
    global $url;
    $data = $_POST["data"];
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data); 
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_HEADER, false);
    
    $html = curl_exec($ch);
    curl_close($ch);
}

function GetQuery(){
    $login = $_POST["login"];
    $current_url = $GLOBALS["url"];
    $current_url .= "?limit=10&page=1&search=$login";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $current_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $html = curl_exec($ch);
    curl_close($ch);
    echo ($html);
}


main();
?>