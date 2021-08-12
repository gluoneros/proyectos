<?php
function placesRecomendation($condition = '', $question = ''){
    $weather = array("Bogota" => "cold", "Monteria" => "hot", "Medellin" => "mild");    
    $ubication = array("Guajira" => "north","Leticia" => "south", "Santander" => "east", "Antioquias" => "west");
    $tourism = array("Santa marta" => "sea", "Villavicncio" => "plains", "Rioacha" => "desert", "Quindia" => "vlley");

    switch($condition){
        case "weather":
            $search = $weather;
        break;
        case "ubication":
            $search = $ubication;
        break;
        case "tourism":
            $search = $tourism;
        break;

        default:
            echo "Welcome to Colombia" ;
            
    }

    echo "The perfect place for you is ".array_search($question, $search);
}


placesRecomendation("weather", "cold");
