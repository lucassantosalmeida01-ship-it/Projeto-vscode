let frases = ['F1', 'F2', 'F3', 'F4', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10']
let frasesCopiada = [...frases]

function geradorMensagens() {
    if (frases.length == 0) {
        frases = [...frasesCopiada]
    }
    let indiceGerado = Math.floor(Math.random()*(frases.length));
    let fraseGerada = frases[indiceGerado];
    document.querySelector("#msg").textContent = fraseGerada;
    frases.splice(indiceGerado, 1);
}

geradorMensagens()