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

function validate() {
	$("[id=error]").hide();
	var pdf = $("#pdf").is(":checked");
	var zip = $("#zip").is(":checked");

	if (!pdf && !zip) {
		$(".option-error").show();
		return false;
	}

	var csv = $("textarea[name='csv']").val();
	var csvFile = $('input[type=file][name="file"]').val();

	if (csv === "" && csvFile === "") {
		$(".no-data-error").show();
		return false;
	}

	if (csv !== undefined && csv !== null && csv !== "") {
		var csvLines = csv.split("\n");
		var countLines = 0;
		csvLines.forEach(function(csvLine) {
			var line = csvLine.split(",");
			if (line.length === 4) {
				countLines += 1
			}
		});
		if (countLines !== csvLines.length) {
			$(".csv-error").show();
			return false;
		}
	}

	if (csvFile !== "") {
		if (csvFile.indexOf(".csv") === -1) {
			$(".csvfile-error").show();
			return false;
		}
	}

	var imgDefault = $('input[type=hidden][name="img-default"]').val();
	var imgUploaded = $('input[type=file][name="image"]').val();

	if (imgDefault === "" && imgUploaded === "") {
		$(".no-image-error").show();
		return false;
	}

	if (imgUploaded !== "") {
		if (imgUploaded.indexOf(".png") === -1) {
			$(".image-error").show();
			return false;
		}
	}

	var configJson = $('input[type=file][name="config"]').val();
	console.log(configJson);
	if (configJson !== "") {
	    if (configJson.indexOf(".json") === -1) {
		    $(".config-error").show();
		    return false;
	    }
	}

	return true;
}
