console.log("JOSEPH ALI-SHAW")

const itemForm = document.querySelector('#itemForm')
const itemsList = document.querySelector('#itemsList')
const responseBox = document.querySelector('#response')

function renderItems(items) {
    if (!itemsList) return

    const entries = Object.entries(items)
    if (!entries.length) {
        itemsList.innerHTML = '<div class="item-card"><strong>No items found.</strong></div>'
        return
    }

    itemsList.innerHTML = entries.map(([id, item]) => `
        <div class="item-card">
            <p><strong>ID:</strong> ${id}</p>
            <p><strong>Name:</strong> ${item.name || 'N/A'}</p>
            <p><strong>Price:</strong> ${item.price ?? 'N/A'}</p>
            <div class="button-row item-actions">
                <a href="/items/${id}/update" class="button-link">Update</a>
                <a href="/items/${id}/delete" class="button-link secondary-btn">Delete</a>
            </div>
        </div>
    `).join('')
}

async function loadItems() {
    try {
        const res = await fetch('/items')
        const items = await res.json()
        renderItems(items)
        if (responseBox) {
            responseBox.innerHTML = `Loaded ${Object.keys(items).length} item(s).`
        }
    } catch (error) {
        if (responseBox) {
            responseBox.innerHTML = 'Response: ERROR ' + error
        }
    }
}

if (itemForm) {
    itemForm.addEventListener("submit", async function(event) {
        event.preventDefault()
        const name = document.querySelector('#name').value
        const price = document.querySelector('#price').value

        try {
            const res = await fetch("/items", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name: name, price: Number(price) })
            })
            const data = await res.json()
            if (responseBox) {
                responseBox.innerHTML = "Response: " + JSON.stringify(data)
            }
            loadItems()
        } catch (error) {
            if (responseBox) {
                responseBox.innerHTML = "Response: ERROR " + error
            }
        }
    })
}

const loadItemsBtn = document.querySelector('#loadItemsBtn')
if (loadItemsBtn) {
    loadItemsBtn.addEventListener('click', loadItems)
}

loadItems()