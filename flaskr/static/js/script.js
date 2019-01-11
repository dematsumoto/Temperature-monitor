document.getElementById('deviceStatsForm').deviceId.onchange = function() {
    form = document.getElementById('deviceStatsForm').deviceId;
    document.getElementById('deviceStatsForm').action = form.options[form.selectedIndex].value + "/stats";
};