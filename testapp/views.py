from django.shortcuts import render

# Question class
class Questions:
    def __init__(self, que, a, b, c, d, correct, explanation):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct
        self.explanation = explanation


def testpaper(request):
    questions = [

        # =====================================================
        #     ALL 16 SCREENSHOT QUESTIONS (RESPIRATION MCQs)
        # =====================================================

        Questions(
            'अंतः श्वसन के समय डायफ्राम —',
            'a. ऊपर उठता है', 'b. नीचे की ओर जाता है', 'c. स्थिर रहता है', 'd. सिकुड़ता नहीं है',
            'b',
            'Inspiration में डायफ्राम सिकुड़कर नीचे की ओर जाता है जिससे फेफड़ों का आयतन बढ़ता है।'
        ),

        Questions(
            'बाह्य श्वसन के समय फेफड़ों का आयतन —',
            'a. बढ़ता है', 'b. घटता है', 'c. स्थिर रहता है', 'd. अत्यधिक बढ़ता है',
            'b',
            'Expiration में डायफ्राम ऊपर उठता है और रिब्स नीचे आती हैं जिससे आयतन कम होता है।'
        ),

        Questions(
            'अंतः श्वसन किस प्रकार की प्रक्रिया है?',
            'a. निष्क्रिय', 'b. सक्रिय', 'c. दोनों', 'd. कोई नहीं',
            'b',
            'Inspiration में डायफ्राम व इंटरकॉस्टल मांसपेशियां सक्रिय रूप से सिकुड़ती हैं।'
        ),

        Questions(
            'बाह्य श्वसन में फेफड़ों का दबाव —',
            'a. कम हो जाता है', 'b. बढ़ जाता है', 'c. बराबर हो जाता है', 'd. शून्य हो जाता है',
            'b',
            'आयतन घटने से दबाव वातावरण से अधिक हो जाता है, इसलिए हवा बाहर निकलती है।'
        ),

        Questions(
            'अंतः श्वसन में रिब्स कैसे चलती हैं?',
            'a. ऊपर व बाहर', 'b. नीचे व भीतर', 'c. ऊपर व भीतर', 'd. नीचे व बाहर',
            'a',
            'Inspiration में external intercostal muscles रिब्स को ऊपर व बाहर उठाती हैं।'
        ),

        Questions(
            'बाह्य श्वसन आमतौर पर —',
            'a. सक्रिय प्रक्रिया', 'b. निष्क्रिय प्रक्रिया', 'c. मस्तिष्क द्वारा नियंत्रित', 'd. मांसपेशियों के बिना',
            'b',
            'Expiration में मांसपेशियां relax होती हैं इसलिए यह निष्क्रिय प्रक्रिया है।'
        ),

        Questions(
            'अंतः श्वसन के समय फेफड़ों का दबाव —',
            'a. अधिक होता है', 'b. कम होता है', 'c. समान रहता है', 'd. अत्यधिक बढ़ जाता है',
            'b',
            'आयतन बढ़ने पर दबाव वातावरण से कम हो जाता है जिससे हवा अंदर जाती है।'
        ),

        Questions(
            'बाह्य श्वसन में डायफ्राम —',
            'a. नीचे जाता है', 'b. ऊपर उठता है', 'c. स्थिर रहता है', 'd. आगे बढ़ता है',
            'b',
            'Expiration में डायफ्राम relax होकर ऊपर उठ जाता है।'
        ),

        Questions(
            'किस अवस्था में हवा फेफड़ों से बाहर जाती है?',
            'a. जब दबाव कम हो', 'b. जब दबाव अधिक हो', 'c. जब आयतन बढ़े', 'd. जब मांसपेशियां सक्रिय हों',
            'b',
            'फेफड़ों का दबाव वातावरण से अधिक होने पर हवा बाहर निकलती है।'
        ),

        Questions(
            'अंतः श्वसन शुरू होने की मुख्य वजह —',
            'a. डायफ्राम ऊपर उठता है', 'b. फेफड़ों का आयतन घटता है',
            'c. फेफड़ों का दबाव वातावरण से कम होता है', 'd. पसलियां नीचे जाती हैं',
            'c',
            'दबाव कम होने पर हवा उच्च दबाव वाले वातावरण से फेफड़ों में प्रवेश करती है।'
        ),

        Questions(
            'अंतः श्वसन का मुख्य उद्देश्य —',
            'a. CO₂ बाहर निकालना', 'b. O₂ अंदर लेना',
            'c. हवा का तापमान घटाना', 'd. फेफड़े सिकोड़ना',
            'b',
            'Inspiration का उद्देश्य शरीर को ऑक्सीजन उपलब्ध कराना है।'
        ),

        Questions(
            'बाह्य श्वसन में कौन-सी गैस बाहर निकलती है?',
            'a. O₂', 'b. CO₂', 'c. N₂', 'd. NH₃',
            'b',
            'CO₂ शरीर में metabolism से बनती है जिसे expiration में बाहर निकाला जाता है।'
        ),

    ]

    # POST request evaluation
    if request.method == "POST":
        score = 0
        detailed_result = []

        for i, q in enumerate(questions, 1):
            selected_option = request.POST.get(f'option{i}')

            if selected_option == q.correct:
                score += 1

            detailed_result.append({
                'question': q.que,
                'options': [q.a, q.b, q.c, q.d],
                'correct': q.correct,
                'selected': selected_option,
                'explanation': q.explanation
            })

        total = len(questions)
        percentage = round((score / total) * 100, 1)

        context = {
            'score': score,
            'total': total,
            'percentage': percentage,
            'result': detailed_result
        }
        return render(request, 'result.html', context)

    return render(request, 'question.html', {'questions': questions})