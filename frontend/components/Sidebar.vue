<template>
  <div class="w-full">
    <HeadlessTransitionRoot as="template" :show="sidebarOpen">
      <HeadlessDialog as="div" class="relative z-40 md:hidden" @close="sidebarOpen = false">
        <HeadlessTransitionChild as="template" enter="transition-opacity ease-linear duration-300"
          enter-from="opacity-0" enter-to="opacity-100" leave="transition-opacity ease-linear duration-300"
          leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-600 bg-opacity-75" />
        </HeadlessTransitionChild>

        <div class="fixed inset-0 z-40 flex">
          <HeadlessTransitionChild as="template" enter="transition ease-in-out duration-300 transform"
            enter-from="-translate-x-full" enter-to="translate-x-0"
            leave="transition ease-in-out duration-300 transform" leave-from="translate-x-0"
            leave-to="-translate-x-full">
            <HeadlessDialogPanel class="relative flex w-full max-w-xs flex-1 flex-col bg-white pt-5 pb-4">
              <HeadlessTransitionChild as="template" enter="ease-in-out duration-300" enter-from="opacity-0"
                enter-to="opacity-100" leave="ease-in-out duration-300" leave-from="opacity-100" leave-to="opacity-0">
                <div class="absolute top-0 right-0 -mr-12 pt-2">
                  <button type="button"
                    class="ml-1 flex h-10 w-10 items-center justify-center rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                    @click="sidebarOpen = false">
                    <span class="sr-only">Close sidebar</span>
                    <Icon name="heroicons:x-mark" class="h-6 w-6 text-white" aria-hidden="true" />
                  </button>
                </div>
              </HeadlessTransitionChild>
              <div class="flex flex-shrink-0 items-center px-4">
                <img class="h-10 w-auto rounded-full" src="/LoungeScanner-Logo.svg" alt="Lounge Scanner Logo" />
              </div>
              <div class="mt-5 h-0 flex-1 overflow-y-auto">
                <nav class="space-y-1 px-2">
                  <nuxt-link v-for="item in navigation" :key="item.name" @click="sidebarOpen = false" :to="item.href"
                    v-slot="{ isActive }">
                    <div :class="[
  isActive
    ? 'bg-gray-100 text-gray-900'
    : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
  'group flex items-center px-2 py-2 text-sm font-medium rounded-md ',
]">
                      <component :is="item.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true" />
                      {{ item.name }}
                    </div>
                  </nuxt-link>
                </nav>
              </div>
            </HeadlessDialogPanel>
          </HeadlessTransitionChild>
          <div class="w-14 flex-shrink-0" aria-hidden="true">
            <!-- Dummy element to force sidebar to shrink to fit close icon -->
          </div>
        </div>
      </HeadlessDialog>
    </HeadlessTransitionRoot>

    <!-- Static sidebar for desktop -->
    <div class="hidden md:fixed md:inset-y-0 md:flex md:w-64 md:flex-col">
      <!-- Sidebar component, swap this element with another sidebar if you like -->
      <div class="flex flex-grow flex-col overflow-y-auto border-r border-gray-200 bg-white pt-5 custom_scrollbar">
        <div class="flex flex-shrink-0 items-center px-4">
          <img class="h-10 w-auto rounded-full" src="/LoungeScanner-Logo.svg" alt="Lounge Scanner Logo" />
        </div>
        <div class="mt-5 flex flex-grow flex-col">
          <nav class="flex-1 space-y-1 px-2 pb-4">
            <nuxt-link v-for="item in navigation" :key="item.name" :to="item.href" v-slot="{ isActive }">
              <div :class="[
  isActive
    ? 'bg-gray-100 text-gray-900'
    : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
  'group flex items-center px-2 py-2 text-sm font-medium rounded-md ',
]">
                <!-- <component :is="item.icon" :class="[item.current ? 'text-gray-300' : 'text-gray-400 group-hover:text-gray-300', 'mr-3 flex-shrink-0 h-6 w-6']" aria-hidden="true" /> -->
                <!-- <component :is="item.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true"/> -->
                <Icon :name="item.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="false" />
                <!-- <component :is="item.icon" :class="[isActive ? 'bg-gray-900 text-white' : 'text-gray-400 group-hover:text-gray-300', 'mr-3 flex-shrink-0 h-6 w-6']" aria-hidden="true" /> -->
                <!-- <component :is="item.icon" :class="[isActive? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white', 'mr-3 flex-shrink-0 h-6 w-6']" aria-hidden="true" /> -->
                {{ item.name }}
              </div>
            </nuxt-link>
          </nav>
        </div>
      </div>
    </div>
    <div class="flex flex-col md:pl-64">
      <div class="sticky top-0 z-10 flex h-16 flex-shrink-0 bg-white shadow">
        <button type="button"
          class="border-r border-gray-200 px-4 text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500 md:hidden"
          @click="sidebarOpen = true">
          <span class="sr-only">Open sidebar</span>
          <Icon name="heroicons:bars-3-bottom-left" class="h-6 w-6" aria-hidden="true" />
        </button>
        <div class="flex flex-1 justify-between px-4">
          <div class="flex flex-1">
            <form class="flex w-full md:ml-0" action="#" method="GET">
              <label for="search-field" class="sr-only">Search</label>
              <div class="relative w-full text-gray-400 focus-within:text-gray-600">
                <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center">
                  <Icon name="heroicons:magnifying-glass-20-solid" class="h-5 w-5" aria-hidden="true" />
                </div>
                <input id="search-field"
                  class="block h-full w-full border-transparent py-2 pl-8 pr-3 text-gray-900 placeholder-gray-500 focus:border-transparent focus:placeholder-gray-400 focus:outline-none focus:ring-0 sm:text-sm"
                  placeholder="Search" type="search" name="search" />
              </div>
            </form>
          </div>
          <div class="flex items-center justify-center">
            <!-- <button type="button"
              class="inline-flex items-center rounded-md border border-transparent bg-indigo-600 p-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
              <Icon name="heroicons:home" class="h-5 w-5" aria-hidden="true" />
            </button> -->

          </div>
          <div class="ml-4 flex items-center md:ml-6">
            <button type="button"
              class="rounded-full bg-white p-1 text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
              <span class="sr-only">View notifications</span>
              <Icon name="heroicons:bell" class="h-6 w-6" aria-hidden="true" />
            </button>

            <!-- Profile dropdown -->
            <HeadlessMenu as="div" class="relative ml-3">
              <div>
                <HeadlessMenuButton
                  class="flex max-w-xs items-center rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                  <span class="sr-only">Open user menu</span>
                  <img class="h-8 w-8 rounded-full"
                    :src="GetDefaultImage()"
                    alt="Default User Profile Picture" />
                </HeadlessMenuButton>
              </div>
              <transition enter-active-class="transition ease-out duration-100"
                enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
                leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
                leave-to-class="transform opacity-0 scale-95">
                <HeadlessMenuItems
                  class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                  <HeadlessMenuItem v-for="item in userNavigation" :key="item.name" v-slot="{ active }">
                    <router-link :to="item.href"
                      :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">{{ item.name
                      }}</router-link>
                  </HeadlessMenuItem>
                </HeadlessMenuItems>
              </transition>
            </HeadlessMenu>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const navigation = ref([
  {
    name: "Dashboard",
    href: "/admin/hub/",
    icon: "heroicons:home",
    current: false,
  },
  {
    name: "Airports",
    href: "/admin/airports/",
    icon: "heroicons:paper-airplane",
    current: false,
  },
  {
    name: "Terminals",
    href: "/admin/terminals/",
    icon: "heroicons:folder",
    current: false,
  },
  {
    name: "Amenities",
    href: "/admin/amenities/",
    icon: "heroicons:calendar",
    current: false,
  },
  {
    name: "Lounges",
    href: "/admin/lounges/",
    icon: "heroicons:inbox",
    current: false,
  },
  {
    name: "Users",
    href: "/admin/users/",
    icon: "heroicons-outline:user-group",
    current: false,
  },
  {
    name: "Review",
    href: "/admin/review",
    icon: "heroicons:bars-3-bottom-left",
    current: false,
  },
  {
    name: "Blogs",
    href: "/admin/blog/",
    icon: "heroicons:bars-3-bottom-left",
    current: false,
  },
  {
    name: "Card issuers",
    href: "/admin/card-issuers",
    icon: "heroicons:clipboard",
    current: false,
  },
  {
    name: "Card network",
    href: "/admin/card-networks",
    icon: "heroicons:building-storefront",
    current: false,
  },
  {
    name: "Card",
    href: "/admin/card",
    icon: "heroicons:credit-card",
    current: false,
  },
  {
    name: "Card programs",
    href: "/admin/card-programs",
    icon: "heroicons:bars-3-bottom-left",
    current: false,
  },

  {
    name: "Pages",
    href: "/admin/pages",
    icon: "heroicons:bars-3-bottom-left",
    current: false,
  },
  {
    name: "Admin logs",
    href: "/admin/adminlog",
    icon: "heroicons:user",
    current: false,
  },
]);
const userNavigation = [
  {
    name: "Your Profile",
    href: "#",
  },
  {
    name: "Settings",
    href: "#",
  },
  {
    name: "Go to frontend site",
    href: "/",
  },
  {
    name: "Sign Out",
    href: "/admin/signout",
  },
];

const sidebarOpen = ref(false);
</script>
