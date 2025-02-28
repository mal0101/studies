<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    function traiterTexte(string $texte)  {
        $texte = strtolower($texte);
        // le nombre total de mots dans la chaîne:
        echo str_word_count($texte);  
        // le mot le plus long
        $words = explode(" ", $texte);
        $longestWordLength = strlen($words[0]);
        $longestWord = $words[0];
        foreach ($words as $word) {
            if (strlen($word) > $longestWordLength) {
                $longestWord = $word;
                $longestWordLength = strlen($word);
            }
        }
        echo "<br>";
        echo $longestWord ;
        echo "<br>";
        // le nombre d'occurences de chaque mot dans une chaine de caractère
        $wordCounts = array_count_values($words);
        foreach ($wordCounts as $word => $count) {
            echo $word . ": " . $count;
            echo "<br>";
        }
    }
    traiterTexte("Hello how are You YOU you malak MALAK malak MalAk malak");
    ?>
</body>
</html>