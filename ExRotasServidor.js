const express = require('express');
const app = express();

app.get('/', function (req, res){
    res.send('Bem-vindos ao nosso site!')
});

app.get('/contato', function (req, res){
    res.send('Entre em contato através do email "empresatal@contato.com"')
});

app.get('/ajuda', function (req, res){
    res.send('Em que posso ajudar?')
});

app.listen(8080, () =>{
    console.log('Servidor iniciado na porta 8080.')
});