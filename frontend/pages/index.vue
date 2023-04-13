
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
          <ion-button  @click="presentAlert">Register</ion-button>
          <ion-button  >Login</ion-button>
          <ion-alert trigger="present-alert" header="Please enter your info" :buttons="alertButtons" :inputs="alertInputs"></ion-alert>
        </ion-buttons>
        <ion-title>Meta</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">



      <ion-card v-for="data in all_data" :key="data.id">
        <ion-card-header>

          <ion-card-title>{{ data.title }}</ion-card-title>
          <ion-card-subtitle>{{ data.desc }}</ion-card-subtitle>
        </ion-card-header>


        <ion-card-content>
          <img style="width:100%" alt="Silhouette of mountains" :src="data.image" />

          <ion-grid style="width:100%">
          <ion-row class="ion-justify-content-center">
            <ion-col class="ion-justify-content-center"><ion-button id="open-toast">Like</ion-button></ion-col>
            <ion-col > <ion-button id="open-toast">comment</ion-button></ion-col>
            <ion-col > <ion-button id="open-toast">Open </ion-button></ion-col>
          </ion-row>
        </ion-grid>
        </ion-card-content>


      </ion-card>



    </ion-content>
  </ion-page>



</template>

<script setup>
  import { IonButton, alertController } from '@ionic/vue';

  const all_data = ref('')
  // const alert = ref('')


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

// modal.addEventListener('willDismiss', (ev) => {
//   if (ev.detail.role === 'confirm') {
//     const message = document.querySelector('#message');
//     message.textContent = `Hello ${ev.detail.data}!`;
//   }
// });

const alertButtons = ['Submit'];
// const alertInputs = [
//   {
//     placeholder: 'Name',
//   },
//   {
//     placeholder: 'Nickname (max 8 characters)',
//     attributes: {
//       maxlength: 8,
//     },
//   },
//   {
//     type: 'number',
//     placeholder: 'Age',
//     min: 1,
//     max: 100,
//   },
//   {
//     type: 'textarea',
//     placeholder: 'A little about yourself',
//   },
// ];


// const alertInputs =  alertController.create({
//     inputs: [
//     {
//         name: 'name1',
//         type: 'text'
//     }],    
//     buttons: [
//         {
//             text: 'Cancel',
//             role: 'cancel',
//             cssClass: 'secondary',
//             handler: () => {
//                 console.log('Confirm Cancel');
//             }
//         }, 
//         {
//             text: 'Ok',
//             handler: (alertData) => { //takes the data 
//                 console.log(alertData.name1);
//             }
//         }
//     ]
// });



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

</script>


<style>
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