#atividades serve como dicionario para todas as funcionalidades de um proficional
atividades = {
    'pedreiro': ['construir', 'construção', 'reforma', 'reformar', 'assentamento', 'alvenaria', 'piso', 'forro', 'pavimentação', 'assentamento', 'alvenaria', 'reboco', 'concreto', 'argamassa'],
    'servente': ['construir', 'construção', 'reforma', 'reformar', 'assentamento', 'limpeza', 'capinar', 'reboco', 'catatumba', 'tumulo', 'escavação', 'nivelamento'],
    'encanador': ['banheiro', 'piscina', 'pia', 'sanitario', 'chuveiro', 'hidraulico', 'canalização', 'vazamento', 'tubulação', 'água', 'esgoto'],
    'pintor': ['pintar','pintura', 'retoque', 'textura', 'invernizar', 'tinta', 'grafite'],
    'eletricista': ['eletrico', 'instalar', 'tomada', 'interruptor', 'quadro de luz', 'fiação', 'iluminação', 'luminária'],
    'marceneiro': ['porta', 'madeira', 'móvel', 'armário', 'prateleira', 'escada', 'cama', 'sofá'],
    'vidraceiro': ['janela', 'vidro', 'box', 'espelho', 'blindex', 'esquadria'],
    'empreiteira especializada': ['demolição', 'demolir', 'terraplenagem', 'pavimentação', 'pavimentar', 'asfaltamento', 'construção civil', 'construtora'],
    'telhadista': ['telhado', 'pingueira', 'calha', 'cobertura', 'telha', 'impermeabilização', 'isolamento térmico', 'chaminé'],
    'azulejista': ['piso', 'piscina', 'cerâmica', 'mármore', 'granito', 'pastilha', 'porcelanato', 'revestimento', 'mosaico', 'ladrilho'],
    'gesseiro': ['gesso', 'forro', 'sancas', 'molduras', 'iluminação embutida', 'paredes de gesso', 'drywall'],
    'bombeiro hidráulico': ['hidraulico', 'piscina', 'encanamento', 'válvula', "caixa d'água", 'bombas', 'pressurizador'],
    'decorador': ['decoração', 'design de interiores', 'móveis', 'acabamento', 'ambiente', 'iluminação', 'cores', 'texturas'],
    'designer de interiores': ['decoração', 'design de interiores', 'projeto', 'mobiliário', 'iluminação', 'acabamentos', 'cores', 'texturas'],
    'arquiteto': ['projetar', 'reforma', 'arquitetura', 'construção civil', 'licenciamento', 'legalização', 'layout', 'paisagismo', 'iluminação', 'interiores', 'fachada', 'projeto estrutural', 'acompanhamento de obra'],
    'engenheiro civil': ['projetar', 'pavimentação', 'pavimentar', 'construção', 'construir', 'reforma', 'reformar', 'acompanhar', 'estrutura', 'geotecnia', 'hidráulica', 'saneamento', 'transporte', 'proteção contra incêndios', 'perícias e avaliações'],
    'serralheiro' : ['portão', 'ferro', 'academia', 'ubs', 'quadra', 'grades', 'estruturas metálicas', 'corrimão', 'guarda-corpo', 'escadas', 'portas de enrolar', 'coberturas metálicas']
}

# Ajudará (junto ao while) a identificar se é a primeira vez que é solicitado o objetivo
contador = 0

objetoObra = ''

while not objetoObra:
    if contador == 0:
      #caso seja digitado em maiusculo podemos usar lower que serve para deixar todas as entradas em menuculos, assim não tendo erros na consulta do array
        objetoObra = input("Qual objeto da obra?\n")
        contador += 1
    else:
        print("\nDesculpe, mas parece que você não informou nada")
        objetoObra = input("Qual objeto da obra?\n")

print("\nESTAMOS PROCESSANDO A INFORMAÇÃO")

# O comando split divide a string de entrada em um array de palavras para poder analisar se há alguma referência como o dicionário supracitado
palavrasObjeto = objetoObra.split(" ")

profissionais_recomendados = []

for palavra in palavrasObjeto:
    for profissional, atividades_profissional in atividades.items():
        if palavra in atividades_profissional:
            if profissional not in profissionais_recomendados:
                profissionais_recomendados.append(profissional)

if profissionais_recomendados:
    print("\nOs profissionais recomendados para essa tarefa são:")
    for profissional in profissionais_recomendados:
        print("- " + profissional)
else:
    print("Desculpe, mas por se tratar de um projeto de avaliação de conhecimentos de uma matéria de introdução, não possuo capacidade computacional para ajudar com esse objetivo.")
