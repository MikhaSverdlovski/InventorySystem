function getItemById(itemId) {
    // Выполнить AJAX запрос к серверу
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_item?id=' + itemId, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var item = JSON.parse(xhr.responseText);
            // Заполнить поля всплывающего окна данными из полученного объекта
            document.getElementById("editItemId").value = item.id;
            document.getElementById("editName").value = item.name;
            document.getElementById("editDescription").value = item.description;
            document.getElementById("editType").value = item.type;
            document.getElementById("editManufacturer").value = item.manufacturer;
            document.getElementById("editYear").value = item.year;
            document.getElementById("editCountry").value = item.country;
            document.getElementById("editPrice").value = item.price;
            document.getElementById("editQuantity").value = item.quantity;
            document.getElementById("editPopup").style.display = "block";
            document.getElementById("overlay").style.display = "block";
        }
    };
    xhr.send();
}

    function editItem(itemId) {
        // Здесь нужно реализовать получение данных по itemId и заполнение полей всплывающего окна
        // Пример:
        var item = getItemById(itemId); // Функция getItemById должна вернуть объект с данными по ID
        document.getElementById("editItemId").value = item.id;
        document.getElementById("editName").value = item.name;
        document.getElementById("editDescription").value = item.description;
        document.getElementById("editType").value = item.type;
        document.getElementById("editManufacturer").value = item.manufacturer;
        document.getElementById("editYear").value = item.year;
        document.getElementById("editCountry").value = item.country;
        document.getElementById("editPrice").value = item.price;
        document.getElementById("editQuantity").value = item.quantity;

        document.getElementById("editPopup").style.display = "block";
        document.getElementById("overlay").style.display = "block";
    }

    function closeEditPopup() {
        document.getElementById("editPopup").style.display = "none";
        document.getElementById("overlay").style.display = "none";
    }