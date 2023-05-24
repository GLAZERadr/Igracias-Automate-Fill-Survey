// ==UserScript==
// @name         Males banget euyy
// @namespace    http://tampermonkey.net/
// @version       Alphaedition
// @description  Males Banget Isi Survey
// @author       Secret
// @match        https://igracias.telkomuniversity.ac.id/*
// @grant        none
// @require      http://code.jquery.com/jquery-3.3.1.min.js
// ==/UserScript==

(function() {
    'use strict';

    var jawaban = 'Sangat puas';
    var option = 'Ya';
    var Masukan = 'Boleh diterangkan mengenai materi dan memberikan mahasiswa masukan terhadap sumber-sumner materi dari luar kampus';
    var ibdCodes = ['IBD', 'IBR', 'ERW', 'YGO', 'VMD', 'RSC'];

    $('.answerlist1:contains('+jawaban+'), .answerlist1:contains('+option+')').each(function(){
        $(this).parent().each(function(){
            $(this).find('.answerlist2').children().click()
        })
    });

    // Mengisi semua elemen <textarea> dengan tanda "-"
    $('textarea').val(Masukan);

    // Menekan tombol "Simpan" secara otomatis
    $('input[name="button"]').click();


    // Click on image with title "start" only if it has a href link containing any of the codes in the ibdCodes list
    $('img[title="start"]').each(function() {
        var href = $(this).parent().attr('href');
        if (ibdCodes.some(code => href.includes(code))) {
            $(this).click();
        }
    });
})();

