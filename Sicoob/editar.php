<?php require 'config.php';

$info = [];
$id = filter_input(INPUT_GET, 'id');
if($id) {

    $sql = $pdo->prepare("SELECT * FROM portfoliodev WHERE id= :id");
    $sql->bindValue(':id', $id);
    $sql->execute();

    if($sql->rowCount() > 0) {

        $info = $sql->fetch(PDO::FETCH_ASSOC);

    } else {
        header("Location: index.php");
        exit;
   } 
   
}else {
    header("Location: index.php");
    exit;
}
?>

<h1>Editar Portfólio Dev</h1>

<form method="POST" action="editar_action.php">

    <input type="hidden" name="id" value="<?=$info['id'];?>">
    <label>
        Título Do Projeto:<br/>
        <input type="text" name="name" value="<?=$info['tituloprojeto'];?>" />        
    </label><br/><br/>
    <label>
        Linguagem Desenvolvida:<br/>
        <input type="text" name="secname" value="<?=$info['linguagemdes'];?>" />        
    </label><br/><br/>
    <label>
        Descrição:<br/>
        <input type="text" name="tername" value="<?=$info['descricao'];?>" />        
    </label><br/><br/>

    <input type="submit" value="Salvar" />

</form>