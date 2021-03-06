const addNode = async () => {
  const response = await fetch('http://127.0.0.1:5000/addNode', {
    method: 'POST',
    body: document.getElementById("nodeText").value, // string or object
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson
}

const addEdge = async () => {
  const response = await fetch('http://127.0.0.1:5000/addEdge', {
    method: 'POST',
    body: document.getElementById("edgeText1").value+"."+document.getElementById("edgeText2").value,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson
}




const generateJson = async () => {
  const response = await fetch('http://127.0.0.1:5000/generateJSON', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
}





const generateGraph = async () => {
  var e = document.getElementById("selectGraph");
  var selected = e.value;
  var type;
  console.log(selected)
  switch (selected){
  	case '1':
  	  type = "Simple"
  	  break;
  	case '2':
  	  type = "Random"
  	  break;
  	case '3':
  	  type = "Circular"
  	  break;
  	case '4':
  	  type = "Kamada"
  	  break;
  	case '5':
  	  type = "Fruchterman"
  	  break; 
  	 
  }
  
  const response = await fetch('http://127.0.0.1:5000/get'+type, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  document.getElementById("graphImage").src = "../BackEnd_Python/grafo_"+type+".png?" + new Date().getTime()
  console.log(myJson)
  // do something with myJson
}

const getDegree = async () => {
if(!document.getElementById("degreeText").value){
	document.getElementById("grauText").innerHTML = "Passe o grau no campo node1"
	return
}
  const response = await fetch('http://127.0.0.1:5000/getDegree', {
    method: 'POST',
    body: document.getElementById("degreeText").value,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  

  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
  document.getElementById("grauText").innerHTML = myJson
}


const getPath = async () => {
if(!document.getElementById("degreeText").value){
	document.getElementById("pathText").innerHTML += "Passe o grau no campo node1"
	return
}
if(!document.getElementById("degreeText2").value){
	document.getElementById("pathText").innerHTML += "Passe o grau no campo node2"
	return
}
  const response = await fetch('http://127.0.0.1:5000/getPath', {
    method: 'POST',
    body: document.getElementById("degreeText").value+"."+document.getElementById("degreeText2").value,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  document.getElementById("pathText").innerHTML = myJson
  // do something with myJson
}





const getAdjList = async () => {
  const response = await fetch('http://127.0.0.1:5000/getList', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  

  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
  document.getElementById("listText").innerHTML = myJson
}


const getAdjMatrix = async () => {
  const response = await fetch('http://127.0.0.1:5000/getMatrix', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  

  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
  document.getElementById("matrixText").innerHTML = myJson.replaceAll("]","]</br>")
}




const getNNodes = async () => {
  const response = await fetch('http://127.0.0.1:5000/getNNodes', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  

  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
  document.getElementById("nnodesText").innerHTML = myJson
}

const getNEdges = async () => {
  const response = await fetch('http://127.0.0.1:5000/getNEdges', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  

  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
  document.getElementById("nedgesText").innerHTML = myJson
}



const getNComponents = async () => {
  const response = await fetch('http://127.0.0.1:5000/getNComponents', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  

  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
  document.getElementById("ncomponentsText").innerHTML = myJson
}


const getDensity = async () => {
  const response = await fetch('http://127.0.0.1:5000/getDensity', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  

  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
  document.getElementById("densityText").innerHTML = myJson
}



const getClustering = async () => {
  const response = await fetch('http://127.0.0.1:5000/getClustering', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  

  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson)
  // do something with myJson
  document.getElementById("clusteringText").innerHTML = myJson
}


const calculus = async () =>{
	//degreeText1
	getDegree()
	getNNodes()
	getNEdges()
	getNComponents()
	getDensity()
	getAdjList()
	getClustering()
	getAdjMatrix()
	getPath()
}

const clearGraph = async () => {
  const response = await fetch('http://127.0.0.1:5000/Clear');
  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson);
  // do something with myJson
}

