
const shopContent = document.getElementById("shopContent");

const verCarrito = document.getElementById("verCarrito");

const modalContainer = document.getElementById("modal-container");

const cantidadCarrito = document.getElementById("cantidadCarrito");




let carrito = JSON.parse(localStorage.getItem("carrito")) || []; 



destinos.forEach((destino) => {
  let content = document.createElement("div"); 
  
  content.className = "card-destino"; 

  content.innerHTML = `  
     <img src="${destino.img}">
     <h3>${destino.nombre}</h3>
     <p class = "price">${destino.precio} $</p> 
    `; 

  shopContent.append(content);//7


  let comprar = document.createElement("button"); 
  comprar.innerText = "comprar"; 
  comprar.className = "comprar-boton-carrito";

  content.append(comprar); 

  comprar.addEventListener("click" , () =>{  



    const repeat = carrito.some((repeatProduct) => repeatProduct.id === destino.id);

    if (repeat) {
      carrito.map((prod) => {
        if (prod.id === destino.id) {
          prod.cantidad++;
        };
      });
    } else{
      carrito.push({  
      id : destino.id, 
      img : destino.img,
      nombre : destino.nombre,
      precio : destino.precio,
      cantidad : destino.cantidad,

      });

    }
    console.log(carrito);

    carritoCounter(); 
    saveLocal();

  });

});




const saveLocal = () => {

  localStorage.setItem("carrito", JSON.stringify(carrito)); 
  

};



