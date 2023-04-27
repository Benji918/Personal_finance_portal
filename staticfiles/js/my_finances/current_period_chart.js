$(document).ready(function () {
    $.get("/my_finances/get_summary_tiles", function (data) {
        for (const [data_name, v] of Object.entries(data)) {
            if (data_name === 'error') {
                $('#summary_tiles').html(v)
            } else if (data_name === 'last_balance_date') {
                $(`#${data_name}`).html(v)
            } else {
                $(`#${data_name}`).html(
                    new Intl.NumberFormat('en-IE', {style: 'currency', currency: 'NGN'}).format(v)
                )
            }
        }
    });

    $.get("/my_finances/get_income_or_outcome_by_type?get_what=income&summary_type=current_period", function (res) {
        doughnut_chart(res, 'income_by_type')
    });

    $.get("/my_finances/get_income_or_outcome_by_type?get_what=outcome&summary_type=current_period", function (res) {
        doughnut_chart(res, 'outcome_by_type')
    });

})