from build import Graph
from build import Addons
import flask
from flask import jsonify
from flask import request

def main():
    my_graph = Graph()
    
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    
    ##################          ALL GET DATA ENDPOINTS           ###########################
    @app.route('/', methods=['GET'])
    def home():
       return jsonify("Grafos")
    
    @app.route('/getNodes', methods=['GET'])
    def getNodes():
       print(my_graph.ShowNodes())
       return jsonify(list(my_graph.ShowNodes()))
       
       
       
    @app.route('/getEdges', methods=['GET'])
    def getEdges():    
       return jsonify(list(my_graph.ShowEdges()))
       
       
    @app.route('/getList', methods=['GET'])
    def getAdjacencia():    
       print(my_graph.ShowListAdj())
       return jsonify(str(my_graph.ShowListAdj()))   
       
    @app.route('/getMatrix', methods=['GET'])
    def getMatrix():    
       print(my_graph.AdjMatrix())
       return jsonify(str(my_graph.AdjMatrix())) 
        
    @app.route('/getNNodes', methods=['GET'])
    def getNVertice():    
       return jsonify(str(my_graph.NumberOfNodes()))
       
       
    @app.route('/getNEdges', methods=['GET'])
    def getNEdges():    
       return jsonify(str(my_graph.NumberOfEdges()))
    
    
    
    @app.route('/getNComponents', methods=['GET'])
    def getNComponents():    
       return jsonify(str(my_graph.NumberOfComponents()))
       
       
    @app.route('/getDensity', methods=['GET'])
    def getDensity():    
       return jsonify(str(my_graph.GraphDensity()))
       
       
    @app.route('/getClustering', methods=['GET'])
    def getClustering():    
       return jsonify(str(my_graph.AverageClustering()))
        
       
       
       
    @app.route('/getDegree', methods=['POST'])
    def getDegree():    
       
       node = request.get_json()
       print(my_graph.ShowDegreeNode(node))
       return jsonify(my_graph.ShowDegreeNode(node))   
       
       
       
       
    @app.route('/getPath', methods=['POST'])
    def getPath():
       data = str(request.json)
      # data.replace("b","'")
       #data = request.args.get('body')
       data = data.split(".")
       print(data[1])
       result = my_graph.ShortestPath(int(data[0]) , int(data[1]))
       
       return jsonify(str(result))   
       
       
          
    @app.route('/Clear', methods=['GET'])
    def clear():
        my_graph.ClearGraph()
        return jsonify("Grafo Limpo")   
      
    ###################            Generate files ENDPOINTS          ######################
    @app.route('/generateJSON', methods=['GET'])
    def generateJson():    
       return jsonify(my_graph.dump_json_graph("graph")) 
    
    @app.route('/getKamada', methods=['GET'])
    def getKamada():    
       my_graph.KamadaGraph()
       return jsonify("teste") 
       
       
    @app.route('/getSimple', methods=['GET'])
    def getSimple():    
       my_graph.PlotGraph()
       return jsonify("teste")
       
       
    @app.route('/getCircular', methods=['GET'])
    def getCircular():    
       my_graph.CircularGraph()
       return jsonify("teste")  
       
       
    @app.route('/getRandom', methods=['GET'])
    def getRandom():    
       my_graph.RandomGraph()
       return jsonify("teste") 
      
      
    @app.route('/getFruchterman', methods=['GET'])
    def getFruchterman():    
       my_graph.FruchtermanGraph()
       return jsonify("teste") 
      
    ###################            ALL POST DATA ENDPOINTS           ######################
       
    @app.route('/addNode', methods=['POST'])
    def addNode():
       print("aq")
       data = request.get_json()
       print("data:")
       print(data)
       my_graph.AddNode(data)
       
       return jsonify("adicionado")
       
       
    @app.route('/addEdge', methods=['POST'])
    def addEdge():
       print("aq")
       data = str(request.json)
      # data.replace("b","'")
       #data = request.args.get('body')
       data = data.split(".")
       print(data[1])
       my_graph.AddEdge(int(data[0]) , int(data[1]))
       
       return jsonify("adicionado")   
       
       
    
	
	
	
	
	
	
	
    app.run()
  
        
       # print("\nBem vindo ao projeto av2 ! ")
       # print("\n1- Adicionar vertice individualmente.") DONE
      #  print("2- Adicionar varios vertices.") #"spam"  4 nos: 's', 'p', 'a', 'm' DONE
      #  print("3- Adicionar arestas individualmente.") DONE
       # print("4- Salvar json.") DONE
      #  print("5- Exibir vertices.") DONE
      #  print("6- Exibir arestas.") DONE
      #  print("7- Exibir lista de adjacencia.") DONE
      #  print("8- Grau de um vertice especifico.") DONE
       # print("9- Limpar todos os nos e arestas do grafo.") DONE
       # choice = input("\nEscolha uma das opcoes acima: ")
        
    @app.route('/api/v1/resources/books', methods=['GET'])
    def api_id():
        my_graph.AddMultNodes(1)
        return jsonify(my_graph.ShowNodes())
        
'''
        if choice == '1':
            #my_graph.AddNode(input("Digite o vertice: "))
            #my_graph.PlotGraph()
            my_graph.AdjMatrix()
        elif choice == '2':
            my_graph.AddMultNodes(input("Digite os vertices: "))
        elif choice == '3':
            my_graph.AddEdge(input("Digite a aresta inicial: "),input("Digite a aresta final: "))
            #my_graph.CircularGraph()
            #my_graph.RandomGraph()
            #my_graph.KamadaGraph()
            #my_graph.FruchtermanGraph()
            #my_graph.NumberOfComponents()
            #my_graph.AdjMatrix()
        elif choice == '4':
            my_graph.dump_json_graph("grafo_json")
        elif choice == '5':
            my_graph.ShowNodes()
        elif choice == '6':
            my_graph.ShowEdges()
        elif choice == '7':
            my_graph.ShowListAdj()
        elif choice == '8':
            my_graph.ShowDegreeNode(input("Digite o no desejado: "))
        elif choice == '9':
            my_graph.ClearGraph()
        elif choice == '0':
            my_graph.WritePajek()    
    
        print("\n")

'''

if __name__ == "__main__":
    main()
