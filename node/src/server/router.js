import express from 'express'

const router = express.Router()

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' })
})

var todos =[]
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
// # 模拟数据
function mock_data(){
    for (var i = 0; i < 100; i++) {
        var todo = {'name': 'build an API '+i , 'ranking': getRandomInt(1, 5)};
        todos.push(todo);
    }
}

//# 模拟分页
function get_page_data(page, page_size){
    var start = (page-1)*page_size;
    var end = page*page_size;
    var tmp = []
    for (var i = 0; i < todos.length; i++) {
        if(i >= start && i<= end){
            tmp.push(todos[i])
        }
    }
    return tmp;
}

// RESTfulAPI
router.get('/todos', function(req, res, next) {
    var page = req.query.page;
    var pageSize = req.query.pageSize;
    console.log(page);
    console.log(pageSize);
    var data = get_page_data(page,pageSize);
    res.append('total', todos.length);
    res.append('page', page);
    res.json( data);
})
mock_data()
export default router
