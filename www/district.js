const getDistrict = () => {
    const searchParams = new URLSearchParams(window.location.search);
    return searchParams.get('district');
}

document.addEventListener("DOMContentLoaded", () => {
    let district = getDistrict();
    if (district) {
        district = district[0].toUpperCase() + district.substring(1);
        const districtTitle = document.getElementById("district-title");
        districtTitle.textContent = district;
    }

    fetch(`http://127.0.0.1:5000/api/district?${district ? 'q=' + district : ''}`)
        .then(res => res.json())
        .then(data => {
            data = data.map(flcDetail => {
                return {
                    area: flcDetail.area,
                    name: flcDetail.flc_name,
                    totalBeds: flcDetail.Abeds,
                    totalOxygen: flcDetail.Aoxybeds,
                    occupiedBeds: flcDetail.Obeds,
                    occupiedOxyBeds: flcDetail.OOybeds
                }
            });
            const tbody = document.createElement("tbody");
            const createTd = (textContent) => {
                const td = document.createElement('td');
                td.textContent = textContent; 
                return td;
            }
            data.forEach(flcDetail => {
                const { area, name, totalBeds, totalOxygen, occupiedBeds, occupiedOxyBeds } = flcDetail;
                const tr = document.createElement('tr');
                tr.appendChild(createTd(area));
                tr.appendChild(createTd(name));
                tr.appendChild(createTd(`${totalBeds - occupiedBeds}/${totalBeds}`));
                tr.appendChild(createTd(`${totalOxygen - occupiedOxyBeds}/${totalOxygen}`));
                tbody.appendChild(tr);
            });
            document.getElementById("data-table").appendChild(tbody)
        })
});
