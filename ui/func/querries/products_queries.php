<?php
include_once __DIR__ . "/../../configuration/config.php";
$url = $GLOBALS["apiUrl"] . "products/";
//print_r ($_POST);
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
    $current_url = $GLOBALS["url"];
    $data = $_POST["data"];
    $ch = curl_init($current_url);
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
    $page = $_POST["page"];
    $search = $_POST["search"];
    $current_url = $GLOBALS["url"] . "?page=" . $page;
    if(!empty($search)){ 
        $current_url .= "&search=" . $search;
    }
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $current_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $html = curl_exec($ch);
    curl_close($ch);
    echo ($html);
}
main();
?>