<html>
<html lang="en">

<!--
    go to root folder
    php -s localhost:8000
-->

<head>
    <meta charset="utf-8">
    <title>Moonfall Ransomware | Dashboard</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==" crossorigin="anonymous" />

    <link rel="shortcut icon" href="./cloud-moon-solid.svg">
</head>

<body style="background: lightgray;">
    <nav class="navbar navbar-dark bg-dark" style="box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <i class="fas fa-cloud-moon"></i>
                <strong>Moonfall</strong> Ransomware
            </a>
        </div>
    </nav>
    <div class="container" style="background: white; border-radius: 2px; margin: auto; width: auto; margin-top: 2%; box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);">
        <h4 style="padding: 15px; text-align: center">History of attacks</h4>
        <table class="table">
            <thead class="thead-light">
                <tr>
                    <th scope="col" style="text-align: left;">IP Address</th>
                    <th scope="col" style="text-align: left;">Encoded Key</th>
                    <th scope="col" style="text-align: left;">Date of infection</th>
                    <th scope="col" style="text-align: left;">State</th>
                </tr>
            </thead>
            <tbody>
                <?php
                try{
                    $conn = new PDO('sqlite:database.db');

                    $conn->setAttribute(
                        PDO::ATTR_ERRMODE,
                        PDO::ERRMODE_EXCEPTION
                    );

                    $rows = $conn->query("SELECT * FROM infected_hosts")->fetchAll(PDO::FETCH_ASSOC);
                    
                    foreach ($rows as $row){
                        echo '<tr>';
                        echo '<td>';
                        echo $row['ip'];
                        echo '</td>';
                        echo '<td>';
                        echo $row['key'];
                        echo '</td>';
                        echo '<td>';
                        echo $row['date'];
                        echo '</td>';
                        echo '<td>';
                        echo $row['state'];
                        echo '</td>';
                        echo '</tr>';
                    }
                    
                }catch(PDOException $e){
                    echo $sql . "<br>" . $e->getMessage();
                }
                $conn = null;
                ?>
            </tbody>
        </table>
        <br>
    </div>
</body>

</html>