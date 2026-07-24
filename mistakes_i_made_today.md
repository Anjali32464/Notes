### 11 July 2026

❌ Used:

<form action="/login">

while my route was:

@app.route("/")

Result:
404 Not Found

✅ Fix:
Changed action="/".


❌ Used render_template() after a failed POST.

Result:
Refreshing repeated the POST request, so the error message never disappeared.

✅ Lesson:
Use the POST → Redirect → GET pattern for forms.


❌ i did not specify the type for toggle button that's why it was buggy.

## Buttons inside forms

<button> defaults to type="submit".

So,

<button>Click</button>

is actually treated as

<button type="submit">Click</button>

If a button is only for JavaScript (like Show Password),
always write:

<button type="button">