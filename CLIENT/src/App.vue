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
        <div v-for="i in 31" class="day" v-on:click="dayClicker(self, i)">
          <strong>{{ i }}</strong><br>
          <div v-for="task in tasksByMAY['tasks']" v-if="task['day_num'] == i">
            {{ task['task_title'] }}
          </div>
        </div>
      </div>
    </div>
    <div class="detailedDayModal" :class="!isDetailedDayModal || isDetailedDayModal === undefined ? 'hidden' : ''">
      <div class="modal-block">
        <div>
          {{ selectedDay.day_num }}
        </div>
        
        <div class="modal-footer">
          <b-button @click="addTask" class="search-button" variant="primary">добавить</b-button>
          <b-button @click="isDetailedDayModal = false" class="search-button" >закрыть</b-button>
        </div>
        

      </div>
    </div>
  </div>
</template>

<script>

window.tasksByMAY = []

export default {
  data () {
    return {
      self: this,
      openDays: false,
      tasks: this.getTasks(),
      tasksByMAY: [],
      i: 0,
      selectedMonth: null,
      selectedYear: null,
      selectedDay: "",
      isDetailedDayModal: undefined,
      
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
  methods:{

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
    },

    dayClicker(self, _day_num) {
      var clickedDay = {
        day_num: _day_num,
        day_tasks: [] 
      }
      self.tasksByMAY['tasks'].forEach(day => {
        day['day_num'] === _day_num ? clickedDay.day_tasks.push(day['task_title']) : "";
      });
      self.selectedDay = clickedDay
      self.isDetailedDayModal = true
    },

    addTask() {
      alert('123')
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
.detailedDayModal {
  position: fixed;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: rgba(0,0,0,0.8);
	z-index: 99999;
	-webkit-transition: opacity 400ms ease-in;
	-moz-transition: opacity 400ms ease-in;
	transition: opacity 400ms ease-in;
  display: flex;
  justify-content: center;

  padding-top: 250px;
	/* pointer-events: none; */
}
.modal-block {
  width: 500px;  
  height: 250px;
  /* height: auto; */
  text-align: center;
  padding: 30px 50px;
  background: white;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
}

.modal-footer {
  flex-grow: 1;
}

.hidden {
  display: none;
}
</style>
