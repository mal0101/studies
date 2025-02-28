<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        function mettreMaj(array $data) {
            for ($i = 0; $i < count($data); $i++) {
                // the following line turns the entire string to lowercase and the first letter of said string to uppercase
                $data[$i] = ucfirst(strtolower($data[$i]));
                $length = strlen($data[$i]);
                if ($length > 1) {
                    $data[$i][$length - 2] = strtoupper($data[$i][$length - 2]);
                }
            }
            return $data;
        }

        // Example usage
        $tab = ['madrId', 'PaRis', 'casablanca'];
        $result = mettreMaj($tab);
        print_r($result);
    ?>
</body>
</html>