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



 
    
const fileTempl = document.getElementById("file-template"),
  imageTempl = document.getElementById("image-template"),
  empty = document.getElementById("empty");

// use to store pre selected files
let FILES = {};

// check if file is of type image and prepend the initialied
// template to the target element
function addFile(target, file) {
  const isImage = file.type.match("image.*"),
    objectURL = URL.createObjectURL(file);

  const clone = isImage
    ? imageTempl.content.cloneNode(true)
    : fileTempl.content.cloneNode(true);

  clone.querySelector("h1").textContent = file.name;
  clone.querySelector("li").id = objectURL;
  clone.querySelector(".delete").dataset.target = objectURL;
  clone.querySelector(".size").textContent =
    file.size > 1024
      ? file.size > 1048576
        ? Math.round(file.size / 1048576) + "mb"
        : Math.round(file.size / 1024) + "kb"
      : file.size + "b";

  isImage &&
    Object.assign(clone.querySelector("img"), {
      src: objectURL,
      alt: file.name
    });

  empty.classList.add("hidden");
  target.prepend(clone);

  FILES[objectURL] = file;
}

const gallery = document.getElementById("gallery"),
  overlay = document.getElementById("overlay");

// click the hidden input of type file if the visible button is clicked
// and capture the selected files
const hidden = document.getElementById("hidden-input");
document.getElementById("button").onclick = () => hidden.click();
hidden.onchange = (e) => {
  for (const file of e.target.files) {
    addFile(gallery, file);
  }
};

// use to check if a file is being dragged
const hasFiles = ({ dataTransfer: { types = [] } }) =>
  types.indexOf("Files") > -1;

// use to drag dragenter and dragleave events.
// this is to know if the outermost parent is dragged over
// without issues due to drag events on its children
let counter = 0;

// reset counter and append file to gallery when file is dropped
function dropHandler(ev) {
  ev.preventDefault();
  for (const file of ev.dataTransfer.files) {
    addFile(gallery, file);
    overlay.classList.remove("draggedover");
    counter = 0;
  }
}

// only react to actual files being dragged
function dragEnterHandler(e) {
  e.preventDefault();
  if (!hasFiles(e)) {
    return;
  }
  ++counter && overlay.classList.add("draggedover");
}

function dragLeaveHandler(e) {
  1 > --counter && overlay.classList.remove("draggedover");
}

function dragOverHandler(e) {
  if (hasFiles(e)) {
    e.preventDefault();
  }
}

// event delegation to caputre delete events
// fron the waste buckets in the file preview cards
gallery.onclick = ({ target }) => {
  if (target.classList.contains("delete")) {
    const ou = target.dataset.target;
    document.getElementById(ou).remove(ou);
    gallery.children.length === 1 && empty.classList.remove("hidden");
    delete FILES[ou];
  }
};

// print all selected files
document.getElementById("submit").onclick = () => {
//   alert(`Submitted Files:\n${JSON.stringify(FILES)}`);
  console.log(FILES);
};

// clear entire selection
document.getElementById("cancel").onclick = () => {
  while (gallery.children.length > 0) {
    gallery.lastChild.remove();
  }
  FILES = {};
  empty.classList.remove("hidden");
  gallery.append(empty);
};