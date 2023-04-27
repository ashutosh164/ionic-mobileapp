
 <template>


  <ion-menu content-id="main-content">
    <ion-header>
      <ion-toolbar>
        <ion-title>Menu Content</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      <ion-card>
        <span v-for="data in all_data">

          <img class="h-25 w-25 ml-auto mr-auto mt-2 rounded-full"  :src="data.current_user_profile[1]" />
        </span>
        <ion-card-header>
          <ion-card-title class="text-center">{{ current_username }}</ion-card-title>
          <!-- <ion-card-subtitle >Card Subtitle</ion-card-subtitle> -->
        </ion-card-header>

        <ion-card-content class="text-center">
          Here's a small text description for the card content. Nothing more, nothing less.
        </ion-card-content>
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
      </ion-card>


      <!-- <ion-list>
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
  </ion-list> -->



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
      


    <div>
      <ion-card>
        <ion-grid>
          <ion-row>
            <ion-col >{{ current_username }}-{{ user_id }}
                <span class="relative inline-block">
                  <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                </span>
            </ion-col>
            <ion-col size="10">

              <ion-row>
                <ion-input class="input" required v-model.trim="title" label="What's happening?" label-placement="floating" fill="outline" ></ion-input>
              </ion-row>
              <ion-row style="height:42px">
                <ion-col size="1"><ion-icon class="h-6 w-6" :icon="image"></ion-icon></ion-col>
                <ion-col size="7"><ion-icon class="h-6 w-6 ml-2" :icon="image"></ion-icon></ion-col>
                <!-- <ion-col v-if="title" size="1"><ion-button class="h-6 w-16 font-semibold" @click="postTweet()">Tweet</ion-button></ion-col> -->
                <ion-col v-if="title" size="1">
                  <ion-button v-if="user_id" class="h-6 w-16 font-semibold" @click="postTweet()">Tweet</ion-button>
                  <ion-button v-else class="h-6 w-16 font-semibold" @click="loginAlert">Tweet</ion-button>
                </ion-col>

              </ion-row>

            </ion-col>
            <!-- <ion-col >3</ion-col> -->
          </ion-row>
          <!-- <ion-row>sfga</ion-row> -->
        </ion-grid>

      </ion-card>
    </div>



      <ion-card v-for="data in all_data" :key="data.id">
        <ion-grid>
          <ion-row>
            <ion-col >
                <span class="relative inline-block" >
                  <!-- <img class="h-12 w-12 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" /> -->
                  <img v-if="data.profiles_url != null" class="h-12 w-12 rounded-full" alt="" :src="data.profiles_url"/>
                  
                </span>
            </ion-col>
            <ion-col class="user-info" size="10">
              <ion-row class="user-name font-bold" >{{data.user_name}}</ion-row>
              <ion-row v-if="data.profiles_details[0].bio">{{ data.profiles_details[0].bio }}</ion-row>
              <ion-row v-else>No Bio</ion-row>
              <ion-row>{{ formatDate(data.created_on) }}</ion-row>
            </ion-col>
            <!-- <ion-col>3</ion-col> -->
          </ion-row>
        </ion-grid>
        <ion-card-header>
          <ion-card-title>{{ data.title }}</ion-card-title>
          <!-- <ion-card-subtitle>{{ data.title }}</ion-card-subtitle> -->
        </ion-card-header>
       

        <ion-card-content>
          <img v-if="data.image != null" style="width:100%" alt="Silhouette of mountains" :src="data.image" />

          <ion-grid style="width:100%">
          <ion-row class="ion-justify-content-center">

              <ion-col v-if="data.check_user_like_post == user_id" class="ion-justify-content-center">     


              <!-- <ion-col v-if="data.liked.length && token != null " class="ion-justify-content-center">      -->
              <!-- <ion-col v-if="current_username== data.user_name && data.liked.length" class="ion-justify-content-center">      -->
                <!-- <span @click="likePost(data.id)" class="rotate-45 "> -->
                <span @click="likePost(data.id)" class="heart animate-heart mt-2" ></span>
                <!-- <spam class="heart animate-ping mt-2 absolute inline-flex"></spam> -->
                
                <!-- </span> -->

            <ion-col class="ion-justify-content-center ml-5">{{data.total_like}}</ion-col>

            </ion-col>

            <ion-col v-else class="ion-justify-content-center mt-2">     
              <span class="heartless absolute inline-flex" @click="likePost(data.id)" ></span>
              <!-- <Icon   @click="unlikePost(data.id)" class="mt-3 rotate-45 heartless"   aria-hidden="true" /> -->
              <ion-col class="ion-justify-content-center ml-5 ">{{data.total_like}}</ion-col>


            </ion-col>
              <!-- <Icon name="heroicons-outline:chat-bubble-bottom-center" class="-ml-1 mr-2 h-5 w-5"  aria-hidden="true"/> -->




            <ion-col class="ion-justify-content-center">
              <!-- <ion-icon :icon="create"  @click="commentAlert(data.id)"></ion-icon> -->
              <Icon name="heroicons-outline:chat-bubble-bottom-center" @click="commentAlert(data.id)" class="-ml-1 mr-2 h-7 w-7"   aria-hidden="true" />
              <!-- <ion-col class="ion-justify-content-center ml-5">4444</ion-col> -->
              <ion-col class="ion-justify-content-center -ml-2">{{data.total_comment}}</ion-col>


            </ion-col>
            <ion-col class="ion-justify-content-center">
                <Icon name="heroicons-outline:paper-airplane" class="-ml-1 mr-2 h-7 w-7 rotate-45"   aria-hidden="true" />
                <ion-col class="ion-justify-content-center -ml-2">{{data.total_like}}</ion-col>

            </ion-col>
            <ion-col class="ion-justify-content-center">
                <Icon name="heroicons:arrow-path-rounded-square-20-solid"  class="-ml-1 mr-2 h-7 w-7"   aria-hidden="true" />
                <ion-col class="ion-justify-content-center -ml-2">{{data.total_like}}</ion-col>
            </ion-col>
          </ion-row>
        </ion-grid>
        </ion-card-content>


      </ion-card>



    </ion-content>
  </ion-page>



</template>

<script setup>
  import { IonButton, alertController, toastController } from '@ionic/vue';
  import { Preferences } from '@capacitor/preferences';
  import { Filesystem, Directory, Encoding } from '@capacitor/filesystem';
  import { ActionSheet, ActionSheetButtonStyle } from '@capacitor/action-sheet';
  import moment from 'moment'

  // import { create, ellipsisHorizontal, ellipsisVertical, helpCircle, personCircle, search, star } from 'ionicons/icons';
import { create, heart, thumbsDown, document, image} from 'ionicons/icons';
  const all_data = ref('')
  const token = ref('')
  const username = ref('')
  const user_id = ref('')
  const current_username = ref('')
  const title = ref('')
  const check_current_user_like_post = ref(false)

  
  // computed(()=> {
  //   console.log(response.data.liked === user_id.value)
  //   return response.data.liked === user_id.value

  // })


  // GET TOKEN DATA FROM CAPACITOR 
async function getObject() {
  const ret = await Preferences.get({ key: 'token' });
  const user = JSON.parse(ret.value);
  // console.log(user)
  if (user != null){
    token.value = user.token_id
    // console.log(user.token_id)
    user_id.value = user.id
    current_username.value = user.current_username
  }else{token.value = null}
  // console.log(user.id)

}
getObject()
  

async function logOut(){
  await useFetch('http://127.0.0.1:8000/logout/')
  .then((response)=>{
    // console.log(response.data.value.Message)
    // if(response.data.value.Message){
      // LogoutToast('top')
      token.value = null
      user_id.value = null
      
      // user_id.value = null
    // }
  })
  removeName()
  loginAlert()
}


async function getData(){
  // console.log(await Preferences.get({ key: 'token' }))
  const ret = await Preferences.get({ key: 'token' });
  const user = JSON.parse(ret.value);
  if (user != null){
    user_id.value = user.id
  token.value = user.token_id
      await useFetch('http://127.0.0.1:8000/posts/', {"headers": {"Authorization": 'Token ' + token.value}})
      .then((response)=>{
        console.log(response.data.value)
        all_data.value = response.data.value 
        const data = response.data.value
        // console.log('hiiii',user_id.value)


        if(response.data.value){
          data.map((value, key) => {
            // console.log(value.liked == user_id.value)
            // console.log(value.liked)
            const filter_data = value.liked
            // console.log(filter_data)
            // filter_data.map((value, key) =>{
            //   console.log(value)
            // })
            // if (value.liked.length > 1){
              // console.log(value.liked)

            // }
            
            // if (value.liked[0] == user_id.value){
            //   // check_current_user_like_post.value = true
            // }

          })
        }
const obj = {0: 3, 1: 2, 2: 5, 3: 1};

// const filteredObj = Object.keys(obj).filter(key => obj[key] == user_id.value).reduce((result, key) => {
//   result[key] = obj[key];
//   return result;
// }, {});

// console.log(filteredObj);


// async function filteredObj(obj){
//   console.log('kjjjkjk')
//   Object.keys(obj).filter(key => obj[key] == user_id.value).reduce((result, key) => {
//   result[key] = obj[key];
//   console.log(result)
//   return result;

  
// }, {});
// }
// async function filteredObj(liked_data){
//   console.log(user_id.value)
//   console.log(liked_data)
// }
// filteredObj()

     
      })
    }}
getData()

// async function checkCurrentUserLikedPost(liked){
//   console.log(liked.filter(checkLiked))
// }
// checkCurrentUserLikedPost()
// function checkLiked(age) {
//   return age == user_id.value;
// }



async function postTweet(){
  let formData = new FormData();
  formData.append('title', title.value)
  formData.append('author', user_id.value)
  console.log(title.value)

  await useFetch('http://127.0.0.1:8000/posts/',{
    body: formData,
    method: 'POST',
    headers: {"Authorization": 'Token ' + token.value}
    
  })
  .then((response)=>{
    console.log(response)
    title.value = null
    getData()

  })
}


function isEmpty(val){
    return (val === undefined || val == null || val.length <= 0) ? true : false;
}
isEmpty(title.val)
    // let modal = document.querySelector('ion-modal');

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
                // console.log(alertData);
                async function postData(){
                  await useFetch('http://127.0.0.1:8000/login/', {
                    method: 'POST',
                    body: alertData
                  }).then((response)=>{
                    console.log(response)
                    if(response.data.value){
                      presentToastLogin('top')
                    }
                    current_username.value = response.data.value.data.username
                    const auth_token = response.data.value.data.token
                    // console.log(response.data.value.data)
                    // console.log(response.data.value.data.username)
                    
                    


                    // SET DATA IN CAPACITOR
                    async function setObject() {
                      await Preferences.set({
                        key: 'token',
                        // value: JSON.stringify(auth_token),
                        // id: response.data.value.data.user_id
                        value: JSON.stringify({
                          id: response.data.value.data.user_id,
                          token_id: auth_token,
                          current_username:response.data.value.data.username
                        })
                      });
                    }
                    setObject()
                    getData()

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

async function presentToastLogin(position) {
    const toast = await toastController.create({
      message: 'Login successfull!!',
      duration: 1500,
      position: position
    });

    await toast.present();
  } 

  async function LogoutToast(position) {
    const toast = await toastController.create({
      message: 'Logout successfull!!',
      duration: 1500,
      position: position
    });

    await toast.present();
  } 

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
              // console.log(response)
              if(response.error.value){
                  loginAlert()
                }else{

                  getData()
                }
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



async function likePost(post_id){
  let formData = new FormData();
  formData.append('user', user_id.value)
  formData.append('post', post_id)
  await useFetch('http://127.0.0.1:8000/like/', {
    method: 'POST',
    body: formData
  })
    .then((response)=>{
      console.log(response)
      if(response.error.value){
        loginAlert()
        console.log(response.error.value)
      }

        getData()
      
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

async function writeSecretFile(){
  await Filesystem.writeFile({
    path: 'secrets/text.txt',
    data: "This is a test",
    directory: Directory.Documents,
    encoding: Encoding.UTF8,
  });
};

async function showActions()  {
  const result = await ActionSheet.showActions({
    title: 'Photo Options',
    message: 'Select an option to perform',
    options: [
      {
        title: 'Upload',
      },
      {
        title: 'Share',
      },
      {
        title: 'Remove',
        style: ActionSheetButtonStyle.Destructive,
      },
    ],
  });

  console.log('Action Sheet result:', result);
};


function formatDate(value) {
    if (value) {
        return moment(String(value)).format('MMMM DD, YYYY [at] hh:mm a')
    }
};

</script>



<style>
.user-info{
  font-size: 11px;
}
.user-name{
  font-size: 14px;
}
.heart {
  width: 15px;
  height: 15px;
  background-color: #f00; /* red color for heart shape */
  position: absolute;
  transform: rotate(45deg); 
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
  animation: beat 1s infinite ;
  /* position: absolute;
  transform: rotate(45deg); */

}

@keyframes beat {
  0% {
    transform: scale(0.8)rotate(45deg);
  }
  50% {
    transform: scale(1)rotate(45deg);
  }
  100% {
    transform: scale(0.8) rotate(45deg);
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