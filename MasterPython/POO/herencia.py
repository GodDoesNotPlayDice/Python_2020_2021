import herenciaClases

persona = herenciaClases.Persona()
persona.setNombre('Vicente')
persona.setApellido('Vasquez')
persona.setAltura('160cm')
persona.setEdad('19 ages')

print(f'La persona es: {persona.getNombre()} {persona.getApellido()}')
print(persona.hablar())


informatico = herenciaClases.Informatico()
informatico.setNombre('Carlos')
informatico.setApellido('Martinez')
informatico.setEdad('19')

print(f'El informatico es: {informatico.getNombre()} {informatico.getApellido()} y el sabe {informatico.getLenguajes()}')
print(informatico.caminar())

print(informatico.experiencia)

tecnico = herenciaClases.TecnicoRedes()
tecnico.setNombre('Manolo')
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())