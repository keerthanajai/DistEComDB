from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

from search import search_products, get_product_detail, get_reviews

app = FastAPI()
templates = Jinja2Templates(directory="templates")

ITEMS_PER_PAGE = 20

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "query": "",
        "results": [],
        "page": 1,
        "has_next": False
    })

@app.get("/search", response_class=HTMLResponse)
def ui_search(request: Request, q: str = "", page: int = 1):
    offset = (page - 1) * ITEMS_PER_PAGE
    results, total_count = search_products(q, ITEMS_PER_PAGE, offset)

    has_next = offset + ITEMS_PER_PAGE < total_count

    return templates.TemplateResponse("index.html", {
        "request": request,
        "query": q,
        "results": results,
        "page": page,
        "has_next": has_next
    })

@app.get("/product/{asin}", response_class=HTMLResponse)
def product_page(request: Request, asin: str):
    product = get_product_detail(asin)
    reviews = get_reviews(asin)

    return templates.TemplateResponse("product.html", {
        "request": request,
        "product": product,
        "reviews": reviews
    })
