/*
 * Adds a "Select all" icon inside any <select multiple> marked with the
 * "netbox-backupjobs-select-all" class (used for the hour/day/month schedule fields).
 *
 * These selects are enhanced client-side into a TomSelect dropdown by NetBox's own JS bundle
 * (see project-static/src/select/static.ts). The icon is anchored to the outer `.ts-wrapper`
 * element (exposed as `tomselect.wrapper`) rather than `.ts-control`, because TomSelect
 * re-renders the contents of `.ts-control` every time an item is added/removed - anything
 * inserted there directly gets wiped out or shifted as soon as a value is selected. Anchoring
 * to the wrapper with absolute positioning keeps the icon fixed in place on the left.
 */
(function () {
  const MARKER_CLASS = 'netbox-backupjobs-select-all';
  const ICON_CLASS = 'backupjobs-select-all-icon';
  const INIT_ATTR = 'data-backupjobs-selectall-init';

  function allValues(select) {
    return Array.from(select.options).map(function (option) {
      return option.value;
    });
  }

  function selectAll(select) {
    if (select.tomselect) {
      select.tomselect.setValue(allValues(select));
    } else {
      Array.from(select.options).forEach(function (option) {
        option.selected = true;
      });
      select.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }

  function attachIcon(select) {
    const tomselect = select.tomselect;
    const wrapper = tomselect && (tomselect.wrapper || select.closest('.ts-wrapper'));
    if (!tomselect || !wrapper || !tomselect.control) {
      return false;
    }
    if (wrapper.querySelector('.' + ICON_CLASS)) {
      return true;
    }

    if (!wrapper.style.position) {
      wrapper.style.position = 'relative';
    }

    const icon = document.createElement('i');
    icon.className = 'mdi mdi-playlist-check ' + ICON_CLASS;
    icon.title = 'Select all';
    icon.setAttribute('role', 'button');
    icon.style.position = 'absolute';
    icon.style.left = '.5rem';
    icon.style.top = '50%';
    icon.style.transform = 'translateY(-50%)';
    icon.style.zIndex = '2';
    icon.style.cursor = 'pointer';
    icon.style.fontSize = '1.35rem';
    icon.addEventListener('click', function (event) {
      // Prevent the click from opening/closing the TomSelect dropdown.
      event.preventDefault();
      event.stopPropagation();
      selectAll(select);
    });

    wrapper.appendChild(icon);
    // Make room so the icon never overlaps the selected item tags or input text.
    tomselect.control.style.paddingLeft = '2.25rem';

    // Hide the icon once every choice is already selected - clicking it again would be a
    // no-op. Re-checked on every value change (added item, removed item, or Select all itself).
    const totalOptionCount = select.options.length;
    function updateVisibility() {
      icon.style.display = tomselect.items.length >= totalOptionCount ? 'none' : '';
    }
    tomselect.on('change', updateVisibility);
    updateVisibility();

    return true;
  }

  function initField(select) {
    if (select.hasAttribute(INIT_ATTR)) {
      return;
    }
    select.setAttribute(INIT_ATTR, 'true');

    if (attachIcon(select)) {
      return;
    }
    // TomSelect may not have finished initializing yet; poll briefly for it.
    let attempts = 0;
    const interval = setInterval(function () {
      attempts += 1;
      if (attachIcon(select) || attempts > 50) {
        clearInterval(interval);
      }
    }, 100);
  }

  function init() {
    document.querySelectorAll('select.' + MARKER_CLASS).forEach(initField);
  }

  if (document.readyState === 'complete') {
    init();
  } else {
    window.addEventListener('load', init);
  }
})();
