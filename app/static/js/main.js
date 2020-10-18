/*
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
*/

function compras() {

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

function adicionar() {

    let itens = JSON.parse(localStorage.getItem('carrinho'));
    
    for (let i = 0; i < itens.length; i++) { 
        
        let nome =  itens[i].nome;
        let preco = itens[i].valor;
        let qtd = itens[i].quantidade;

        let total = (parseFloat(preco.replace(',','.')) * parseInt(qtd))

        document.querySelector('#resultado').innerHTML += `\
            <tr>\
                <td style="word-wrap: break-word;"><a href="">` + nome + `</a></td>\
                <td style="word-wrap: break-word;">` + preco + `</td>\
                <td style="word-wrap: break-word;">` + parseInt(qtd) + `</td>\
                <td style="word-wrap: break-word;">` + total.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'}) + `</td>\
            </tr>`;

    };

};

function remover() {

    vendas();

    if (localStorage.length === 0) {

        console.log('Carrinho vazio!')

    } else {

        localStorage.removeItem('carrinho');

        console.log('Carrinho esvaziado!')

    };

};

function vendas() {

    let itens = JSON.parse(localStorage.getItem('carrinho'));

    let total = 0;

    for (let i = 0; i < itens.length; i++) { 
        
        let preco = itens[i].valor;
        let qtd = itens[i].quantidade;

        let soma = total + (parseFloat(preco.replace(',','.')) * parseInt(qtd))

    };

    console.log(soma);

};