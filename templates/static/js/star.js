if ($(".starRandom").length > 0) {
  $(".starRandom").each(function (index, el) {
    console.log();
    const aleatorio = Math.floor(Math.random() * (5 - 1 + 1) + 1);

    for (let i = 0; i < aleatorio; i++) {
      $(el).append("<i class='bi bi-star-fill checkedStar'></i>");
    }
    if (aleatorio == 1) {
      $(el).append(
        "<i class='bi bi-star'></i><i class='bi bi-star'></i><i class='bi bi-star'></i><i class='bi bi-star'></i>"
      );
    } else if (aleatorio == 2) {
      $(el).append(
        "<i class='bi bi-star'></i><i class='bi bi-star'></i><i class='bi bi-star'></i>"
      );
    } else if (aleatorio == 3) {
      $(el).append("<i class='bi bi-star'></i><i class='bi bi-star'></i>");
    } else if (aleatorio == 4) {
      $(el).append("<i class='bi bi-star'></i>");
    }
  });
}
