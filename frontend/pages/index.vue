
 <template>


  <ion-menu content-id="main-content">
    <ion-header>
      <ion-toolbar>
        <ion-title>Menu Content</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      
      This is the menu content.


      <ion-list>
    <ion-item>
      <ion-label>Followers</ion-label>
      <ion-badge color="primary">22k</ion-badge>
    </ion-item>
    <ion-item>
      <ion-label>Likes</ion-label>
      <ion-badge color="secondary">118k</ion-badge>
    </ion-item>
    <ion-item>
      <ion-label>Stars</ion-label>
      <ion-badge color="tertiary">34k</ion-badge>
    </ion-item>
    <ion-item>
      <ion-label>Completed</ion-label>
      <ion-badge color="success">80</ion-badge>
    </ion-item>
    <ion-item>
      <ion-label>Warnings</ion-label>
      <ion-badge color="warning">70</ion-badge>
    </ion-item>
    <ion-item>
      <ion-label>Notifications</ion-label>
      <ion-badge color="danger">1000</ion-badge>
    </ion-item>
  </ion-list>



    </ion-content>
  </ion-menu>
  <ion-page id="main-content">
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-menu-button></ion-menu-button>
        </ion-buttons>
        <ion-buttons slot="end">
          <div v-if="token != null">
            <ion-button  @click="logOut()">logout</ion-button>

          </div>
          <div v-else>
            <ion-button @click="loginAlert">Login</ion-button>
            <ion-button  @click="presentAlert">Register</ion-button>

          </div>

          <ion-alert trigger="present-alert" header="Please enter your info" :buttons="alertButtons" :inputs="alertInputs"></ion-alert>
        </ion-buttons>
        <ion-title>Meta</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      


    <div v-if="user_id">
      <ion-card>
          <ion-card-header>
            <ion-card-subtitle>            
              <ion-input class="input" label="Post you thought...." label-placement="floating" fill="outline" ></ion-input>
            </ion-card-subtitle>
          </ion-card-header>

          <ion-card-content>
            <ion-icon :icon="logoIonic" size="large" color="primary"></ion-icon>
            <!-- <ion-icon :icon="logoIonic"></ion-icon>
            <ion-icon :icon="logoIonic" size="large"></ion-icon>
            <ion-icon :icon="logoIonic" color="primary"></ion-icon>
            <ion-icon :icon="logoIonic" size="large" color="primary"></ion-icon> -->
          </ion-card-content>
      </ion-card>
    </div>



      <ion-card v-for="data in all_data" :key="data.id">
        <ion-card-header>

          <ion-card-title>{{ data.title }}</ion-card-title>
          <ion-card-subtitle>{{ data.desc }}</ion-card-subtitle>
        </ion-card-header>


        <ion-card-content>
          <img style="width:100%" alt="Silhouette of mountains" :src="data.image" />

          <ion-grid style="width:100%">
          <ion-row class="ion-justify-content-center">
            <ion-col class="ion-justify-content-center"><ion-button id="open-toast" @click="likePost(data.id)">Like</ion-button></ion-col>
            <ion-col > <ion-button id="open-toast" @click="commentAlert(data.id)">comment</ion-button></ion-col>
            <ion-col > <ion-button id="open-toast" @click="unlikePost(data.id)">Unlike </ion-button></ion-col>
          </ion-row>
        </ion-grid>
        </ion-card-content>


      </ion-card>



    </ion-content>
  </ion-page>



</template>

<script setup>
  import { IonButton, alertController } from '@ionic/vue';
  import { Preferences } from '@capacitor/preferences';

  const all_data = ref('')
  const token = ref('')
  const username = ref('')
  const user_id = ref('')


async function logOut(){
  await useFetch('http://127.0.0.1:8000/logout/')
  .then((response)=>{
    console.log(response.data.value.Message)
  })
  removeName()
}


async function getData(){
      await useFetch('http://127.0.0.1:8000/posts/')
      .then((response)=>{
        all_data.value = response.data.value
      })
    }
getData()

    let modal = document.querySelector('ion-modal');

    // console.log(modal)

function cancel() {
  modal.dismiss(null, 'cancel');
}

function confirm() {
  const input = document.querySelector('ion-input');
  modal.dismiss(input.value, 'confirm');
}


const alertButtons = ['Submit'];


const presentAlert = async () => {
        const alert = await alertController.create({
          inputs: [
                {
                    name: 'username',
                    placeholder: 'Enter username',
                    type: 'text'
                },
                {
                    name: 'email',
                    placeholder: 'Enter your email',
                    type: 'text'
                },
                {
                    name: 'password',
                    placeholder: 'Enter password',
                    type: 'password'
                },
              
              ],
          header: 'Registration Form',
          message: 'Enter User details',
          buttons: [
        {
            text: 'Cancel',
            role: 'cancel',
            // cssClass: 'danger',
            handler: () => {
                console.log('Confirm Cancel');
            }
        }, 
        {
            text: 'Submit',
            handler: (alertData) => { //takes the data 
                console.log(alertData);
                async function postData(){
                  await useFetch('http://127.0.0.1:8000/register/', {
                    method: 'POST',
                    body: alertData
                  }).then((response)=>{
                    console.log(response)
                  })
                }
                postData()
            }
        }
    ]
        });

        await alert.present();
      };

const loginAlert = async () => {
      const alert = await alertController.create({
          inputs: [
                {
                    name: 'username',
                    placeholder: 'Enter username',
                    type: 'text'
                },
                {
                    name: 'password',
                    placeholder: 'Enter password',
                    type: 'password'
                },
              
              ],
          header: 'Login Form',
          message: 'Enter User details',
          buttons: [
        {
            text: 'Cancel',
            role: 'cancel',
            // cssClass: 'danger',
            handler: () => {
                console.log('Confirm Cancel');
            }
        }, 
        {
            text: 'Submit',
            handler: (alertData) => { //takes the data 
                console.log(alertData);
                async function postData(){
                  await useFetch('http://127.0.0.1:8000/login/', {
                    method: 'POST',
                    body: alertData
                  }).then((response)=>{
                    console.log(response.data.value.data.user_id)
                    username.value = response.data.value.username
                    // getData()

                    const auth_token = response.data.value.data.token


                    // SET DATA IN CAPACITOR
                    async function setObject() {
                      await Preferences.set({
                        key: 'token',
                        // value: JSON.stringify(auth_token),
                        // id: response.data.value.data.user_id
                        value: JSON.stringify({
                          id: response.data.value.data.user_id,
                          token_id: auth_token
                        })
                      });
                    }
                    setObject()

                      // JSON "get" example
                      // async function getObject() {
                      //   const ret = await Preferences.get({ key: 'token' });
                      //   const user = JSON.parse(ret.value);
                      //   console.log(user)
                      // }
                      // getObject()
              })
                }
                postData()
            }
        }
    ]
        });

        await alert.present();
      };

async function commentAlert(post_id){
  const alert = await alertController.create({
    inputs: [
          {
              name: 'body',
              placeholder: 'Write a comment..',
              type: 'textarea'
          }   
        ],
    // header: 'Leave your thought here',
    message: 'Leave your thought here',
    buttons: [
  {
      text: 'Cancel',
      role: 'cancel',
      // cssClass: 'danger',
      handler: () => {
          console.log('Confirm Cancel');
      }
  }, 
  {
      text: 'Submit',
      handler: (alertData) => { //takes the data 
          async function postData(){
            console.log(post_id)
            console.log(user_id.value)
            // console.log(alertData[0])
            // console.log(alertData)
            let formData = new FormData();
            formData.append('body',alertData['body'])
            formData.append('user', user_id.value)
            formData.append('post', post_id)

            await useFetch('http://127.0.0.1:8000/comment/', {
              method: 'POST',
              body: formData
            }).then((response)=>{
              console.log(response)
            })
          }
          postData()
      }
  }
]
  });

  await alert.present();
};

//CLEAR TOKEN FROM CAPACITOR
async function removeName(){
  await Preferences.remove({ key: 'token' });
};


// GET TOKEN DATA FROM CAPACITOR 
async function getObject() {
  const ret = await Preferences.get({ key: 'token' });
  const user = JSON.parse(ret.value);
  if (user != null){
    token.value = user.token_id
    user_id.value = user.id
  }else{token.value = null}
  // console.log(user.id)

}
getObject()



async function likePost(post_id){
  let formData = new FormData();
  formData.append('user', user_id.value)
  formData.append('post', post_id)
  await useFetch('http://127.0.0.1:8000/like/', {
    method: 'POST',
    body: formData
  })
      .then((response)=>{
        console.log(response.data.value)
      })
  }

  async function unlikePost(post_id){
  let formData = new FormData();
  formData.append('user', user_id.value)
  formData.append('post', post_id)
  formData.append('value', 'Unlike')
  await useFetch('http://127.0.0.1:8000/like/', {
    method: 'POST',
    body: formData
  })
      .then((response)=>{
        console.log(response.data.value)
      })
  }  





</script>


<style>
.input{
  background-color: var(--color-realbox-background);
    border: none;
    border-radius: var(--ntp-realbox-border-radius);
    color: var(--color-realbox-foreground);
    font-family: inherit;
    font-size: inherit;
    height: 100%;
    outline: 0;
    padding-inline-end: calc(var(--ntp-realbox-voice-icon-offset) + var(--ntp-realbox-icon-width) + var(--ntp-realbox-inner-icon-margin));
    padding-inline-start: 52px;
    position: relative;
    width: 100%;
}


/* ion-input.custom {
    --background: #fffff;
    --color: #000000;
    --placeholder-color: #ddd;
    --placeholder-opacity: .8;

    --padding-bottom: 10px;
    --padding-end: 10px;
    --padding-start: 10px;
    --padding-top: 10px;
    border-radius: 4px;
  }
  
  ion-input.custom .helper-text,
  ion-input.custom .counter {
    color: var(--ion-color-step-700, #373737);
  } */




  ion-segment-button::part(indicator-background) {
    background: #08a391;
  }

  /* Material Design styles */
  ion-segment-button.md::part(native) {
    color: #000;
  }

  .segment-button-checked.md::part(native) {
    color: #08a391;
  }

  ion-segment-button.md::part(indicator-background) {
    height: 4px;
  }

  /* iOS styles */
  ion-segment-button.ios::part(native) {
    color: #08a391;
  }

  .segment-button-checked.ios::part(native) {
    color: #fff;
  }

  ion-segment-button.ios::part(indicator-background) {
    border-radius: 20px;
  }
</style>