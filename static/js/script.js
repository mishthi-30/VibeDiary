@app.route("/mood-insights")
def mood_insights():

    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]

    entries = DiaryEntry.query.filter_by(
        username=username
    ).all()

    mood_counts = {}

    for entry in entries:
        if entry.mood:
            mood_counts[entry.mood] = mood_counts.get(entry.mood, 0) + 1

    return render_template(
        "mood_insights.html",
        mood_counts=mood_counts
    )