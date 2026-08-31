// Kiosk Global Interactive Controller
document.addEventListener('DOMContentLoaded', () => {
  // 1. Live Realtime Clock
  function updateClock() {
    const timeEl = document.getElementById('kioskLiveTime');
    const dateEl = document.getElementById('kioskLiveDate');
    if (!timeEl) return;

    const now = new Date();
    let hours = now.getHours();
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // 12-hour format
    const formattedHours = String(hours).padStart(2, '0');

    timeEl.textContent = `${formattedHours}:${minutes} ${ampm}`;

    if (dateEl) {
      const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      const dayName = days[now.getDay()];
      const dayNum = now.getDate();
      const monthName = months[now.getMonth()];
      const year = now.getFullYear();
      dateEl.textContent = `${dayName}, ${dayNum} ${monthName} ${year}`;
    }
  }

  updateClock();
  setInterval(updateClock, 1000);

  // 2. Global Modal Helpers
  window.openKioskModal = function(id) {
    const m = document.getElementById(id);
    if (m) m.classList.add('open');
  };

  window.closeKioskModal = function(id) {
    const m = document.getElementById(id);
    if (m) m.classList.remove('open');
  };

  // 3. Search Bar Interaction
  const searchInput = document.getElementById('kioskSearchInput');
  if (searchInput) {
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const query = searchInput.value.trim();
        if (query) {
          window.location.href = `map.html?search=${encodeURIComponent(query)}`;
        }
      }
    });
  }

  // 4. Voice Search Simulation
  window.simulateVoiceSearch = function() {
    openKioskModal('voiceSearchModal');
    setTimeout(() => {
      const statusText = document.getElementById('voiceStatusText');
      if (statusText) statusText.textContent = "Listening... 'Show me coffee shops'";
    }, 1200);
    setTimeout(() => {
      closeKioskModal('voiceSearchModal');
      window.location.href = 'food.html';
    }, 3000);
  };

  // 5. Feedback Rating Selection
  const ratingBtns = document.querySelectorAll('.rating-face-btn');
  ratingBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      ratingBtns.forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
    });
  });

  // 6. Feedback Category Pills Multi-select
  const feedbackCatPills = document.querySelectorAll('.feedback-cat-pill');
  feedbackCatPills.forEach(pill => {
    pill.addEventListener('click', () => {
      pill.classList.toggle('selected');
    });
  });

  // 7. Feedback Textarea Character Counter
  const feedbackTextarea = document.getElementById('feedbackComment');
  const charCounter = document.getElementById('feedbackCharCounter');
  if (feedbackTextarea && charCounter) {
    feedbackTextarea.addEventListener('input', () => {
      charCounter.textContent = `${feedbackTextarea.value.length}/500`;
    });
  }

  // 8. Submit Feedback Action
  window.submitKioskFeedback = function(e) {
    if (e) e.preventDefault();
    openKioskModal('feedbackSuccessModal');
  };

  // 9. Event Book Now Trigger
  window.bookEvent = function(eventName) {
    const titleEl = document.getElementById('eventModalTitle');
    if (titleEl) titleEl.textContent = eventName || 'Event Booking';
    openKioskModal('eventBookingModal');
  };

  // 10. Map Floor Switcher
  window.selectMapFloor = function(btn, floorName) {
    document.querySelectorAll('.kiosk-segmented-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const floorLabel = document.getElementById('currentFloorLabel');
    if (floorLabel) floorLabel.textContent = floorName;
  };

  // 11. Food Segment Switcher
  window.switchFoodTab = function(btn, category) {
    document.querySelectorAll('.kiosk-segmented-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  };

  // 12. Promotional Carousel Switcher & Auto-rotation
  let currentPromoIndex = 0;
  const promoSlides = document.querySelectorAll('.promo-slide');
  const promoDots = document.querySelectorAll('.carousel-dot');

  window.switchPromoSlide = function(index) {
    if (!promoSlides.length) return;
    currentPromoIndex = index % promoSlides.length;
    promoSlides.forEach((s, idx) => {
      s.classList.toggle('active', idx === currentPromoIndex);
    });
    promoDots.forEach((d, idx) => {
      d.classList.toggle('active', idx === currentPromoIndex);
    });
  };

  if (promoSlides.length > 1) {
    setInterval(() => {
      switchPromoSlide((currentPromoIndex + 1) % promoSlides.length);
    }, 6000);
  }

  // 13. Global Inactivity Idle Timer (Attract Mode Trigger)
  // Configurable idle timeout (set to 15 seconds for live client presentation)
  const KIOSK_IDLE_TIMEOUT_SECONDS = 15;
  let idleTimer = null;

  function resetIdleTimer() {
    if (idleTimer) clearTimeout(idleTimer);
    // Only start idle countdown if not already on the attract screen
    if (!window.location.pathname.endsWith('attract.html')) {
      idleTimer = setTimeout(() => {
        window.location.href = 'attract.html';
      }, KIOSK_IDLE_TIMEOUT_SECONDS * 1000);
    }
  }

  // Listen for any user interaction (touch, click, mousemove, keypress)
  ['touchstart', 'touchend', 'click', 'mousemove', 'keypress', 'scroll'].forEach(evt => {
    window.addEventListener(evt, resetIdleTimer, { passive: true });
  });

  resetIdleTimer();
});

