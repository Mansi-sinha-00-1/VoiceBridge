from django.shortcuts import render
from .tts_engine import generate_voice
from django.contrib.auth.decorators import login_required
from .models import VoiceHistory
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def voice_home(request):
    audio_url = None

    if request.method == "POST":
        text = request.POST.get("text")
        tone = request.POST.get("tone", "normal")
        language = request.POST.get("language", "en")
        engine = request.POST.get("engine", "gtts")

        if text:
            try:
                audio_path = generate_voice(text, tone, language)
                print("Generated:", audio_path)
            except Exception as e:
                print("VOICE ERROR:", e)
                audio_path = None

            record = VoiceHistory.objects.create(
                user=request.user,
                text=text
            )

            record.audio_file.name = audio_path
            record.save()

            audio_url = record.audio_file.url

    return render(request, "voice.html", {"audio_url": audio_url})


@login_required
def history_view(request):
    records = VoiceHistory.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'records': records})


@login_required
def delete_voice(request, id):
    record = get_object_or_404(VoiceHistory, id=id, user=request.user)

    if record.audio_file:
        record.audio_file.delete()

    record.delete()

    return redirect('history')


@login_required
@csrf_exempt
def save_speech(request):
    if request.method == "POST":
        text = request.POST.get("text")

        if text:
            VoiceHistory.objects.create(
                user=request.user,
                text=text,
                source="speech"
            )

        return JsonResponse({"status": "ok"})
    

@csrf_exempt
def suggest_text(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get("text", "").strip()

        if not text:
            return JsonResponse({"error": "No text"}, status=400)

        base = text.capitalize()

        suggestions = [
            {
                "type": "Direct",
                "text": base
            },
            {
                "type": "Polite",
                "text": f"I would like to request that {base.lower()}"
            },
            {
                "type": "Urgent",
                "text": f"This is urgent. {base}"
            },
            {
                "type": "Expanded",
                "text": f"{base} Please assist as soon as possible."
            },
            {
                "type": "Expanded",
                "text": f"I need {base}. Please Help!"
            },
            {
                "type": "Expanded",
                "text": f"Can you get me {base}?"
            }
        ]

        return JsonResponse({"results": suggestions})