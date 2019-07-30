ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [57.558173, 62.751976],
            zoom: 11
        }, {
            searchControlProvider: 'yandex#search'
        }),

        // Создаём макет содержимого.
        MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
            '<div style="color: #000000; font-weight: bold;">$[properties.iconContent]</div>'
        ),

        myPlacemarkWithContent = new ymaps.Placemark([57.567735, 62.715042], {
            // Зададим содержимое заголовка балуна.
            balloonContentHeader: 'Скородумское, село<br>',
            // Зададим содержимое основной части балуна.
            balloonContentBody: 'Метрические книги:  ' + '<a href="metric1801.html">1801</a> '   +'   '+ '<a href="metric1802.html">1802</a><br > ' +
            'Ревизские сказки:  ' + '<a href="revision1710.html">1710</a>' +'  ' +'<a href="revision1762.html">1762</a>',
            // Зададим содержимое всплывающей подсказки.
            iconContent: 'Скродумское'
        }, {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#imageWithContent',
            // Своё изображение иконки метки.
            iconImageHref: 'images/church.png',
            // Размеры метки.
            iconImageSize: [40, 40],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [-20, -40],
            // Смещение слоя с содержимым относительно слоя с картинкой.
            iconContentOffset: [-5, 42],
            // Макет содержимого.
            iconContentLayout: MyIconContentLayout,

            hideIconOnBalloonOpen: false
        });


        myPlacemarkWithContent1 = new ymaps.Placemark([57.554896, 62.661929], {
            // Зададим содержимое заголовка балуна.
            balloonContentHeader: 'Ретнева, деревня<br>',
            // Зададим содержимое основной части балуна.
            balloonContentBody: 'Метрические книги:  ' + '<a href="metric1801.html">1801</a> '   +'   '+ '<a href="metric1802.html">1802</a><br > ' +
            'Ревизские сказки:  ' + '<a href="revision1710.html">1710</a>' +'  ' +'<a href="revision1762.html">1762</a>',
            // Зададим содержимое всплывающей подсказки.
            iconContent: 'Ретнева'
        }, {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#imageWithContent',
            // Своё изображение иконки метки.
            iconImageHref: 'images/ballon.png',
            // Размеры метки.
            iconImageSize: [40, 40],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [-20, -40],
            // Смещение слоя с содержимым относительно слоя с картинкой.
            iconContentOffset: [-5, 42],
            // Макет содержимого.
            iconContentLayout: MyIconContentLayout,

            hideIconOnBalloonOpen: false
        });

        myPlacemarkWithContent2 = new ymaps.Placemark([57.551560, 62.489906], {
            // Зададим содержимое заголовка балуна.
            balloonContentHeader: 'Осинцева, деревня<br>',
            // Зададим содержимое основной части балуна.
            balloonContentBody: 'Метрические книги:  ' + '<a href="metric1801.html">1801</a> '   +'   '+ '<a href="metric1802.html">1802</a><br > ' +
            'Ревизские сказки:  ' + '<a href="revision1710.html">1710</a>' +'  ' +'<a href="revision1762.html">1762</a>',
            // Зададим содержимое всплывающей подсказки.
            iconContent: 'Осинцева'
        }, {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#imageWithContent',
            // Своё изображение иконки метки.
            iconImageHref: 'images/ballon.png',
            // Размеры метки.
            iconImageSize: [40, 40],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [-20, -40],
            // Смещение слоя с содержимым относительно слоя с картинкой.
            iconContentOffset: [-5, 42],
            // Макет содержимого.
            iconContentLayout: MyIconContentLayout,

            hideIconOnBalloonOpen: false
        });




        myPlacemarkWithContent3 = new ymaps.Placemark([57.540910, 62.608760], {
            // Зададим содержимое заголовка балуна.
            balloonContentHeader: 'Меркушина, деревня (исчезн.)<br>',
            // Зададим содержимое основной части балуна.
            balloonContentBody: 'Метрические книги:  ' + '<a href="metric1801.html">1801</a> '   +'   '+ '<a href="metric1802.html">1802</a><br > ' +
            'Ревизские сказки:  ' + '<a href="revision1710.html">1710</a>' +'  ' +'<a href="revision1762.html">1762</a>',
            // Зададим содержимое всплывающей подсказки.
            iconContent: 'Меркушина'
        }, {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#imageWithContent',
            // Своё изображение иконки метки.
            iconImageHref: 'images/ischez.png',
            // Размеры метки.
            iconImageSize: [27, 40],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [-20, -40],
            // Смещение слоя с содержимым относительно слоя с картинкой.
            iconContentOffset: [-5, 42],
            // Макет содержимого.
            iconContentLayout: MyIconContentLayout,

            hideIconOnBalloonOpen: false
        });

    myMap.geoObjects
        .add(myPlacemarkWithContent)
        .add(myPlacemarkWithContent1)
        .add(myPlacemarkWithContent2)
        .add(myPlacemarkWithContent3);
});