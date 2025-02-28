<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    function age(DateTime $datedenaissance) {
        $givendate = new DateTime($datedenaissance->format("Y-m-d"));
        $currentdate = new DateTime();
        $age = $currentdate->diff($givendate)->y;
        if ($age < 18) {
            echo "khoya rak mashi majeur et vacciné";
    }
    else {
        echo "khoya rak majeure et vacciné";
    }
    }
    age(new DateTime("1999-01-22"));

    ?>
</body>
</html>