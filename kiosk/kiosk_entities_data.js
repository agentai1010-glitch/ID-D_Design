// Shared Kiosk Entity Registry Data Model (Stores, Offers, Events, Services)

// =========================================================================
// 1. STORES & PHYSICAL ENTITIES
// =========================================================================
window.KIOSK_ENTITIES = {
  "nike": {
    id: "nike",
    name: "Nike",
    category: "Sportswear",
    categoryType: "shop",
    logo: "https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg",
    heroImages: [
      "../images/kiosk_search_adidas_store.jpg",
      "../images/kiosk_festive_sale_hero.jpg",
      "../images/kiosk_highlight_style.jpg"
    ],
    heroTagline: "JUST DO IT.",
    floor: "Ground Floor",
    unit: "GF-12",
    location: "Central Wing, Near Atrium",
    hours: "10:00 AM - 10:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567890",
    website: "www.nike.com",
    rating: 4.6,
    reviewCount: 128,
    ratingBreakdown: { 5: 78, 4: 15, 3: 4, 2: 2, 1: 1 },
    reviews: [
      { author: "Vikram Malhotra", rating: 5, date: "2 days ago", comment: "Amazing collection of Pegasus 40 and Jordan series. Helpful staff!" },
      { author: "Ananya Sharma", rating: 4, date: "1 week ago", comment: "Great store ambiance and quick billing at the cashier desk." }
    ],
    deals: [
      {
        id: "deal-nike-1",
        title: "FLAT 40% OFF",
        subtitle: "On Running Shoes",
        validity: "Valid till 31 Aug 2026",
        badge: "40% OFF",
        image: "../images/kiosk_highlight_style.jpg"
      },
      {
        id: "deal-nike-2",
        title: "30% OFF",
        subtitle: "On Backpacks & Duffels",
        validity: "Valid till 31 Aug 2026",
        badge: "30% OFF",
        image: "../images/kiosk_store_zara.jpg"
      }
    ],
    similarEntities: [
      { id: "adidas", name: "Adidas", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg", unit: "GF-14" },
      { id: "puma", name: "Puma", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/8/88/Puma-Logo.png", unit: "GF-16" },
      { id: "reebok", name: "Reebok", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/d/d7/Reebok_2019_logo.svg", unit: "GF-18" },
      { id: "under-armour", name: "Under Armour", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/4/44/Under_armour_logo.svg", unit: "GF-22" },
      { id: "new-balance", name: "New Balance", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/e/ea/New_Balance_logo.svg", unit: "GF-24" }
    ]
  },

  "adidas": {
    id: "adidas",
    name: "Adidas",
    category: "Sportswear",
    categoryType: "shop",
    logo: "https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg",
    heroImages: [
      "../images/kiosk_search_adidas_store.jpg",
      "../images/kiosk_search_adidas_event.jpg",
      "../images/kiosk_highlight_style.jpg"
    ],
    heroTagline: "IMPOSSIBLE IS NOTHING.",
    floor: "Ground Floor",
    unit: "GF-14",
    location: "Central Wing, West Corridor",
    hours: "10:00 AM - 10:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567891",
    website: "www.adidas.co.in",
    rating: 4.5,
    reviewCount: 112,
    ratingBreakdown: { 5: 72, 4: 18, 3: 6, 2: 3, 1: 1 },
    reviews: [
      { author: "Rohan Sen", rating: 5, date: "3 days ago", comment: "Ultraboost light range is fully in stock. Excellent trial rooms." }
    ],
    deals: [
      {
        id: "deal-adidas-1",
        title: "FLAT 35% OFF",
        subtitle: "On Originals & Stan Smith",
        validity: "Valid till 30 Sep 2026",
        badge: "35% OFF",
        image: "../images/kiosk_search_adidas_store.jpg"
      }
    ],
    similarEntities: [
      { id: "nike", name: "Nike", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg", unit: "GF-12" },
      { id: "puma", name: "Puma", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/8/88/Puma-Logo.png", unit: "GF-16" }
    ]
  },

  "puma": {
    id: "puma",
    name: "Puma",
    category: "Sportswear",
    categoryType: "shop",
    logo: "https://upload.wikimedia.org/wikipedia/commons/8/88/Puma-Logo.png",
    heroImages: [
      "../images/kiosk_highlight_style.jpg",
      "../images/kiosk_store_zara.jpg"
    ],
    heroTagline: "FOREVER FASTER.",
    floor: "Ground Floor",
    unit: "GF-16",
    location: "North Promenade",
    hours: "10:00 AM - 10:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567892",
    website: "in.puma.com",
    rating: 4.4,
    reviewCount: 94,
    ratingBreakdown: { 5: 68, 4: 20, 3: 7, 2: 3, 1: 2 },
    reviews: [
      { author: "Kunal Mehra", rating: 5, date: "Yesterday", comment: "Motorsport collection is top notch. Great discounts on sneakers." }
    ],
    deals: [
      {
        id: "deal-puma-1",
        title: "BUY 2 GET 1 FREE",
        subtitle: "On Activewear & Tees",
        validity: "Valid till 15 Sep 2026",
        badge: "SPECIAL",
        image: "../images/kiosk_highlight_style.jpg"
      }
    ],
    similarEntities: [
      { id: "nike", name: "Nike", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg", unit: "GF-12" },
      { id: "adidas", name: "Adidas", category: "Sportswear", logo: "https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg", unit: "GF-14" }
    ]
  },

  "zara": {
    id: "zara",
    name: "Zara",
    category: "Fashion",
    categoryType: "shop",
    logo: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Zara_Logo.svg",
    heroImages: [
      "../images/kiosk_store_zara.jpg",
      "../images/kiosk_festive_sale_hero.jpg"
    ],
    heroTagline: "AUTUMN / WINTER 2026 COLLECTION",
    floor: "Lower Ground",
    unit: "LG-08",
    location: "South Atrium Promenade",
    hours: "10:00 AM - 10:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567893",
    website: "www.zara.com/in",
    rating: 4.7,
    reviewCount: 245,
    ratingBreakdown: { 5: 82, 4: 12, 3: 3, 2: 2, 1: 1 },
    reviews: [
      { author: "Pooja Hegde", rating: 5, date: "4 days ago", comment: "Massive 2-floor store with latest global runway styles. Loved it!" }
    ],
    deals: [
      {
        id: "deal-zara-1",
        title: "UP TO 50% OFF",
        subtitle: "Mid-Season Fashion Gala",
        validity: "Valid till 20 Sep 2026",
        badge: "50% OFF",
        image: "../images/kiosk_store_zara.jpg"
      }
    ],
    similarEntities: [
      { id: "hm", name: "H&M", category: "Fashion", logo: "https://upload.wikimedia.org/wikipedia/commons/5/53/H%26M-Logo.svg", unit: "LG-10" },
      { id: "levis", name: "Levi's", category: "Denim", logo: "https://upload.wikimedia.org/wikipedia/commons/8/84/Levi%27s_logo.svg", unit: "UG-21" }
    ]
  },

  "hm": {
    id: "hm",
    name: "H&M",
    category: "Fashion",
    categoryType: "shop",
    logo: "https://upload.wikimedia.org/wikipedia/commons/5/53/H%26M-Logo.svg",
    heroImages: [
      "../images/kiosk_store_hm.jpg",
      "../images/kiosk_store_zara.jpg"
    ],
    heroTagline: "FASHION & QUALITY AT BEST PRICE",
    floor: "Lower Ground",
    unit: "LG-10",
    location: "South Wing Entrance",
    hours: "10:00 AM - 10:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567894",
    website: "www2.hm.com/en_in",
    rating: 4.5,
    reviewCount: 180,
    ratingBreakdown: { 5: 70, 4: 20, 3: 5, 2: 3, 1: 2 },
    reviews: [
      { author: "Deepak Rawat", rating: 5, date: "3 days ago", comment: "Great sustainable cotton collection and kids section." }
    ],
    deals: [
      {
        id: "deal-hm-1",
        title: "FLAT 20% OFF",
        subtitle: "On Men's & Women's Basics",
        validity: "Valid till 30 Sep 2026",
        badge: "20% OFF",
        image: "../images/kiosk_store_hm.jpg"
      }
    ],
    similarEntities: [
      { id: "zara", name: "Zara", category: "Fashion", logo: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Zara_Logo.svg", unit: "LG-08" }
    ]
  },

  "levis": {
    id: "levis",
    name: "Levi's",
    category: "Denim",
    categoryType: "shop",
    logo: "https://upload.wikimedia.org/wikipedia/commons/8/84/Levi%27s_logo.svg",
    heroImages: [
      "../images/kiosk_store_zara.jpg",
      "../images/kiosk_highlight_style.jpg"
    ],
    heroTagline: "LIVE IN LEVI'S - 501® ORIGINAL",
    floor: "Upper Ground",
    unit: "UG-21",
    location: "Denim Boulevard",
    hours: "10:00 AM - 10:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567895",
    website: "www.levi.in",
    rating: 4.6,
    reviewCount: 140,
    ratingBreakdown: { 5: 75, 4: 16, 3: 5, 2: 2, 1: 2 },
    reviews: [
      { author: "Sameer Joshi", rating: 5, date: "5 days ago", comment: "Custom tailorshop inside the store to personalize denim jackets!" }
    ],
    deals: [
      {
        id: "deal-levis-1",
        title: "BUY 2 AT FLAT 30% OFF",
        subtitle: "On 511 & 501 Series",
        validity: "Valid till 25 Sep 2026",
        badge: "30% OFF",
        image: "../images/kiosk_store_zara.jpg"
      }
    ],
    similarEntities: [
      { id: "zara", name: "Zara", category: "Fashion", logo: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Zara_Logo.svg", unit: "LG-08" }
    ]
  },

  "sephora": {
    id: "sephora",
    name: "Sephora",
    category: "Beauty & Cosmetics",
    categoryType: "shop",
    logo: "https://upload.wikimedia.org/wikipedia/commons/6/6b/Sephora_logo.svg",
    heroImages: [
      "../images/kiosk_store_sephora.jpg",
      "../images/kiosk_highlight_style.jpg"
    ],
    heroTagline: "BEAUTY UNCOMPLICATED & LUXURIOUS",
    floor: "Ground Floor",
    unit: "GF-05",
    location: "Beauty Boulevard",
    hours: "10:00 AM - 10:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567896",
    website: "sephora.nnnow.com",
    rating: 4.8,
    reviewCount: 310,
    ratingBreakdown: { 5: 85, 4: 10, 3: 3, 2: 1, 1: 1 },
    reviews: [
      { author: "Kavya Menon", rating: 5, date: "Yesterday", comment: "Complimentary flash makeover and Dior lip glow samples!" }
    ],
    deals: [
      {
        id: "deal-sephora-1",
        title: "FREE BEAUTY DELUXE BOX",
        subtitle: "On orders above ₹4,999",
        validity: "Valid till 30 Sep 2026",
        badge: "GIFT",
        image: "../images/kiosk_store_sephora.jpg"
      }
    ],
    similarEntities: [
      { id: "zara", name: "Zara", category: "Fashion", logo: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Zara_Logo.svg", unit: "LG-08" }
    ]
  },

  "copper-chimney": {
    id: "copper-chimney",
    name: "Copper Chimney",
    category: "North Indian & Mughlai",
    categoryType: "food",
    logo: "https://upload.wikimedia.org/wikipedia/commons/e/ef/Restaurant_icon.svg",
    heroImages: [
      "../images/kiosk_food_copper_chimney.jpg",
      "../images/kiosk_highlight_food.jpg"
    ],
    heroTagline: "CULINARY TRADITIONS SINCE 1972",
    floor: "First Floor",
    unit: "FF-04",
    location: "Fine Dining Terrace",
    hours: "11:30 AM - 11:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567888",
    website: "www.copperchimney.in",
    rating: 4.8,
    reviewCount: 380,
    ratingBreakdown: { 5: 88, 4: 8, 3: 2, 2: 1, 1: 1 },
    reviews: [
      { author: "Rajesh Khanna", rating: 5, date: "Yesterday", comment: "The Dum Biryani and Paneer Tikka melt in your mouth. Exceptional hospitality!" }
    ],
    deals: [
      {
        id: "deal-cc-1",
        title: "20% OFF ON DINNER",
        subtitle: "For Tables of 4 or More",
        validity: "Valid till 30 Sep 2026",
        badge: "20% OFF",
        image: "../images/kiosk_food_copper_chimney.jpg"
      }
    ],
    similarEntities: [
      { id: "starbucks", name: "Starbucks Coffee", category: "Café", logo: "https://upload.wikimedia.org/wikipedia/en/d/d3/Starbucks_Corporation_Logo_2011.svg", unit: "GF-02" }
    ]
  },

  "starbucks": {
    id: "starbucks",
    name: "Starbucks Coffee",
    category: "Café & Bakery",
    categoryType: "food",
    logo: "https://upload.wikimedia.org/wikipedia/en/d/d3/Starbucks_Corporation_Logo_2011.svg",
    heroImages: [
      "../images/kiosk_food_starbucks.jpg",
      "../images/kiosk_highlight_food.jpg"
    ],
    heroTagline: "TO INSPIRE & NURTURE THE HUMAN SPIRIT",
    floor: "Ground Floor",
    unit: "GF-02",
    location: "Central Piazza Garden",
    hours: "08:00 AM - 11:00 PM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567889",
    website: "www.starbucks.in",
    rating: 4.7,
    reviewCount: 420,
    ratingBreakdown: { 5: 80, 4: 14, 3: 4, 2: 1, 1: 1 },
    reviews: [
      { author: "Meera Nair", rating: 5, date: "2 days ago", comment: "Best Caramel Macchiato and Java Chip Frappuccino with fast Wi-Fi." }
    ],
    deals: [
      {
        id: "deal-sb-1",
        title: "COMPLIMENTARY COOKIE",
        subtitle: "With any Grande or Venti Beverage",
        validity: "Valid till 15 Sep 2026",
        badge: "FREE",
        image: "../images/kiosk_food_starbucks.jpg"
      }
    ],
    similarEntities: [
      { id: "copper-chimney", name: "Copper Chimney", category: "Dining", logo: "https://upload.wikimedia.org/wikipedia/commons/e/ef/Restaurant_icon.svg", unit: "FF-04" }
    ]
  },

  "atm": {
    id: "atm",
    name: "24/7 ATM Lounge",
    category: "Banking & Financial Service",
    categoryType: "services",
    logo: "https://upload.wikimedia.org/wikipedia/commons/1/12/ATM_icon.svg",
    heroImages: [
      "../images/kiosk_previw_mall.png",
      "../images/mall_atrium_hero_1787351821606.jpg"
    ],
    heroTagline: "SECURE CASH WITHDRAWALS & BANKING",
    floor: "Ground Floor",
    unit: "GF-ATM",
    location: "Near Gate 2 / Parking Lobby",
    hours: "24 Hours Open",
    isOpen: true,
    status: "Open Now",
    phone: "1800-425-3800",
    website: "www.grandmetromall.com/services",
    rating: 4.9,
    reviewCount: 88,
    ratingBreakdown: { 5: 92, 4: 6, 3: 2, 2: 0, 1: 0 },
    reviews: [
      { author: "Sunil Verma", rating: 5, date: "1 week ago", comment: "Air conditioned lounge with HDFC, ICICI, and SBI multi-currency ATMs." }
    ],
    deals: [],
    similarEntities: []
  },

  "pvr": {
    id: "pvr",
    name: "PVR Cinemas IMAX & 4DX",
    category: "Cinema & Entertainment",
    categoryType: "events",
    logo: "https://upload.wikimedia.org/wikipedia/commons/c/c5/PVR_Cinemas_logo.svg",
    heroImages: [
      "../images/kiosk_highlight_gaming.jpg",
      "../images/kiosk_search_adidas_event.jpg"
    ],
    heroTagline: "EXPERIENCE MOVIES IN LASER IMAX",
    floor: "Third Floor",
    unit: "L3-Cinema",
    location: "Level 3 Entertainment Hub",
    hours: "09:00 AM - 01:00 AM",
    isOpen: true,
    status: "Open Now",
    phone: "0124-4567899",
    website: "www.pvrcinemas.com",
    rating: 4.8,
    reviewCount: 520,
    ratingBreakdown: { 5: 86, 4: 10, 3: 2, 2: 1, 1: 1 },
    reviews: [
      { author: "Aditya Roy", rating: 5, date: "Yesterday", comment: "Dolby Atmos audio and plush recliner seats are unmatched!" }
    ],
    deals: [
      {
        id: "deal-pvr-1",
        title: "FLAT ₹150 OFF",
        subtitle: "On Morning IMAX Shows (Mon-Thu)",
        validity: "Valid till 30 Sep 2026",
        badge: "OFFER",
        image: "../images/kiosk_highlight_gaming.jpg"
      }
    ],
    similarEntities: []
  }
};

// =========================================================================
// 2. DEDICATED OFFERS & PROMOTIONS REGISTRY
// =========================================================================
window.KIOSK_OFFERS = {
  "deal-nike-1": {
    id: "deal-nike-1",
    title: "FLAT 40% OFF On Running Shoes",
    subtitle: "Pegasus, Infinity Run & Zoom Fly Series",
    category: "Fashion & Sports",
    categoryType: "sports",
    discountBadge: "40% OFF",
    promoCode: "RUNFAST40",
    storeId: "nike",
    storeName: "Nike Flagship Store",
    storeFloor: "Ground Floor (GF-12)",
    storeLogo: "https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg",
    heroImage: "../images/kiosk_search_adidas_store.jpg",
    validity: "Valid till 31 Aug 2026",
    daysLeft: "Ends in 4 Days",
    summary: "Upgrade your fitness routine with authentic Nike premium road and trail running footwear at an unprecedented 40% discount.",
    terms: [
      "Applicable exclusively on selected performance running shoes (Pegasus 40, Invincible 3, Zoom Fly 5).",
      "Must present promo code RUNFAST40 at store checkout counter before billing.",
      "Cannot be clubbed with existing loyalty club points, gift vouchers, or clearance items.",
      "Valid strictly for in-store purchases at Grand Metro Mall branch.",
      "Standard exchange policy applies within 14 days of purchase with original receipt."
    ],
    howToRedeem: [
      "Visit the Nike Store located on Ground Floor (GF-12).",
      "Select your eligible running shoe sizes and head to the cashier desk.",
      "Scan this kiosk QR code or present code 'RUNFAST40' to claim your instant 40% bill markdown."
    ],
    similarOffers: ["deal-adidas-1", "deal-puma-1", "deal-nike-2"]
  },

  "deal-nike-2": {
    id: "deal-nike-2",
    title: "30% OFF On Backpacks & Training Bags",
    subtitle: "Duffels, Gym Sacks & Urban Commuter Packs",
    category: "Sports Accessories",
    categoryType: "sports",
    discountBadge: "30% OFF",
    promoCode: "NIKEPACK30",
    storeId: "nike",
    storeName: "Nike Flagship Store",
    storeFloor: "Ground Floor (GF-12)",
    storeLogo: "https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg",
    heroImage: "../images/kiosk_store_zara.jpg",
    validity: "Valid till 31 Aug 2026",
    daysLeft: "Ends in 4 Days",
    summary: "Durable water-resistant backpacks and gym duffels engineered for athletes and daily urban commuters.",
    terms: [
      "Valid on all Nike Brasilia, Hayward, and Utility gym bags.",
      "Offer valid while stocks last.",
      "Limit of 2 discounted bags per customer transaction.",
      "Non-transferable and non-refundable for cash."
    ],
    howToRedeem: [
      "Pick your desired backpack from the accessories section at Nike (GF-12).",
      "Show promo code NIKEPACK30 to cashier at payment."
    ],
    similarOffers: ["deal-nike-1", "deal-puma-1"]
  },

  "deal-zara-1": {
    id: "deal-zara-1",
    title: "UP TO 50% OFF Mid-Season Fashion Gala",
    subtitle: "Autumn / Winter Trench Coats, Knitwear & Blazers",
    category: "Fashion & Apparel",
    categoryType: "fashion",
    discountBadge: "50% OFF",
    promoCode: "ZARAGALA",
    storeId: "zara",
    storeName: "ZARA Flagship Store",
    storeFloor: "Lower Ground (LG-08)",
    storeLogo: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Zara_Logo.svg",
    heroImage: "../images/kiosk_store_zara.jpg",
    validity: "Valid till 20 Sep 2026",
    daysLeft: "Limited Period Sale",
    summary: "Transform your seasonal wardrobe with global runway designs across women's, men's, and children's formal and casual fashion.",
    terms: [
      "Discount tiers range from 20% to 50% on items marked with red and yellow sale tags.",
      "Applicable across outerwear, tailored trousers, dresses, and selected leather footwear.",
      "Alterations on sale merchandise are chargeable at standard store rates.",
      "No returns or refunds on final clearance items; exchange permitted within 7 days."
    ],
    howToRedeem: [
      "Explore the 2-level ZARA flagship on Lower Ground (LG-08).",
      "Discounts are automatically calculated at the point of sale on eligible tagged apparel."
    ],
    similarOffers: ["deal-hm-1", "deal-levis-1", "deal-sephora-1"]
  },

  "deal-adidas-1": {
    id: "deal-adidas-1",
    title: "FLAT 35% OFF On Originals & Stan Smith",
    subtitle: "Superstar, Samba & Gazelle Classics",
    category: "Footwear & Fashion",
    categoryType: "sports",
    discountBadge: "35% OFF",
    promoCode: "ADIORIG35",
    storeId: "adidas",
    storeName: "Adidas Flagship",
    storeFloor: "Ground Floor (GF-14)",
    storeLogo: "https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg",
    heroImage: "../images/kiosk_search_adidas_store.jpg",
    validity: "Valid till 30 Sep 2026",
    daysLeft: "Ends in 28 Days",
    summary: "Iconic streetwear silhouettes crafted with sustainable Primegreen leather and timeless trefoil branding.",
    terms: [
      "Valid on select Adidas Originals footwear and lifestyle hoodies.",
      "Cannot be combined with student or employee discounts.",
      "Receipt required for warranty and size exchanges."
    ],
    howToRedeem: [
      "Visit Adidas on Ground Floor (GF-14).",
      "Mention code ADIORIG35 to store associate."
    ],
    similarOffers: ["deal-nike-1", "deal-puma-1"]
  },

  "deal-hm-1": {
    id: "deal-hm-1",
    title: "FLAT 20% OFF On Conscious Organic Basics",
    subtitle: "Men's, Women's & Kids Essential Wear",
    category: "Fashion & Lifestyle",
    categoryType: "fashion",
    discountBadge: "20% OFF",
    promoCode: "HMCONSCIOUS",
    storeId: "hm",
    storeName: "H&M Store",
    storeFloor: "Lower Ground (LG-10)",
    storeLogo: "https://upload.wikimedia.org/wikipedia/commons/5/53/H%26M-Logo.svg",
    heroImage: "../images/kiosk_store_hm.jpg",
    validity: "Valid till 30 Sep 2026",
    daysLeft: "Active This Month",
    summary: "Soft, breathable 100% organic cotton tees, hoodies, and loungewear made responsibly for the whole family.",
    terms: [
      "Minimum purchase of ₹1,999 required to unlock 20% discount.",
      "Garment collecting voucher can be combined with this offer.",
      "Valid in-store only."
    ],
    howToRedeem: [
      "Head to H&M at LG-10.",
      "Provide mobile number or barcode at counter."
    ],
    similarOffers: ["deal-zara-1", "deal-levis-1"]
  },

  "deal-cc-1": {
    id: "deal-cc-1",
    title: "20% OFF ON DINNER For Tables of 4+",
    subtitle: "Gourmet Mughlai Feast & Signature Biryanis",
    category: "Food & Fine Dining",
    categoryType: "food",
    discountBadge: "20% OFF",
    promoCode: "FEAST20",
    storeId: "copper-chimney",
    storeName: "Copper Chimney Restaurant",
    storeFloor: "First Floor (FF-04)",
    storeLogo: "https://upload.wikimedia.org/wikipedia/commons/e/ef/Restaurant_icon.svg",
    heroImage: "../images/kiosk_food_copper_chimney.jpg",
    validity: "Valid till 30 Sep 2026",
    daysLeft: "Dinner Special (7 PM - 11 PM)",
    summary: "Relish heritage culinary recipes including melt-in-mouth Galouti Kebabs, Paneer Tikka, and slow-dum biryanis with your family.",
    terms: [
      "Valid for dine-in tables of 4 persons or more between 7:00 PM and 11:00 PM.",
      "Not applicable on alcoholic beverages, tobacco, or pre-fixed buffet menus.",
      "Prior reservation recommended on weekends."
    ],
    howToRedeem: [
      "Arrive at Copper Chimney on First Floor (FF-04).",
      "Mention code FEAST20 to the restaurant steward prior to bill generation."
    ],
    similarOffers: ["deal-sb-1", "deal-pvr-1"]
  },

  "deal-sb-1": {
    id: "deal-sb-1",
    title: "COMPLIMENTARY COOKIE With Beverage",
    subtitle: "On Any Grande or Venti Handcrafted Coffee",
    category: "Café & Bakery",
    categoryType: "food",
    discountBadge: "FREE GIFT",
    promoCode: "STARCOOKIE",
    storeId: "starbucks",
    storeName: "Starbucks Coffee",
    storeFloor: "Ground Floor (GF-02)",
    storeLogo: "https://upload.wikimedia.org/wikipedia/en/d/d3/Starbucks_Corporation_Logo_2011.svg",
    heroImage: "../images/kiosk_food_starbucks.jpg",
    validity: "Valid till 15 Sep 2026",
    daysLeft: "Daily Happy Hours (3 PM - 7 PM)",
    summary: "Enjoy a fresh oven-baked chocolate chunk or oatmeal cookie free with your favorite handcrafted Frappuccino or Macchiato.",
    terms: [
      "Valid on Grande and Venti beverage sizes only.",
      "Choice of cookie subject to bakery counter availability.",
      "One free cookie per beverage transaction."
    ],
    howToRedeem: [
      "Order at Starbucks Central Piazza (GF-02).",
      "Show kiosk coupon code STARCOOKIE to the barista."
    ],
    similarOffers: ["deal-cc-1"]
  },

  "deal-pvr-1": {
    id: "deal-pvr-1",
    title: "FLAT ₹150 OFF On Morning IMAX Shows",
    subtitle: "Monday to Thursday Shows Before 12:00 PM",
    category: "Cinema & Entertainment",
    categoryType: "entertainment",
    discountBadge: "₹150 OFF",
    promoCode: "PVRIMAX150",
    storeId: "pvr",
    storeName: "PVR Cinemas IMAX & 4DX",
    storeFloor: "Third Floor (L3-Cinema)",
    storeLogo: "https://upload.wikimedia.org/wikipedia/commons/c/c5/PVR_Cinemas_logo.svg",
    heroImage: "../images/kiosk_highlight_gaming.jpg",
    validity: "Valid till 30 Sep 2026",
    daysLeft: "Weekday Special",
    summary: "Immerse yourself in crystal-clear laser projection and 12-channel audio with ₹150 instant markdown per IMAX ticket.",
    terms: [
      "Valid on IMAX 2D and 3D screenings starting before 12:00 PM (Mon-Thu).",
      "Convenience fees and government taxes applicable.",
      "Valid at Grand Metro Mall Box Office and Kiosk self-checkout."
    ],
    howToRedeem: [
      "Visit PVR Cinemas Box Office at Level 3.",
      "Select your IMAX morning show and apply code PVRIMAX150 at ticket kiosk."
    ],
    similarOffers: ["deal-cc-1", "deal-nike-1"]
  }
};

// =========================================================================
// 3. DEDICATED EVENTS & EXPERIENCES REGISTRY
// =========================================================================
window.KIOSK_EVENTS = {
  "armaan": {
    id: "armaan",
    title: "Armaan Malik Live In Concert",
    type: "Live Musical Concert",
    category: "Music & Live Shows",
    categoryType: "music",
    dateBadge: "Sat, 12 Sep 2026",
    timeBadge: "7:00 PM – 10:30 PM",
    venue: "Main Atrium Stage, Ground Floor",
    venueCode: "atrium",
    entryType: "Free Access / VIP Seating RSVP",
    organizer: "Grand Metro Live & Universal Music",
    heroImage: "../images/kiosk_search_adidas_event.jpg",
    statusBadge: "Upcoming Mega Event",
    artistBio: "Armaan Malik is an internationally acclaimed Indian singer, songwriter, and youth icon known for chartbusters like 'Bol Do Na Zara', 'Pehla Pyaar', and his global English singles.",
    summary: "Experience an electrifying musical evening featuring Bollywood chartbusters, soulful acoustic ballads, and live interactive crowd sessions under the Grand Metro central atrium dome.",
    schedule: [
      { time: "06:30 PM", title: "Gates Open & Ambient DJ Warmup", desc: "VIP seating check-in and atrium general admission" },
      { time: "07:15 PM", title: "Opening Act by Indie Acoustic Duo", desc: "Acoustic covers and original indie compositions" },
      { time: "08:00 PM", title: "Armaan Malik Live Performance", desc: "Full band live musical set with lasers and synchronized lighting" },
      { time: "10:15 PM", title: "Encore & Fan Interaction", desc: "Grand finale and meet-and-greet for VIP pass holders" }
    ],
    guidelines: [
      "Admission to general standing atrium is complimentary on a first-come, first-served basis.",
      "Reserved seating passes can be claimed at the mall concierge desk with shopping receipts of ₹5,000+.",
      "Professional DSLR cameras and outside food/beverages are strictly prohibited.",
      "Dedicated wheelchair viewing ramp available near Gate 1 elevator lobby."
    ],
    similarEvents: ["festive-2026", "fashion-showcase", "food-carnival"]
  },

  "festive-2026": {
    id: "festive-2026",
    title: "Grand Festive Celebration 2026",
    type: "Cultural Festival & Dandiya Nights",
    category: "Cultural Festivals",
    categoryType: "festivals",
    dateBadge: "20 Sep – 05 Oct 2026",
    timeBadge: "All Day (10:00 AM – 10:00 PM)",
    venue: "Grand Central Promenade & Courtyard",
    venueCode: "courtyard",
    entryType: "Free Entry for Families",
    organizer: "Grand Metro Cultural Arts Guild",
    heroImage: "../images/kiosk_festive_sale_hero.jpg",
    statusBadge: "Festive Season Flagship",
    artistBio: "Featuring top regional folk dance troupes, live Shehnai maestros, and celebrity Dandiya choreographers from across Gujarat and Rajasthan.",
    summary: "A 15-day cultural extravaganza with grand light installations, live traditional music, traditional handicraft bazaars, and nightly Garba sessions.",
    schedule: [
      { time: "11:00 AM", title: "Handicraft & Artisan Bazaars Open", desc: "Over 40 artisanal stalls featuring festive ethnic apparel and decor" },
      { time: "05:30 PM", title: "Live Folk Orchestra & Shehnai", desc: "Melodious classical evening recitals at Central Fountain" },
      { time: "07:30 PM", title: "Mega Dandiya & Garba Night", desc: "High-energy traditional group dancing with live dhol beats" }
    ],
    guidelines: [
      "Traditional festive attire encouraged for Dandiya participants.",
      "Wooden Dandiya sticks provided complimentary at entry gates.",
      "Family-friendly environment with enhanced security surveillance."
    ],
    similarEvents: ["armaan", "food-carnival", "magic-show"]
  },

  "food-carnival": {
    id: "food-carnival",
    title: "Grand Food & Taste Carnival",
    type: "Culinary Pop-ups & Celebrity Chef Demos",
    category: "Food & Dining",
    categoryType: "food",
    dateBadge: "19 – 27 Sep 2026",
    timeBadge: "12:00 PM – 10:00 PM Daily",
    venue: "Level 1 Open Terrace & Food Promenade",
    venueCode: "foodpromenade",
    entryType: "Free Admission (Tasting Passes Available)",
    organizer: "Culinary Masters India & Gourmet Guild",
    heroImage: "../images/kiosk_highlight_food.jpg",
    statusBadge: "Foodie Paradise",
    artistBio: "Curated by Michelin-starred guest chefs and celebrated mixologists showcasing fusion street foods, authentic regional thalis, and molecular desserts.",
    summary: "Embark on an epicurean journey featuring 30+ artisan pop-up kitchens, live cooking masterclasses, barbecue grills, and sweet dessert alleys.",
    schedule: [
      { time: "12:00 PM", title: "Tasting Stalls Open", desc: "Global street foods, Mexican tacos, dim sums, and Mughlai grills" },
      { time: "04:00 PM", title: "Chef Masterclass & Live Demo", desc: "Interactive cooking session with Chef Ranveer Brar" },
      { time: "08:00 PM", title: "Cocktail/Mocktail Mixology Clash", desc: "Flair bartending demonstrations and craft tasting" }
    ],
    guidelines: [
      "Cashless food cards available at carnival recharge kiosks.",
      "All dietary preferences (Pure Veg, Jain, Vegan, Gluten-Free) clearly labeled."
    ],
    similarEvents: ["armaan", "festive-2026"]
  },

  "kids-clay": {
    id: "kids-clay",
    title: "Kids Pottery & Creative Clay Workshop",
    type: "Interactive Workshop for Children",
    category: "Kids & Workshops",
    categoryType: "kids",
    dateBadge: "Every Weekend (Sat & Sun)",
    timeBadge: "11:00 AM – 2:00 PM",
    venue: "Activity Zone, Level 2 (Play Arena)",
    venueCode: "playzone",
    entryType: "Free Registration (Ages 5-14)",
    organizer: "Hamleys Kids Discovery Studio",
    heroImage: "../images/kiosk_highlight_gaming.jpg",
    statusBadge: "Weekend Special",
    artistBio: "Led by certified ceramic artists and child craft educators specialized in sensory development, wheel pottery, and sculpting.",
    summary: "Hands-on pottery wheels, terracotta clay modeling, and canvas painting where kids create and paint their own custom pots to take home.",
    schedule: [
      { time: "11:00 AM", title: "Pottery Wheel Basics", desc: "Introduction to clay centering and spinning on electric wheels" },
      { time: "12:15 PM", title: "Hand-building & Sculpting", desc: "Crafting ceramic animals, cups, and pinch pots" },
      { time: "01:15 PM", title: "Painting & Glazing Session", desc: "Organic paint application to personalize finished pieces" }
    ],
    guidelines: [
      "Complimentary aprons and clay modeling kits provided.",
      "Parents can relax in adjacent café lounge with clear viewing glass."
    ],
    similarEvents: ["magic-show", "festive-2026"]
  },

  "fashion-showcase": {
    id: "fashion-showcase",
    title: "Autumn Runway Fashion Showcase 2026",
    type: "Fashion Runway & Designer Premiere",
    category: "Fashion & Lifestyle",
    categoryType: "fashion",
    dateBadge: "Fri, 25 Sep 2026",
    timeBadge: "6:30 PM Onwards",
    venue: "Main Atrium Runway, Ground Floor",
    venueCode: "atrium",
    entryType: "Open Seating & VIP Invitations",
    organizer: "Vogue India & Grand Metro Luxury Brands",
    heroImage: "../images/kiosk_store_zara.jpg",
    statusBadge: "Glamour Premiere",
    artistBio: "Showcasing signature collections from ZARA, H&M, Levi's, Jack & Jones, and luxury designer couture with top supermodels.",
    summary: "A dazzling fashion extravaganza presenting the hottest autumn/winter trends, sustainable fabrics, and haute couture styling.",
    schedule: [
      { time: "06:30 PM", title: "Red Carpet Arrival & Photo Wall", desc: "Celebrity and influencer red carpet interviews" },
      { time: "07:15 PM", title: "International High Street Segment", desc: "Runway showcase featuring ZARA and H&M collections" },
      { time: "08:30 PM", title: "Festive Couture Grand Finale", desc: "Showstopper runway presentation with dramatic choreography" }
    ],
    guidelines: [
      "Front row VIP seating reserved for mall Gold/Platinum tier members.",
      "Flash photography permitted from designated media zones."
    ],
    similarEvents: ["armaan", "festive-2026"]
  },

  "magic-show": {
    id: "magic-show",
    title: "Grand Illusion & Magic Spectacular",
    type: "Family Magic & Illusion Show",
    category: "Kids & Entertainment",
    categoryType: "kids",
    dateBadge: "Sunday, 27 Sep 2026",
    timeBadge: "5:00 PM & 7:30 PM (2 Shows)",
    venue: "Level 3 Entertainment Amphitheater",
    venueCode: "amphitheater",
    entryType: "Free Family Entry",
    organizer: "Magic Circle of India",
    heroImage: "../images/kiosk_highlight_gaming.jpg",
    statusBadge: "Family Favorite",
    artistBio: "Featuring Master Illusionist Aryan Roy, winner of International Merlin Award with over 2,000 global stage performances.",
    summary: "Mind-boggling levitations, teleportation illusions, mind reading, and hilarious interactive magic tricks featuring kids from the audience.",
    schedule: [
      { time: "05:00 PM", title: "Show 1: Kids Wonder Magic Hour", desc: "Interactive animal illusions and card tricks" },
      { time: "07:30 PM", title: "Show 2: Grand Stage Levitation Act", desc: "Dramatic large-scale illusions with special effects" }
    ],
    guidelines: [
      "Entry opens 20 minutes prior to each showtime.",
      "Children under 10 must be accompanied by an adult."
    ],
    similarEvents: ["kids-clay", "festive-2026"]
  }
};
