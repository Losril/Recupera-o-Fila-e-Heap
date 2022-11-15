#HELENA KUCHINSKI FERREIRA
#Para obter estes pontos você precisará criar as estruturas de dados especificadas nos itens a eb, sem esquecer que uma estrutura de dados é composta de uma representação em memória e, nomínimo três funções (ou métodos) para a sua manipulação. Sendo assim, todas as estruturas de dadosterão, um método para inclusão, um método para exclusão e um método para busca.a) Usando, C, C++, Python ou Java, crie uma estrutura de dados chamada minhaNovaFila quedeverá usar como representação em memória uma lista linkada. Para testar esta estruturavocê precisará criar uma fila com 100 registros compostos de uma string com até 100caracteres e um valor numérico do conjunto dos números reais. Para gerar os strings e osvalores números você deverá usar um gerador de números randômicos baseado noMersenne Twister.Durante a criação dos registros você deverá escolher, aleatóriamente dois destes registrospara testar a função de busca.Uma vez que a lista tenha sido criada você deve contar o tempo necessário para tirar 20%dos registros desta fila e o tempo necessário para encontrar a posição na fila onde estãodois dos registros criados. Neste exercício, o tempo gasto em todas as operações com aestrutura de dados deverá ser registrado.A saída esperada será feita por meio de um arquivo onde teremos a fila original impressana horizontal com comprimento inferior a 5 registros por linha, seguida da fila depois daexclusão de 20% dos seus registros, também na horizontal.As últimas linhas do arquivo de saída serão reservadas para o registro dos tempos médiosutilizados para cada uma das operações da estrutura de dados (criação, inclusão, exclusão,nova inclusão) como estes tempos serão muito pequenos será necessário tirar as médiascom, no mínimo, 50 repetições.b) Usando, C, C++, Python ou Java, crie uma estrutura de dados chamada eitaHeap que deveráusar como representação em memória uma lista linkada. Para testar esta estrutura vocêprecisará criar um heap (min heap) com 100 registros compostos de uma string com até 100caracteres e um valor numérico do conjunto dos números reais. Para gerar os strings e osvalores números você deverá usar um gerador de números randômicos baseado noMersenne Twister.Durante a criação dos registros você deverá escolher, aleatoriamente dez destes registrospara testar a função de busca.Uma vez que a heap tenha sido criada você deve contar o tempo necessário para tirar 16%dos registros deste heap, o tempo necessário para encontrar a posição na fila onde estão osregistros escolhidos para teste e o tempo necessário para inserir 45 registros novos nesteheap. Sem dúvida os testes para a localização dos dez registros selecionados para o resgistrodos tempos de localização deverão ser feitos com o heap originalmente criado, antes daexclusão de 16% ou da inclusão de novos registros. Como a estrutura é muito pequena, todos os tempos deverão ser calculados na forma demédia o que implica na repetição dos processos de criação, inserção, remoção, busca e novainserção, no mínimo 50 vezes.A saída esperada será feita por meio de um arquivo onde teremos o heap estruturado emformato de árvore usando ASCII, seguido do heap com menos 16% dos registros, tambémestruturado no formato de uma árvore usando ASCII, seguido do heap após a inclusão denovos registros, seguido dos tempos médios de inclusão, exclusão, busca e nova inclusãoidentificados cada um em sua própria linha.

import time
import random
import string

# Classe que representa cada nó da fila
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
  def __repr__(self):
    return '%s -> %s' % (self.data, self.next)

# Classe que representa a Linkedlist
class Linkedlist:
  def __init__(self):
    self.head = None
    self.tail = None

  def __repr__(self):
    return "[" + str(self.head) + "]" 

  def push(self, node):
    new = Node(node)
    if self.head == None:
      self.head = new
      self.tail = new
      new.next = self.head
    else:
      self.tail.next = new
      self.tail = new

  def search(self, val):
    if self.head is None:
      print("Vazio...")
      return
    flag=pos=0
    ptr=self.head
    while ptr:
      pos= pos + 1
      if(ptr.data == val):
        flag = 1
      ptr=ptr.next
    if(flag==0):
      print(val, "Não existe na fila")

  def pop(self):
    if not self.head:
      return
    self.head = self.head.next
    if self.head == None:
      self.tail = None

  def printList(self):
    # declara variável referência do primeiro elemento da fila
    temp = self.head
    # inicia contador
    count = 0
    # enquanto (temp != NULL) a referência do elemento da lista existir
    while (temp): 
      # printa elemento atual + " -> "
      print(temp.data, " -> ", end = '')
      # define temp igual ao próximo elemento da fila
      temp = temp.next
      # incrementa contador
      count = count + 1
      # caso contador seja igual a 5 pula uma linha e reseta contador
      if(count == 5):
        print("\n")
        count = 0

  def get(self, pos):
    temp = self.head
    count = 0
    while(temp):
      if(count == pos):
        return temp
      count += 1
      temp = temp.next

  def set(self, pos, k):
    temp = self.head
    count = 0
    while(temp):
      if(count == pos):
        self.head = k
      count += 1
      temp = temp.next
      
# Classe do objeto utilizado para preencher registros da fila
class Obj:
  def __init__(self, index, str):
    self.index = index
    self.str = str
    
  # getters
  def get_index(self):
    return self.index

  def get_str(self):
    return self.str

  # setters
  def set_index(self, x):
    self.index = x

  def set_str(self, y):
    self.str = y

  def __str__(self):
    return self.str + "(" + str(self.index) + ")"

class heapNode:
  def __init__(self, key, str):
    self.str = str
    self.key = key
    self.next = None
    
  def __repr__(self):
    return '%s(%s)' % (self.str, self.key)

# classe que representa a linked list
class newList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __repr__(self):
    return "[" + str(self.head) + "]"

  def push(self, str, key):
    new = heapNode(str, key)
    if self.head == None:
      self.head = new
      self.tail = new
      new.next = self.head
    else:
      self.tail.next = new
      self.tail = new

  def search(self, val):
    if self.head is None:
      print("Vazio...")
      return
    flag=pos=0
    ptr=self.head
    while ptr:
      pos= pos + 1
      if(ptr.key == val):
        # print("{} está presente na lista na posição: {}".format(val, pos))
        flag = 1
      ptr=ptr.next
    if(flag==0):
      print(val, "Não existe na lista")

  def pop(self):
    if not self.head:
      return
    self.head = self.head.next
    if self.head == None:
      self.tail = None

  def get(self, pos):
    temp = self.head
    count = 0
    while(temp):
      if(count == pos):
        return temp
      count += 1
      temp = temp.next

  def swapNodeValues(self, node1, node2):
    #1. count the number of nodes in the list
    temp = self.head
    N = 0
    while (temp != None):
      N += 1
      temp = temp.next
  
    #2. check if the swap positions are valid entries
    if(node1 < 1 or node1 > N or node2 < 1 or node2 > N):
      return
  
    #3. traverse to the nodes where values to be swapped
    pos1 = self.head
    pos2 = self.head
    for i in range(1, node1):
      pos1 = pos1.next;
    for i in range(1, node2):
      pos2 = pos2.next;
  
    #4. swap the values of two nodes
    val = pos1.key
    valk = pos1.str
    pos1.key = pos2.key
    pos1.str = pos2.str
    pos2.key = val
    pos2.str = valk

  def getNth(self, index):
    current = self.head  # Initialise temp
    count = 0  # Index of current node

    # Loop while end of linked list is not reached
    while (current):
        if (count == index):
            return current.key
        count += 1
        current = current.next
    return 0
# Função que retorna string com até 100 caracteres
def gen_random_string():
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters)  for i in range(random.randint(0, 100)))
  return result_str
    
# Função que cria um objeto da classe Obj utilizando princípio MT com string e inteiro aleatório
def RandObj():
  # Valor numérico real
  x = random.randint(1,100)
  y = gen_random_string()
  myObj = Obj(x, y)
  return myObj

# Função que retorna fila
def CreateFila():
  # Declara minhaNovaFila derivada da classe Linkedlist
  minhaNovaFila = Linkedlist()
  
  # Cria 100 registros na fila
  
  for i in range(100):
    # Declara novo obj contendo dados do registro
    newObj = RandObj()

# Condicional para definir classes a serem buscadas pelo método da lista
    if(i == 55):
      findObj1 = newObj
    if(i == 33):
      findObj2 = newObj
      
    minhaNovaFila.push(newObj)

  return minhaNovaFila, findObj1, findObj2

# Função que retorna tempo para buscar e remover
def getTimeSearch(result):
# recebe retorno da função create list em array [randlist, findObj1, findObj2]
  minhaNovaFila = result[0]
  
# Variáveis que recebem valores para serem buscados posteriormente
  finder1 = result[1]
  finder2 = result[2]

  tPInicio1 = time.process_time() 
  # Método de busca
  minhaNovaFila.search(finder1)
  minhaNovaFila.search(finder2)
  tPFinal1 = time.process_time()

  timesearch = (tPFinal1 - tPInicio1)*1000000

  return timesearch

# Função que apaga 20 registros de uma nova fila (apaga 20 primeiras posições seguindo teoria de fila) para contabilizar o tempo
def getTimeErase():
  # Variável que recebe nova fila com novos valores
  result = CreateFila()
  # Recebe retorno da função create list em array
  filaSearch = result[0]
  
  tPInicio2 = time.process_time()
  
  # Apaga 20 registros
  for i in range(20):
    filaSearch.pop()
  tPFinal2 = time.process_time()
  
  timeerase = (tPFinal2 - tPInicio2)*1000000

  return timeerase
class MinHeap:
  def __init__(self, maxsize):
    self.maxsize = maxsize
    self.size = 0
    self.heapList = newList()
    self.FRONT = 1

  def parent(self, pos):
    return pos//2

  def leftChild(self, pos):
    return 2*pos

  def rightChild(self, pos):
    return (2 * pos) + 1

	# Function that returns true if the passed
	# node is a leaf node
  def isLeaf(self, pos):
    return pos*2 > self.size
    
  # def swap(self, fpos, spos):
  #  self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
  
  def push(self, key, str):
    if (self.size >= self.maxsize):
      return
    self.size += 1
    self.heapList.push(key, str)
    current = self.size 
    
    while self.heapList.getNth(current) < self.heapList.getNth(self.parent(current)):
      self.heapList.swapNodeValues(current, self.parent(current))
      current = self.parent(current)
  
  def printHeapList(self):
    for i in range(1, (self.size//2)+1):
      print("PARENT : "+ str(self.heapList.get(i)) + "\nLEFT CHILD : "+ 
                          str(self.heapList.get(2 * i)) + "\nRIGHT CHILD :"                       +  str(self.heapList.get(2 * i + 1)) + "\n")
  
  def minHeapify(self, pos):
    if not self.isLeaf(pos):
        if (self.heapList.getNth(pos) > self.heapList.getNth(self.leftChild(pos)) or 
           self.heapList.getNth(pos) > self.heapList.getNth(self.rightChild(pos))):
          if self.heapList.getNth(self.leftChild(pos)) < self.heapList.getNth(self.rightChild(pos)):
            self.heapList.swapHeapList(pos, self.leftChild(pos))
            self.minHeapify(self.leftChild(pos))
          else:
            self.heapList.swapHeapList(pos, self.rightChild(pos))
            self.minHeapify(self.rightChild(pos))
  
  def minHeap(self):
    for pos in range(self.size//2, 0, -1):
        self.minHeapify(pos)
    
  def remove(self):
    popped = self.heapList.getNth(self.FRONT)
    self.heapList.pop()
    self.size-= 1
    return popped


def getTimeSearchHeap(result):
  tempHeap = result[0]
  search = result[1]
  
  tPInicio3 = time.process_time() 
    # busca os 10 registros
  for i in range(len(search)):
    obj = search[i]
    tempHeap.heapList.search(obj.index)
  tPFinal3 = time.process_time()
  timesearchheap = (tPFinal3 - tPInicio3)*1000
  
  return timesearchheap

def getTimeEraseHeap():
  tempHeap = CreateHeap(100)[0]
  # remove 16% dos registros
  tPInicio4 = time.process_time() 
  for i in range(16):
    tempHeap.remove()
  tPFinal4 = time.process_time()
  timeeraseheap = (tPFinal4 - tPInicio4)*1000
  
  return timeeraseheap

def getTimeInsertHeap():
  tempHeap = CreateHeap(129)[0]

  tPInicio5 = time.process_time() 
  # insere 45 registros
  for i in range(45):
    newObj = RandObj()
    tempHeap.push(newObj.index, newObj.str)
  tPFinal5 = time.process_time()
  timeinsert = (tPFinal5 - tPInicio5)*1000
  
  return timeinsert
  
# Funcao que cria heap com 100 registros aleatorios e retorna heap + arr[10] registros aleatorios
def CreateHeap(x):
  heap = MinHeap(x)
  search = []
  for i in range(x-1):
    newObj = RandObj()
    heap.push(newObj.index, newObj.str)
    if i <= 10:
      search.append(newObj)
  return heap, search
  
if __name__ == "__main__":
  result = CreateFila()
  minhaNovaFila = result[0]
  
  # Imprime lista antes de remover 20%
  print("Fila antes da remoção de 20 registros\n")
  minhaNovaFila.printList()
  
  # Arrays para alocar tempo da busca e remoção
  timesearch = []
  timeerase = []
  
  # Laço para iterar 50 vezes sobre MainProcess e calcular média de tempos
  for i in range(50):
    # Declara variável que recebe resultado da função MainProcess
    timeresult = getTimeSearch(result)
    timesearch.append(timeresult)
    timeerase.append(getTimeErase())

  for i in range(20):
    minhaNovaFila.pop()

  print("\nFila após remoção de 20 registros\n")
  minhaNovaFila.printList()
  print(f'Tempo de busca: {round(sum(timesearch)/50,3)} µs')
  print(f'Tempo de remoção: {round(sum(timeerase)/50,3)} µs')
  
  result = CreateHeap(100)
  minHeap = result[0]
  search = result[1]
  
  timesearch1 = []
  timeerase1 = []
  timeinsert = []
  
  print("\nHeap antes da remoção de 16 registros\n \n")
  minHeap.printHeapList()

  # busca os 10 registros
  for i in range(50):
    timesearch1.append(getTimeSearchHeap(result))
    timeerase1.append(getTimeEraseHeap())
    timeinsert.append(getTimeInsertHeap())

    # remove 16% dos registros
  for i in range(16):
    minHeap.remove()
  
  print("\nHeap após remoção de 16 registros\n")
  minHeap.printHeapList()

  minHeap.maxsize = 129
  # insere 45 registros
  for i in range(45):
    newObj = RandObj()
    minHeap.push(newObj.index, newObj.str)

  print("\nHeap após inserção de 45 registros\n")
  minHeap.printHeapList()

  print(f'Tempo de busca: {round(sum(timesearch1)/50,3)} ms')
  print(f'Tempo de remoção: {round(sum(timeerase1)/50,3)} ms')
  print(f'Tempo de nova inserção: {round(sum(timeinsert)/50,3)} ms')