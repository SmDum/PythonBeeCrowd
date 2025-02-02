hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())

inicio_total = hora_inicio * 60 + minuto_inicio
fim_total = hora_fim * 60 + minuto_fim

if fim_total > inicio_total:
    duracao_total = fim_total - inicio_total
    
elif inicio_total == fim_total:
    duracao_total = 24 * 60
    
else:
    duracao_total = (24 * 60 - inicio_total) + fim_total

horas = duracao_total // 60
minutos = duracao_total % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
