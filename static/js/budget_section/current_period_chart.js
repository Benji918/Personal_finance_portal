
var ctx = document.getElementById('daily-spending-chart');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: Object.keys(daily_spending),
        datasets: [{
            label: 'Daily Spending',
            data: Object.values(daily_spending),
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
