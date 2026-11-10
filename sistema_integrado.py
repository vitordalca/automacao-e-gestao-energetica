
colonia_aurora = {
  "clima": {
    "vento_kmh":11,
    "tem_ext_celsius": -60
  },
  "sistema_energetico": {
    "geracao": {
      "solar": 40,
      "eolico": 0
    },
    "reserva_bateria": 45,
    "consumo_total": 70
  },
  "modulos": {
    "suporte_vida": {
      "prioridade": 1,
      "status": "LIGADO",
      "consumo": 30
    },
    "pesquisa_cientifica": {
      "prioridade": 2,
      "status": "LIGADO",
      "consumo": 30
    }
  }
}

vento_atual = colonia_aurora["clima"] ["vento_kmh"]
energia_solar = colonia_aurora["sistema_energetico"]["geracao"]["solar"]
bateria = colonia_aurora["sistema_energetico"]["reserva_bateria"]

print(f"--- DADOS DA COLÔNIA ---")
print(f"Vento atual: {vento_atual} km/h")
print(f"Geração Solar: {energia_solar} MW")
print(f"Nível da Bateria: {bateria}%")



def previsao_energia_eolica(historico_vento, historico_energia, vento_atual):
  n = len(historico_vento)

  media_x = sum(historico_vento) / n
  media_y = sum(historico_energia) / n

  numerador = 0
  denominador = 0
  for i in range(n):
    numerador += (historico_vento[i] - media_x) * (historico_energia[i] - media_y)
    denominador += (historico_vento[i] - media_x) ** 2

  m = numerador / denominador
  b = media_y - (m * media_x)

  previsao = (m * vento_atual) + b
  return previsao

lista_vento = [8,10, 12]
lista_energia = [20,25,30]

vento_hoje = colonia_aurora ["clima"]["vento_kmh"]
previsao_eolica = previsao_energia_eolica(lista_vento, lista_energia, vento_hoje)

colonia_aurora["sistema_energetico"]["geracao"]["eolico"] = previsao_eolica

print(f"\n--- PREVISÃO DE ENERGIA EÓLICA ---")
print(f"Histórico de ventos: {lista_vento}")
print(f"Histórico de energia gerada: {lista_energia}")
print(f"Vento de hoje: {vento_hoje} km/h -> Previsão Matemática: {previsao_eolica} MW")


def analise_decisao(colonia):
  print("\n--- ANÁLISE DE ENERGIA E DECISÕES ---")
  geracao_solar = colonia["sistema_energetico"]["geracao"]["solar"]
  geracao_eolica = colonia["sistema_energetico"]["geracao"]["eolico"]
  geracao_total = geracao_solar + geracao_eolica
  consumo_total = colonia["sistema_energetico"]["consumo_total"]
  bateria = colonia["sistema_energetico"]["reserva_bateria"]

  print(f"Entrada -> Geração: {geracao_total} MW | Consumo: {consumo_total} MW | Bateria: {bateria}%")

  if consumo_total > geracao_total and bateria < 50:
    
    if colonia["modulos"]["pesquisa_cientifica"]["status"] == "LIGADO":
      print("Ação -> Desligando Módulo de Pesquisa Científica (Prioridade 2)...")
      colonia["modulos"]["pesquisa_cientifica"]["status"] = "DESLIGADO"

      economia = colonia["modulos"]["pesquisa_cientifica"]["consumo"]
      colonia["sistema_energetico"]["consumo_total"] -= economia

      print("Ação -> Módulo de Suporte à Vida (Prioridade 1) mantido LIGADO com sucesso.")
      print(f"Ação -> Novo Consumo Total ajustado para: {colonia['sistema_energetico']['consumo_total']} MW")

  elif consumo_total > geracao_total:
    print("Saída -> ALERTA: Consumo maior que geração. Iniciar monitoramento da bateria.")
  elif geracao_total > consumo_total:
    print("Saída -> SUGESTÃO: Armazenar energia excedente nas baterias da base.")
  else:
    print("Saída -> STATUS: Balanço energético estável.")  

analise_decisao(colonia_aurora)

