const pintarCarrito = () => { // 26

    modalContainer.innerHTML = ""; //25

    modalContainer.style.display = "flex";//24 aca le damos otro estilo para que al volver a ver el carrito podamos ver de nuevo los productos


    const modalHeader = document.createElement("div"); //13 aca creo el div que contiene todo lo del modal
    modalHeader.className = "modal-header"; //le asigno una clase y en el siguiente creo el contenido HTML
    modalHeader.innerHTML = `
     <h1 class = "modal-header-title">Carrito</h1>
     `;

    modalContainer.append(modalHeader); //15

    const modalButton = document.createElement("h1");//16 el h1 simula a un boton
    modalButton.innerText = "x";
    modalButton.className = "modal-header-button";

    modalButton.addEventListener("click", () => {
        modalContainer.style.display = "none"; //23 esto es para que el modal se cierre style.display es un estilo de css

    });

    modalHeader.append(modalButton); //17 



    //18 y 19
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
       `;//33 cantidad//37 ahi se multiplica para saber el total a pagar
       //49 le agregamos los span + y -
       //53

        modalContainer.append(carritoContent);


        let restar = carritoContent.querySelector(".restar");  //50 de carritoContent selecciona la clase restar
        restar.addEventListener("click", () => {  //51
            if(destino.cantidad !== 1){
                destino.cantidad--;
            };
            
            saveLocal();
            pintarCarrito();
    
           
        });

        let sumar = carritoContent.querySelector(".sumar");  //50 de carritoContent selecciona la clase sumar
        sumar.addEventListener("click", () => {  //51
            destino.cantidad++;
            
            saveLocal();
            pintarCarrito();
    
        });

        let eliminar = carritoContent.querySelector(".delete-product"); //53 aca somos mas especificos
        eliminar.addEventListener("click" , () =>{

            eliminarProducto(destino.id); //53

        });

        //52 para que las cantidades del carrito esten bien, tambien hay que guardarlas en el localstorage


        //console.log(carrito.length);


        //let eliminar = document.createElement("span");//28 el span simula un boton
        //eliminar.innerText = "❌";
        //eliminar.className = "delete-product";
        //carritoContent.append(eliminar); //29


        eliminar.addEventListener("click", eliminarProducto); //32 el boton tiene que escuchar el click para ejecutar la funcion
        //32 eliminarProducto sino no borra nada

    });


    const total = carrito.reduce((acc, el) => acc + el.precio * el.cantidad, 0) //20- el cero es de donde arranca el acumulador y en cada vuelta se le suma el precio
    //38 le agregraos * el.cantidad para que lo multiplique por el precio
    const totalCompra = document.createElement("div"); //21
    totalCompra.className = "toal-content";
    totalCompra.innerHTML = `Total a pagar: $ ${total}`;
    modalContainer.append(totalCompra);//22 // el le puso totalBuying

};

verCarrito.addEventListener("click", pintarCarrito); //27 aca estamos diciendo que cuando se escuche el click se va a ejecutar la funcion pintarcarrito


const eliminarProducto = (id) => { //30 //53 le pongo el id para conectarlo con el id que toca el boton
   const foundId = carrito.find((element) => element.id === id); //30 buscame dentro de carrito. (element signiffica cada elemento del carrito), busca ese id 

   console.log(foundId);

   carrito = carrito.filter((carritoId) => { // carritoId representa todos los elementos del carrito
     return carritoId !== foundId; // aca retorna todos los elementos del carrito que sean distintos a foundId, que no contenga ese id
   
    });
    carritoCounter();//42
    saveLocal();
    pintarCarrito(); //31

   
};


const carritoCounter = () => {//40
    cantidadCarrito.style.display = "block"; // 40 aca se le saca el display none para que pinte el carrito

    const carritoLength = carrito.length; //45 esto es para guardar la constante en el local storage, para despues eliminar
    // del localstorage, lo que ya borre del carrito

    localStorage.setItem("carritoLength", JSON.stringify(carritoLength)); // 46 aca estamos guardando el dato de la variable de
    //arriba al localstorage

    cantidadCarrito.innerText = JSON.parse(localStorage.getItem("carritoLength")); //41 para que muestre el numero
    //47 obtenemos lo guardado
};

carritoCounter();// 48 llamamos a la funcion para que cada vez que actualice se muestren los numeros

