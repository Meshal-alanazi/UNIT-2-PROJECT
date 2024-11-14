document.addEventListener('DOMContentLoaded', function() {
    const developerSection = document.getElementById('developer');
    const photographerSection = document.getElementById('photographer');
    const heroSection = document.querySelector('.hero');
   
   
    developerSection.addEventListener('mouseenter', function() {
        heroSection.style.backgroundImage = "url('https://images.unsplash.com/photo-1554774853-aae0a22c8aa4?auto=format&fit=crop&q=80')";
    });

   
    photographerSection.addEventListener('mouseenter', function() {
        heroSection.style.backgroundImage = "url('https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&q=80')";
    });

  
    developerSection.addEventListener('mouseleave', function() {
        heroSection.style.backgroundImage = "url('https://i.pinimg.com/originals/61/8f/08/618f083c61a7460ce0a6064319af41bd.gif')";
    });
    photographerSection.addEventListener('mouseleave', function() {
        heroSection.style.backgroundImage = "url('https://i.pinimg.com/originals/61/8f/08/618f083c61a7460ce0a6064319af41bd.gif')";
    });
});

