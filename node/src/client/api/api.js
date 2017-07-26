/* globals localStorage */
// import Vue from 'vue'
import $ from 'jquery'

// var todos = [];
// var total = 0;
// var pageIndex = 1;
// var pageSize = 10;

export default {
  getData(page, cb) {
    getData(page, (data,total,pageIndex) => {
      if (cb) cb(data,total,pageIndex)
    })
  }
}

function getData(page, cb) {
  $.ajax({
    url: 'todos?pageSize=10&page=' + page,
    type: 'GET',
    success: function(data, textStatus, jqXHR) {
      let total = parseInt(jqXHR.getResponseHeader('total'))
      let pageIndex = parseInt(jqXHR.getResponseHeader('page'))
      console.log(pageIndex)
      console.log(total)
      cb(data,total,pageIndex)
    }
  })
}
