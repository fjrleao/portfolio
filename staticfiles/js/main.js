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