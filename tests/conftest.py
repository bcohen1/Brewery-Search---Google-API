import pytest


@pytest.fixture
def test_addr():
    return "40.807416, -96.675035"


@pytest.fixture
def sample_search_result():
    results = [
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": 38.8841996, "lng": -77.0929036},
                "viewport": {
                    "northeast": {"lat": 38.88537317989272, "lng": -77.09138857010728},
                    "southwest": {"lat": 38.88267352010728, "lng": -77.09408822989273},
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
            "icon_background_color": "#7B9EB0",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_pinlet",
            "name": "Board Room Brewing Company",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 3391,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/105810330768688784806">A Google User</a>'
                    ],
                    "photo_reference": "Aap_uEAUQRsWB8tkP9hlvq_gewVJYRJOgebctjVKeaskhdFkAwQvEPFC4THuJ7zNGg-gZRbn_XTx_BUr0x52EtTOVlhx0wit7P1ghp6oqbZhKR4_bIq9_w_QSHfnCUYD1LcD500xTqeHcb-YJUAT5_MvVdejjIqE4Cdj9-UyYHre7f1f85Tl",
                    "width": 2331,
                }
            ],
            "place_id": "ChIJM3N_k8K3t4kRP7rfKw9klUU",
            "plus_code": {
                "compound_code": "VWM4+MR Arlington, Virginia",
                "global_code": "87C4VWM4+MR",
            },
            "rating": 5,
            "reference": "ChIJM3N_k8K3t4kRP7rfKw9klUU",
            "scope": "GOOGLE",
            "types": ["food", "point_of_interest", "establishment"],
            "user_ratings_total": 6,
            "vicinity": "925 N Garfield St, Arlington",
        },
        {
            "business_status": "CLOSED_TEMPORARILY",
            "geometry": {
                "location": {"lat": 38.8882754, "lng": -77.09341529999999},
                "viewport": {
                    "northeast": {"lat": 38.88963902989273, "lng": -77.09195132010727},
                    "southwest": {"lat": 38.88693937010728, "lng": -77.09465097989272},
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
            "icon_background_color": "#FF9E67",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
            "name": "Heritage Brewing Co.",
            "permanently_closed": True,
            "photos": [
                {
                    "height": 4016,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/102656930953020682056">A Google User</a>'
                    ],
                    "photo_reference": "Aap_uEAP68NlFFYF3s2F6mqRnIcy8aCoXmIB9EyQKZ00n6JMZiRrTvGgec2JPs-8i-A8hHLohOzgnOcyV8qTnNU77Y1BJAKdHx_rWYDcKMIBvyLANh3pBblRUtqBUeu0KBlrLlc0R6vV-gTYE3pR2shQgxCYfm1NT63tWpRTZwV_-TxWkzw",
                    "width": 6016,
                }
            ],
            "place_id": "ChIJFSHTZoa2t4kRSmdiwtSPM9M",
            "plus_code": {
                "compound_code": "VWQ4+8J Arlington, Virginia",
                "global_code": "87C4VWQ4+8J",
            },
            "price_level": 2,
            "rating": 4.4,
            "reference": "ChIJFSHTZoa2t4kRSmdiwtSPM9M",
            "scope": "GOOGLE",
            "types": [
                "cafe",
                "bar",
                "restaurant",
                "food",
                "point_of_interest",
                "store",
                "establishment",
            ],
            "user_ratings_total": 205,
            "vicinity": "1300-1398 N Fillmore St, Arlington",
        },
    ]
    return results
