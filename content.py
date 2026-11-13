# -*- coding: utf-8 -*-
# Conteúdo revisado do Guia Educacional da Trilha Ecológica do Estuário do Rio Pacoti
# Autor do texto original: Erick Souza da Rocha. Revisão técnica: PEAM (nov/2026).
# Marcação: **negrito**, [[a confirmar: ...]] = pendência visível no rascunho.

TH = {  # temas por ambiente (cores amostradas dos slides do Erick)
 'agua':   dict(name='Apresentação', rib='#275db1', lab='#2280b8', bg='#dfeeee', ink='#14315f', soft='#eef6f6', dark=False),
 'trilha': dict(name='A trilha', rib='#275db1', lab='#2280b8', bg='#dfeeee', ink='#14315f', soft='#eef6f6', dark=False),
 'tab':    dict(name='Mata de tabuleiro', rib='#53683d', lab='#7d960f', bg='#ba9f49', ink='#2f3b1f', soft='#f6f2e2', dark=True),
 'mang':   dict(name='Manguezal', rib='#1f8a63', lab='#339d70', bg='#6d6156', ink='#16422f', soft='#eef7f2', dark=True),
 'api':    dict(name='Apicum', rib='#b46502', lab='#ad8400', bg='#eddac5', ink='#5a3505', soft='#fbf4ea', dark=False),
 'fim':    dict(name='Encerramento', rib='#275db1', lab='#2280b8', bg='#dfeeee', ink='#14315f', soft='#eef6f6', dark=False),
}

# Cada página: dict(th, title, tag (subtítulo da faixa), blocks=[...])
# Blocos:
#  ('card', label, [parágrafos])
#  ('list', label, [itens])
#  ('sp', dict(name, sci, img, pos, items=[...], note=..., extra=[(img,legenda)]))
#  ('gal', label, [(nome, sci, img)])
#  ('note', texto)   -> caixa de destaque
#  ('img', arquivo, legenda)
P = []

def pg(th, title, tag, *blocks, sec=None):
    P.append(dict(th=th, title=title, tag=tag, blocks=list(blocks), sec=sec))

# ---------------- APRESENTAÇÃO
pg('agua','Apresentação','PEAM',
 ('card','Introdução',[
  'O **Programa de Educação Ambiental Marinha (PEAM)** é um programa de extensão da Universidade Federal do Ceará (UFC), criado em **1988** e hoje coordenado pela Dra. Ravena Nogueira, ecóloga e servidora do Instituto de Ciências do Mar (LABOMAR).',
  'Desde a sua criação, o PEAM tem como missão **aproximar ciência e comunidade**, promovendo a educação ambiental marinha e costeira por meio de atividades interativas, práticas e acessíveis a diferentes públicos.']),
 ('card','Objetivo',[
  'Sensibilizar a sociedade e formar cidadãos conscientes da importância do ambiente marinho e costeiro diante dos impactos ambientais e das mudanças climáticas, estimulando atitudes de **conservação**, o **uso sustentável** dos recursos naturais, o **respeito à biodiversidade** e o **sentimento de pertencimento** em relação ao litoral cearense.',
  'O programa atende um público amplo e diverso, de crianças a idosos, de diferentes classes sociais e níveis de escolaridade.']), sec='apresentacao')

pg('agua','Apresentação','PEAM',
 ('card','Estrutura',[
  'O PEAM funciona como um **programa guarda-chuva**: abriga diferentes projetos e frentes de atuação, todos com foco na educação ambiental participativa. Entre eles:']),
 ('list','Projetos',[
  '**Acervo da Vida Marinha**: exemplares da fauna e da flora marinha, costeira e estuarina, em acervo fixo e itinerante, levado a escolas, comunidades e eventos em diferentes municípios.',
  '**Trilha do Estuário do Rio Pacoti**: visitas guiadas na Área de Proteção Ambiental (APA) do Rio Pacoti, em que monitores interpretam a fauna, a flora e a dinâmica do estuário.']),
 ('img','p03_4.jpg','Letreiro do PEAM no CEAC.'))

pg('agua','Apresentação','CEAC',
 ('card','Introdução',[
  'O **Centro de Estudos Ambientais Costeiros (CEAC)** é a base de campo do LABOMAR, às margens do Rio Pacoti, dentro da APA do Rio Pacoti, em Eusébio. Funciona como estação avançada de **pesquisa, educação e extensão** da UFC e abriga o PEAM e outras atividades do instituto.']),
 ('card','Origem',[
  'O CEAC foi viabilizado por uma parceria entre a UFC, a **Prefeitura Municipal de Eusébio** e a **Fundação Alphaville**. O terreno foi doado à universidade pela Prefeitura em **2021**, consolidando a presença do LABOMAR no estuário do Rio Pacoti e criando um espaço que une pesquisa, extensão e conservação. [[a confirmar: data exata da doação e se houve compensação ambiental]]']),
 ('img','p06_4.jpg','Vista aérea do CEAC, às margens do Rio Pacoti.'))

pg('agua','Apresentação','CEAC',
 ('card','Objetivos',[
  'O CEAC é um laboratório natural e um núcleo de apoio científico e educativo. Ele **apoia as atividades do PEAM**, com estrutura para trilhas, oficinas, palestras e exposições; **serve de base para pesquisas** sobre o estuário, o manguezal e os ecossistemas costeiros; **recebe escolas, universidades e comunidades**; e ajuda a **conservar a biodiversidade**, com ações de manejo, recuperação e monitoramento.']),
 ('list','Estrutura',[
  '**Laboratório de Carcinicultura**: cultivo e manejo de camarões.',
  '**Laboratório de Peixes Ornamentais**: estudos de espécies aquáticas e reprodução controlada.',
  '**Centro de Atendimento Emergencial às Tartarugas Marinhas**: resgate de tartarugas feridas ou em risco.',
  '**Laboratório de Educação Marinha e Inclusão Socioambiental (LAMARIS)**: onde as atividades do PEAM são planejadas.',
  '**Trilha Ecológica do Estuário do Rio Pacoti**: percurso que parte do CEAC e funciona como espaço de aprendizado vivo.']))

pg('agua','Apresentação','APA',
 ('card','Definição',[
  '**APA** significa **Área de Proteção Ambiental**, uma unidade de conservação de **uso sustentável** prevista na Lei nº 9.985/2000 (SNUC). Ela protege áreas naturais importantes e permite atividades humanas, desde que respeitem regras de manejo e não causem danos significativos ao ambiente.',
  'Seus objetivos são preservar ecossistemas frágeis, disciplinar o uso do solo (evitando ocupações irregulares e poluição), conservar os recursos hídricos e a biodiversidade e incentivar o turismo ecológico e a educação ambiental.']),
 ('card','APA do Rio Pacoti',[
  'Criada pelo **Decreto Estadual nº 25.778/2000**, a APA do Rio Pacoti fica no baixo curso e no estuário do rio, nos municípios de **Fortaleza, Eusébio e Aquiraz**, com área de **2.914,93 ha**. As nascentes do rio estão na APA da Serra de Baturité, e no médio curso fica o Corredor Ecológico do Rio Pacoti.']))

pg('agua','Apresentação','APA',
 ('card','Objetivos',[
  'A APA do Rio Pacoti foi criada para preservar os ecossistemas da região, como **dunas, manguezais, mata de tabuleiro e praias**, uma área de equilíbrio ecológico frágil que precisa de proteção especial do poder público e da sociedade.',
  'Ao mesmo tempo, a unidade permite atividades econômicas, sociais, culturais e científicas, como a **pesca artesanal**, o **turismo**, a **agricultura familiar** e os **festejos tradicionais**. Além da beleza da paisagem, a bacia do Rio Pacoti tem importância estratégica para o **abastecimento de água de Fortaleza**.']),
 ('img','p12_1.jpg','Imagem de satélite da APA do Rio Pacoti. O CEAC fica na margem do estuário.'))

# ---------------- TRILHA
pg('trilha','Trilha Ecológica','Introdução',
 ('card','Introdução',[
  'A Trilha Ecológica do Rio Pacoti proporciona uma **vivência direta** com diferentes ecossistemas costeiros, para que os visitantes compreendam, na prática, a importância da conservação. A proposta é sensibilizar para as funções ecológicas desses ambientes, a sua biodiversidade e a sua relevância para as comunidades humanas.',
  'Ao longo do percurso, os participantes conhecem três ecossistemas principais: a **mata de tabuleiro**, o **manguezal** e o **apicum**. Eles estão interligados e formam um **gradiente ecológico**, que mostra como a paisagem muda à medida que nos aproximamos do estuário.']),
 ('img','p16_1.jpg','Mapa do percurso da trilha a partir do CEAC.'), sec='trilha')

pg('trilha','Trilha Ecológica','Recomendações',
 ('list','Antes e durante a trilha',[
  'Use **calçados fechados**.','Leve **água** para se hidratar.','Use **protetor solar**.','Aplique **repelente**.',
  'Evite **tocar** em plantas e animais.','Não **retire** elementos naturais.','Não deixe **lixo** ao longo da trilha.','Siga as **orientações dos monitores**.']),
 ('note','Na trilha vivem animais peçonhentos, como a cobra-coral e algumas aranhas. Observe de longe e nunca tente pegar um animal.'))

# ---------------- MATA DE TABULEIRO
T='tab'
pg(T,'Mata de Tabuleiro','Introdução',
 ('card','Introdução',[
  'A mata de tabuleiro é o **primeiro ambiente** da trilha. Ela faz parte das formações vegetais que ocorrem sobre os **tabuleiros costeiros** do Nordeste, áreas relativamente planas e um pouco mais altas que as planícies litorâneas.',
  'No litoral do Ceará, aparece em manchas descontínuas e funciona como uma **zona de transição ecológica**, reunindo espécies típicas da **Caatinga, do Cerrado e da Mata Atlântica**. Essa mistura gera grande diversidade de plantas e animais e ajuda a proteger **nascentes e aquíferos**.']), sec='tabuleiro')

pg(T,'Mata de Tabuleiro','Formação',
 ('card','Formação',[
  'Os tabuleiros costeiros são formações geológicas antigas (**Formação Barreiras**), originadas do acúmulo de sedimentos marinhos e fluviais ao longo de milhões de anos, quando o nível do mar variava. Com o tempo, esses depósitos se consolidaram e formaram planaltos baixos, planos ou suavemente ondulados, perto do litoral.',
  'Os solos são, em geral, **arenosos ou areno-argilosos**, com baixa fertilidade natural e drenagem rápida: a água se infiltra depressa. Por isso, podem ocorrer períodos de **escassez hídrica**, que influenciam a vegetação e os animais que vivem ali.']))

pg(T,'Mata de Tabuleiro','Flora',
 ('card','Flora',[
  'É uma **mata densa**, com árvores e arbustos de muitas espécies, que apresentam diferentes adaptações à pouca água no solo: folhas mais espessas, **queda parcial das folhas** na estação seca e raízes profundas.',
  'A vegetação depende da rápida ciclagem de nutrientes da **serrapilheira** (folhas, galhos e cascas que caem no chão). Essa camada mantém a umidade do solo, reduz a erosão e evita o ressecamento. Pequenos organismos fragmentam o material, e os microrganismos o decompõem, devolvendo os nutrientes ao solo.',
  'Apesar da forte insolação, a estrutura da mata forma um **microclima mais ameno** e serve de **refúgio para a fauna**.']),
 ('pair',[('p20_5.jpg','Placa da trilha sobre a mata de tabuleiro.'),('p20_6.jpg','Placa da trilha sobre a fauna local.')]))

def sp(th,title,tag,name,sci,img,items,note=None,extra=None,pos='50% 50%',flag=None,sec=None):
    pg(th,title,tag,('sp',dict(name=name,sci=sci,img=img,items=items,note=note,extra=extra or [],pos=pos,flag=flag)),sec=sec)

sp(T,'Mata de Tabuleiro','Flora','Imburana','Commiphora leptophloeos','p21_6.jpg',[
 'Típica de regiões **semiáridas**, pode crescer de 6 a 9 m de altura.',
 'O tronco tem **casca lisa, fina e descamante**, que ajuda a proteger a planta do fogo.',
 'Sua madeira é usada em **marcenaria**, sobretudo em móveis e serviços leves.',
 'Na **medicina popular**, é usada para problemas respiratórios e digestivos, em garrafadas, xaropes e banhos.'])

sp(T,'Mata de Tabuleiro','Flora','Torém','Cecropia pachystachya','p22_6.jpg',[
 'Também chamada de **embaúba**, é uma espécie **pioneira** de crescimento rápido, comum em todo o país; cresce de 10 a 20 m.',
 'Seus frutos alimentam **aves, morcegos e pequenos mamíferos**. Em outras regiões do Brasil, as folhas são um dos alimentos preferidos das **preguiças**, que hoje são consideradas provavelmente extintas no Ceará.',
 'Costuma ter uma relação de **mutualismo com formigas**, que vivem no seu tronco oco e a defendem.',
 'Tem usos na medicina popular para problemas respiratórios, pressão alta e inflamações.'])

sp(T,'Mata de Tabuleiro','Flora','Barriguda','Ceiba sp.','p23_6.jpg',[
 'Árvore da família das paineiras, típica do Nordeste; cresce de 6 a 18 m e é adaptada ao clima seco.',
 'O **tronco dilatado**, em forma de barriga, armazena água para os períodos de estiagem.',
 'Na estação chuvosa produz **flores grandes e vistosas**, que atraem polinizadores.',
 'As sementes são levadas pelo **vento** (anemocoria), envoltas numa fibra branca e leve, a **paina**.'],
 flag='a confirmar: espécie de Ceiba registrada na APA (Rabelo, 2022)')

sp(T,'Mata de Tabuleiro','Flora','Coaçu','Coccoloba latifolia','p24_6.jpg',[
 'Árvore do Nordeste, pouco ramificada, de 5 a 12 m. Na APA do Rio Pacoti há registros dela **perto do CEAC**, onde também é chamada de **cabeça-de-macaco**.',
 'Chama atenção pelo contraste entre o tronco fino e as **folhas muito grandes**, que captam mais luz, fazem sombra e ajudam a manter a umidade do solo.',
 'Na Amazônia vive uma parente, a ***Coccoloba gigantifolia***, que tem **a maior folha entre as dicotiledôneas**, com até 2,5 m de comprimento.'])

sp(T,'Mata de Tabuleiro','Flora','Carnaúba','Copernicia prunifera','p25_10.jpg',[
 'É a **árvore-símbolo do Ceará** (Decreto Estadual nº 27.413/2004) e é conhecida como **"árvore da vida"**, porque quase todas as suas partes podem ser aproveitadas.',
 'As folhas são usadas no **artesanato tradicional** e em brincadeiras infantis, e os frutos alimentam diversos animais.',
 'O tronco, duro e resistente a cupins e à umidade, é valioso na **construção rural**.',
 'As raízes são usadas em chás da medicina popular.'], pos='50% 35%')

pg(T,'Mata de Tabuleiro','Flora',
 ('sp',dict(name='Carnaúba',sci='Copernicia prunifera',img='p27_12.jpg',pos='50% 50%',flag=None,extra=[],items=[
  'As folhas são cobertas por uma camada de **cera**, que evita a perda de água e protege a planta do calor.',
  'A **cera de carnaúba** tem grande valor econômico e é usada em cosméticos, medicamentos, alimentos (como cobertura de balas e frutas), vernizes e polidores. No fim do século XIX, foi usada até nos **cilindros dos primeiros fonógrafos**.'],
  note=None)),
 ('sp',dict(name='Unha-do-diabo',sci='Cryptostegia madagascariensis',img='p27_14.jpg',pos='50% 50%',flag=None,extra=[],items=[
  'Trepadeira **exótica e invasora**, vinda de Madagascar, também chamada de viúva-alegre. Envolve o tronco e as folhas da carnaúba e pode **matar a palmeira**.',
  'Está na lista oficial de **plantas exóticas invasoras do Ceará** (Portaria SEMA nº 155/2022).'],note=None)))

sp(T,'Mata de Tabuleiro','Flora','Gameleira','Ficus gomelleira','p28_6.jpg',[
 'Também chamada de **figueira-mata-pau**; pode chegar a 20 m, com copa larga e muita sombra, e forma **raízes aéreas** que viram colunas.',
 'Muitas vezes **começa a crescer sobre outra árvore**: os ramos buscam a luz e as raízes descem até o solo. Com o tempo, as raízes envolvem a árvore hospedeira, que acaba **estrangulada**.',
 'Quando a hospedeira apodrece, forma-se um grande **oco**, que vira abrigo para muitos animais. Os frutos alimentam a fauna ao longo do ano.',
 'A madeira era usada para fazer **gamelas**. Em tradições afro-brasileiras, é considerada **árvore sagrada**, ligada à ancestralidade.'],
 extra=[('p29_3.jpg','Raízes da gameleira envolvendo o tronco.')], flag='a confirmar: espécie de Ficus da foto')

sp(T,'Mata de Tabuleiro','Flora','Croatá','Bromelia karatas','p30_6.jpg',[
 'Bromélia **terrestre** de folhas espinhosas, comum no semiárido; forma touceiras de 1 a 1,5 m.',
 'Seus **frutos amarelos** são comestíveis e servem de alimento para animais silvestres.',
 'Muitas bromélias acumulam água entre as folhas, formando um pequeno ecossistema chamado **fitotelmo**, onde vivem insetos, aranhas e anfíbios.'],
 note='**Sapinho-de-maranguape** (*Adelophryne maranguapensis*): anfíbio de cerca de 2 cm que só existe nas partes altas da **Serra de Maranguape**, onde vive em bromélias. Os ovos eclodem já como **sapinhos, sem fase de girino** (desenvolvimento direto). Está **criticamente em perigo** nas listas nacional e estadual.',
 extra=[('p30_8.jpg','Sapinho em uma folha de bromélia.')])

sp(T,'Mata de Tabuleiro','Flora','Orquídea','Rodriguezia sp.','p31_6.jpg',[
 'É uma orquídea **epífita**: vive apoiada sobre outra planta, sem retirar nutrientes dela.',
 'Usa a árvore só como suporte. Com as **raízes aéreas**, absorve água e nutrientes da umidade do ar e da matéria orgânica acumulada.',
 'É muito sensível a alterações ambientais e pode indicar a **qualidade do ambiente**.',
 'Há crenças populares que associam as orquídeas à boa sorte e à prosperidade.'],
 flag='a confirmar: no Ceará há registro de Rodriguezia bracteata')

pg(T,'Mata de Tabuleiro','Fauna',
 ('card','Fauna',[
  'Mesmo fragmentada, a mata abriga uma fauna diversa: **vertebrados** (mamíferos, aves, répteis e anfíbios) e **invertebrados** (insetos, aracnídeos, anelídeos e moluscos). Esses animais polinizam flores, dispersam sementes e reciclam nutrientes.',
  'Essa fauna é ameaçada pela **expansão agrícola e urbana**, que reduz e isola os habitats, além da **caça**, do **tráfico de animais silvestres**, das queimadas, dos eventos climáticos extremos e das **espécies invasoras**.']))

pg(T,'Mata de Tabuleiro','Fauna · insetos',('gal','Insetos',[
 ('Formiga-gigante','Dinoponera quadriceps','p33_5.jpg'),('Saúva','Atta sp.','p33_6.jpg'),
 ('Rola-bosta','Canthidium sp.','p33_8.jpg'),('Cavalo-do-cão','Pepsis sp.','p33_7.jpg')]))

pg(T,'Mata de Tabuleiro','Fauna · aracnídeos',('gal','Aracnídeos',[
 ('Viúva-marrom','Latrodectus geometricus','p34_6.jpg'),('Caranguejeira','Iridopelma hirsutum','p34_5.jpg'),('Aranha-de-prata','Argiope argentata','p34_7.jpg')]),
 ('note','A **viúva-marrom** é uma espécie **exótica**, provavelmente de origem africana, comum em construções. Ela e a caranguejeira não devem ser manuseadas.'))

pg(T,'Mata de Tabuleiro','Fauna · répteis',('gal','Répteis',[
 ('Teju','Salvator merianae','p35_9.jpg'),('Jiboia','Boa constrictor','p35_5.jpg'),('Salamanta','Epicrates assisi','p35_6.jpg'),
 ('Coral-verdadeira','Micrurus ibiboboca','p35_10.jpg'),('Calango','Tropidurus sp.','p35_7.png'),('Iguana','Iguana iguana','p35_8.jpg')]),
 ('note','A **coral-verdadeira** é peçonhenta. Se encontrar uma, afaste-se e avise o monitor.'))

pg(T,'Mata de Tabuleiro','Fauna · aves',('gal','Aves',[
 ('Caburé','Glaucidium brasilianum','p36_9.jpg'),('Tuim','Forpus xanthopterygius','p36_6.jpg'),('Choca-barrada-do-nordeste','Thamnophilus capistratus','p36_12.jpg'),
 ('Cancão','Cyanocorax cyanopogon','p36_7.jpg'),('Beija-flor-tesoura','Eupetomena macroura','p36_8.jpg'),('Periquito-da-caatinga','Eupsittula cactorum','p36_2.jpg')]))

pg(T,'Mata de Tabuleiro','Fauna · mamíferos',('gal','Mamíferos',[
 ('Cassaco','Didelphis sp.','p37_6.jpg'),('Mão-pelada','Procyon cancrivorus','p37_10.jpg'),('Capivara','Hydrochoerus hydrochaeris','p37_7.jpg'),('Raposinha','Cerdocyon thous','p37_2.png')]),
 ('note','A **capivara** chegou a ser considerada extinta no Ceará nos anos 1970. As que vivem hoje na Região Metropolitana de Fortaleza vêm de reintroduções e de solturas sem controle, e os órgãos ambientais estudam um plano de manejo.'))

# ---------------- MANGUEZAL
M='mang'
pg(M,'Manguezal','Introdução',
 ('card','Introdução',[
  'Na trilha, o manguezal é um dos ambientes mais importantes para a biodiversidade. É um dos ecossistemas **mais produtivos do planeta** e sustenta cadeias alimentares marinhas e costeiras. Por isso é chamado de **berçário da vida marinha**: muitas espécies usam o mangue para se reproduzir e crescer.',
  'É um ecossistema típico de regiões **tropicais e subtropicais**, que ocorre na transição entre os ambientes terrestre, fluvial e marinho, onde a **água doce dos rios encontra a água salgada do mar** (estuários, baías e lagunas).']), sec='manguezal')

pg(M,'Manguezal','Formação',
 ('card','Formação',[
  'Os manguezais se formam em **planícies fluviomarinhas**, moldadas pelos rios e pelo mar. São áreas de **águas calmas**, onde se depositam os sedimentos trazidos pelos rios e os sais vindos do mar.',
  'O estuário do Rio Pacoti recebe **pouca água doce**, sobretudo na estação seca, e por isso pode ficar **mais salgado que o próprio mar** (hipersalino).',
  'As **marés** inundam a área periodicamente e redistribuem sedimentos, nutrientes e sais. O solo encharcado tem **pouco oxigênio** (é anóxico): os decompositores trabalham devagar e a matéria orgânica não se decompõe totalmente. O resultado é um solo **salgado, lamacento, escuro e rico em matéria orgânica**.']))

pg(M,'Manguezal','Ciclo da matéria',
 ('card','Ciclo da matéria',[
  'Grande parte da energia que sustenta o manguezal não vem das plantas vivas, mas da **matéria orgânica morta**, o **detrito** (cadeia detritívora).',
  'Folhas e galhos que caem são degradados por **fungos e bactérias**, que reciclam os nutrientes. Poliquetas, moluscos e crustáceos se alimentam desses detritos e dos microrganismos; depois, servem de alimento para **peixes e aves**.']),
 ('note','O cheiro de **"ovo podre"** do mangue vem do **sulfeto de hidrogênio (H₂S)**, um gás produzido pelas bactérias que decompõem a matéria sem oxigênio.'))

pg(M,'Manguezal','Ciclo do carbono',
 ('card','Carbono azul',[
  'Os manguezais são grandes reservatórios de **carbono azul**, o carbono capturado e armazenado por ecossistemas costeiros e marinhos, como marismas e pradarias marinhas.',
  'O mangue cresce rápido e captura o **CO₂** da atmosfera. Ele armazena esse carbono nas árvores e, sobretudo, **no solo**: sem oxigênio, a matéria orgânica se decompõe devagar e o carbono fica enterrado por muito tempo.',
  'Por hectare, os manguezais podem estocar **de três a quatro vezes mais carbono** que muitas florestas tropicais, a maior parte no solo (Donato et al., 2011).',
  'Quando o mangue é desmatado, esse carbono volta para a atmosfera e **agrava o efeito estufa**. Conservar os manguezais é proteger a biodiversidade, as comunidades costeiras e o **clima do planeta**.']))

pg(M,'Manguezal','Flora',
 ('card','Flora',[
  'A vegetação do manguezal é chamada de **mangue**. Ela produz a matéria orgânica que sustenta a cadeia alimentar, segura o solo, protege a linha da costa e cria habitats para muitos animais.',
  'São **poucas espécies**, mas com adaptações notáveis às condições extremas: só plantas **halófitas** (tolerantes ao sal) conseguem viver ali. No Rio Pacoti ocorrem o mangue-vermelho, duas espécies de mangue-preto, o mangue-branco e o mangue-de-botão.']))

sp(M,'Manguezal','Flora','Mangue-vermelho','Rhizophora mangle','p44_5.jpg',[
 'Ocupa as áreas **mais próximas da água**, inundadas com mais frequência pelas marés.',
 'Tem **raízes-escora**: raízes aéreas arqueadas que saem do tronco e dos galhos, estabilizam a árvore, retêm sedimentos, reduzem a força das correntes e criam abrigo para peixes, moluscos e crustáceos.',
 'Apresenta **viviparidade**: a semente germina ainda presa à planta-mãe e forma o **propágulo** (a "caneta do mangue"), que cai e se fixa na lama ou é levado pela água.',
 'Tem **lenticelas**, pontinhos brancos no caule e nas raízes que fazem as trocas gasosas.'],
 extra=[('p45_4.jpg','Propágulos.'),('p45_5.jpg','Lenticelas.')])

sp(M,'Manguezal','Flora','Mangue-preto','Avicennia germinans e A. schaueriana','p46_4.jpg',[
 'No Rio Pacoti ocorrem **duas espécies** de mangue-preto.',
 'Aparecem em áreas um pouco **mais altas**, ainda inundadas, mas com menos intensidade.',
 'As folhas são alongadas e têm **glândulas de sal**, que eliminam o excesso de sal.',
 'Têm raízes que crescem para cima, saindo da lama como pequenos "lápis": os **pneumatóforos**, que ajudam na respiração.'])

sp(M,'Manguezal','Flora','Mangue-branco','Laguncularia racemosa','p47_4.jpg',[
 'Aparece nas partes **mais altas** do manguezal, onde a maré chega com menos frequência, e na transição com outros ambientes costeiros.',
 'Tem folhas arredondadas, com **pecíolo avermelhado** e duas pequenas glândulas na base da folha.',
 'Também elimina sal pelas folhas e tem pneumatóforos menos desenvolvidos.'],
 flag='a confirmar com especialista: descrição das glândulas')

sp(M,'Manguezal','Flora','Mangue-de-botão','Conocarpus erectus','p48_4.jpg',[
 'Cresce nas partes mais altas, perto do **apicum** ou da terra firme.',
 'Tem folhas pequenas e coriáceas e tolera bem a **seca** e a **alta salinidade**.',
 'As flores se reúnem em pequenos **"botões"** esféricos, que dão nome à planta.',
 'Não tem raízes-escora nem pneumatóforos evidentes; por se adaptar também à terra firme, alguns cientistas não o consideram um mangue verdadeiro.'])

pg(M,'Manguezal','Fauna',
 ('card','Fauna',[
  'A fauna do manguezal é muito diversa e adaptada a esse ambiente. Participa da ciclagem de nutrientes e forma uma **teia alimentar** complexa. O mangue é abrigo, área de alimentação, reprodução e crescimento para animais terrestres, aquáticos e semiaquáticos.',
  'No Rio Pacoti, muitos organismos vivem nas **raízes, na lama, nos troncos e nos canais de maré**: moluscos, crustáceos, peixes, aves e mamíferos.']),
 ('card','Moluscos',[
  'Os moluscos são invertebrados de **corpo mole**, em geral protegidos por uma **concha calcária**. O corpo tem cabeça, massa visceral e **pé muscular**, usado para rastejar, escavar ou nadar. O **manto** reveste o corpo e produz a concha.',
  'Os principais grupos são os **gastrópodes** (caracóis e caramujos), os **bivalves** (ostras e mariscos) e os **cefalópodes** (polvos e lulas).']))

sp(M,'Manguezal','Fauna · moluscos','Caramujo-do-mangue','Littoraria angulifera','p51_5.jpg',[
 'Também chamado de **lambe-pau**, é um gastrópode adaptado às variações de salinidade e temperatura.',
 'Tem concha grossa e cônica, com faixas escuras, e um **opérculo**, uma "tampa" que fecha a concha.',
 'Vive sobre troncos, raízes e pneumatóforos, na zona entre marés, e raspa algas e detritos com a **rádula**.',
 'Respira por brânquias, mas prefere ficar **fora d\'água**: guarda água dentro da concha para aguentar a exposição.'],
 extra=[('p52_5.jpg','Caramujos no tronco do mangue.')])

sp(M,'Manguezal','Fauna · moluscos','Caramujo-grão-de-café','Melampus coffea','p53_5.jpg',[
 'Gastrópode **hermafrodita** que vive nos solos mais lamacentos e se alimenta de matéria orgânica.',
 'A concha marrom ou acinzentada lembra um **grão de café**.',
 'Respira ar (é **pulmonado**) e não aguenta ficar submerso: na maré baixa procura alimento na lama e, quando a maré enche, **sobe em procissão** pelos troncos.'])

sp(M,'Manguezal','Fauna · moluscos','Ostra-do-mangue','Crassostrea spp.','p54_6.jpg',[
 'No Brasil há **duas ostras nativas** de mangue, *C. rhizophorae* e *C. gasar*, difíceis de distinguir pela concha.',
 'Tem concha irregular, áspera e resistente, e vive **fixada** nas raízes do mangue-vermelho, em troncos e pedras, formando **bancos de ostras**.',
 'É filtradora e muito importante para **marisqueiras e pescadores**, na alimentação e na renda.'])

sp(M,'Manguezal','Fauna · moluscos','Neritina','Vitta virginea','p55_6.jpg',[
 'Pequeno gastrópode de concha arredondada, lisa e resistente.',
 'Os desenhos variados de **manchas, listras e cores** funcionam como camuflagem e ajudam a proteger contra o sol e a perda de água na maré baixa.'])

sp(M,'Manguezal','Fauna · moluscos','Berbigão','Anomalocardia flexuosa','p56_6.jpg',[
 'Conhecido também como **vôngole**, chumbinho ou maçunim, conforme a região.',
 'É um **bivalve** que vive enterrado no sedimento e se alimenta **filtrando** partículas orgânicas, microalgas e microrganismos da água.',
 'A concha é triangular, com linhas de crescimento bem marcadas.'])

sp(M,'Manguezal','Fauna · moluscos','Tarioba','Iphigenia brasiliana','p57_6.jpg',[
 'Bivalve que vive **enterrado**, de concha alongada, lisa e triangular; em Fortaleza também é chamado de **lambreta**.',
 'Tem **sifões**, tubos flexíveis por onde a água entra e sai, para respirar, comer e excretar.',
 'É muito usada por **marisqueiras** na alimentação e na renda.',
 'Por filtrar a água, acumula contaminantes e serve como **bioindicadora** da saúde do estuário.'],
 flag='a confirmar: grafia do nome científico (WoRMS)')

sp(M,'Manguezal','Fauna · moluscos','Unha-de-velho','Tagelus plebeius','p58_6.png',[
 'Bivalve de concha alongada, lisa e retangular, também chamado de **pixoleta** em Fortaleza.',
 'Escava galerias profundas em forma de **Y** e se move só para cima e para baixo.',
 'É **suspensívoro**: filtra a água para se alimentar.',
 'É muito usado na culinária de comunidades ribeirinhas e pesqueiras.'],
 extra=[('p58_7.jpg','Unha-de-velho no sedimento.')])

sp(M,'Manguezal','Fauna · moluscos','Turu','Neoteredo reynei','p59_6.png',[
 'Conhecido como **"cupim do mar"**: vive dentro de **troncos submersos** do mangue, onde se alimenta da madeira e se abriga.',
 'É um **bivalve** de corpo comprido e gelatinoso, parecido com uma minhoca, que pode passar de meio metro.',
 'Na ponta da cabeça tem duas pequenas **valvas serrilhadas**, usadas para perfurar a madeira.',
 'Em várias regiões é uma **iguaria**, comida crua ou cozida; a fama de afrodisíaco é **crença popular**.'],
 extra=[('p59_7.png','Turu inteiro, fora do tronco.')])

pg(M,'Manguezal','Fauna · crustáceos',
 ('card','Crustáceos',[
  'São invertebrados com **exoesqueleto** de quitina, que precisam trocar durante o crescimento (**muda** ou ecdise). O corpo costuma ter **cefalotórax e abdômen**, antenas, peças para mastigar e **cinco pares de patas**, especializadas para andar, cavar, nadar, comer ou se defender.',
  'Muitos vivem associados à lama e cavam **tocas**, que ajudam a **oxigenar o solo**. Comem matéria orgânica, folhas e pequenos organismos e são essenciais na **decomposição** e na ciclagem de nutrientes.']))

pg(M,'Manguezal','Fauna · crustáceos',
 ('gal','Chama-marés',[('Chama-maré','Leptuca leptodactyla','p61_6.jpg'),('Violinista','Leptuca thayeri','p61_7.jpg'),('Maracoani','Uca maracoani','p62_5.jpg')]),
 ('list','Chama-maré',[
  'Pequenos caranguejos cujo nome vem do movimento da **pinça**, que parece "acenar" para a maré.',
  'Os machos têm uma pinça **muito maior** que a outra, usada para atrair fêmeas e disputar território.',
  'Às vezes constroem **"chaminés"** de lama na entrada da toca.',
  'Para se defender, correm para a toca ou ficam **imóveis**.']))

sp(M,'Manguezal','Fauna · crustáceos','Aratu','Goniopsis cruentata','p63_5.jpg',[
 'Tem carapaça **avermelhada, arroxeada ou marrom-escura**, com pintas claras, e patas com muitas cerdas.',
 'Vive em vários pontos do manguezal, da lama às árvores: é **semiarborícola**.',
 'Não costuma cavar tocas e muitas vezes **ocupa a toca de outros** caranguejos.'])

sp(M,'Manguezal','Fauna · crustáceos','Uçá','Ucides cordatus','p64_5.jpg',[
 'Também chamado de **caranguejo-do-mangue**, é o caranguejo de **maior interesse comercial** dos manguezais brasileiros e importante fonte de renda das comunidades litorâneas.',
 'É grande: a carapaça oval pode chegar a **10 cm de largura**. As patas são longas, fortes e cheias de pelos.',
 'Come sobretudo **folhas de mangue** e é peça-chave na reciclagem de nutrientes.',
 'É classificado como **quase ameaçado** pelo ICMBio, por causa da sobrepesca e da degradação do mangue.'],
 note='**Andada e defeso.** Nas luas cheia e nova do início do ano, os uçás saem das tocas para se reproduzir: é a **andada**. Nesses períodos a captura é proibida no Ceará (Portaria Interministerial MPA/MMA nº 45/2026), e a captura de **fêmeas** é proibida de 1º de dezembro a 31 de maio.')

sp(M,'Manguezal','Fauna · crustáceos','Guaiamum','Cardisoma guanhumi','p65_5.jpg',[
 'É um dos maiores **caranguejos terrestres**, adaptado às áreas mais afastadas da água, na transição do mangue com o **apicum** e a mata.',
 'Guarda água na câmara das brânquias, o que permite passar bastante tempo **fora d\'água**, desde que o ambiente esteja úmido.',
 'De dia fica em **tocas profundas**, que alcançam o lençol freático; à noite sai para comer.',
 'Para diferenciar os sexos, olhe o **abdômen**, dobrado sob o corpo: largo nas fêmeas, que carregam os ovos, e estreito nos machos.'],
 note='O guaiamum está **ameaçado de extinção**, na categoria **vulnerável** (Portaria GM/MMA nº 1.667/2026), por causa da captura excessiva e da perda do seu habitat.',
 extra=[('p66_5.jpg','Guaiamum visto por baixo.')])

sp(M,'Manguezal','Fauna · crustáceos','Siri','Callinectes spp.','p67_6.jpg',[
 'Excelente **nadador**: tem a carapaça achatada e larga e o último par de patas em forma de **remo**.',
 'No Ceará, o **siri-azul** é sobretudo *C. danae*; também ocorrem outras espécies do gênero, como *C. bocourti* e *C. sapidus*.',
 'Tem grande importância para a **pesca artesanal**, no consumo e na venda.'])

sp(M,'Manguezal','Fauna · crustáceos','Camarão-pistola','Alpheus spp.','p68_5.jpg',[
 'Pequenos camarões com uma das pinças **muito maior** que a outra. Na lama do manguezal do Nordeste, uma das espécies comuns é *A. estuariensis*.',
 'Ao fechar a pinça muito rápido, o camarão lança um **jato de água** que forma uma bolha.',
 'O **estalo** que ouvimos não vem do jato, mas do **estouro dessa bolha**, que libera som, calor e até um breve brilho de luz.'])

sp(M,'Manguezal','Fauna · crustáceos','Cracas','Chthamalus proteus e outras','p69_6.jpg',[
 'Pequenos crustáceos que vivem **fixos para sempre** em raízes de mangue, troncos e pedras.',
 'O corpo fica protegido por **placas calcárias**, que evitam a perda de água na maré baixa.',
 'Comem **filtrando** a água com apêndices em forma de pente, os **cirros**.',
 'São alimento para outros animais e participam da ciclagem de nutrientes.'],
 flag='a confirmar: espécies de cracas no Rio Pacoti')

sp(M,'Manguezal','Fauna · peixes','Cavalo-marinho-de-focinho-longo','Hippocampus reidi','p71_5.jpg',[
 'Tem o corpo **na vertical**, coberto de anéis ósseos, focinho comprido e **cauda preênsil**, que usa para se prender à vegetação.',
 'Nada devagar, em pé, impulsionado pela **nadadeira dorsal**; as nadadeiras peitorais ajudam a manobrar.',
 'Forma **casais** na época reprodutiva. A fêmea deposita os ovos na **bolsa do macho**, que os incuba até o nascimento.',
 'A destruição dos habitats e a captura para comércio tornam a espécie **vulnerável** à extinção (Portaria GM/MMA nº 1.667/2026).'],
 extra=[('p70_5.jpg','Cavalo-marinho preso pela cauda à vegetação.')])

pg(M,'Manguezal','Fauna · peixes',('gal','Peixes',[
 ('Baiacu-mirim','Sphoeroides testudineus','p72_5.jpg'),('Amboré','Bathygobius soporator','p72_6.jpg'),('Carapicu','Eucinostomus sp.','p72_7.jpg'),
 ('Baúna-de-fogo','Lutjanus alexandrei','p72_8.jpg'),('Robalo','Centropomus spp.','p72_10.jpg')]),
 ('note','A **baúna-de-fogo** só existe no **Nordeste do Brasil**. Os filhotes usam as raízes do mangue do Rio Pacoti como berçário (Osório et al., 2011).'))

pg(M,'Manguezal','Cultura',
 ('card','Dimensão simbólica e cultural',[
  'Os manguezais também são territórios de **lendas, mistérios e crenças populares**, criados ao longo do tempo pelas comunidades que vivem no seu entorno. Essas narrativas misturam **saberes indígenas, africanos** e da tradição oral local.',
  'São comuns personagens que **punem quem desrespeita** o ambiente, reforçando valores de cuidado e equilíbrio com a natureza. Muitas histórias também explicam fenômenos que acontecem no mangue.',
  'Assim, as lendas são expressões culturais e também formas tradicionais de **educação ambiental**, que ajudam a preservar os recursos naturais e a construir uma identidade ligada ao território.']), sec='lendas')

pg(M,'Manguezal','Lendas',('legend','Vovó do Mangue',[
 'A Vovó do Mangue é uma velha de pele enrugada e escura, com uma perna só, lenço na cabeça e cachimbo na boca, vestida de farrapos. Ela vive nos manguezais de **Maragogipe (BA)** e os protege de quem quer destruí-los.',
 'A quem lhe dá um agrado, ela protege e ensina o caminho de volta. Já quem devasta o mangue ou mata seus animais sem necessidade fica **desnorteado e perdido** no meio do manguezal, como castigo.',
 'A Vovó do Mangue é associada a **Nanã**, orixá das águas paradas, das chuvas, dos mangues e da lama, ligada ao ciclo da vida e da morte.'],'Lenda da Bahia.'))

pg(M,'Manguezal','Lendas',('legend','Pai do Mangue',[
 'O Pai do Mangue é uma lenda contada por moradores dos manguezais de **Pernambuco e da Paraíba**. Dizem que ele é um ser invisível que governa a vegetação das margens, e muitos pescadores contam ouvir os seus **passos lentos** na água rasa.',
 'Ele teria a aparência de um velho, com roupa de pescador e um chapéu que esconde o rosto, sempre fumando um cigarro que nunca apaga. Quem entra no mangue deve **oferecer um pouco de fumo** para agradá-lo; caso contrário, com luzes e assobios, ele pode confundir o pescador e fazê-lo se perder.',
 'Quem acredita e respeita o Pai do Mangue pode ser recompensado com **pesca farta**.'],'Lenda de Pernambuco e da Paraíba (Galvão-Neto, 2010).'))

pg(M,'Manguezal','Lendas',('legend','Guajara',[
 'O Guajara é uma entidade brincalhona, conhecida do **povo Tremembé**, que habita os mangues de **Almofala, no Ceará**. Também chamado de Duende dos Manguezais, Guari e Pajé do Rio, ele imita sons e se diverte com o medo que provoca. Às vezes vira **pato** e entra nas casas para assustar as pessoas.',
 'Os pescadores dizem que, se alguém ouvir barulhos estranhos no mangue (sons de machado, gritos ou assobios), deve **voltar para casa**: é aviso de que a pescaria será ruim. Quem insiste pode ficar com febre e dor no corpo, como se tivesse apanhado dos galhos que o Guajara carrega.',
 'Para não ser incomodado, o pescador deixa um pouco de **fumo nas raízes do mangue** como oferenda.'],'Lenda do Ceará.'))

pg(M,'Manguezal','Lendas',('legend','A criação do caranguejo',[
 'Conta uma lenda do **Delta do Parnaíba** que havia um belo príncipe indígena chamado **Lupã**, que não era fiel a ninguém. A Deusa do Amor fez com que ele se apaixonasse por **Yaramey**, que também o amava. Mesmo assim, Lupã continuou enganando a amada.',
 'Muito magoada, Yaramey subiu no galho mais alto de um mangue-vermelho, à beira do rio, e **mergulhou na lama**, de onde nunca mais voltou.',
 'Arrependido, Lupã pediu à Deusa uma forma de procurá-la. Ela o transformou no **primeiro caranguejo**, que passou a viver das folhas do mangue e a **cavar buracos na lama**, em busca do seu grande amor.',
 'Para nunca esquecer o rosto de Yaramey, Lupã **desenhou a figura dela na própria carapaça**, e até hoje esse desenho aparece no casco do caranguejo-uçá.'],'Lenda do Delta do Parnaíba (PI/MA). [[a confirmar: fonte da lenda]]'),
 ('img','p78_5.jpg','O "desenho" de Yaramey na carapaça do uçá.'))

pg(M,'Manguezal','Lendas',('legend','O baiacu e o aratu',[
 'Houve um tempo em que nem o aratu nem o baiacu tinham pintas: os dois eram de uma cor só. Um dia, o baiacu pediu ao aratu que pintasse o seu corpo, para ficar mais bonito. O aratu aceitou, mas pediu para ser pintado primeiro.',
 'O baiacu pintou o aratu com todo o capricho, **bolinha por bolinha**. Quando chegou a vez do baiacu, o carnaval estava começando, e o aratu, com pressa de cair na folia, pintou o amigo **de qualquer jeito**.',
 'Ao ver que não tinha ficado tão bonito, o baiacu correu atrás do aratu, mas a maré estava vazando e ele não conseguiu alcançá-lo. Jurou que um dia o pegaria.',
 'É por isso que, **toda vez que a maré enche**, o aratu sobe nas árvores e o baiacu fica rodeando as raízes, à espera do seu desafeto.'],'Lenda popular dos manguezais.'))

# ---------------- APICUM
A='api'
pg(A,'Apicum','Introdução',
 ('card','Introdução',[
  'O nome **apicum** vem do tupi (*ape\'kũ*) e quer dizer "brejo de água salgada à beira-mar" ou "limite da terra firme com o mangue". É um ambiente associado aos manguezais, que ocorre nas bordas ou nas partes mais altas, formando uma **zona de transição** (ecótono) entre o mangue e outros ambientes, como a restinga e a mata de tabuleiro.',
  'No Rio Pacoti, o apicum é uma **área aberta**, de vegetação escassa e solo esbranquiçado pelo acúmulo de sal. Pode ser uma área de **expansão futura do mangue**, serve de **refúgio para aves**, inclusive migratórias, e participa da dinâmica de salinidade do estuário.']), sec='apicum')

pg(A,'Apicum','Formação',
 ('card','Formação',[
  'O apicum se forma em terrenos **um pouco mais altos** que o manguezal, inundados só nas marés muito altas (marés de **sizígia**) ou em tempestades.',
  'Quando a maré invade e depois recua, a água fica retida no solo exposto ao sol. O calor faz a água **evaporar** rapidamente, mas os **sais ficam**. Com o tempo, o solo fica cada vez mais salgado: é a **hipersalinização**.']),
 ('card','O apicum da trilha',[
  'No caso do apicum da trilha, há indícios de **origem humana**, como os barrancos ao redor da área. Quando o mangue é cortado para abrir **salinas** ou **viveiros**, ou quando o fluxo de água da região é alterado, o solo fica exposto à evaporação e acumula sal, e a área pode virar um ambiente parecido com um apicum.',
  'Esse processo pode **dificultar ou atrasar** a regeneração natural do manguezal.']))

pg(A,'Apicum','Flora',
 ('card','Flora',[
  'A vegetação tem **poucas espécies**, sobretudo plantas rasteiras e suculentas, adaptadas ao sal, ao sol forte e à falta de água. Elas formam **tapetes** sobre o solo e ajudam a fixar o sedimento.',
  'São **plantas facilitadoras**: melhoram as condições do solo e ajudam o mangue a voltar. Pesquisas do LABOMAR no Rio Pacoti mostraram que elas favorecem o estabelecimento e o crescimento do **mangue-preto** em áreas em recuperação.']),
 ('gal','Plantas do apicum',[('Beldroega-do-mar','Sesuvium portulacastrum','p84_10.jpg'),('Salsa-do-mangue','Batis maritima','p84_11.jpg')]),
 ('note','As duas têm folhas **suculentas**, que armazenam água e diluem o excesso de sal, e são **comestíveis**: estão entre as Plantas Alimentícias Não Convencionais (**PANC**).'))

pg(A,'Apicum','Fauna',
 ('card','Fauna',[
  'A fauna é menos diversa que a do manguezal e a da mata, mas muito bem adaptada. Caranguejos como o **chama-maré**, o **uçá** e o **guaiamum** cavam tocas no solo, e **aves limícolas**, que vivem e comem na lama, procuram pequenos invertebrados, sobretudo na maré baixa.',
  'O apicum também é área de passagem e alimentação para animais terrestres: é comum encontrar **pegadas de teju**, além de rastros e fezes de **mãos-peladas** e **capivaras**.']),
 ('gal','Aves',[('Socozinho','Butorides striata','p86_10.jpg'),('Garça-branca','Ardea alba','p86_14.jpg'),('Quero-quero','Vanellus chilensis','p86_13.jpg'),
  ('Maçarico-pintado','Actitis macularius','p86_11.jpg'),('Martim-pescador','Megaceryle torquata','p86_12.jpg')]),
 ('note','O **maçarico-pintado** é migratório: vem da América do Norte e é visto aqui sobretudo entre **setembro e abril**.'))

# ---------------- ENCERRAMENTO
F='fim'
pg(F,'Encerramento','Importância ecológica',
 ('card','Importância ecológica',[
  'O estuário do Rio Pacoti, com seus manguezais, apicuns e matas de tabuleiro, tem papel fundamental no **equilíbrio ambiental** da costa: protege a linha da costa contra a **erosão**, regula a água e retém sedimentos e nutrientes.',
  'O manguezal é um dos ambientes mais produtivos do planeta e funciona como **berçário** para peixes, crustáceos e moluscos. A vegetação ainda **captura e armazena carbono**, ajudando a enfrentar as mudanças climáticas.',
  'Esses ambientes sofrem com a **expansão urbana**, a degradação dos habitats e o acúmulo de **lixo**, especialmente plástico, que prejudica a fauna e a qualidade da água. Conservá-los é uma necessidade para manter os **serviços ecossistêmicos** que sustentam a vida.']), sec='encerramento')

pg(F,'Encerramento','Relevância socioeconômica',
 ('card','Relevância socioeconômica',[
  'O Rio Pacoti é muito importante para **comunidades tradicionais**, como pescadores artesanais e marisqueiras, que dependem do manguezal e do estuário para se alimentar e gerar renda. Essas práticas estão ligadas ao **conhecimento tradicional** acumulado por gerações.',
  'A poluição, a expansão urbana e a pressão humana comprometem os recursos naturais e os **modos de vida** dessas comunidades. Ao mesmo tempo, a região tem grande potencial para o **turismo ecológico** e a **educação ambiental**.',
  'Conservar esses ecossistemas é garantir a continuidade das **práticas culturais**, da **segurança alimentar** e da sustentabilidade da região.']))

REFS = [
 'BERTANI, R. Revision, cladistic analysis and biogeography of *Typhochlaena*, *Pachistopelma* and *Iridopelma* (Araneae, Theraphosidae). **ZooKeys**, v. 230, 2012.',
 'BRASIL. Ministério do Meio Ambiente e Mudança do Clima. **Portaria GM/MMA nº 1.667, de 27 de abril de 2026**. Lista Nacional Oficial de Espécies da Fauna Ameaçadas de Extinção – Peixes e Invertebrados Aquáticos. Brasília: DOU, 2026.',
 'BRASIL. Ministério do Meio Ambiente e Mudança do Clima. **Portaria MMA nº 1.704, de 16 de junho de 2026**. Lista Nacional Oficial de Espécies da Fauna Ameaçadas de Extinção. Brasília: DOU, 2026.',
 'BRASIL. Ministério da Pesca e Aquicultura; Ministério do Meio Ambiente e Mudança do Clima. **Portaria Interministerial MPA/MMA nº 45, de 12 de janeiro de 2026**. Períodos de defeso do caranguejo-uçá. Brasília: DOU, 2026.',
 'BRUSCA, R. C.; BRUSCA, G. J. **Invertebrados**. 2. ed. Rio de Janeiro: Guanabara Koogan, 2007.',
 'CASSIANO-LIMA, D. et al. The reproductive mode of *Adelophryne maranguapensis* (Anura, Eleutherodactylidae). **North-Western Journal of Zoology**, v. 7, n. 1, 2011.',
 'CEARÁ. **Decreto Estadual nº 25.778, de 15 de fevereiro de 2000**. Dispõe sobre a criação da Área de Proteção Ambiental do Rio Pacoti. Fortaleza, 2000.',
 'CEARÁ. **Decreto Estadual nº 27.413, de 30 de março de 2004**. Institui a carnaúba como árvore-símbolo do Estado do Ceará. Fortaleza, 2004.',
 'CEARÁ. Secretaria do Meio Ambiente e Mudança do Clima. **Portaria SEMA nº 155/2022**. Lista oficial de espécies vegetais exóticas invasoras para o Estado do Ceará. Fortaleza, 2022.',
 'CEARÁ. Secretaria do Meio Ambiente e Mudança do Clima. **Livro Vermelho dos Animais Ameaçados de Extinção do Ceará**. Fortaleza: SEMA, 2022 (atualizado em 2025).',
 'DIEGUES, A. C. **Pescadores, camponeses e trabalhadores do mar**. São Paulo: Ática, 1983.',
 'DONATO, D. C. et al. Mangroves among the most carbon-rich forests in the tropics. **Nature Geoscience**, v. 4, p. 293-297, 2011.',
 'GALVÃO-NETO, 2010. [[a confirmar: referência completa]]',
 'IBGE. **Manual técnico da vegetação brasileira**. 2. ed. Rio de Janeiro: IBGE, 2012.',
 'LACERDA, L. D. **Manguezais**: ciência e conservação. Rio de Janeiro: Mauad X, 2006.',
 'MELO, A. G. C. et al. Molecular identification, phylogeny and geographic distribution of Brazilian mangrove oysters (*Crassostrea*). **Genetics and Molecular Biology**, v. 33, n. 3, p. 564-572, 2010.',
 'OSÓRIO, F. M.; GODINHO, W. O.; LOTUFO, T. M. C. Ictiofauna associada às raízes de mangue do estuário do Rio Pacoti – CE, Brasil. **Biota Neotropica**, v. 11, n. 1, 2011.',
 'PINHEIRO, M. A. A. et al. Avaliação do caranguejo-uçá, *Ucides cordatus*. In: PINHEIRO, M.; BOOS, H. (org.). **Livro Vermelho dos Crustáceos do Brasil**: avaliação 2010-2014. Porto Alegre: SBC, 2016.',
 'RABELO, S. T. **Flora e estrutura fitossociológica de fitofisionomias costeiras da APA do Rio Pacoti, Ceará**: relações biogeográficas entre restingas do Norte e Nordeste do Brasil. 2022. Dissertação (Mestrado em Ciências Marinhas Tropicais) – Instituto de Ciências do Mar, Universidade Federal do Ceará, Fortaleza, 2022.',
 'RIOS, E. C. **Compendium of Brazilian sea shells**. Rio Grande: Evangraf, 2009.',
 'RUPPERT, E. E.; FOX, R. S.; BARNES, R. D. **Zoologia dos invertebrados**. 7. ed. São Paulo: Roca, 2005.',
 'SEMACE. **Plano de manejo da Área de Proteção Ambiental do Rio Pacoti**. Fortaleza: SEMACE. [[a confirmar: ano]]',
 'SOUZA, M. M. A.; SAMPAIO, E. V. S. B. Estrutura dos mangues em áreas pouco antropizadas e em regeneração no Rio Pacoti, CE. 2011. [[a confirmar: periódico, volume e páginas]]',
 'UNIVERSIDADE FEDERAL DO CEARÁ. **As herbáceas *Sesuvium portulacastrum* e *Batis maritima* facilitam o estabelecimento e crescimento de *Avicennia germinans* em um manguezal em recuperação na APA do estuário do Rio Pacoti**. Fortaleza: LABOMAR/UFC, 2020. [[a confirmar: autoria]]',
]
