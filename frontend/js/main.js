$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});


$(document).on("click", ".js-add-item", function(e) {
    e.preventDefault();
    const action = $(this).attr("data-action")
    console.log(action)
    
    $.ajax({
        type: 'POST',
        url:$(this).data("url"),
        data: {
            action: action,
            product: $(this).data("name")
        },
        success: (data) => {
          location.reload();

            console.log(data)
            $(".js-cart-text").text(data.wording)
            if(action == "add-item") {
                // Change wording to unfollow
                console.log("DEBUG", "remove-item")
                $(this).attr("data-action", "remove-item")
            } else {
                // The opposite
                console.log("DEBUG", "add-item")
                $(this).attr("data-action", "add-item")
            }
        },
        error: (error) => {
            console.warn(error)
        }
    });
})
$(document).on("click", ".js-remove-item", function(e) {
    e.preventDefault();
    
    $.ajax({
        type: 'POST',
        url:$(this).data("url"),
        data: {
            product: $(this).data("name")
        },
        success: (data) => {
            console.log(data)
          location.reload();

          
        },
        error: (error) => {
            console.warn(error)
        }
    });
})

$(document).on("click", ".js-remove-product", function(e) {
  e.preventDefault();
  $.ajax({
      type: 'POST',
      url:$(this).data("remove-url"),
      data: {
          product: $(this).data("name")
      },
      success: (data) => {
          console.log(data)
          document.location.href="/"
          // location.reload();
      },
      error: (error) => {
          console.warn(error)
      }
  });
})

$(document).on("click", ".js-rating-submit", function(e) {
  e.preventDefault();
  var ele = document.getElementsByName('rating');
  for(i = 0; i < ele.length; i++) {
    if(ele[i].checked)
    var rate=ele[i].value
  }
  // const  = $(".js-rating").val()
  console.log(rate)
  
  $.ajax({
      type: 'POST',
      url:$(this).data("post-url"),
      data: {
        rating: rate,
          product: $(this).data("name")
      },
      success: (data) => {
        location.reload();

          console.log(data)
          $(".js-cart-text").text(data.wording)
          if(action == "add-item") {
              // Change wording to unfollow
              console.log("DEBUG", "remove-item")
              $(this).attr("data-action", "remove-item")
          } else {
              // The opposite
              console.log("DEBUG", "add-item")
              $(this).attr("data-action", "add-item")
          }
      },
      error: (error) => {
          console.warn(error)
      }
  });
})


document.addEventListener("alpine:init", () => {
    Alpine.data("app", () => ({
        total: 0,
        selected: [],

        toggleCheckbox(element, amount) {
            if (element.checked) {
                this.selected.push(element.value);
                this.total += amount;
            } else {
                const index = this.selected.indexOf(element.value);

                if (index > -1) this.selected.splice(index, 1);

                this.total -= amount;
            }
        },
    }));
});