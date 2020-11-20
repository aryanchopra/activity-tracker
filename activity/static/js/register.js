const usernameField=document.querySelector('#usernameField');
const feedBackArea = document.querySelector('.invalid_feedback_user');
const emailField=document.querySelector('#emailField');
const feedBackAreaEmail=document.querySelector('.invalid_feedback_email');
const showPasswordToggle = document.querySelector('.showPasswordToggle');
const passwordField=document.querySelector('#passwordField');
const submitbtn= document.querySelector('.submit-btn');
const handleToggleInput= (e)=>{
    if(showPasswordToggle.textContent==="SHOW"){
        showPasswordToggle.textContent="HIDE";
        passwordField.setAttribute("type","text");
    }
    else{
        showPasswordToggle.textContent="SHOW";
        passwordField.setAttribute("type","password");
    }
};


showPasswordToggle.addEventListener("click",handleToggleInput);


/* Username Validation */
usernameField.addEventListener("keyup", (e)=>{
    /* Clear after backspace */
    usernameField.classList.remove('is-invalid');
    feedBackArea.style.display="none";
    
    const usernameVal=e.target.value;
    if(usernameVal.length > 0){
        fetch('/authentication/validate-username',{
            body: JSON.stringify({username:usernameVal}),
            method:'POST',
    })
        .then((res)=>res.json())
        .then((data)=>{
        if(data.username_error){
            submitbtn.setAttribute("disabled","disabled");
            usernameField.classList.add('is-invalid');
            feedBackArea.style.display="block";
            feedBackArea.innerHTML=`<p> ${data.username_error} </p>`;

        }else{
            submitbtn.removeAttribute("disabled");
        }
        });
    }
});

/* Email Validation */
emailField.addEventListener("keyup", (e)=>{
    /* Clear after backspace */
    emailField.classList.remove('is-invalid');
    feedBackAreaEmail.style.display="none";
    
    const emailVal=e.target.value;
    if(emailVal.length > 0){
        fetch('/authentication/validate-email',{
            body: JSON.stringify({email:emailVal}),
            method:'POST',
    })
        .then((res)=>res.json())
        .then((data)=>{
        console.log("data",data);
        if(data.email_error){
            submitbtn.setAttribute("disabled","disabled");
            emailField.classList.add('is-invalid');
            feedBackAreaEmail.style.display="block";
            feedBackAreaEmail.innerHTML=`<p> ${data.email_error} </p>`;

        }else{
            submitbtn.removeAttribute("disabled");
        }
        });
    }
});