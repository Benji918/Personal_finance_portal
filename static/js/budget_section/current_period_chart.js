
var ctx = document.getElementById('daily-spending-chart');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [
            {% for date, spending in daily_spending.items %}
            "{{ date }}",
            {% endfor %}
        ],
        datasets: [{
            label: 'Daily Spending',
            data: [
                {% for date, spending in daily_spending.items %}
                {{ spending }},
                {% endfor %}
            ],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
console.log(daily_spending);

