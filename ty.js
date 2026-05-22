let nomes = ["Lukkinhas","Ana"];

function buscar() {
    let nomeBusca = document.querySelector("#input").value;
    for (let i = 0; i < nomes.length; i++) {
        if (nomeBusca == nomes[i]) {
            document.querySelector('#saida').textContent = nomeBusca + " encontrado :3"

        }
        break;
    }
}

buscar();