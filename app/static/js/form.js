$(document).ready(

    function () {
        $("#csvupload").click(function () {
            $("#csvupload-input").css("display", "block");
            $("#text-input").css("display", "none");
        });
        $("#manualdata").click(function () {
            $("#csvupload-input").css("display", "none");
            $("#text-input").css("display", "block");
        });
        $("#pngupload").click(function () {
            $("#upimage-input").css("display", "block");
            $("#deimage-input").css("display", "none");
            $("#background-input").css("display", "none");
        });
        $("#defimage").click(function () {
            $("#upimage-input").css("display", "none");
            $("#deimage-input").css("display", "block");
            $("#background-input").css("display", "none");
        });
        $("#defback").click(function () {
            $("#upimage-input").css("display", "none");
            $("#deimage-input").css("display", "none");
            $("#background-input").css("display", "block");
            $("input[name='img-default']").val("user_defined.png");
        });
        $("#text").click(function () {
            $("#cutext-input").css("display", "block");
            $("#config-input").css("display", "none");
        });
        $("#json").click(function () {
            $("#cutext-input").css("display", "none");
            $("#config-input").css("display", "block");
        });

        $("input[type=file], input[type=hidden], input[type=text], textarea").on("keyup change", function () {
            var csv = $("textarea[name='csv']").val();
            var csvFile = $('input[type=file][name="file"]').val();
            var imgDefault = $('input[type=hidden][name="img-default"]').val();
            var imgUploaded = $('input[type=file][name="image"]').val();
            if ((csv || csvFile) && (imgDefault || imgUploaded)) {
                $('button[type=submit]').removeAttr('disabled');
            } else {
                $('button[type=submit]').attr('disabled', 'disabled');
            }
        });
    });

function validate() {
    $("[id=error]").hide();

    var csv = $("textarea[name='csv']").val();
    var csvFile = $('input[type=file][name="file"]').val();

    if (csv === "" && csvFile === "") {
        $(".no-data-error").show();
        return false;
    }

    if (csv !== undefined && csv !== null && csv !== "") {
        var csvLines = csv.split("\n");
        var countLines = 0;
        csvLines.forEach(function (csvLine) {
            var line = csvLine.split(",");
            if (line.length === 4) {
                countLines += 1;
            }
        });
        if (countLines !== csvLines.length) {
            $(".csv-error").show();
            return false;
        }
    }

    if (csvFile !== "") {
        if (csvFile.split(".")[csvFile.split(".").length - 1] !== "csv") {
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

    var configJson = $('input[type=file][name="config"]').val();
    if (configJson !== "") {
        if (configJson.split(".")[configJson.split(".").length - 1] !== "json") {
            $(".config-error").show();
            return false;
        }
    }

    return true;
}
