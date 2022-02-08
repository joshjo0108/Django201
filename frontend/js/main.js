// AJAX CALLS

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

// EVENT LISTENER
// ANY CLASS NAME WITH ".js-toggle-modal" IN "base.html"
$(document).on("click", ".js-toggle-modal", function(e) {
    // IF IT IS A LINK DON'T DO ANYTHING
    e.preventDefault()
    // TOGGLE ON AND OFF
    $(".js-modal").toggleClass("hidden")
})
.on("click", ".js-submit", function(e) {
    e.preventDefault()
    // GET THE TEXT THAT IS WRITTEN IN base.html
    const text = $(".js-post-text").val().trim()
    const $btn = $(this)

    // IF NOTHING IS WRITTEN, RETURN FALSE
    if(!text.length) {
        return false
    }
    // MAKE IT NOT CLICKABLE AGAIN
    $btn.prop("disabled", true).text("Posting!")

    // AJAX: use of the XMLHttpRequest object to communicate with servers.
    $.ajax({
        type: 'POST',
        // "js-post-text" IS A CLASS FOR TEXTAREA
        url: $(".js-post-text").data("post-url"),
        data: {
            text: text
        },
        // ON SUCCESS, RETURN def post() FUNCTION FROM "views.py"
        success: (dataHtml) => {
            // IN CLASS ".js-modal", ADD CLASS "hidden"
            $(".js-modal").addClass("hidden");

            // "#posts-container" USED IN homepage.html
            // IT PUTS AT THE VERY "TOP" OF ITS PAGE
            $("#posts-container").prepend(dataHtml);

            // MAKE IT CLICKABLE AGAIN
            $btn.prop("disabled", false).text("New Post");

            // EMPTY THE TEXT AREA
            $(".js-post-text").val('')
        },
        error: (error) => {
            console.warn(error)
            // NOT DISABLED ANYMORE
            // prop() -> sets or returns properties and values of the selected elements
            $btn.prop("disabled", false).text("Error");
        }
    });
})
.on("click", ".js-follow", function(e) {
    e.preventDefault();
// CACHING OUT
// FROM "detail.html" IN ONE OF THE CLASS USED
    const action = $(this).attr("data-action")

    $.ajax({
        type: 'POST',
        url: $(this).data("url"),
        data: {
            action: action,
            username: $(this).data("username"),
        },
        // data IN FORM OF JSON
        success: (data) => {
            $(".js-follow-text").text(data.wording)
            if(action == "follow") {
                // Change wording to unfollow
                console.log("DEBUG", "unfollow")
                $(this).attr("data-action", "unfollow")
            } else {
                // The opposite
                console.log("DEBUG", "follow")
                $(this).attr("data-action", "follow")
            }
        },
        error: (error) => {
            console.warn(error)
        }
    });
})