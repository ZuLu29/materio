/**
 * One Piece Dashboard Analytics
 */

'use strict';

(function () {
  let cardColor, labelColor, borderColor, chartBgColor, bodyColor;

  cardColor = config.colors.cardColor;
  labelColor = config.colors.textMuted;
  borderColor = config.colors.borderColor;
  chartBgColor = config.colors.chartBgColor;
  bodyColor = config.colors.bodyColor;

  // Movies Released Over Time
  fetch('/api/movies-over-time/')
    .then(res => res.json())
    .then(data => {
      new ApexCharts(document.querySelector("#moviesOverTimeChart"), {
        chart: { type: 'line', height: 300 },
        series: [{ name: 'Movies', data: data.counts }],
        xaxis: { categories: data.years },
        colors: ['#f39c12'],
      }).render();
    });

  // Genre Distribution
  fetch('/api/genre-distribution/')
    .then(res => res.json())
    .then(data => {
      new ApexCharts(document.querySelector("#genreDistributionChart"), {
        chart: { type: 'pie', height: 300 },
        series: data.counts,
        labels: data.labels,
        colors: ['#3498db', '#2ecc71', '#9b59b6', '#e74c3c']
      }).render();
    });

  // Characters by Movie Appearances
  fetch('/api/character-movie-counts/')
    .then(res => res.json())
    .then(data => {
      const barHeight = 35;
      const chartHeight = data.counts.length * barHeight;

      new ApexCharts(document.querySelector("#characterAppearancesChart"), {
        chart: {
          type: 'bar',
          height: chartHeight
        },
        series: [{ name: 'Appearances', data: data.counts }],
        xaxis: { categories: data.characters },
        plotOptions: {
          bar: { horizontal: true }
        },
        dataLabels: { enabled: true },
        colors: ['#1abc9c']
      }).render();
    });

  // Most Featured Straw Hat Pirates
  fetch('/api/most-featured-strawhats/')
    .then(res => res.json())
    .then(data => {
      new ApexCharts(document.querySelector("#mostFeaturedStrawhatsChart"), {
        chart: { type: 'donut', height: 300 },
        series: data.counts,
        labels: data.labels,
        colors: ['#e67e22', '#2980b9', '#16a085', '#8e44ad', '#f1c40f']
      }).render();
    });

})();
