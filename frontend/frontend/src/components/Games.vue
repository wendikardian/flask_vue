<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- Bootswatch cdn -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Games Library
          </h1>
          <hr />
          <br />
          <!-- Alert Message -->
          <b-alert variant="success" v-if="showMessage" show>{{message}}</b-alert>
          <button type="button" class="btn btn-success btn-sm" v-b-modal.game-modal>Add Game</button>
          <br /><br />
          <table class="table table-hover">
            <!-- Table Head -->
            <thead>
              <tr>
                <!-- Tabble Header Cells -->
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played ?</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, index) in games" :key="index">
                <td>{{ game.title }}</td>
                <td>{{ game.genre }}</td>
                <td>
                  <span v-if="game.played">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button typpe="button" class="btn btn-info btn-sm">
                      Update
                    </button>
                    <button typpe="button" class="btn btn-danger btn-sm">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 20px"
          >
            Copyright &copy; Wendi Kardian All Rights Reserved 2023
          </footer>
        </div>
      </div>
      <!-- First Modal -->
      <b-modal
        ref="addGameModal"
        id="game-modal"
        title="Add a new game"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="from-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addGamesForm.title"
              required
              placeholder="Enter Games"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            id="form-genre-group"
            label="Genre:"
            label-for="from-genre-input"
          >
            <b-form-input
              id="form-genre-input"
              type="text"
              v-model="addGamesForm.genre"
              required
              placeholder="Enter Genre"
            >
            </b-form-input>
          </b-form-group>

          <!-- Checkbox -->

          <b-form-group id="form-played-group">
            <b-form-checkbox-group v-model="addGamesForm.played" id="form-checks">
                <b-form-checkbox value="true"> Played ? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <!-- Button  -->
          <b-button type="submit" variant="outline-info">
            Submit
          </b-button>
          <b-button type="reset" variant="outline-danger">
            Reset
          </b-button>

        </b-form>
      </b-modal>

      <!-- End of The First Modal -->
       
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      games: [],
      addGamesForm : {
        title : "",
        genre : "",
        played : [],
      }
    };
  },
  message : "",
  methods: {
    getGames() {
      const path = "http://localhost:5000/games";
      axios
        .get(path)
        .then((res) => {
          console.log(res);
          this.games = res.data.games;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // Post Function
    addGame(payload){
        const path = "http://localhost:5000/games"
        axios.post(path, payload).then((res) => {
            this.getGames()
            // Show message alert
            this.message = "Game Added"
            // To show message
            this.showMessage = true
        }).catch((err) => {
            console.error(err);
            this.getGames()
        })
    },
    initForm(){
        this.addGamesForm.title = "",
        this.addGamesForm.genre = "",
        this.addGamesForm.played = []
    },
    onSubmit(e) {
        e.preventDefault();
        this.$refs.addGameModal.hide()
        let played = false
        if (this.addGamesForm.played[0]) played = true
        const payload = {
            title : this.addGamesForm.title,
            genre : this.addGamesForm.genre,
            played
        }
        this.addGame(payload)
        this.initFormat
    },
    onReset(e) { 
        e.preventDefault()
        this.$ref.addGameModal.hide()
        this.initForm()
    }
  },
  created() {
    this.getGames();
  },
};
</script>
