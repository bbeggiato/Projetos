<?php
require 'config.php';
$id = filter_input(INPUT_POST, 'id');
$titulo = filter_input(INPUT_POST, 'name');
$linguagem = filter_input(INPUT_POST, 'secname');
$descricao = filter_input(INPUT_POST, 'tername');

If($titulo && $linguagem && $descricao) {
   
    $sql = $pdo->prepare("UPDATE portfoliodev SET tituloprojeto = :titulo, linguagemdes = :linguagem, descricao = :descricao WHERE id = :id");
    $sql->bindValue(':titulo', $titulo);
    $sql->bindValue(':linguagem', $linguagem);
    $sql->bindValue(':descricao', $descricao);
    $sql->bindValue(':id', $id);
    $sql->execute();   

    header("Location: index.php");
    exit;

} else {
    header("Location: adicionar.php");
    exit;
}
