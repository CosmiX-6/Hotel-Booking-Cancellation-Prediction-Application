from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from server.models.models import ProcessSchema
from server.predictor.booking_predictor import predict_booking
import numpy as np

templates = Jinja2Templates('server/templates')

router = APIRouter()

# Loads the main page


@router.get("/booking_cancellation_predictor", include_in_schema=False)
def search_tweet(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

# Process the form data


@router.post("/booking_cancellation_predictor")
def search_tweet(request: Request,
                 lead_time: float = Form(...),
                 adult: int = Form(...),
                 children: int = Form(...),
                 baby: int = Form(...),
                 agent: int = Form(...),
                 repeated_guest: str = Form(...),
                 cancellation: str = Form(...),
                 pbnc: str = Form(...),
                 com_code: int = Form(...),
                 parking: str = Form(...),
                 tsr: int = Form(...),
                 adr: float = Form(...),
                 hotel_type: str = Form(...),
                 month: str = Form(...),
                 ms: str = Form(...),
                 dc: str = Form(...),
                 dt: str = Form(...),
                 ct: str = Form(...),
                 room_change: str = Form(...),
                 ):
    data_dict = {
        "lead_time": lead_time,
        "adults": adult,
        "children": children,
        "babies": baby,
        "agent": agent,
        "is_repeated_guest": 0 if repeated_guest == "no" else 1,
        "previous_cancellations": 0 if cancellation == "no" else 1,
        "previous_bookings_not_canceled": 0 if pbnc == "no" else 1,
        "company": com_code,
        "required_car_parking_spaces": 0 if parking == "no" else 1,
        "total_of_special_requests": tsr,
        "adr": adr,
        "hotel_Resort Hotel": 0 if hotel_type == "City" else 1,
        "arrival_date_month_August": 1 if month == "aug" else 0,
        "arrival_date_month_December": 1 if month == "dec" else 0,
        "arrival_date_month_February": 1 if month == "feb" else 0,
        "arrival_date_month_January": 1 if month == "jan" else 0,
        "arrival_date_month_July": 1 if month == "jul" else 0,
        "arrival_date_month_June": 1 if month == "jun" else 0,
        "arrival_date_month_March": 1 if month == "mar" else 0,
        "arrival_date_month_May": 1 if month == "may" else 0,
        "arrival_date_month_November": 1 if month == "nov" else 0,
        "arrival_date_month_October": 1 if month == "oct" else 0,
        "arrival_date_month_September": 1 if month == "sep" else 0,
        "market_segment_Complementary": 1 if ms == "com" else 0,
        "market_segment_Corporate": 1 if ms == "cor" else 0,
        "market_segment_Direct": 1 if ms == "dir" else 0,
        "market_segment_Groups": 1 if ms == "grp" else 0,
        "market_segment_Offline TA/TO": 1 if ms == "off" else 0,
        "market_segment_Online TA": 1 if ms == "on" else 0,
        "distribution_channel_Direct": 1 if dc == "dir" else 0,
        "distribution_channel_GDS": 1 if dc == "gds" else 0,
        "distribution_channel_TA/TO": 1 if dc == "tato" else 0,
        "distribution_channel_Undefined": 1 if dc == "undef" else 0,
        "deposit_type_Non Refund": 1 if dt == "nref" else 0,
        "deposit_type_Refundable": 1 if dt == "ref" else 0,
        "customer_type_Group": 1 if ct == "grp" else 0,
        "customer_type_Transient": 1 if ct == "trn" else 0,
        "customer_type_Transient-Party": 1 if ct == "trnp" else 0,
        "room_change_True": 1 if room_change == "yes" else 0,
    }
    print(predict_booking(np.asarray(list(data_dict.values())).reshape(1, -1)))
