/*
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
*/

function adicionar() {

    let produto = document.querySelector('#produto').textContent;
    let preco = document.querySelector('#preco').textContent;
    let disponivel = document.querySelector('#dispo').textContent;
    let qtd = document.querySelector('#qtd').value;

    if (parseInt(disponivel) == 0) {

        window.alert('Produto esgotado!')

    } else {

        let compra = {
            nome: produto,
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

function compras() {
    
    if (localStorage.getItem('carrinho') === null) {} else {

        let itens = JSON.parse(localStorage.getItem('carrinho'));

        for (let i = 0; i < itens.length; i++) { 

            let nome =  itens[i].nome;
            let preco = itens[i].valor;
            let qtd = itens[i].quantidade;

            let total = (parseFloat(preco.replace(',','.')) * parseInt(qtd))

            document.querySelector('#resultado').innerHTML += `\
                <tr>\
                    <td style="word-wrap: break-word;">` + nome + `</td>\
                    <td style="word-wrap: break-word;">` + preco + `</td>\
                    <td style="word-wrap: break-word;">` + parseInt(qtd) + `</td>\
                    <td style="word-wrap: break-word;">` + total.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'}) + `</td>\
                    <td style="word-wrap: break-word;"><a href="/cart"><span onclick="removerItem(\'` + nome + `\')" class="span-titulo-2"><i class="fas fa-minus-circle"></i><span></a></td>\
                </tr>`;

        };
        
    };

};

function fecharVenda() {

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
    
    /*
    document.querySelector('#resultado-vendas').innerHTML += `\
        <tr>\
            <td><a href="/records"><span class="span-titulo-2"><i class="fas fa-user-edit"></i></span></a></td>\
            <td><span>${soma.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}</span></td>\
            <td>\
                <select name="" id="">\
                    <option value="">dinheiro</option>\
                    <option value="">debito</option>\
                    <option value="">credito</option>\
                </select>\
            </td>\
            <td><a href=""><span class="span-titulo-2"><i class="fas fa-search-plus"></i></span></a></td>\
            <td><a href=""><span class="span-titulo-2"><i class="fas fa-file"></i></span></a></td>\
            <td>\
                <select name="" id="">\
                    <option value="">aberto</option>\
                    <option value="">fechado</option>\
                </select>\
            </td>\
        </tr>`;
    */
    
    let recibo = JSON.parse(localStorage.getItem('carrinho'));
    
    console.log(recibo);
    
    confirmarVenda();

};

function vendas() {

    let itens = JSON.parse(localStorage.getItem('carrinho'));

    var soma = 0;

    for (let i = 0; i < itens.length; i++) { 
        
        let preco = itens[i].valor;
        let qtd = itens[i].quantidade;

        let total = (parseFloat(preco.replace(',','.')) * parseInt(qtd));

        soma += total;

    };

    document.querySelector('#soma').innerHTML = `${soma.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}`;
    
    return soma

};

function removerVenda() {

    if (localStorage.length === 0) {} else {

        localStorage.removeItem('carrinho');

        localStorage.removeItem('resultadoVenda');

        localStorage.removeItem('cliente');

    };

};

function removerItem(nome) {
    
    let itens = JSON.parse(localStorage.getItem('carrinho'));
    
    for (let i = 0; i < itens.length; i++) {
        
        if (itens[i].nome === nome) {
            itens.splice(i, 1);
        };
        
        localStorage.setItem('carrinho', JSON.stringify(itens));
        
    };
    
};

function confirmarVenda() {
    
    if (document.querySelector('#confirmacao').style.display == 'none') {
        
        document.querySelector('#confirmacao').style.display = 'block';
        
    } else {
    
        document.querySelector('#confirmacao').style.display = 'none';
    
    };

};

/*

function tipoPagamento() {
    
    let tipoSelecao = document.querySelector('#tipoPagamento-form');
    let tipoSelecionado = tipoSelecao.options[tipoSelecao.selectedIndex].value;
    
    if (tipoSelecionado == 'dinheiro') {
        
        document.querySelector('#tipoDependencia').style.display = 'block';
        
    } else {
    
        document.querySelector('#tipoDependencia').style.display = 'none';
    
    };
};

function calculo() {
    
    let total = vendas();
    
    document.querySelector('#valorTotal-form').value = `${total}`;
    
    let desconto = document.querySelector('#valorDesconto').value;
    let recebido = document.querySelector('#valorRecebido').value;
    let troco = document.querySelector('#valorTroco').value;
    
    if (desconto != null) {
    
        let totalDescontado = (total - desconto)
        
        document.querySelector('#valorTotal-form').value = `${totalDescontado}`;
        
    } else {};
    
    if (recebido != null) {
        
        if (desconto != null) {
    
            let totalTroco = ((total - desconto) - recebido)
            
            document.querySelector('#valorTroco').value = `${totalTroco}`;
            
        } else {
            
            let totalTroco = (total - recebido)
            
            document.querySelector('#valorTroco').value = `${totalTroco}`;
            
        };

    } else {};

};
*/

