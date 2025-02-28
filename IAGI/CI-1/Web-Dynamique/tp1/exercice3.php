<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    function remplacerLettres(string $texte) {
        $texte = strtolower($texte);
        // always use /word/ when using preg_replace
        $texte = preg_replace("/e/","3", $texte);
        $texte = preg_replace("/i/","1", $texte);
        $texte = preg_replace("/o/","0", $texte);
        return $texte;
    }
    echo remplacerLettres("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.");

    ?>
</body>
</html>