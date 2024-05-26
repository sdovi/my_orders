// Loader window
document.addEventListener('DOMContentLoaded', function () {
	let preloader = document.querySelector('.loader-wrap');
	let wrapper = document.querySelector('.wrapper');

	window.addEventListener('load', function () {
		setTimeout(function () {
			preloader.classList.remove('anime');
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
			if (
				lastClickedAccordionContent &&
				lastClickedAccordionContent !== accordionContent
			) {
				lastClickedAccordionContent.style.maxHeight = null;
				lastClickedAccordionContent.previousElementSibling
					.querySelector('.plus_img')
					.classList.remove('active');
			}

			accordionContent.style.maxHeight = accordionContent.style.maxHeight
				? null
				: accordionContent.scrollHeight + 'px';
			accordionIcon.classList.toggle('active');

			lastClickedAccordionContent = accordionContent.style.maxHeight
				? accordionContent
				: null;
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
	let constructorItems = document.querySelectorAll(
		'.constructor_item-goups-more',
	);

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
			lazy: false,
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
		rangeInput1(parseInt(this.value));
	});

	function initRangeSlider() {
		let initialValue = 21;
		$rangeAfter.text(initialValue + ' дней');
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
			transform: 'rotate(' + rotateValue + ')',
		});

		$rate.text(rateText);
		$rateMob.text(rateText);
		$priceBenefit.text(newBenefitPrice + '$');
		$priceBenefit2.text(newBenefitPrice + '$');
		$priceRange.text(newPrice + '$');
		$priceRange2.text(newPrice + '$');
		$rangeAfter.text(curVal + ' дней');

		let val = (curVal - 10) * (100 / 777);
		let gradientStyle =
			'linear-gradient(90.00deg, #00ffff99,#11484e99 ' +
			val +
			'%, #1d2933 ' +
			val +
			'%, #1d2933 100%)';
		$('.constructor_item-rental1 .range').css('background', gradientStyle);
	}

	let $rangeInput2 = $('.constructor_item-rental2 .range input');
	let $rangeAfter2 = $('.constructor_item-rental2 .range').find('span');

	let sheet2 = document.createElement('style');
	document.body.appendChild(sheet);

	$rangeInput2.on('input', function () {
		rangeInput2(parseInt(this.value));
	});

	function initRangeSlider2() {
		let initialValue = 5;
		$rangeAfter2.text(initialValue + ' дней');
	}

	initRangeSlider2();

	$('.range-labels li').on('click', function () {
		let index = $(this).index();
		$rangeInput2.val(index + 1).trigger('input');
	});

	function rangeInput2(inp) {
		let $priceRange21 = $('.constructor_item-rental2 .price-range');
		let $priceRange22 = $('.constructor_item-rental2 .price-range2');
		let $priceBenefit21 = $('.constructor_item-rental2 .price-benefit');
		let $rateMob2 = $('.constructor_item-rental2 .mob-rate b');
		let $rate2 = $('.constructor_item-rental2 .rate');
		let $priceBenefit22 = $(
			'.constructor_item-rental2 .item_mob-price-title b',
		);

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
			newBenefitPrice = 1;
			newPrice = 209 + (curVal - 180);
		}

		$('#constructorWrap').css({
			transform: 'rotate(' + rotateValue + ')',
		});

		$rate2.text(rateText);
		$rateMob2.text(rateText);
		$priceBenefit21.text(newBenefitPrice + '$');
		$priceBenefit22.text(newBenefitPrice + '$');
		$priceRange21.text(newPrice + '$');
		$priceRange22.text(newPrice + '$');
		$rangeAfter2.text(curVal + ' дней');

		let val = (curVal - 5) * (100 / 365);
		let gradientStyle =
			'linear-gradient(90.00deg, #00ffff99,#11484e99 ' +
			val +
			'%, #1d2933 ' +
			val +
			'%, #1d2933 100%)';
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
					img.style.opacity = Math.max(0, 1 - (value - imgIndex) / 100);
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
				timer = setTimeout(() => {
					func.apply(this, args);
				}, timeout);
			};
		}

		const debouncedUpdateImages = debounce(updateImages, 30);

		sliderInput.addEventListener('input', function () {
			let activeIcons = 0;

			let activeInput = document.querySelectorAll(
				'.constructor_item-goup input',
			);
			activeInput.forEach((item) => {
				if (item.checked) {
					activeIcons++;
				}
			});

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
				debouncedUpdateImages(
					parseInt(this.value),
					document.querySelectorAll('.bg-image'),
				);
			}
		});

		updateImages(
			parseInt(sliderInput.value),
			document.querySelectorAll('.bg-image'),
		);

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
					img.style.opacity = Math.max(0, 1 - (value - imgIndex2) / 74);
				} else {
					img.style.opacity = 0;
				}
				img.style.transform = `rotate(${rotationDegree}deg)`;
			});
		}

		const debouncedUpdateImages2 = debounce(updateImages2, 30);

		sliderInput2.addEventListener('input', function () {
			let activeIcons = 0;

			let activeInput = document.querySelectorAll(
				'.constructor_item-goup input',
			);
			activeInput.forEach((item) => {
				if (item.checked) {
					activeIcons++;
				}
			});

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
				debouncedUpdateImages2(
					parseInt(this.value),
					document.querySelectorAll('.bg-image2'),
				);
			}
		});

		updateImages2(
			parseInt(sliderInput2.value),
			document.querySelectorAll('.bg-image2'),
		);

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

				cIcons.forEach((icon) => {
					icon.classList.remove('active');
				});

				tabsInput.forEach((item) => {
					item.checked = false;
				});

				checkLenght();

				if (index === 0) {
					imageContainer1.style.display = 'block';
					imageContainer2.style.display = 'none';
				} else if (index === 1) {
					imageContainer1.style.display = 'none';
					imageContainer2.style.display = 'block';
				}

				$('.clc_item')
					.not('.constructor_item-rental' + (index + 1))
					.css({ display: 'none' });
				$('.constructor_item-rental' + (index + 1)).css({ display: 'flex' });
			});
		});

		tabsInput.forEach((item, idx) => {
			item.onclick = () => {
				let icon = document.querySelector('#itemGroupIcon' + (idx + 1));
				if (item.checked) {
					icon.classList.add('active');
				} else {
					icon.classList.remove('active');
				}
				checkLenght();

				const constructorIcon = document.querySelectorAll(
					'.constructor_icon.active',
				);
				let radius = 180;
				if (window.innerWidth > 577 && window.innerWidth <= 776) {
					radius = 160;
				} else if (window.innerWidth <= 576) {
					radius = 140;
				} else {
					radius = 180;
				}

				const totalActiveImages = constructorIcon.length;
				const angleStep = 360 / totalActiveImages;

				constructorIcon.forEach((image, index) => {
					const angle = index * angleStep;
					const radians = (angle * Math.PI) / 180;
					const x = Math.cos(radians) * radius;
					const y = Math.sin(radians) * radius;
					image.style.transform = `translate(-50%, -50%) translate(${x}px, ${y}px)`;
				});
			};
		});

		// Constructor icon active
		function checkLenght() {
			let activeIcons = 0;
			let activeInput = document.querySelectorAll(
				'.constructor_item-goup input',
			);
			activeInput.forEach((item) => {
				if (item.checked) {
					activeIcons++;
				}
			});

			let n = 0,
				t = 0;
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
	} catch (error) {}

	// AOS js =====
	AOS.init({});

	// Modal open =====
	$(document).ready(function () {
		// authorization modal
		$('.header_personal-link').click(function () {
			$('.authorization').toggleClass('active');
			$('.registration').removeClass('active');  
		});
		$('.authorization-modal-bg').click(function () {
			$('.authorization').removeClass('active');
		});
		// registration modal
		$('.authorization_form-link').click(function () {
			$('.registration').toggleClass('active');
			$('.authorization').toggleClass('active');
		});
		$('.registration-modal-bg').click(function () {
			$('.registration').removeClass('active');
		});
		// confirmation modal
		$('.registration_form-btn').click(function () {
			$('.confirmation').toggleClass('active');
			$('.registration').removeClass('active');
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
			var title = $(this)
				.siblings('.constructor_item-goup')
				.find('label')
				.text();
			$('.info_modal-title span').text(title);
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
		});
	}

	function handleKeyDown({ key, target }) {
		if (key !== 'Backspace') {
			return;
		} else if (target.previousElementSibling) {
			formData.delete(target.name);
			target.value = '';
			target.previousElementSibling.focus();
		}
	}

	inputs[0].addEventListener('paste', handlePaste);

	form.addEventListener('input', handleInput);
	form.addEventListener('focusin', handleFocus);
	form.addEventListener('keydown', handleKeyDown);

	// Country number =====
	let input2 = document.querySelector('#authorizationFrom');
	let input1 = document.querySelector('#registrationFrom');
	window.intlTelInput(input1, {});
	window.intlTelInput(input2, {});

	let inputValue1 = document.querySelector('#authorizationFrom');
	let inputValue2 = document.querySelector('#registrationFrom');
	let countryCode = '+998';
	inputValue1.value = countryCode;
	inputValue2.value = countryCode;

	$('.authorization_form-group1').each(function (idx, el) {
		let inp = $(el).find('input[type="tel"]')[0];
		$(inp).inputmask({ mask: '+999 (99) 999 99 99' });
		$(inp).on('input', function () {
			setTimeout(() => {
				let ico = $(el)
					.find('.iti__selected-flag .iti__flag')[0]
					.getAttribute('class')
					.split(' ')[1];
				if (ico.length > 5) {
					ico = ico.slice(ico.length - 2);
					fetchCountry(inp, ico.toUpperCase());
				}
			}, 200);
		});

		$(el)
			.find('.iti__country-list li')
			.each(function (li_idx, li) {
				$(li).click(function () {
					let code = $(li).find('.iti__dial-code').text();
					$(inp).val(code);
					setTimeout(() => {
						let ico = $(el)
							.find('.iti__selected-flag .iti__flag')[0]
							.getAttribute('class')
							.split(' ')[1];
						if (ico.length > 5) {
							ico = ico.slice(ico.length - 2);
							fetchCountry(inp, ico.toUpperCase());
						}
					}, 200);
				});
			});
	});

	//  Registration section
	$('.registration_form-group1').each(function (idx, el) {
		let inp = $(el).find('input[type="tel"]')[0];
		$(inp).inputmask({ mask: '+999 (99) 999 99 99' });
		$(inp).on('input', function () {
			setTimeout(() => {
				let ico = $(el)
					.find('.iti__selected-flag .iti__flag')[0]
					.getAttribute('class')
					.split(' ')[1];
				if (ico.length > 5) {
					ico = ico.slice(ico.length - 2);
					fetchCountry(inp, ico.toUpperCase());
				}
			}, 200);
		});

		$(el)
			.find('.iti__country-list li')
			.each(function (li_idx, li) {
				$(li).click(function () {
					let code = $(li).find('.iti__dial-code').text();
					$(inp).val(code);
					setTimeout(() => {
						let ico = $(el)
							.find('.iti__selected-flag .iti__flag')[0]
							.getAttribute('class')
							.split(' ')[1];
						if (ico.length > 5) {
							ico = ico.slice(ico.length - 2);
							fetchCountry(inp, ico.toUpperCase());
						}
					}, 200);
				});
			});
	});

	function fetchCountry(el, ico) {
		fetch('../js/country.json')
			.then((res) => res.json())
			.then((res) => {
				res.forEach((c) => {
					if (c.iso == ico) {
						let m = c.mask;
						let code = '';
						for (let i = 1; i < c.code.length; i++) {
							code += '9';
						}
						$(el).inputmask({ mask: `+${code}${m}` });
					}
				});
			});
	}

	// GtRobot Forex and Crypto =======
	const cryptoBtn = document.getElementById('gtCryptoBtn');
	const forexBtn = document.getElementById('gtForexBtn');
	const cryptoElement = document.getElementById('gtCrypto');
	const forexElement = document.getElementById('gtForex');

	try {
		cryptoBtn.addEventListener('click', function () {
			forexElement.classList.add('gt-none');
			cryptoElement.classList.remove('gt-none');
		});
		forexBtn.addEventListener('click', function () {
			cryptoElement.classList.add('gt-none');
			forexElement.classList.remove('gt-none');
		});
	} catch (erorr) {}

	// Bilet calc
	let counter1 = 0;
	let counter2 = 0;

	// Add counter
	$('#add-btn1').click(function () {
		if (counter1 < 50) {
			counter1++;
			$('#result-calc1').text(counter1);
		}
	});
	$('#add-btn2').click(function () {
		if (counter2 < 50) {
			counter2++;
			$('#result-calc2').text(counter2);
		}
	});

	// Remove counter
	$('#remove-btn1').click(function () {
		if (counter1 > 0) {
			counter1--;
			$('#result-calc1').text(counter1);
		}
	});
	$('#remove-btn2').click(function () {
		if (counter2 > 0) {
			counter2--;
			$('#result-calc2').text(counter2);
		}
	});
});

// counter
const counters = document.querySelectorAll('.counter');

counters.forEach((counter) => {
	counter.innerText = '0';

	const updateCounter = () => {
		const target = Number(counter.getAttribute('data-target'));
		const c = Number(counter.innerText);
		const increment = target / 500;

		if (c < target) {
			counter.innerText = `${Math.ceil(c + increment)}`;
			setTimeout(updateCounter, 100);
		} else {
			counter.innerText = target;
		}
	};

	updateCounter();
});

// auth function

const BASE_URL = 'https://api.gtrobot.shop/accounts';
const form = document.querySelector('.registration_form');
console.log(form);
let userData = {
	name: '',
	phone: 0,
};
let userPhone = form.addEventListener('submit', (event) => {
	event.preventDefault();

	let userNumber = document.querySelector('.input-number').value;
	let userName = document.querySelector('.input-name').value;

	let user = {
		name: userName,
		phone: userNumber,
	};

	userPhone = user.phone;
	userData = { ...user };

	fetch(`${BASE_URL}/register/`, {
		method: 'POST',
		body: JSON.stringify(userData),
		headers: {
			'Content-type': 'application/json; charset=UTF-8',
		},
	})
		.then((response) => response.json())
		.then((data) => {
			//handle data
			localStorage.setItem('token', data.access_token);
		})
		.catch((error) => {
			//handle error
		});
	console.log(userData);
	console.log('submit boldi');
});

const confirmBtn = document.querySelector('.confirmation-btn');

confirmBtn.addEventListener('click', (event) => {});


// cmc kod post

const verifyForm = document.querySelector('.confirmation-btn');

verifyForm.addEventListener('click', (event) => {
	event.preventDefault();

	let n1 = document.querySelector(`.n1`).value;
	let n2 = document.querySelector(`.n2`).value;
	let n3 = document.querySelector(`.n3`).value;
	let n4 = document.querySelector(`.n4`).value;
	let n5 = document.querySelector(`.n5`).value;
	let n6 = document.querySelector(`.n6`).value;
	let code = `${n1}${n2}${n3}${n4}${n5}${n6}`;

	let userVerify = {
		phone: userPhone,
		code: code,
	};

	console.log(userVerify);

	fetch(`${BASE_URL}/verify/`, {
		method: 'POST',
		body: JSON.stringify(userVerify),
		headers: {
			'Content-type': 'application/json; charset=UTF-8',
			Authorization: `Token ${localStorage.getItem('token')}`,
		},
	})
		.then((response) => response.json())
		.then((data) => {
			//handle data
			if (data.verified != true) {
				alert('SMS code qayta kiriting');
			} else {
				$('.confirmation').removeClass('active');
			}
		})
		.catch((error) => {
			//handle error
		});
	console.log('verify submit');
});



// --------------------- LOGIN -----------------------------------
document.addEventListener("DOMContentLoaded", function() {
    const verifyForm2 = document.forms["verifyForm"];
    const authorizationForm = document.querySelector(".authorization_form");
    let phoneNumber;

    verifyForm2.addEventListener("submit", function(event) {
        event.preventDefault();
        const codeInputs = document.querySelectorAll(".confirmation-input input");
        let code = "";
        codeInputs.forEach(function(input) {
            code += input.value;
        });
        
        fetch("https://api.gtrobot.shop/accounts/login/", {
            method: "POST",
            body: JSON.stringify({ phone: phoneNumber, code: code }),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const accessToken = data.access_token;
            console.log(accessToken);
			
			localStorage.setItem('token', accessToken);
            window.location.href = 'account.html';
        })
        .catch(error => {
            console.error("Ошибка:", error);
        });
    });

    authorizationForm.addEventListener("submit", function(event) {
        event.preventDefault();
        phoneNumber = document.getElementById("authorizationFrom").value;
        
        fetch("https://api.gtrobot.shop/accounts/send-code/", {
            method: "POST",
            body: JSON.stringify({ phone: phoneNumber }),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error("Ошибка:", error);
        });
    });
});




// karzina
const serviceCheck1 = document.querySelector('#serviceCheck1');
const serviceCheck2 = document.querySelector('#serviceCheck1');
const serviceCheck3 = document.querySelector('#serviceCheck3');
const serviceCheck4 = document.querySelector('#serviceCheck4');
const serviceCheck5 = document.querySelector('#serviceCheck5');
const serviceCheck6 = document.querySelector('#serviceCheck6');
const serviceCheck7 = document.querySelector('#serviceCheck7');
const serviceCheck8 = document.querySelector('#serviceCheck8');
const serviceCheck9 = document.querySelector('#serviceCheck9');
const serviceCheck10 = document.querySelector('#serviceCheck10');
const serviceCheck11 = document.querySelector('#serviceCheck11');
const serviceCheck12 = document.querySelector('#serviceCheck12');
const serviceCheck13 = document.querySelector('#serviceCheck13');
const serviceCheck14 = document.querySelector('#serviceCheck14');
const serviceCheck15 = document.querySelector('#serviceCheck15');
const serviceCheck16 = document.querySelector('#serviceCheck16');
const serviceCheck17 = document.querySelector('#serviceCheck17');
const serviceCheck18 = document.querySelector('#serviceCheck18');
const serviceCheck19 = document.querySelector('#serviceCheck19');
const serviceCheck20 = document.querySelector('#serviceCheck20');
const serviceCheck21 = document.querySelector('#serviceCheck21');

let korzinka = [];

serviceCheck1.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 1;
	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck2.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 2;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck3.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 3;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck4.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 4;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck5.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 5;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck6.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 6;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck7.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 7;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck8.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 8;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck9.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 9;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck10.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 10;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck11.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 11;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck12.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 12;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck13.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 13;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck14.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 14;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck15.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 15;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck16.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 16;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck17.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 17;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck18.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 18;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck19.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 19;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck20.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 11;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

serviceCheck21.addEventListener('change', (event) => {
	event.preventDefault();
	console.log('change');
	let id = 11;

	if (event.target.checked) {
		korzinka.push(id);
	} else {
		korzinka.splice(korzinka.indexOf(id), 1);
	}
	console.log(korzinka);
});

console.log(checkboxInput);
// const korzinaPost = () => {
// 	let service = {
// 		sevice: korzinka,
// 		days: 21,
// 	};
// 	fetch(`https://api.gtrobot.shop/services/buy/`, {
// 		method: 'POST',
// 		body: JSON.stringify(service),
// 		headers: {
// 			'Content-type': 'application/json; charset=UTF-8',
// 		},
// 	})
// 		.then((response) => response.json())
// 		.then((data) => {
// 			//handle data
// 			if (data.token) {
// 				localStorage.setItem('token', data.token);
// 			}
// 		})
// 		.catch((error) => {
// 			//handle error
// 		});
// };

const img1 = document.querySelector('.img1');
const img2 = document.querySelector('.img2');

console.log(img1)
console.log(img2)

img1.addEventListener('click', (e) => {
	e.target.preventDefault();
	console.log('bosildi');
	fetch(`https://api.gtrobot.shop/services/buy/`, {
		method: 'POST',
		body: JSON.stringify(service),
		headers: {
			'Content-type': 'application/json; charset=UTF-8',
		},
	})
		.then((response) => response.json())
		.then((data) => {
			//handle data
			if (data.token) {
				localStorage.setItem('token', data.token);
			}
		})
		.catch((error) => {
			//handle error
		});
	let service = {
		sevice: korzinka,
		days: 21,
	};
	// ----------------------------------------------
	fetch(`https://api.gtrobot.shop/payments/click/create/`, {
		method: 'POST',
		body: JSON.stringify(service),
		headers: {
			'Content-type': 'application/json; charset=UTF-8',
		},
	})
		.then((response) => response.json())
		.then((data) => {
			//handle data
			console.log(data);
			if (data) {
			}
		})
		.catch((error) => {
			//handle error
		});
});




img2.addEventListener('click', (e) => {
	e.target.preventDefault();
	console.log('bosildi');
	// korzinaPost();
	let service = {
		sevice: korzinka,
		days: 21,
	};
	fetch(`https://api.gtrobot.shop/payments/click/create/`, {
		method: 'POST',
		body: JSON.stringify(service),
		headers: {
			'Content-type': 'application/json; charset=UTF-8',
		},
	})
		.then((response) => response.json())
		.then((data) => {
			//handle data
			console.log(data);
			if (data) {
			}
		})
		.catch((error) => {
			//handle error
		});
});

