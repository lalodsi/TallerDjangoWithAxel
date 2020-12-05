window.addEventListener('load', function() {
	let Grupos = document.getElementsByClassName("flex-container");
	for (let i = 0; i < 10 ; i++){
		let CuadroGrupo = document.createElement("div");
		let texto = document.createTextNode("Grupo número: " + (i + 1));
		CuadroGrupo.appendChild(texto);
		CuadroGrupo.setAttribute("ID","Contenido");
		CuadroGrupo.setAttribute("class","complement-1");
		Grupos[0].appendChild(CuadroGrupo);
	}
});