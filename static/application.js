up.link.config.instantSelectors.unshift('a[up-follow]')
up.link.config.preloadSelectors.unshift('a[up-follow]')
up.link.config.instantSelectors.push('a[href]')

// Enable more logging for curious users.
//up.log.enable()

// Gray out tour dots once clicked.
up.on('up:link:follow', '.tour-dot', (event, element) => { element.classList.add('viewed') })

/*
up.compiler('nav a[href]', (link) => {
  if(!link.href.endsWith('#')) link.setAttribute('up-alias', link.href + '?*')
})
*/

up.compiler('.pagination .page-item a.page-link', (link) => {
  link.setAttribute('up-follow', link.href)
  link.setAttribute('up-target', ".table-container")
  link.setAttribute('up-history', "true")
})

up.compiler('th.orderable a[href]', (link) => {
  link.setAttribute('up-follow', link.href)
  link.setAttribute('up-target', ".table-container")
  link.setAttribute('up-history', "true")
})

async function reloadWithFlash(selector, flash) {
  await up.reload(selector, { focus: ':main' })
  up.element.affix(document.getElementById('flash-messages'), '.alert.fade.show.alert-success', { text: flash })
}

async function reloadWithFlashIfEvent(selector, flash, value) {
  await up.reload(selector, { focus: ':main' })
  if(value instanceof Event || value == ':peel') {
    up.element.affix(document.getElementById('flash-messages'), '.alert.fade.show.alert-danger', { text: flash })
  }
}

// Don't highlight the fragment insertion from the initial compile on DOMContentLoaded.
window.addEventListener('load', (event) => {
  // Show the yellow flash when a new fragment was inserted.
  up.on('up:fragment:inserted', (event, fragment) => {
    fragment.classList.add('new-fragment', 'inserted')
    up.util.timer(0, () => fragment.classList.remove('inserted'))
    up.util.timer(1000, () => fragment.classList.remove('new-fragment'))
  })
})

