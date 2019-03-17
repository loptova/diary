<template>
  <div id="app">
    <h3></h3>
    <div class="combobox-wrapper">
      <b-form-select v-model="selectedMonth" :options="options.months"  />
      <b-form-select v-model="selectedYear" :options="options.years" />
    </div>
    
    <div class="combobox-wrapper">
      <b-button @click="getTasksByMonthAndYear(self, selectedMonth, selectedYear)" class="search-button" variant="primary">Найти</b-button>
    </div>
    <br>
    <div v-if="openDays">
      <div v-if="selectedMonth == 'February' || selectedMonth == 'April' || selectedMonth == 'June' || selectedMonth == 'September' || selectedMonth == 'November'"  class="days-grid">
        <div v-for="i in 30" class="day"> 
          {{ i }} <br>
          {{ tasksByMAY[i] }}
        </div>
      </div>
      <div v-else class="days-grid">
        <div v-for="i in 31" class="day">
          {{ i }}<br>
          <div v-for="task in tasksByMAY['tasks']" v-if="task['day_num'] == i">
            {{ task['task_title'] }}
          </div>
        </div>
      </div>
    </div>
    <!-- <h3 v-for="i in tasksByMAY['tasks']">{{ i }}<br></h3> -->
  </div>
</template>

<script>

window.tasksByMAY = []

export default {
  // a: '123',
  

  data () {
    return {
      self: this,
      openDays: false,
      tasks: this.getTasks(),
      tasksByMAY: [],
      i: 0,
      selectedMonth: null,
      selectedYear: null,
      
      options: {
        months: [
          { value: null, text: 'Выберите месяц' },
          { value: 'January', text: 'Январь' },
          { value: 'February', text: 'Февраль' },//30
          { value: 'March', text: 'Март' },
          { value: 'April', text: 'Апрель' },//30
          { value: 'May', text: 'Май' },
          { value: 'June', text: 'Июнь' },//30
          { value: 'July', text: 'Июль' },
          { value: 'August', text: 'Август' },
          { value: 'September', text: 'Сентябрь' },//30
          { value: 'October', text: 'Октябрь' },
          { value: 'November', text: 'Ноябрь' },//30
          { value: 'December', text: 'Декабрь' }
        ],
        years: [
          { value: null, text: 'Выберите год' },
          { value: '2018', text: '2018'},
          { value: '2019', text: '2019'},
          { value: '2020', text: '2020'}
        ]
      }
    }
  },
  computed: {
    
  },
  methods: {
    getTasks () {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'http://127.0.0.1:5000/diary/api/tasks', false);
      xhr.send();
      if (xhr.status != 200) {
        alert( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
      } else {
        return xhr.responseText // responseText -- текст ответа.
      }
    },
    getTasksByMonthAndYear(self, month, year) {
      var _month = new Date('1 '+ month +' 1999').getMonth()
      _month += 1
      var xhr = new XMLHttpRequest();

      xhr.open('GET', 'http://127.0.0.1:5000/diary/api/tasksbymonthandyear/'+ _month +'&'+ year +'', false);
      xhr.send();
      if (xhr.status != 200) {
        alert( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
      } else {
        self.tasksByMAY = JSON.parse(xhr.responseText) // responseText -- текст ответа.
        self.openDays = true
      }
    }
  }
}
</script>

<style>

body{
  background: #fafafa;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  height: 100%;
  width: 100%;
}

.combobox-wrapper {
  display: flex;
}

.days-grid {
  display: flex;
  width: 100%;
  height: 600px;
  background: #fafafa;
  justify-content: center;
  flex-wrap: wrap;
}

.day {
  width: 150px;
  height: 150px;
  background: white;
  border: 5px solid #fafafa;
  min-width: 250px;
  min-height: 250px;
  cursor: pointer;
}

.day:hover {
  background: #fafafa;
  border: 1px solid black;
}

.search-button {
  width: 100%;
}
</style>
