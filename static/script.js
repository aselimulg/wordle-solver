const form = document.querySelector("form");
if (form) {
    form.addEventListener("submit", function(e){
        submitForm(e, this);
    })
}