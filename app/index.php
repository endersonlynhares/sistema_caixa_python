<!DOCTYPE html>
<html lang="pt_BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilo/estilo.css">
    <style media="print">
        button{
            display:none;
        }
    </style>
    <title>Caixa - PY</title>
</head>
<body>

    <h1>VENDAS DO DIA</h1>

    <?php
        $arquivo = file_get_contents('../config/vendas.json');
        $json = json_decode($arquivo);
        $i = 1;
        $soma_produtos = 0;
        $apuro_dia = 0;
        echo "<main><div id='container'>";
        foreach($json as $produto){
            $id = (string)$i;
            echo "<div class='box_model'>";
            echo "<header>VENDA ".$id."</header><br>";
            echo "<ul>";
            foreach($produto as $valor){
                print_r("<li>".$valor->Produto.": R$");
                print_r($valor->Preço."</li>");
                $val = number_format($valor->Preço, 2, '.', '');
                $soma_produtos = $soma_produtos + $val;
            }
            echo "<li><strong>Total: R$".((string)number_format($soma_produtos,2, '.','')."</strong></li>");
            echo "<ul>";
            echo "</div>";
            $apuro_dia = $apuro_dia + $soma_produtos;
            $i = $i + 1;
            $soma_produtos = 0;
        }

        echo "</div></main>";
        echo "<p> <strong>APURAMENTO DO DIA: R$".$apuro_dia."</strong></p>" ;
    ?>
  
    <button onclick="window.print()">IMPRIMIR</button>
</body>
</html>