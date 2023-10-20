//6 aca estoy capturando el id del div shopContent, div padre en el otro paso pongo el div que hice dentro de este
const shopContent = document.getElementById("shopContent");
//12-aca capturamos el icono carrito 
const verCarrito = document.getElementById("verCarrito");
//14-aca capturamos el div padre modal-container
const modalContainer = document.getElementById("modal-container");
//39
const cantidadCarrito = document.getElementById("cantidadCarrito");




let carrito = JSON.parse(localStorage.getItem("carrito")) || []; //2 //get item o tiene algo o es vacio

//3 en (destino)puede ir cualquier nombre que querramos

destinos.forEach((destino) => {
  let content = document.createElement("div"); //4-aca estamos creando el div 
  //4- en content.innerHTML voy a crear los elementos que va dentro del div, aca asignamos contenido HTML
  content.className = "card-destino"; //9-aca agregamos una clase al div content

  content.innerHTML = `  
     <img src="${destino.img}">
     <h3>${destino.nombre}</h3>
     <p class = "price">${destino.precio} $</p> 
    `; //9-aca agregamos las clases directamente en la etiqueta

  shopContent.append(content);//7


  let comprar = document.createElement("button"); //8 creo el elemento boton
  comprar.innerText = "comprar"; //8-con innerText le agrego el texto al boton
  comprar.className = "comprar-boton-carrito";

  content.append(comprar); //8 con append agrego el boton al contenido de arriba (div)

  comprar.addEventListener("click" , () =>{  //11-aca estamos haciendo que se escuche click en el boton comprar



    const repeat = carrito.some((repeatProduct) => repeatProduct.id === destino.id);//35 este metodo evalua si hay algo repetido

    if (repeat) {
      carrito.map((prod) => {
        if (prod.id === destino.id) {
          prod.cantidad++;
        };
      });
    } else{
      carrito.push({   //-11 la funcion flecha al escuchar el click va a agregar al carrito el producto
      id : destino.id, // con esto llamamos a todo lo que va a ir al carrito
      img : destino.img,
      nombre : destino.nombre,
      precio : destino.precio,
      cantidad : destino.cantidad,//34 

      });

    }
    console.log(carrito);

    carritoCounter(); //42 llamamos a la funcion para que pinte y muestre el numero del carrito
    saveLocal();

  });

});




// set item


const saveLocal = () => {

  localStorage.setItem("carrito", JSON.stringify(carrito)); // 43 la primer palabra va lo que quieras, y despues la variable que quieran guardar en el localstorage
  // stringify porque al localstorage solo se le puede mandar strings 

};



// get item 44

//JSON.parse(localStorage.getItem(carrito)); // hay que parsearla porque es un string, si es una cadena de texto no se puede trabajar con ella en el programa

