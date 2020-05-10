//controle de eventos do materialize
document.addEventListener('DOMContentLoaded', function() {
	let sidenav = document.querySelector('.sidenav')
    let materialBoxed = document.querySelectorAll('.materialboxed')
	let parallax = document.querySelectorAll('.parallax')
	let tooltip = document.querySelectorAll('.tooltipped')
	M.Tooltip.init(tooltip);
    M.Parallax.init(parallax)
    M.Sidenav.init(sidenav)
    M.Materialbox.init(materialBoxed)
})

function abreModal(botao){

	let corpo = document.getElementById('corpo-'+botao.name).textContent
	let titulo = document.getElementById('titulo-'+botao.name).textContent
	let titulo_modal = document.getElementById('titulo-modal')
	let corpo_modal = document.getElementById('corpo-modal')


	//preenche informações no modal
	corpo_modal.innerHTML = corpo
	titulo_modal.innerHTML = titulo

	//inicializa e abre o modal
	let modal = document.getElementById('modal')
    let initModal = M.Modal.init(modal)
	initModal.open()
}

//pega os botoes do menu
const botoesMenu = document.querySelectorAll('.sidenav li a')

//verifica clique nos botoes do menu
botoesMenu.forEach(item => {
	item.addEventListener('click', mudarDeSessao)
})

function mudarDeSessao(event){
	event.preventDefault()
	const elemento = event.target
	const idElemento = elemento.getAttribute('href')
	const sessao = document.querySelector(idElemento)

	const pxSessao = sessao.offsetTop

	window.scroll({
		top: pxSessao,
		behavior: "smooth"
	})
}