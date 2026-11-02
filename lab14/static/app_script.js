console.log("JOSEPH ALI-SHAW")
const itemForm = document.querySelector('#itemForm')
itemForm.addEventListener("submit", async function(event){
    event.preventDefault()
    const name = document.querySelector('#name').value
    const price = document.querySelector('#price').value
    try{
        const res = await fetch("http://127.0.0.1:5000/items", {method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ name: name, price:Number(price) })})
        const data = await res.json()
        document.querySelector('#response').innerHTML ="Response: " + JSON.stringify(data)
    } 
    catch(error) {
        document.querySelector('#response').innerHTML = "Response:ERROR" + error
    }
})