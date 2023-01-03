
$(document).ready(function () {



    $.get("/my_finances/get_year_chart?balance_type=current", function (res) {
        line_chart(res, 'year_chart_canvas')
    });


    $.get("/my_finances/get_income_or_outcome_by_type?get_what=income&summary_type=year_overview", function (res) {
        doughnut_chart(res, 'income_by_type')
    });

    $.get("/my_finances/get_income_or_outcome_by_type?get_what=outcome&summary_type=year_overview", function (res) {
        doughnut_chart(res, 'outcome_by_type')
    });

    $.get("/my_finances/get_year_chart?balance_type=savings", function (res) {
        line_chart(res, 'savings_year')
    });

})