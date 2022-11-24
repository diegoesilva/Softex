const express = require('express');
const app = express();

app.get('/', function (req, res){
    return res.send('Recebi um HTTP GET!')
});

app.post('/', function (req, res){
    return res.send('Recebi um HTTP POST!')
});

app.put('/', function (req, res){
    return res.send('Recebi um HTTP PUT!')
});

app.delete('/', function (req, res){
    return res.send('Recebi um HTTP DELETE!')
});

app.listen(8080, () =>{
    console.log('Servidor iniciado na porta 8080.')
});