<?php
require 'config.php';

$lista = [];
$sql = $pdo->query("SELECT * FROM portfoliodev");
if($sql->rowCount() > 0 ) {
 $lista = $sql->fetchAll(PDO::FETCH_ASSOC);
} 

?>

<body style = "background:lightblue; margin:30px">  

    <a href="adicionar.php" style="text-decoration:none; color:green;">ADICIONAR AO PORTFÓLIO</a>

    <table border="1" width="100%">
        <tr>
            <th>ID</th>
            <th>Título Do Projeto</th>
            <th>Linguagem Desenvolvida</th>
            <th>Descrição</th>
            <th>Ações</th>
        </tr>
        <?php foreach($lista as  $portfolio): ?>
            <tr>
                <td><?= $portfolio['id'];?></td>
                <td><?= $portfolio['tituloprojeto'];?></td>
                <td><?= $portfolio['linguagemdes'];?></td>
                <td><?= $portfolio['descricao'];?></td>
                <td>
                    <a style="text-decoration:none; color:blue;" href="editar.php?id=<?=$portfolio['id'];?>">[ Editar ]</a>
                    <a style="text-decoration:none; color:red;" href="excluir.php?id=<?=$portfolio['id'];?>" onclick="return confirm('Tem certeza que deseja excluir?')">[ Excluir ]</a>
                </td>
            </tr>
        <?php endforeach; ?>
    </table> 

</body>