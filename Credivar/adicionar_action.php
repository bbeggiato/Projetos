<?php
require 'config.php';

$titulo = filter_input(INPUT_POST, 'name');
$linguagem = filter_input(INPUT_POST, 'secname');
$descricao = filter_input(INPUT_POST, 'tername');

If($titulo && $linguagem && $descricao) {
   
    $sql = $pdo->prepare("SELECT * FROM portfoliodev WHERE  tituloprojeto = :titulo");
    $sql->bindValue(':titulo', $titulo);
    $sql->execute();

    if ($sql->rowCount() === 0) {

       $sql = $pdo->prepare("INSERT INTO portfoliodev(tituloprojeto, linguagemdes, descricao) VALUES(:titulo, :linguagem, :descricao)");
       $sql->bindValue(':titulo', $titulo);
       $sql->bindValue(':linguagem', $linguagem);
       $sql->bindValue(':descricao', $descricao);
       $sql->execute();

       header("Location: index.php");
       exit;
    } else {
        header("Location: adicionar.php");
        exit;
    }
} else {
    header("Location: adicionar.php");
    exit;
}


   

 



