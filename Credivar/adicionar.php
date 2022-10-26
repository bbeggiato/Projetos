<body style = "background:lightblue; margin:30px">   


<h2>ADICIONAR DADOS</h2>

<form method="POST" action="adicionar_action.php" >
    <label>
        Título Do Projeto:<br/>
        <input style="height:30px;" type="text" name="name" size="40" placeholder="Digite o Título Aqui..." required/>        
    </label><br/><br/>
    <label>
        Linguagem Desenvolvida:<br/>
        <input style="height:25px;" type="text" name="secname" size="30" placeholder="Digite a Linguagem Aqui..." required/>        
    </label><br/><br/>

    <label>Descrição:</label><br/>

        <textarea  name="tername" rows="10" cols="40">        
        </textarea><br/><br/>

    <input type="submit" value="Adicionar" />
</form>

</body>
