let frases = ['Provérbios 1:7: "O temor do Senhor é o princípio do saber, mas os insensatos desprezam a sabedoria e o ensino".', 'Provérbios 3:5-6: "Confie no Senhor de todo o seu coração e não se estribe no seu próprio entendimento. Reconheça o Senhor em todos os seus caminhos, e ele endireitará as suas veredas".', 'Provérbios 9:10: "O temor do Senhor é o princípio da sabedoria, e o conhecimento do Santo é prudência." ', 'Provérbios 4:23: "Sobre tudo o que se deve guardar, guarda o teu coração, porque dele procedem as fontes da vida".','Provérbios 15:1: "A resposta branda desvia o furor, mas a palavra dura suscita a ira."', 'Provérbios 16:3: "Consagre ao Senhor tudo o que você faz, e os seus planos serão bem-sucedidos".', 'Provérbios 18:21: "A morte e a vida estão no poder da língua; o que bem a utiliza come do seu fruto."', 'Provérbios 14:1: "A mulher sábia edifica a sua casa, mas com as próprias mãos a insensata derruba a sua".', 'Provérbios 17:17: "O amigo ama em todos os momentos; é um irmão na adversidade".', 'Provérbios 22:1: "Mais vale o bom nome do que as muitas riquezas; e o favor é melhor do que a prata e o ouro."']
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