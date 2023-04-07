let hypeLink1 = document.querySelector('.hypeLink1')
let hypeLink2 = document.querySelector('.hypeLink2')
let hypeLink3 = document.querySelector('.hypeLink3')
let hypeLink4 = document.querySelector('.hypeLink4')
 if(document.URL.includes('index.html')){

    hypeLink1.style.color = '#477bff'
    hypeLink1.style.textDecoration = 'underline'
    hypeLink2.style.color = 'black'
    hypeLink2.style.textDecoration = 'none'
    hypeLink3.style.color = 'black'
    hypeLink3.style.textDecoration = 'none'
    hypeLink4.style.color = 'black'
    hypeLink4.style.textDecoration = 'none'

 }
 else if (document.URL.includes('about_me.html')){
    
    hypeLink1.style.color = 'black'
    hypeLink1.style.textDecoration = 'none'
    hypeLink2.style.color = '#477bff'
    hypeLink2.style.textDecoration = 'underline'
    hypeLink3.style.color = 'black'
    hypeLink3.style.textDecoration = 'none'
    hypeLink4.style.color = 'black'
    hypeLink4.style.textDecoration = 'none'
  
} else if(document.URL.includes('hobby.html')){
    
    hypeLink1.style.color = 'black'
    hypeLink1.style.textDecoration = 'none'
    hypeLink3.style.color = '#477bff'
    hypeLink3.style.textDecoration = 'underline'
    hypeLink2.style.color = 'black'
    hypeLink2.style.textDecoration = 'none'
    hypeLink4.style.color = 'black'
    hypeLink4.style.textDecoration = 'none'
  
} else if(document.URL.includes('education.html')){
    
    hypeLink1.style.color = 'black'
    hypeLink1.style.textDecoration = 'none'
    hypeLink4.style.color = '#477bff'
    hypeLink4.style.textDecoration = 'underline'
    hypeLink3.style.color = 'black'
    hypeLink3.style.textDecoration = 'none'
    hypeLink2.style.color = 'black'
    hypeLink2.style.textDecoration = 'none'
}