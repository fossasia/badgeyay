$(document).on("ready", function() {

	$(document).mouseup(function(e) {
		var container = $(".custom-menu-content");
		var button = $(".glyphicon-th");
		// if the target of the click is not the button,
		// the container or a descendant of the container
		if (!button.is(e.target) && !container.is(e.target) && container.has(e.target).length === 0) {
			container.addClass("hidden");
		}
	});

	$(".glyphicon-th").click(function(){
		$(".custom-menu-content").toggleClass("hidden");
	});

	$(".menu-options").click(function(){
		var i = $(this).data("item");
		$(".placeholder").text(i);
		$("input[name='img-default']").val(i);
	});

	$("#picker").minicolors({
		control: "hue",		
		format: "hex",
		letterCase: "lowercase",
		position: "bottom left",
		theme: "bootstrap"
	});

	var apiUrl = "https://api.github.com/repos/fossasia/badgeyay/git/refs/heads/development";
	$.ajax({
		url: apiUrl,
		async: true,
		success(result) {
			if(typeof result.object !== "undefined" && typeof result.object.sha !== "undefined") {
				var version = result["object"]["sha"];
				var versionLink = "https://github.com/fossasia/badgeyay/tree/"+version;
				var deployLink = $(".version").attr("href", versionLink).html(version);
			} else {
				$(".version").html("Failed to access version");
			}
		},
		error(error) {
			$(".version").html("Failed to access version");
		}
	});
});
