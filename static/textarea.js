const textArea = document.querySelector("textarea");
textArea.addEventListener("keyup", e =>{
    textArea.style.height = "160px";
    let scHeight = e.target.scrollHeight;
    textArea.style.height = `${scHeight}px`;
});