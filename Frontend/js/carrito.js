const pintarCarrito = () => { 

    modalContainer.innerHTML = ""; 

    modalContainer.style.display = "flex";


    const modalHeader = document.createElement("div"); 
    modalHeader.className = "modal-header"; 
    modalHeader.innerHTML = `
     <h1 class = "modal-header-title">Carrito</h1>
     `;

    modalContainer.append(modalHeader); 

    const modalButton = document.createElement("h1");
    modalButton.innerText = "x";
    modalButton.className = "modal-header-button";

    modalButton.addEventListener("click", () => {
        modalContainer.style.display = "none"; 

    });

    modalHeader.append(modalButton); 



   
    carrito.forEach((destino) => {
        let carritoContent = document.createElement("div");
        carritoContent.className = "modal-content";
        carritoContent.innerHTML = `
       <img src="${destino.img}">
       <h3>${destino.nombre}</h3>
       <p>${destino.precio} $</p> 
       <span class = "restar"> - </span>
       <p>Cantidad: ${destino.cantidad}</p>
       <span class = "sumar"> + </span>
       <p>Total: ${destino.cantidad * destino.precio}</p>
       <span class = "delete-product"> ❌ </span>
       `;

        modalContainer.append(carritoContent);


        let restar = carritoContent.querySelector(".restar");  
        restar.addEventListener("click", () => {  
            if(destino.cantidad !== 1){
                destino.cantidad--;
            };
            
            saveLocal();
            pintarCarrito();
    
           
        });

        let sumar = carritoContent.querySelector(".sumar");  
        sumar.addEventListener("click", () => {  
            destino.cantidad++;
            
            saveLocal();
            pintarCarrito();
    
        });

        let eliminar = carritoContent.querySelector(".delete-product"); 
        eliminar.addEventListener("click" , () =>{

            eliminarProducto(destino.id); 

        });

        

        eliminar.addEventListener("click", eliminarProducto); 
        

    });


    const total = carrito.reduce((acc, el) => acc + el.precio * el.cantidad, 0);
    
    const totalCompra = document.createElement("div"); 
    totalCompra.className = "toal-content";
    totalCompra.innerHTML = `Total a pagar: $ ${total}`;
    modalContainer.append(totalCompra);

};

verCarrito.addEventListener("click", pintarCarrito); 


const eliminarProducto = (id) => { 
   const foundId = carrito.find((element) => element.id === id); 

   console.log(foundId);

   carrito = carrito.filter((carritoId) => { 
     return carritoId !== foundId; 
   
    });
    carritoCounter();
    saveLocal();
    pintarCarrito(); 

   
};


const carritoCounter = () => {
    cantidadCarrito.style.display = "block"; 

    const carritoLength = carrito.length; 
    

    localStorage.setItem("carritoLength", JSON.stringify(carritoLength)); 
   

    cantidadCarrito.innerText = JSON.parse(localStorage.getItem("carritoLength")); 
    
};

carritoCounter();


