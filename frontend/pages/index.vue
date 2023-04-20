
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
          <ion-menu-button>
            <span class="relative inline-block">
                <img class="h-6 w-6 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                <span class="absolute right-0 top-0 block h-1.5 w-1.5 rounded-full bg-green-400 ring-2 ring-white" />
            </span>

          </ion-menu-button>
        </ion-buttons>
        <ion-buttons slot="end">
          <div v-if="token != null">
            <ion-button  @click="logOut()">
              <Icon name="heroicons-outline:logout" class="-ml-1 mr-2 h-5 w-5 green" style="color: red;" aria-hidden="true"/>
              </ion-button>

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
            <span class="relative inline-block">
              <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
              <span class="absolute bottom-0 left-8 block h-2.5 w-2.5 rounded-full bg-green-400 ring-2 ring-white" />
            </span>
            <ion-card-subtitle>            
              <ion-input class="input" label="What's happening?" label-placement="floating" fill="outline" ></ion-input>
            </ion-card-subtitle>
          </ion-card-header>

          <ion-card-content>
            <ion-button>Tweet</ion-button>
            <!-- <ion-icon name="heart"></ion-icon> -->
            <ion-icon :icon="create"></ion-icon>
            <!-- <ion-icon slot="icon-only" :ios="ellipsisHorizontal" :md="ellipsisVertical"></ion-icon> -->

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
          <ion-card-subtitle>{{ data.author }}</ion-card-subtitle>
        </ion-card-header>
       




        <ion-card-content>
          <img style="width:100%" alt="Silhouette of mountains" :src="data.image" />

          <ion-grid style="width:100%">
          <ion-row class="ion-justify-content-center">
            <!-- <ion-col class="ion-justify-content-center"><ion-button id="open-toast" @click="likePost(data.id)">Like</ion-button></ion-col> -->
            <!-- <ion-col > <ion-button id="open-toast" @click="commentAlert(data.id)">comment</ion-button></ion-col> -->
            <!-- <ion-col > <ion-button id="open-toast" @click="unlikePost(data.id)">Unlike </ion-button></ion-col> -->
            <!-- <ion-col class="ion-justify-content-center"><ion-icon :icon="heart" @click="likePost(data.id)"></ion-icon></ion-col> -->
            <!-- <Icon name="heroicons-outline:heart" class="-ml-1 mr-2 h-5 w-5"  aria-hidden="true"/> -->
            <!-- <span class="relative flex h-4 w-4 mt-1">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-4 w-4 bg-sky-500 "></span>
              </span> -->
              <ion-col class="ion-justify-content-center mt-8">     
                <div @click="likePost(data.id)" class="rotate-45 ion-justify-content-center">
                <span class="heart animate-heart mt-2 absolute inline-flex" ></span>
                <!-- <spam class="heart animate-ping mt-2 absolute inline-flex"></spam> -->
                
              </div></ion-col>
              <!-- <Icon name="heroicons-outline:heart" class="-ml-1 mr-2 h-5 w-5"  aria-hidden="true"/> -->

              <div class="heartless mt-4 ml-1 " @click="likePost(data.id)" ></div>

<!-- HTML -->
<!-- HTML -->
<!-- <button class="flex items-center space-x-2 bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg transition duration-300">
  <svg class="h-5 w-5 animate-like" fill="currentColor" viewBox="0 0 20 20">
    <path d="M10 18l8-5.5V5A2 2 0 0 0 16 3H5.83A2 2 0 0 0 5 3.5L2 5v8l3-1.5V5.35l5 3.5-5 3.5V14l5-3.5L10 18z"></path>
  </svg>
  <span class="hidden md:inline">Like</span>
</button> -->




              <!-- <div class="rotate-45 ion-justify-content-center">
                <span class="heart animate-heart mt-2 absolute inline-flex" ></span>
                <spam class="heart animate-ping mt-2 absolute inline-flex"></spam>
              </div> -->




              <!-- <span class="relative flex h-4 w-4 mt-1">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
                    <div class="heart animate-ping"></div>
                </span> -->
   

              <!-- <span class="relative flex h-4 w-4 mt-1">
              <span class="relative  w-[100px] h-[90px] animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75
                before:content-[''] before:absolute before:top-0 before:left-[50px]
                before:h-[80px] before:w-[50px] before:rounded-t-[50px] 
                before:rounded-r-[50px]before:rounded-b-0 before:rounded-l-0 
                before:bg-black before:-rotate-45 before:origin-[0_100%]

                after:content-[''] after:absolute after:top-0 after:left-0 after:h-[80px]
                after:w-[50px] after:rounded-t-[50px] after:rounded-r-[50px] 
                after:rounded-b-0 after:rounded-l-0 after:bg-black after:rotate-45
                after:origin-[100%_100%] relative inline-flex rounded-full h-4 w-4 bg-sky-500
                ">
                </span>
              </span> -->
       



            <ion-col class="ion-justify-content-center"><ion-icon :icon="create"  @click="commentAlert(data.id)"></ion-icon></ion-col>
            <ion-col class="ion-justify-content-center"><ion-icon :icon="thumbsDown"  @click="unlikePost(data.id)"></ion-icon></ion-col>
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
  // import { create, ellipsisHorizontal, ellipsisVertical, helpCircle, personCircle, search, star } from 'ionicons/icons';
import { create, heart, thumbsDown} from 'ionicons/icons';
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
        console.log(response.data.value)
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
            let formData = new FormData();
            if(alertData['body'] != ''){
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
      console.log(response.data)

      console.log(response.data.value)
    })
}  





</script>



<style>
.heart {
  width: 15px;
  height: 15px;
  background-color: #f00; /* red color for heart shape */
  position: absolute;
  transform: rotate(45deg); /* rotate the heart shape */
}

.heart:before,
.heart:after {
  content: '';
  position: absolute;
  width: 15px;
  height: 15px;
  background-color: #f00; /* red color for heart shape */
  border-radius: 50%;
}

.heart:before {
  top: -10px; /* position the top half of the heart */
  left: 0;
}

.heart:after {
  top: 0; /* position the bottom half of the heart */
  left: -10px;
}

/* Animation classes */
.animate-heart {
  animation: beat 1s infinite;

}

@keyframes beat {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}





.heartless {
  width: 15px;
  height: 15px;
  background-color: rgb(184, 194, 188); 
  position: absolute;
  transform: rotate(45deg);
  border-color: #f10808;

}

.heartless:before,
.heartless:after {
  content: '';
  position: absolute;
  width: 15px;
  height: 15px;
  background-color: rgb(184, 194, 188); 
  border-radius: 50%;
  /* border-color: #f10808; */
}

.heartless:before {
  top: -10px; /* position the top half of the heart */
  left: 0;

}

.heartless:after {
  top: 0; /* position the bottom half of the heart */
  left: -10px;

}




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




/* CSS */

@keyframes like {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

.animate-like:hover {
  animation: like 0.5s ease-in-out infinite;
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