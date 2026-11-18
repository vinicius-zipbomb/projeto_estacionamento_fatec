# NOMES: ISABELA MARTINS, RAPHAEL PRADO, VINICIUS PRADO
# ENTREGA: 02/12/2026 até as 23:59
#
#                                       PROJETO: Estacionamento da FATEC
#
# Linhas (turnos): Manhã, Tarde, Noite
# Colunas (dias): Seg, Ter, Qua, Qui, Sex
# Cada célula: carros de cada turno em cada dia
# 
# Regra A — Estacionamento quase lotado
# O estacionamento tem 120 vagas. Encontre as células com mais de 90% das vagas ocupadas, ou seja, mais de 108 carros.
#
# Condição	valor > 108
# Exemplo	Manhã, Sex = 115 → entra  ·  Manhã, Seg = 88 → não entra
# O programa mostra	Manhã, Sex: 115 carros … e no final Total: N