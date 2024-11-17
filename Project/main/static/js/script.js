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
        heroSection.style.backgroundImage = "url('https://i.pinimg.com/236x/b3/4f/3d/b34f3d4ded10e2cd1456f82821fafe49.jpg')";
    });
    photographerSection.addEventListener('mouseleave', function() {
        heroSection.style.backgroundImage = "url('https://i.pinimg.com/236x/b3/4f/3d/b34f3d4ded10e2cd1456f82821fafe49.jpg')";
    });
});

