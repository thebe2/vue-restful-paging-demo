<template>
  <div id="todo-list-example" class="container text-center">
        <h2>TODO List (任务清单) </h2>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>序号</th>
                    <th class="text-center">名称</th>
                    <th class="text-center">优先级</th>
                    <th class="text-center">-</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(todo,i) in todos">
                    <th scope="row">{{i+1}}</th>
                    <td>{{todo.name}}</td>
                    <td>{{todo.ranking}}</td>
                    <td><a href="">查看</a></td>
                </tr>
            </tbody>
        </table>
        <nav aria-label="Page navigation">
            <ul class="pagination">
                <li v-bind:class="{ 'disabled': !showFirst }" v-on:click="changePage(-1)">
                    <a href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
                </li>
                <li v-for="index in indexs" v-bind:class="{ 'active': pageIndex == index}">
                    <a v-on:click="btnClick(index)">{{index}}</a>
                </li>
                <li v-bind:class="{ 'disabled': !showLast }"  v-on:click="changePage(1)">
                    <a href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
import api from './api/api'
export default {
  data () {
    return {
      todos: [],
      total: 0,
      pageIndex: 1,
      pageSize: 10
    }
  },
  computed: {
    indexs: function() {//计算分页
      let left = 1
      let right = this.total / this.pageSize
      let ar = []
      if (this.all >= 11) {
        if (this.pageIndex > 5 && this.pageIndex < this.total - 4) {
          left = this.pageIndex - 5
          right = this.pageIndex + 4
        } else {
          if (this.pageIndex <= 5) {
            left = 1
            right = 10
          } else {
            right = this.total
            left = this.total - 9
             }
          }
      }
      while (left <= right) {
        ar.push(left)
        left++
      }
      return ar
    },
    showLast: function() {
      if (this.pageIndex == this.total / this.pageSize) {
        return false
      }
      return true
    },
    showFirst: function() {
      if (this.pageIndex == 1) {
        return false
      }
      return true
    }
  },
  methods: {
    btnClick: function(page) { //页码点击事件
    if (page != this.pageIndex) {
      console.log(page)
      api.getData(page, (data,total,pageIndex) => {
        this.todos = data
        this.total = total
        this.pageIndex = pageIndex
      })
    }
   },
   changePage:function(direction){
     this.btnClick(this.pageIndex+direction)
   }
  },
  created () {
    console.log('vue create')
    api.getData(this.pageIndex, (data,total,pageIndex) => {
      this.todos = data
      this.total = total
      this.pageIndex = pageIndex
    })
  }
}
</script>

<style>

</style>
