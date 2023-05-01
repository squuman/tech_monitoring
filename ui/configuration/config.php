<?php
    $apiUrl = "http://107.179.38.11/api/";
    $absolutePath = "//" . substr(strtr(realpath(__DIR__ . "/.."), '\\', '/'), strlen($_SERVER['DOCUMENT_ROOT'])) . "/";
    $absolutePath = str_replace("//", "/", $absolutePath);
?>