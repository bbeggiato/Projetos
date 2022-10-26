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

<body style = "background:lightblue; margin:30px"> 

<h1>Editar Portfólio Dev</h1>

<form method="POST" action="editar_action.php">

    <input type="hidden" name="id" value="<?=$info['id'];?>">
    <label>
        Título Do Projeto:<br/>
        <input style="height:30px;" type="text" name="name" size="40" value="<?=$info['tituloprojeto'];?>" />        
    </label><br/><br/>
    <label>
        Linguagem Desenvolvida:<br/>
        <input style="height:25px;" type="text" name="secname" size="30" value="<?=$info['linguagemdes'];?>" />        
    </label><br/><br/>
    <label>Descrição:</label><br/>
        <textarea id="mytextarea" name="tername" rows="10" cols="40"> 
            <?php echo $info['descricao'];?> 
        </textarea><br/><br/>

    <input type="submit" value="Salvar" />

</form>

</body>