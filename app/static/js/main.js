/*
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
*/

// JS
function adicionar() { // adiciona o item ao carrinho

    let produto = document.querySelector('#produto').textContent;
    let codigo = document.querySelector('#codigo');
    let preco = document.querySelector('#preco').textContent;
    let disponivel = document.querySelector('#dispo').textContent;
    let qtd = document.querySelector('#qtd').value;

    if (parseInt(disponivel) == 0) {

        window.alert('Produto Esgotado!');

    } else if (qtd > parseFloat(disponivel)) {

        window.alert('Quantidade Insuficiente!')

    } else {

        let compra = {
            nome: produto,
            ident: codigo,
            valor: preco,
            quantidade: qtd,
        };
        
        if (localStorage.getItem('carrinho') === null) {

            let itens = [];
            itens.push(compra);

            localStorage.setItem('carrinho', JSON.stringify(itens));

        } else {

            let itens = JSON.parse(localStorage.getItem('carrinho'));
            itens.push(compra);
            
            localStorage.setItem('carrinho', JSON.stringify(itens));

        };

    };

};

function adicionarRapido(produto, codigo, preco, status) { // faz uma adiçao rapida ao carrinho de um unico item

    let disponivel = status;
    let qtd = 1;

    if (disponivel == 'esgotado') {

        window.alert('Produto Esgotado!');

    } else {

        let compra = {
            nome: produto,
            ident: codigo,
            valor: preco,
            quantidade: qtd,
        };
        
        if (localStorage.getItem('carrinho') === null) {

            let itens = [];
            itens.push(compra);

            localStorage.setItem('carrinho', JSON.stringify(itens));

        } else {

            let itens = JSON.parse(localStorage.getItem('carrinho'));
            itens.push(compra);
            
            localStorage.setItem('carrinho', JSON.stringify(itens));

        };

    };
};

function compras() { // adiciona os os produtos selecionados ao carrinho
    
    if (localStorage.getItem('carrinho') === null) {} else {

        let itens = JSON.parse(localStorage.getItem('carrinho'));

        for (let i = 0; i < itens.length; i++) { 

            let nome =  itens[i].nome;
            let codigo = itens[i].codigo;
            let preco = itens[i].valor;
            let qtd = itens[i].quantidade;

            let total = (parseFloat(preco.replace(',','.')) * parseInt(qtd))

            document.querySelector('#resultado').innerHTML += `\
                <tr>\
                    <td style="word-wrap: break-word;">` + nome + `</td>\
                    <td style="word-wrap: break-word;">` + preco + `</td>\
                    <td style="word-wrap: break-word;">` + parseInt(qtd) + `</td>\
                    <td style="word-wrap: break-word;">` + total.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'}) + `</td>\
                    <td style="word-wrap: break-word;"><a href="/cart"><span onclick="removerItem(\'` + nome + `\')" class="botao-editar"><i class="fas fa-minus-circle"></i><span></a></td>\
                </tr>`;

        };
        
    };

};

function fecharVenda() { // mostra os resultados do carrinho

    confirmarVenda();

    let itens = JSON.parse(localStorage.getItem('carrinho'));

    var soma = 0;

    for (let i = 0; i < itens.length; i++) { 
        
        let preco = itens[i].valor;
        let qtd = itens[i].quantidade;

        let total = (parseFloat(preco.replace(',','.')) * parseInt(qtd));

        soma += total;

    };

    let resultadoVenda = {
        valor: soma,
    };

    if (localStorage.getItem('resultadoVenda') === null) {

        let resultadoVendas = [];
        resultadoVendas.push(resultadoVenda);

        localStorage.setItem('resultadoVenda', JSON.stringify(resultadoVendas));

    } else if (localStorage.getItem('resultadoVenda') != null) {} else {

        let resultadoVendas = JSON.parse(localStorage.getItem('resultadoVenda'));
        resultadoVendas.push(resultadoVenda);
        
        localStorage.setItem('resultadoVenda', JSON.stringify(resultadoVendas));

    };

    removerVenda();

};

function vendas() { // adiciona o valor total do carrinho

    let itens = JSON.parse(localStorage.getItem('carrinho'));

    var soma = 0;

    for (let i = 0; i < itens.length; i++) { 
        
        let preco = itens[i].valor;
        let qtd = itens[i].quantidade;

        let total = (parseFloat(preco.replace(',','.')) * parseInt(qtd));

        soma += total;

    };

    document.querySelector('#soma').innerHTML = `${soma.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}`;

};

function removerVenda() { // remove todos os itens do carrinho

    if (localStorage.length === 0) {} else {

        localStorage.removeItem('carrinho');

        localStorage.removeItem('resultadoVenda');

        localStorage.removeItem('cliente');

    };

};

function removerItem(nome) { // remove um item do carrinho
    
    let itens = JSON.parse(localStorage.getItem('carrinho'));
    
    for (let i = 0; i < itens.length; i++) {
        
        if (itens[i].nome === nome) {
            itens.splice(i, 1);
        };
        
        localStorage.setItem('carrinho', JSON.stringify(itens));
        
    };
    
};

function confirmarVenda() { // cria a confirmacao de venda 

    criarLista();
    
    if (document.querySelector('.confirmacao').style.display == 'none') {
        
        document.querySelector('.confirmacao').style.display = 'block';
        
    } else {
    
        document.querySelector('.confirmacao').style.display = 'none';
    
    };

    let itens = JSON.parse(localStorage.getItem('carrinho'));

    var soma = 0;

    for (let i = 0; i < itens.length; i++) { 
        
        let preco = itens[i].valor;
        let qtd = itens[i].quantidade;

        let total = (parseFloat(preco.replace(',','.')) * parseInt(qtd));

        soma += total;

    };
    
    document.querySelector('#valorTotal-form').value = `${soma.toLocaleString('pt-br',{minimumFractionDigits: 2})}`;

};

function criarLista() { // cria uma lista com os produtos da venda para o backend

    let recibo = JSON.parse(localStorage.getItem('carrinho'));

    let item = [];
    let codigo = [];
    let valor = [];
    let qtd = [];

    for (let i = 0; i < recibo.length; i++) { 
        
        item.push(recibo[i].nome);
        codigo.push(recibo[i].ident);
        valor.push((recibo[i].valor).replace(',','.'));
        qtd.push(recibo[i].quantidade);

    };

    document.querySelector('#item-local').value = `${item}`;
    document.querySelector('#codigo-local').value = `${codigo}`;
    document.querySelector('#valor-local').value = `${valor}`;
    document.querySelector('#qtd-local').value = `${qtd}`;

};

function tipoPagamento() { // espeficia o tipo de pagamento
    
    let tipoSelecao = document.querySelector('#tipoPagamento-form');
    let tipoSelecionado = tipoSelecao.options[tipoSelecao.selectedIndex].value;
    
    if (tipoSelecionado == 'dinheiro') {
        
        document.querySelector('#tipoDependencia').style.display = 'block';
        
    } else {
    
        document.querySelector('#tipoDependencia').style.display = 'none';
    
    };
};


function desconto() { // calcula o valor do desconto
    
    let itens = JSON.parse(localStorage.getItem('carrinho'));

    var soma = 0;

    for (let i = 0; i < itens.length; i++) { 
        
        let preco = itens[i].valor;
        let qtd = itens[i].quantidade;

        let total = (parseFloat(preco.replace(',','.')) * parseInt(qtd));

        soma += total;

    };

    let desconto = (document.querySelector('#valorDesconto-form').value).replace(',','.');

    let novoTotal = (soma - desconto);

    document.querySelector('#valorTotal-form').value = `${novoTotal.toLocaleString('pt-br',{minimumFractionDigits: 2})}`;

};

function troco() { // calcula o valor do troco

    let recebido = (document.querySelector('#valorRecebido-form').value).replace(',','.');
    let total = (document.querySelector('#valorTotal-form').value).replace('.','').replace(',','.');

    let troco = (recebido - total);

    document.querySelector('#valorTroco-form').value = `${troco.toLocaleString('pt-br',{minimumFractionDigits: 2})}`;

};
// JS

// JQUERY
$(document).ready(function() { // submit em um elemento tipo 'i'

    let pesquisa = $('#pesquisa');
    let pesquisar = $('#pesquisar');

    $(pesquisar).on('click', function() {

        pesquisa.submit();

    });

});
// JQUERY