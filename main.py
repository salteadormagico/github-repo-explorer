import requests

def obtener_repos(usuario):
	repos_get = requests.get(f"https://api.github.com/users/{usuario}/repos", timeout = 5)
	repos_get.raise_for_status()
	repos = repos_get.json()
	return repos

def mostrar_repos(repos, datos):
	print(f"Usuario: {datos['login']}")
	print(f"Número de repositorios: {datos['public_repos']}")
	for i, repo in enumerate(repos, 1):
		print(f"{i}. {repo['name']} {repo['stargazers_count']}")

def mostrar_repositorio(repo):
	print(f"Nombre: {repo['name']}")
	print(f"Descripción: {repo['description']}")
	print(f"Estrellas: {repo['stargazers_count']}")
	print(f"Lenguaje: {repo['language']}")

while True:
	usuario = input("que usuario quieres buscar? ")

	if usuario.lower() == "salir":
		break

	try:		
		respuesta = requests.get(f"https://api.github.com/users/{usuario}", timeout = 5)
		respuesta.raise_for_status()
		datos = respuesta.json()
		try:
			repos = obtener_repos(usuario)
			mostrar_repos(repos, datos)
		except requests.RequestException as e:
			print(f"Error en la petición: {e}")
			continue
		if len(repos) < 1:
			print("Este usuario no tiene repositorios")
			continue
		while True:
			try:
					eleccion = input("¿Que repositorio quieres consultar?")
					if eleccion == "salir":
						break
					else:
						eleccion = int(eleccion)
						if 1 <= eleccion <= len(repos):
							consultar = repos[eleccion-1]
							mostrar_repositorio(consultar)
						else:
							print("Ese repositorio no existe")
			except ValueError:
				print("Debes introducir un número")
	except requests.RequestException as e:
		print(f"Error de conexión: {e}")
