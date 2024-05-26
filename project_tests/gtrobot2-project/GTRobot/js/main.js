let info_modal_dict = {
    "Тех.Поддержка": "Эта услуга предоставляет помощь со стороны операторов по техническим вопросам связанные с GTRobot.",
    "Куратор": "Эта услуга предоставляет помощь со стороны куратора по всем вопросам связанные с GTRobot.",
    "Главный куратор": "Эта услуга предоставляет помощь со стороны главного куратора по всем вопросам связанные с торговлей и GTRobot.",
    "Уроки Crypto": "Этот комплект включает в себя уроки по Crypto трейдингу которые будут полезны для работы с GTRobot, их количество составляет 19шт. Уроки предоставляются в виде PDF файлов и видео уроков, в нужном вам языке (Рус & Узб) ",
    "Уроки Forex": "Этот комплект включает в себя уроки по Forex трейдингу которые будут полезны для работы с GTRobot, их количество составляет 11шт. Уроки предоставляются в виде PDF файлов и видео уроков, в нужном вам языке (Рус & Узб)",
    "Уроки NFT": "Этот комплект включает в себя уроки по NFT торговле которые будут полезны для работы с GTRobot, их количество составляет 7шт. Уроки предоставляются в виде PDF файлов и видео уроков, в нужном вам языке (Рус & Узб)",
    "Уроки P2P": "Этот комплект включает в себя уроки по P2P арбитражу которые будут полезны для работы с GTRobot, их количество составляет 6шт. Уроки предоставляются в виде PDF файлов и видео уроков, в нужном вам языке (Рус & Узб)",
    "Cloud Mining PRO": "Это расширение предоставит вам больше эффективности в майнинге. Облегчая вам процесс и увеличивая доходность майнинга за счет меньших активаций. <br> <br> Одна активация на 8 часов. <br> + 100% к скорости майнинга. <br> Освобождение от новых заданий.",
    "Cloud Mining ULTRA": "Это расширение предоставит вам больше эффективности в майнинге. Облегчая вам процесс и увеличивая доходность майнинга за счет меньших активаций. <br> <br> Одна активация на 16 часов. <br> Майнинг 24/7 <br> + 200% к скорости майнинга. <br> Освобождение от новых заданий. <br> Лимит заработка в GTRobot Mining составит 300$. (Которые можно будет использовать в виде скидки при покупки тарифа VIP)",
    "Заморозка и замена услуг": "Эта услуга предоставляет вам возможность изменять услуги в вашем тарифном плане после его приобретения. Вы можете добавлять новые услуги, оплачивая только за необходимые вам изменения, а также замораживать ваш текущий тариф на период до 30 дней по вашему желанию.",
    "Baxtli obunachi 3.0": "Билеты для участия в проекте Baxtli obunachi 3.0 2024. (Информацию о проекте можете найти на YouTube Khasanov)",
    "Индикатор": "Это расширение для Trading View, которое поможет вам в проведении анализа и повышении эффективности в торговле.",
    "Регистрация у брокера": "Эта услуга предоставит помощь с регистрацией в вашем брокере, технический помощник зарегистрирует все за вас.",
    "Проп счет": "Эта услуга предоставит помощь с регистрацией в Проп компании, технический помощник зарегистрирует все за вас и приобретет торговый счет для вашего использования.",
    "Премия": "Это соревновательная игра, в рамках которой каждый месяц будут выбираться победители среди пользователей, достигших наилучших результатов. Победителям будут предоставляться денежные премии.",
}

let services_price_crypto_dict = {
    "Тех.Поддержка": 60,
    "Куратор": 99,
    "Главный куратор": 149,
    "Уроки Crypto": 35,
    "Уроки Forex": 25,
    "Уроки NFT": 25,
    "Уроки P2P": 13,
    "Cloud Mining PRO": 5.9,
    "Cloud Mining ULTRA": 9.9,
    "Заморозка и замена услуг": 18,
    "Baxtli obunachi 3.0": 5,
}

let services_price_forex_dict = {
    "Тех.Поддержка": 60,
    "Куратор": 99,
    "Главный куратор": 149,
    "Индикатор": 40,
    "Уроки Forex": 25,
    "Регистрация у брокера": 12,
    "Проп счет": 50,
    "Премия": 10,
    "Заморозка и замена услуг": 19,
    "Baxtli obunachi 3.0": 5,
}

let crypto_rate_services_dict = {
    "": [],
    "Первопроходец рынка": [],
    "Трейдер-Новичок": [],
    "Энтузиаст криптовалют": ["Тех.Поддержка"],
    "Крипто Акула": ["Тех.Поддержка", "Уроки Crypto"],
    "Инвестиционный инсайдер": ["Куратор", "Уроки Crypto", "Заморозка и замена услуг"],
    "Кит крипторынка": ["Куратор", "Уроки Crypto", "Уроки Forex", "Заморозка и замена услуг"],
    "VIP": ["Главный куратор", "Уроки Crypto", "Уроки Forex", "Уроки NFT", "Уроки P2P", "Cloud Mining ULTRA", "Заморозка и замена услуг"],
}

let forex_rate_services_dict = {
    "": [],
    "Пионер рынка": [],
    "Начинающий финансист": [],
    "Корпоративный Инвестор": ["Тех.Поддержка"],
    "Биржевой стратег": ["Тех.Поддержка", "Заморозка и замена услуг"],
    "Форекс гуру": ["Куратор", "Премия", "Заморозка и замена услуг"],
    "Финансовый магнат": ["Куратор", "Уроки Forex", "Премия", "Заморозка и замена услуг"],
    "Волк с Wall-Street": ["Куратор", "Индикатор", "Уроки Forex", "Премия", "Заморозка и замена услуг"],
    "VIP": ["Главный куратор", "Индикатор", "Уроки Forex", "Регистрация у брокера", "Проп счет", "Премия", "Заморозка и замена услуг"],
}


let crypto_active_rate_status = "";
let forex_active_rate_status = "";

let crypto_coef_value = 1;
let forex_coef_value = 1;

let crypto_days_value = 0;
let forex_days_value = 0;


let free_servises_list = [];

let support_gradation = ["Тех.Поддержка", "Куратор", "Главный куратор"];
let mining_gradation = ["Cloud Mining PRO", "Cloud Mining ULTRA"];


// Loader window
document.addEventListener("DOMContentLoaded", function () {
    let preloader = document.querySelector(".loader-wrap");
    let wrapper = document.querySelector(".wrapper");

    window.addEventListener('load', function () {
        setTimeout(function () {
            preloader.classList.remove("anime");
            wrapper.style.opacity = '1';
            document.body.style.overflow = 'auto';
        }, 1500);

        document.body.style.overflow = 'hidden';
    });
});


$(document).ready(function () {

    // Accorion ======
    const accordionItems = document.querySelectorAll('.accordion_item');
    let lastClickedAccordionContent = null;

    accordionItems.forEach((item) => {
        const accordionHeader = item.querySelector('.accordion_header');
        const accordionIcon = item.querySelector('.plus_img');
        const accordionContent = item.querySelector('.accordion_content');

        accordionHeader.addEventListener('click', () => {
            if (lastClickedAccordionContent && lastClickedAccordionContent !== accordionContent) {
                lastClickedAccordionContent.style.maxHeight = null;
                lastClickedAccordionContent.previousElementSibling.querySelector('.plus_img').classList.remove('active');
            }

            accordionContent.style.maxHeight = accordionContent.style.maxHeight ? null : accordionContent.scrollHeight + 'px';
            accordionIcon.classList.toggle('active');

            lastClickedAccordionContent = accordionContent.style.maxHeight ? accordionContent : null;
        });
    });


    // Header menu ======
    let headerMob = document.querySelector('.header_mob');
    let headerMobLink = document.querySelectorAll('.menu_header a');
    let headerMobBg = document.querySelector('.header-mob-bg');
    let menuOpen = document.querySelector('.header-bars');
    let menuClose = document.querySelector('.header-close');

    menuOpen.addEventListener('click', function (e) {
        headerMob.classList.add('active');
    });
    menuClose.addEventListener('click', function (e) {
        headerMob.classList.remove('active');
    });

    headerMobLink.forEach(function (link) {
        link.addEventListener('click', function (e) {
            headerMob.classList.remove('active');
        });
    });

    headerMobBg.addEventListener('click', function (e) {
        headerMob.classList.remove('active');
    });


    // constructor_item-box =====
    let boxTabs = document.querySelectorAll('.constructor_item-box-top');
    let constructorItems = document.querySelectorAll('.constructor_item-goups-more');

    boxTabs.forEach((tab, index) => {
        const constructorItem = constructorItems[index];

        tab.addEventListener('click', () => {
            let boxTabsSpan = tab.querySelector('span');

            tab.classList.toggle('active');
            if (tab.classList.contains('active')) {
                boxTabsSpan.textContent = '';
            } else {
                boxTabsSpan.textContent = 'Ещё';
            }
            constructorItem.classList.toggle('active');
        });
    });


    // Input mask =====
    document.addEventListener('DOMContentLoaded', function () {
        try {
            applyMask('cardNumber', '0000 0000 0000 0000');
            applyMask('cardDate', '00/00');
            applyMask('cardCode', '***');
        } catch (error) {
            console.log();
        }
    });

    function applyMask(elementId, mask) {
        let element = document.getElementById(elementId);
        let maskOptions = {
            mask: mask,
            lazy: false
        };

        element.addEventListener('focus', function () {
            new IMask(element, maskOptions);
        });
    }


    // Input range =====
    let $rangeInput = $('.constructor_item-rental1 .range input');
    let $rangeAfter = $('.constructor_item-rental1 .range').find('span');

    let sheet = document.createElement('style');
    document.body.appendChild(sheet);

    $rangeInput.on('input', function () {
        rangeInput1(parseInt(this.value))
    });

    function initRangeSlider() {
        let initialValue = 21;
        $rangeAfter.text(initialValue + " дней");
    }

    initRangeSlider();

    $('.range-labels li').on('click', function () {
        let index = $(this).index();
        $rangeInput.val(index + 1).trigger('input');
    });

    function rangeInput1(inp) {
        let $priceRange = $('.constructor_item-rental1 .price-range');
        let $priceRange2 = $('.constructor_item-rental1 .price-range2');
        let $priceBenefit = $('.constructor_item-rental1 .price-benefit');
        let $rateMob = $('.constructor_item-rental1 .mob-rate b');
        let $rate = $('.constructor_item-rental1 .rate');
        let $priceBenefit2 = $('.constructor_item-rental1 .item_mob-price-title b');

        let curVal = inp;

        let rateText = '';
        let newBenefitPrice = '';
        let newPrice = '';
        let rotateValue = '';

        if (curVal >= 21 && curVal < 40) {
            rateText = 'Первопроходец рынка';
            newBenefitPrice = 1.9;
            newPrice = 39 + (curVal - 21);
        } else if (curVal >= 40 && curVal < 90) {
            rateText = 'Трейдер-Новичок';
            newBenefitPrice = 1.8;
            newPrice = 72 + (curVal - 40);
        } else if (curVal >= 90 && curVal < 120) {
            rateText = 'Энтузиаст криптовалют';
            newBenefitPrice = 1.5;
            newPrice = 135 + (curVal - 90);
        } else if (curVal >= 120 && curVal < 160) {
            rateText = 'Крипто Акула';
            newBenefitPrice = 1.4;
            newPrice = 168 + (curVal - 120);
        } else if (curVal >= 160 && curVal < 365) {
            rateText = 'Инвестиционный инсайдер';
            newBenefitPrice = 1.2;
            newPrice = 240 + (curVal - 200);
        } else if (curVal >= 365 && curVal <= 776) {
            rateText = 'Кит крипторынка';
            newBenefitPrice = 1.1;
            newPrice = 401 + (curVal - 300);
        } else if (curVal === 777) {
            rateText = 'VIP';
            newBenefitPrice = 1;
            newPrice = 910 + (curVal - 777);
        }

        $('#constructorWrap').css({
            'transform': 'rotate(' + rotateValue + ')',
        });

        $rate.text(rateText);
        $rateMob.text(rateText);
        $priceBenefit.text(newBenefitPrice + "$");
        $priceBenefit2.text(newBenefitPrice + "$");
        $priceRange.text(newPrice + "$");
        $priceRange2.text(newPrice + "$");
        $rangeAfter.text(curVal + " дней");

        crypto_active_rate_status = rateText;

        crypto_coef_value = newBenefitPrice;
        crypto_days_value = curVal;
        
        update_cart();

        let val = (curVal - 10) * (100 / 777);
        let gradientStyle = 'linear-gradient(90.00deg, #00ffff99,#11484e99 ' + val + '%, #1d2933 ' + val + '%, #1d2933 100%)';
        $('.constructor_item-rental1 .range').css('background', gradientStyle);
    }


    let $rangeInput2 = $('.constructor_item-rental2 .range input');
    let $rangeAfter2 = $('.constructor_item-rental2 .range').find('span');

    let sheet2 = document.createElement('style');
    document.body.appendChild(sheet);

    $rangeInput2.on('input', function () {
        rangeInput2(parseInt(this.value))
    });

    function initRangeSlider2() {
        let initialValue = 5;
        $rangeAfter2.text(initialValue + " дней");
    }

    initRangeSlider2();

    $('.range-labels li').on('click', function () {
        let index = $(this).index();
        $rangeInput2.val(index + 1).trigger('input');
    });


    function update_cart() {
        const constructor_type = document.querySelector('#gtForexBtn');
        let is_forex = constructor_type.classList.contains('active');
        let gt_services = is_forex ? document.querySelector('#gtForex') : document.querySelector('#gtCrypto');

        // checked_services.forEach((service) => {
        //     if (is_forex) {
        //         console.log(services_price_forex_dict[service]);
        //     }
        //     else {
        //         console.log(services_price_crypto_dict[service]);
        //     }
        // })

        const basketBoxs = document.querySelector('.basket_boxs');

        basketBoxs.innerHTML = '';

        let totalSum = 0;

        // console.log(forex_days_value);
        // console.log(crypto_days_value);

        days_value = is_forex ? forex_days_value : crypto_days_value;

        let days_slider_price = is_forex ? Math.floor(days_value * forex_coef_value) : Math.floor(days_value * crypto_coef_value);

        // console.log("Price: " + days_slider_price);

        $priceRange = $('.price-range');
        $priceRange.text(days_slider_price + '$');

        user_benefit_value = 0;

        let active_services = is_forex ? forex_rate_services_dict[forex_active_rate_status] : crypto_rate_services_dict[crypto_active_rate_status];

        let constructor_items_info = gt_services.querySelectorAll(".constructor_item-info");
        // let constructor_checkboxes = document.querySelectorAll(".constructor_checkbox");

        // let selected_checkboxes = [];

        // constructor_checkboxes.forEach((selected_checkbox) => {
        //     selected_checkboxes.push(selected_checkbox.id.match(/\d+/)[0]);
        // });

        let active_support_label = "";
        let active_mining_label = "";

        let selected_support_label = "";
        let selected_mining_label = "";

        active_services.forEach((label) => {
            if (support_gradation.includes(label)) {
                active_support_label = label;
            }

            if (mining_gradation.includes(label)) {
                active_mining_label = label;
            }
        });

        constructor_items_info.forEach((constructor_item) => {
            let service_label = constructor_item.querySelector('.constructor_item-label').textContent;
            let service_checkbox = constructor_item.querySelector('.constructor_checkbox');
            
            if (service_checkbox.checked) {
                if (support_gradation.includes(service_label)) {
                    selected_support_label = service_label;
                }

                if (mining_gradation.includes(service_label)) {
                    selected_mining_label = service_label;
                }
            }
        });

        if (active_support_label != "" && selected_support_label != "") {
            if (support_gradation.indexOf(active_support_label) < support_gradation.indexOf(selected_support_label)) {
                active_services = active_services.filter(item => item !== active_support_label);
            }
            else if (support_gradation.indexOf(active_support_label) >= support_gradation.indexOf(selected_support_label)) {
                constructor_items_info.forEach((constructor_item) => {
                    let service_label = constructor_item.querySelector('.constructor_item-label').textContent;
                    let service_checkbox = constructor_item.querySelector('.constructor_checkbox');

                    if (service_label == selected_support_label) {
                        let service_id = service_checkbox.id.match(/\d+/)[0];
                        let service_icon = document.querySelector('#itemGroupIcon' + service_id);

                        service_checkbox.checked = false;
                        service_icon.classList.remove('active');
                    }
                });
            }
        }

        if (active_mining_label != "" && selected_mining_label != "") {
            if (mining_gradation.indexOf(active_mining_label) < mining_gradation.indexOf(selected_mining_label)) {
                active_services = active_services.filter(item => item !== active_mining_label);
            }
            else if (mining_gradation.indexOf(active_mining_label) > mining_gradation.indexOf(selected_mining_label)) {
                constructor_items_info.forEach((constructor_item) => {
                    let service_label = constructor_item.querySelector('.constructor_item-label').textContent;
                    let service_checkbox = constructor_item.querySelector('.constructor_checkbox');

                    if (service_label == selected_mining_label) {
                        let service_id = service_checkbox.id.match(/\d+/)[0];
                        let service_icon = document.querySelector('#itemGroupIcon' + service_id);

                        service_checkbox.checked = false;
                        service_icon.classList.remove('active');
                    }
                });
            }
        }

        constructor_items_info.forEach((constructor_item) => {
            let item_label = constructor_item.querySelector('.constructor_item-label').textContent;
            let service_checkbox = constructor_item.querySelector('.constructor_checkbox');

            if (free_servises_list.includes(item_label)) {
                let service_id = service_checkbox.id.match(/\d+/)[0];
                let service_icon = document.querySelector('#itemGroupIcon' + service_id);

                service_checkbox.checked = false;
                service_icon.classList.remove('active');
            }

            if (active_services.includes(item_label)) {
                let service_id = service_checkbox.id.match(/\d+/)[0];
                let service_icon = document.querySelector('#itemGroupIcon' + service_id);

                service_checkbox.checked = true;
                service_icon.classList.add('active');
            }
        });

        const constructorIcon = document.querySelectorAll('.constructor_icon.active');
        let radius = 180;
        if (window.innerWidth > 577 && window.innerWidth <= 776) {
            radius = 160
        } else if (window.innerWidth <= 576) {
            radius = 140
        } else {
            radius = 180
        }

        const totalActiveImages = constructorIcon.length;
        const angleStep = 360 / totalActiveImages;

        constructorIcon.forEach((image, index) => {
            const angle = index * angleStep;
            const radians = angle * Math.PI / 180;
            const x = Math.cos(radians) * radius;
            const y = Math.sin(radians) * radius;
            image.style.transform = `translate(-50%, -50%) translate(${x}px, ${y}px)`;
        });

        free_servises_list = active_services;
        
        price_by_day = is_forex ? 5 : 1.9;
        user_benefit_value += Math.floor(price_by_day * days_value - days_slider_price);

        $priceBenefit = $('.price-benefit');
        $priceBenefit.text(user_benefit_value + "$")

        totalSum += days_slider_price;

        const checked_services = [];

        const item_groups = gt_services.querySelectorAll('.constructor_item-goup');
        
        item_groups.forEach((item_group) => {
            const checkbox = item_group.querySelector('.constructor_checkbox');
            const service_label = item_group.querySelector('.constructor_item-label');

            if (checkbox.checked) {
                checked_services.push(service_label.textContent);
            }
        });

        // console.log('checked services');
        // console.log(checked_services);

        checked_services.forEach((service) => {
            let price = is_forex ? services_price_forex_dict[service] : services_price_crypto_dict[service];
            let final_price = active_services.includes(service) ? 0 : price;

            const basketBox = document.createElement('div');
            basketBox.className = 'basket_box';

            if (service == 'Baxtli obunachi 3.0') {
                let tickets_count = is_forex ? parseInt(document.querySelector('#result-calc2').textContent, 10) : parseInt(document.querySelector('#result-calc1').textContent, 10);

                final_price = price * tickets_count

                console.log(final_price);
            }
            
            totalSum += final_price;

            // console.log(service);

            if (final_price === 0) {
                basketBox.innerHTML = `
                    <div class="basket_box-texts">
                        <span>${service}</span>
                        <div class="present">Подарок</div>
                    </div>
                    <div class="basket_box-total">
                        <span>$${price}</span>
                        <b>$0</b>
                    </div>
                `;
            } else {
                basketBox.innerHTML = `
                    <span>${service}</span>
                    <b>$${final_price}</b>
                `;
            }

            basketBoxs.appendChild(basketBox);
        });

        const totalElement = document.querySelector('.constructor_total-text b');
        totalElement.textContent = `$${totalSum} USD`;
    }


    function rangeInput2(inp) {
        // let $priceRange21 = $('.constructor_item-rental2 .price-range');
        // let $priceRange22 = $('.constructor_item-rental2 .price-range2');
        // $priceRange21.text(newPrice + "$");
        // $priceRange22.text(newPrice + "$");
        // let $priceBenefit21 = $('.constructor_item-rental2 .price-benefit');
        // let $priceBenefit22 = $('.constructor_item-rental2 .item_mob-price-title b');

        let $rateMob2 = $('.constructor_item-rental2 .mob-rate b');
        let $rate2 = $('.constructor_item-rental2 .rate');

        let curVal = inp;
        let rateText = '';
        let newBenefitPrice = '';
        let newPrice = '';
        let rotateValue = '';

        if (curVal >= 5 && curVal < 15) {
            rateText = 'Пионер рынка';
            newBenefitPrice = 5;
            newPrice = 39 + (curVal - 5);
        } else if (curVal >= 15 && curVal < 30) {
            rateText = 'Начинающий финансист';
            newBenefitPrice = 3;
            newPrice = 48 + (curVal - 15);
        } else if (curVal >= 30 && curVal < 60) {
            rateText = 'Корпоративный Инвестор';
            newBenefitPrice = 2.5;
            newPrice = 62 + (curVal - 30);
        } else if (curVal >= 60 && curVal < 90) {
            rateText = 'Биржевой стратег';
            newBenefitPrice = 2;
            newPrice = 91 + (curVal - 60);
        } else if (curVal >= 90 && curVal < 110) {
            rateText = 'Форекс гуру';
            newBenefitPrice = 1.9;
            newPrice = 120 + (curVal - 90);
        } else if (curVal >= 110 && curVal < 180) {
            rateText = 'Финансовый магнат';
            newBenefitPrice = 1.5;
            newPrice = 140 + (curVal - 110);
        } else if (curVal >= 180 && curVal <= 364) {
            rateText = 'Волк с Wall-Street';
            newBenefitPrice = 1.4;
            newPrice = 209 + (curVal - 180);
        } else if (curVal === 365) {
            rateText = 'VIP';
            newBenefitPrice = 1.23013699;
            newPrice = 209 + (curVal - 180);
        }

        $('#constructorWrap').css({
            'transform': 'rotate(' + rotateValue + ')',
        });

        $rate2.text(rateText);
        $rateMob2.text(rateText);

        // $priceRange21.text(newPrice + "$");
        // $priceRange22.text(newPrice + "$");
        $rangeAfter2.text(curVal + " дней");

        forex_active_rate_status = rateText;

        forex_coef_value = newBenefitPrice;
        forex_days_value = curVal;
    
        update_cart();

        let val = (curVal - 5) * (100 / 365);
        let gradientStyle = 'linear-gradient(90.00deg, #00ffff99,#11484e99 ' + val + '%, #1d2933 ' + val + '%, #1d2933 100%)';
        $('.constructor_item-rental2 .range').css('background', gradientStyle);
    }

    try {
        // imageContainer1 ======
        const sliderInput = document.getElementById('sliderInp');
        const maxSliderValue = parseInt(sliderInput.max);
        let clc1 = 0;
        function updateImages(value, imageList) {
            const rotationDegree = (value / maxSliderValue) * 180;
            imageList.forEach((img, index) => {
                const imgIndex = parseInt(img.getAttribute('data-index'));

                const opacityRangeStart = imgIndex - 100;
                const opacity = (value - opacityRangeStart) / 40;

                if (value >= opacityRangeStart && value < imgIndex) {
                    img.style.opacity = opacity;
                } else if (value >= imgIndex && value < imgIndex + 100) {
                    img.style.opacity = Math.max(0, 1 - ((value - imgIndex) / 100));
                } else {
                    img.style.opacity = 0;
                }
                img.style.transform = `rotate(${rotationDegree}deg)`;
            });
        }

        function debounce(func, timeout = 300) {
            let timer;
            return (...args) => {
                clearTimeout(timer);
                timer = setTimeout(() => { func.apply(this, args); }, timeout);
            };
        }

        const debouncedUpdateImages = debounce(updateImages, 30);

        sliderInput.addEventListener('input', function () {
            let activeIcons = 0;

            let activeInput = document.querySelectorAll('.constructor_item-goup input');
            activeInput.forEach(item => {
                if (item.checked) {
                    activeIcons++;
                }
            })

            let n = 0;
            if (activeIcons >= 0 && activeIcons < 2) {
                n = 0;
            } else if (activeIcons >= 2 && activeIcons < 4) {
                n = 100;
            } else if (activeIcons == 4) {
                n = 200;
            } else if (activeIcons >= 6 && activeIcons < 8) {
                n = 300;
            } else if (activeIcons >= 8 && activeIcons < 10) {
                n = 400;
            } else if (activeIcons >= 10 && activeIcons < 11) {
                n = 700;
            } else if (activeIcons >= 11) {
                n = 777;
            }

            if (n < parseInt(this.value)) {
                debouncedUpdateImages(parseInt(this.value), document.querySelectorAll('.bg-image'));
            }
        });

        updateImages(parseInt(sliderInput.value), document.querySelectorAll('.bg-image'));

        // imageContainer2 ======
        const sliderInput2 = document.getElementById('sliderInp2');
        const maxSliderValue2 = parseInt(sliderInput2.max);

        function updateImages2(value, imageList) {
            const rotationDegree = (value / maxSliderValue2) * 180;
            imageList.forEach((img, index) => {
                const imgIndex2 = parseInt(img.getAttribute('data-index2'));

                const opacityRangeStart = imgIndex2 - 74;
                const opacity = (value - opacityRangeStart) / 40;

                if (value >= opacityRangeStart && value < imgIndex2) {
                    img.style.opacity = opacity;
                } else if (value >= imgIndex2 && value < imgIndex2 + 74) {
                    img.style.opacity = Math.max(0, 1 - ((value - imgIndex2) / 74));
                } else {
                    img.style.opacity = 0;
                }
                img.style.transform = `rotate(${rotationDegree}deg)`;
            });
        }

        const debouncedUpdateImages2 = debounce(updateImages2, 30);

        sliderInput2.addEventListener('input', function () {
            let activeIcons = 0;

            let activeInput = document.querySelectorAll('.constructor_item-goup input');
            activeInput.forEach(item => {
                if (item.checked) {
                    activeIcons++;
                }
            })

            let t = 0;
            if (activeIcons >= 0 && activeIcons < 2) {
                t = 0;
            } else if (activeIcons >= 2 && activeIcons < 4) {
                t = 70;
            } else if (activeIcons == 4) {
                t = 140;
            } else if (activeIcons >= 6 && activeIcons < 8) {
                t = 210;
            } else if (activeIcons >= 8 && activeIcons < 10) {
                t = 280;
            } else if (activeIcons >= 10 && activeIcons < 11) {
                t = 350;
            } else if (activeIcons >= 11) {
                t = 365;
            }

            if (t < parseInt(this.value)) {
                debouncedUpdateImages2(parseInt(this.value), document.querySelectorAll('.bg-image2'));
            }
        });

        updateImages2(parseInt(sliderInput2.value), document.querySelectorAll('.bg-image2'));

        // constructor link active =====
        let tabsWrap = document.querySelectorAll('.constructor_img-wrap');
        let tabs = document.querySelectorAll('.constructor_item-goup');
        let tabsInput = document.querySelectorAll('.constructor_item-goup input');
        let itemBoxTabs = document.querySelectorAll('.constructor_item-box-top ');
        let imageContainer1 = document.querySelector('.clc_bg1');
        let imageContainer2 = document.querySelector('.clc_bg2');

        const tablinks = document.querySelectorAll('.constructor_link');
        const cIcons = document.querySelectorAll('.constructor_icon');

        tablinks.forEach(function (tablink, index) {
            tablink.addEventListener('click', function (e) {
                debouncedUpdateImages(40, document.querySelectorAll('.bg-image'));
                debouncedUpdateImages2(30, document.querySelectorAll('.bg-image2'));
                $('.range input').val(0);

                rangeInput1(21);
                rangeInput2(5);

                tablinks.forEach(function (link) {
                    link.classList.remove('active');
                });
                tablink.classList.add('active');

                cIcons.forEach(icon => {
                    icon.classList.remove('active');
                });

                tabsInput.forEach(item => {
                    item.checked = false;
                })

                checkLenght();

                if (index === 0) {
                    imageContainer1.style.display = 'block';
                    imageContainer2.style.display = 'none';
                } else if (index === 1) {
                    imageContainer1.style.display = 'none';
                    imageContainer2.style.display = 'block';
                }

                $('.clc_item').not('.constructor_item-rental' + (index + 1)).css({ display: 'none' });
                $('.constructor_item-rental' + (index + 1)).css({ display: 'flex' });
            });
        });

        let checkbox_1 = document.querySelector('#serviceCheck1');
        let checkbox_2 = document.querySelector('#serviceCheck2');
        let checkbox_3 = document.querySelector('#serviceCheck3');

        let checkbox_9 = document.querySelector('#serviceCheck9');
        let checkbox_10 = document.querySelector('#serviceCheck10');

        let checkbox_12 = document.querySelector('#serviceCheck12');
        let checkbox_13 = document.querySelector('#serviceCheck13');
        let checkbox_14 = document.querySelector('#serviceCheck14');

        let icon_1 = document.querySelector('#itemGroupIcon1');
        let icon_2 = document.querySelector('#itemGroupIcon2');
        let icon_3 = document.querySelector('#itemGroupIcon3');

        let icon_9 = document.querySelector('#itemGroupIcon9');
        let icon_10 = document.querySelector('#itemGroupIcon10');

        let icon_12 = document.querySelector('#itemGroupIcon12');
        let icon_13 = document.querySelector('#itemGroupIcon13');
        let icon_14 = document.querySelector('#itemGroupIcon14');

        tabsInput.forEach((item, idx) => {
            item.onclick = () => {
                idx_pos = idx + 1;

                let selected_service = document.querySelector('#itemGroupTab' + idx_pos);
                let selected_service_label = selected_service.querySelector('.constructor_item-label');

                let icon = document.querySelector('#itemGroupIcon' + idx_pos);
                
                if (!free_servises_list.includes(selected_service_label)) {
                    if (idx_pos == 1) {
                        if (icon_1.classList.contains('active')) {
                            icon_1.classList.remove('active');
                        }
                        else {
                            icon_1.classList.add('active');
                            icon_2.classList.remove('active');
                            icon_3.classList.remove('active');

                            checkbox_1.checked = true;
                            checkbox_2.checked = false;
                            checkbox_3.checked = false;
                        }
                    }

                    else if (idx_pos == 2) {
                        if (icon_2.classList.contains('active')) {
                            icon_2.classList.remove('active');
                        }
                        else {
                            icon_1.classList.remove('active');
                            icon_2.classList.add('active');
                            icon_3.classList.remove('active');

                            checkbox_1.checked = false;
                            checkbox_2.checked = true;
                            checkbox_3.checked = false;
                        }
                    }

                    else if (idx_pos == 3) {
                        if (icon_3.classList.contains('active')) {
                            icon_3.classList.remove('active');

                        }
                        else {
                            icon_1.classList.remove('active');
                            icon_2.classList.remove('active');
                            icon_3.classList.add('active');

                            checkbox_1.checked = false;
                            checkbox_2.checked = false;
                            checkbox_3.checked = true;
                        }
                    }

                    else if (idx_pos == 9) {
                        if (icon_9.classList.contains('active')) {
                            icon_9.classList.remove('active');
                        }
                        else {
                            icon_9.classList.add('active');
                            icon_10.classList.remove('active');

                            checkbox_9.checked = true;
                            checkbox_10.checked = false;
                        }
                    }

                    else if (idx_pos == 10) {
                        if (icon_10.classList.contains('active')) {
                            icon_10.classList.remove('active');
                        }
                        else {
                            icon_9.classList.remove('active');
                            icon_10.classList.add('active');

                            checkbox_9.checked = false;
                            checkbox_10.checked = true;
                        }
                    }

                    else if (idx_pos == 12) {
                        if (icon_12.classList.contains('active')) {
                            icon_12.classList.remove('active');
                        }
                        else {
                            icon_12.classList.add('active');
                            icon_13.classList.remove('active');
                            icon_14.classList.remove('active');

                            checkbox_12.checked = true;
                            checkbox_13.checked = false;
                            checkbox_14.checked = false;
                        }
                    }

                    else if (idx_pos == 13) {
                        if (icon_13.classList.contains('active')) {
                            icon_13.classList.remove('active');
                        }
                        else {
                            icon_12.classList.remove('active');
                            icon_13.classList.add('active');
                            icon_14.classList.remove('active');

                            checkbox_12.checked = false;
                            checkbox_13.checked = true;
                            checkbox_14.checked = false;
                        }
                    }

                    else if (idx_pos == 14) {
                        if (icon_14.classList.contains('active')) {
                            icon_14.classList.remove('active');
                        }
                        else {
                            icon_12.classList.remove('active');
                            icon_13.classList.remove('active');
                            icon_14.classList.add('active');

                            checkbox_12.checked = false;
                            checkbox_13.checked = false;
                            checkbox_14.checked = true;
                        }
                    }

                    else if (idx_pos == 4) {

                    }

                    else if (idx_pos == 15) {

                    }

                    else {
                        if (item.checked) {
                            icon.classList.add('active');
                        } else {
                            icon.classList.remove('active');
                        }
                    }
                }

                // console.log(idx_pos);
                // console.log(selected_service_label.textContent);

                checkLenght();

                const constructorIcon = document.querySelectorAll('.constructor_icon.active');
                let radius = 180;
                if (window.innerWidth > 577 && window.innerWidth <= 776) {
                    radius = 160
                } else if (window.innerWidth <= 576) {
                    radius = 140
                } else {
                    radius = 180
                }

                const totalActiveImages = constructorIcon.length;
                const angleStep = 360 / totalActiveImages;

                constructorIcon.forEach((image, index) => {
                    const angle = index * angleStep;
                    const radians = angle * Math.PI / 180;
                    const x = Math.cos(radians) * radius;
                    const y = Math.sin(radians) * radius;
                    image.style.transform = `translate(-50%, -50%) translate(${x}px, ${y}px)`;
                });

                update_cart();
            };
        })
        

        // Constructor icon active
        function checkLenght() {
            let activeIcons = 0;
            let activeInput = document.querySelectorAll('.constructor_item-goup input');
            activeInput.forEach(item => {
                if (item.checked) {
                    activeIcons++;
                }
            })

            let n = 0, t = 0;
            if (activeIcons >= 0 && activeIcons < 2) {
                n = 0;
                t = 0;
            } else if (activeIcons >= 2 && activeIcons < 4) {
                n = 100;
                t = 70;
            } else if (activeIcons == 4) {
                n = 200;
                t = 140;
            } else if (activeIcons >= 6 && activeIcons < 8) {
                n = 300;
                t = 210;
            } else if (activeIcons >= 8 && activeIcons < 10) {
                n = 400;
                t = 280;
            } else if (activeIcons >= 10 && activeIcons < 11) {
                n = 700;
                t = 350;
            } else if (activeIcons >= 11) {
                n = 777;
                t = 365;
            }

            if (parseInt(document.querySelector('#sliderInp').value) < n) {
                debouncedUpdateImages(n, document.querySelectorAll('.bg-image'));
            }

            if (parseInt(document.querySelector('#sliderInp2').value) < n) {
                debouncedUpdateImages2(t, document.querySelectorAll('.bg-image2'));
            }
        }
        checkLenght();
    } catch (error) { }


    // AOS js =====
    AOS.init({
    });


    // Modal open =====
    $(document).ready(function () {
        // authorization modal
        $('.header_personal-link').click(function () {
            $('.authorization').toggleClass('active');
        });
        $('.authorization-modal-bg').click(function () {
            $('.authorization').removeClass('active');
        });
        // authorization modal
        // $('.header_personal-link').click(function () {
        //     $('.authorization').toggleClass('active');
        // });
        // $('.authorization-modal-bg').click(function () {
        //     $('.authorization').removeClass('active');
        // });
        // confirmation modal
        $('.authorization_form-btn').click(function () {
            $('.confirmation').toggleClass('active');
            $('.authorization').removeClass('active');
        });
        $('.confirmation-modal-bg').click(function () {
            $('.confirmation').removeClass('active');
        });
        // discount modal
        $('.price_benefit-info').click(function () {
            $('.discount').toggleClass('active');
        });
        $('.discount-close').click(function () {
            $('.discount').removeClass('active');
        });
        $('.discount-modal-bg').click(function () {
            $('.discount').removeClass('active');
        });

        // info modal
        $('.constructor_info-btn').click(function () {
            var title = $(this).siblings('.constructor_item-goup').find('label').text();
            $('.info_modal-title span').text(title);
            $('.info-modal-text').html(info_modal_dict[title]);
            $('.info-modal').toggleClass('active');
        });
        $('.info-modal-close').click(function () {
            $('.info-modal').removeClass('active');
        });
        $('.info-modal-bg').click(function () {
            $('.info-modal').removeClass('active');
        });

    });


    // Verify Form =====
    const form = document.querySelector('[name="verifyForm"]');
    const inputs = form.querySelectorAll('.confirmation-input input');
    const formData = new FormData();

    function shouldSubmit() {
        return [...inputs].every((input) => input.value.length > 0);
    }

    function handleInput(e) {
        const input = e.target;
        if (input.value) {
            formData.append(input.name, input.value);

            if (input.nextElementSibling) {
                input.nextElementSibling.focus();
            }
        }
    }

    function handleFocus(e) {
        if (e.target.value) {
            e.target.select();
        }
    }

    function handlePaste(e) {
        const paste = e.clipboardData.getData('text');
        inputs.forEach((input, i) => {
            input.value = paste[i] || '';
            formData.set(input.name, input.value);
        })
    }

    function handleKeyDown({ key, target }) {
        if (key !== 'Backspace') {
            return;
        } else if (target.previousElementSibling) {
            formData.delete(target.name)
            target.value = '';
            target.previousElementSibling.focus();
        }
    }

    inputs[0].addEventListener('paste', handlePaste)

    form.addEventListener('input', handleInput);
    form.addEventListener('focusin', handleFocus);
    form.addEventListener('keydown', handleKeyDown);


    // Country number =====
    let input2 = document.querySelector("#authorizationFrom");
    window.intlTelInput(input2, {});

    let inputValue1 = document.querySelector("#authorizationFrom");
    let countryCode = "+998";
    inputValue1.value = countryCode;


    $('.authorization_form-group1').each(function (idx, el) {
        let inp = $(el).find('input[type="tel"]')[0];
        $(inp).inputmask({ "mask": "+999 (99) 999 99 99" })
        $(inp).on('input', function () {
            setTimeout(() => {
                let ico = $(el).find('.iti__selected-flag .iti__flag')[0].getAttribute('class').split(' ')[1]
                if (ico.length > 5) {
                    ico = ico.slice(ico.length - 2)
                    fetchCountry(inp, ico.toUpperCase());
                }
            }, 200);
        })

        $(el).find('.iti__country-list li').each(function (li_idx, li) {
            $(li).click(function () {
                let code = $(li).find('.iti__dial-code').text();
                $(inp).val(code);
                setTimeout(() => {
                    let ico = $(el).find('.iti__selected-flag .iti__flag')[0].getAttribute('class').split(' ')[1]
                    if (ico.length > 5) {
                        ico = ico.slice(ico.length - 2)
                        fetchCountry(inp, ico.toUpperCase());
                    }
                }, 200);
            })
        })
    })


    function fetchCountry(el, ico) {
        fetch("../js/country.json")
            .then((res) => res.json())
            .then(res => {
                res.forEach(c => {
                    if (c.iso == ico) {
                        let m = c.mask;
                        let code = ''
                        for (let i = 1; i < c.code.length; i++) {
                            code += '9'
                        }
                        $(el).inputmask({ "mask": `+${code}${m}` })
                    }
                })
            })
    }


    // GtRobot Forex and Crypto =======
    const cryptoBtn = document.getElementById('gtCryptoBtn');
    const forexBtn = document.getElementById('gtForexBtn');
    const cryptoElement = document.getElementById('gtCrypto');
    const forexElement = document.getElementById('gtForex');

    try {
        cryptoBtn.addEventListener('click', function () {
            counter1 = 1;
            counter2 = 1;

            forexElement.classList.add('gt-none');
            cryptoElement.classList.remove('gt-none');
            
            const basketBoxs = document.querySelector('.basket_boxs');
            basketBoxs.innerHTML = '';

            $('#result-calc2').text(1);
            update_cart();
        });
        forexBtn.addEventListener('click', function () {
            counter1 = 1;
            counter2 = 1;

            cryptoElement.classList.add('gt-none');
            forexElement.classList.remove('gt-none');

            const basketBoxs = document.querySelector('.basket_boxs');
            basketBoxs.innerHTML = '';

            $('#result-calc1').text(1);
            update_cart();
        });

    } catch (erorr) { }


    // Bilet calc
    let counter1 = 1;
    let counter2 = 1;

    // Add counter
    $('#add-btn1').click(function () {
        if (counter1 < 50) {
            counter1++;
            $('#result-calc1').text(counter1);
            update_cart();
        }
    });
    $('#add-btn2').click(function () {
        if (counter2 < 50) {
            counter2++;
            $('#result-calc2').text(counter2);
            update_cart();
        }
    });

    // Remove counter
    $('#remove-btn1').click(function () {
        if (counter1 > 1) {
            counter1--;
            $('#result-calc1').text(counter1);
            update_cart();
        }
    });
    $('#remove-btn2').click(function () {
        if (counter2 > 1) {
            counter2--;
            $('#result-calc2').text(counter2);
            update_cart();
        }
    });

    document.getElementById('checkoutLink').addEventListener('click', function(e) {
        crypto_labels_id = {
            "Тех.Поддержка": 1,
            "Куратор": 2,
            "Главный куратор": 3,
            "Уроки Crypto": 4,
            "Уроки Forex": 5,
            "Уроки NFT": 6,
            "Уроки P2P": 7,
            "Cloud Mining PRO": 8,
            "Cloud Mining ULTRA": 9,
            "Заморозка и замена услуг": 10,
            "Baxtli obunachi 3.0": 11,
        }

        forex_labels_id = {
            "Тех.Поддержка": 12,
            "Куратор": 13,
            "Главный куратор": 14,
            "Индикатор": 15,
            "Уроки Forex": 16,
            "Регистрация у брокера": 17,
            "Проп счет": 18,
            "Премия": 19,
            "Заморозка и замена услуг": 20,
            "Baxtli obunachi 3.0": 21,
        }

        const constructor_type = document.querySelector('#gtForexBtn');
        let is_forex = constructor_type.classList.contains('active');

        labels_id = is_forex ? forex_labels_id : crypto_labels_id;

        e.preventDefault();

        cart_boxes = document.querySelectorAll('.basket_box');

        cart_items = []
        cart_boxes.forEach((cart_box) => {
            var is_present = !!cart_box.querySelector('.present');
            
            if (is_present) {
                total = cart_box.querySelector('.basket_box-total');

                item_name = cart_box.querySelector('.basket_box-texts span').textContent;
                old_price = total.querySelector('span').textContent;
                price = total.querySelector('b').textContent;
            }
            else {
                item_name = cart_box.querySelector('span').textContent;
                old_price = 0;
                price = cart_box.querySelector('b').textContent;
            }

            cart_item = {
                "id": labels_id[item_name],
                "name": item_name,
                "is_present": is_present,
                "old_price": old_price,
                "price": price,
                "is_forex": is_forex 
            }
            
            cart_items.push(cart_item);
        });

        let priceText = $('.price-range').text(); 
        let priceNumber = parseInt(priceText.match(/\d+/), 10);
        days_data = {
            "days": is_forex ? parseInt($rangeInput2.val(), 10) : parseInt($rangeInput.val(), 10),
            "price": priceNumber
        }

        title = document.querySelector('.constructor_item-rate').querySelector('.rate').textContent;

        localStorage.setItem('cartData', JSON.stringify({"cart_items": cart_items, "cart_days": days_data, "title": title}));
        
        window.location.href = 'checkout.html';
    });

    console.log("123");
    rangeInput1(21);
    update_cart();
});
