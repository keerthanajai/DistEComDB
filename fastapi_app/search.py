from db import get_connection

def search_products(q, limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    count_sql = """
        SELECT COUNT(*)
        FROM products
        WHERE title ILIKE %s OR description ILIKE %s OR brand ILIKE %s
    """
    like = f"%{q}%"
    cur.execute(count_sql, (like, like, like))
    total_count = cur.fetchone()[0]

    sql = """
        SELECT asin, title, brand, category, price, description
        FROM products
        WHERE title ILIKE %s OR description ILIKE %s OR brand ILIKE %s
        ORDER BY title
        LIMIT %s OFFSET %s
    """
    cur.execute(sql, (like, like, like, limit, offset))
    rows = cur.fetchall()

    conn.close()

    results = [
        {
            "asin": r[0],
            "title": r[1],
            "brand": r[2],
            "category": r[3],
            "price": r[4],
            "description": r[5]
        }
        for r in rows
    ]

    return results, total_count


def get_product_detail(asin):
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        SELECT asin, title, brand, category, price, description
        FROM products
        WHERE asin=%s
    """
    cur.execute(sql, (asin,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "asin": row[0],
        "title": row[1],
        "brand": row[2],
        "category": row[3],
        "price": row[4],
        "description": row[5]
    }


def get_reviews(asin):
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        SELECT overall, summary, reviewText
        FROM reviews
        WHERE asin=%s
        LIMIT 20
    """
    cur.execute(sql, (asin,))
    rows = cur.fetchall()
    conn.close()

    return [
        {
            "overall": r[0],
            "summary": r[1],
            "reviewText": r[2]
        }
        for r in rows
    ]
