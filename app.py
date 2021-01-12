# -*- coding: utf-8 -*- 
import loadquestion
from flask import render_template,  Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('loading.html')

@app.route('/hdti')
def hdti():
    return render_template('hdti.html', questions=loadquestion.questions)

@app.route('/result', methods=["POST","GET"])
def result():
    result_listname = 'answersInput'
    result_list = request.form[result_listname]
    result_list = result_list.split(',')
    score_A = score_T = score_R = score_F = score_E = score_C = score_P = score_I = score_gae = score_gi = 0
    score_A = int(result_list[0]) + int(result_list[7])
    score_T = int(result_list[9]) + int(result_list[8])
    score_R = int(result_list[6]) + int(result_list[4]) + int(result_list[2])
    score_F = int(result_list[5]) + int(result_list[3]) + int(result_list[1])
    score_E = int(result_list[10]) + int(result_list[12]) + int(result_list[14])
    score_C = int(result_list[11]) + int(result_list[13]) + int(result_list[15])
    score_P = int(result_list[16]) + int(result_list[18]) + int(result_list[20])
    score_I = int(result_list[17]) + int(result_list[19]) + int(result_list[21])
    score_gae = int(result_list[22]) + int(result_list[24]) + int(result_list[26])
    score_gi  = int(result_list[23]) + int(result_list[25]) + int(result_list[27])

    if score_A >= score_T:
        type_1 = 'T'
    else:
        type_1 = 'A'
    if score_R >= score_F:
        type_2 = 'F'
    else:
        type_2 = 'R'
    if score_E >= score_C:
        type_3 = 'C'
    else:
        type_3 = 'E'
    if score_P >= score_I:
        type_4 = 'I'
    else:
        type_4 = 'P'
    if score_gae >= score_gi:
        type_5 = '기'
    else:
        type_5 = '개'

    type_name = type_1 + type_2 + type_3 + type_4
    if type_name == 'AREI':
        img_src = '../static/img/매기_움짤.gif'
        type_ex = '괴짜 프로그래머'
        explanation = '스스로 개발하는 자기 자신을 보며 뿌듯해하는 전형적인 코딩덕후이다. 자기 주장이 강하고 고집이 센 편이어서 협업 프로젝트를 할 때 혼자 모든 일을 떠맡게 되는 경우가 허다하다. 하지만 힘들어하면서도 꿋꿋이 해내는 편이다. 개발할 때는 머릿속에 생각나는 대로 폭풍처럼 코드를 작성한다. 오류가 자주 발생하지만, 딱 5분만 절망한 뒤 새로 코드를 작성할 자신이 있다!'
    elif type_name == 'AREP':
        img_src = '../static/img/흐규_움짤.gif'
        type_ex = '소심한 아이디어뱅크'
        explanation = '코딩을 사랑한다. 평소 늦어도 오전 8시에 기상하여 오늘 할 일을 계획하고, 그에 맞춰 하루일과를 실천하는 완벽주의자적 성격의 소유자이다. 혼자 방에 틀어박혀 관심있는 주제의 무언가를 뽀짝뽀짝 개발하고 있는 유형이다. 무리에 섞여 여러 사람들과 함께하는 것을 좋아하지만 내향적인 성격으로 인해 처음보는 사람들과 어울리는 것을 어려워한다.'
    elif type_name == 'ARCI':
        img_src = '../static/img/시라용_움짤.gif'
        type_ex = '에디슨형'
        explanation = '머릿속이 엉뚱한 아이디어로 넘쳐나며, 하고 싶은 것이 있으면 꼭 해봐야 직성이 풀리는 유형이다. 그러면서도 대충하는 적이 없어 가끔 과도한 스트레스에 힘들어하지만 곧 힘을 내고 다시 하던 일에 몰두한다. 개발 시에는 프레임워크에 의존하기 보다는 본인이 처음부터 개발하는 것이 더 속 편하다고 생각하며 하나부터 열까지 스스로 코드를 술술 작성해 나간다.'
    elif type_name == 'ARCP':
        img_src = '../static/img/해달이_움짤.gif'
        type_ex = '극한의 효율형'
        explanation = '수시전형, 현역으로 대학교에 입학하였으며 학점은 안 봐도 3점대 후반에서 4점대 사이이다. 아직 프로그래밍에 미숙할 수 있으나 기본적으로 뭐든 열심히 하기 때문에 단기간 내의 실력이 상승하여 일당백이 기대되는 유형이다. 개발하는 것을 좋아하고 코드나 문서 작성 시에도 주석을 하나하나 달아가며 누가 보더라도 쉽게 이해가도록 노력하는, 크게 될 상이니 앞으로 가까이 하도록 하자.'
    elif type_name == 'AFEI':
        img_src = '../static/img/김두근_움짤.gif'
        type_ex = '코딩계 마당발'
        explanation = '일단 질러놓고 생각하는 편이다. 스스로 프로그래밍을 잘하고 싶은 욕구가 커서 이것저것 발 들여놓는 유형이다. 적극적인 모습으로 주변인의 호평이 자자하며, 본인도 기대에 부응하기 위해 항상 노력한다. 겉보기와 달리 예민한 성격이어서 남들의 시선에 신경쓴다. 주말에는 혼자 카페에서 바닐라라떼를 마시며 맥북을 켜고 코딩하는 것이 취미이자 소소한 행복이다.'
    elif type_name == 'AFEP':
        img_src = '../static/img/스팸_움짤.gif'
        type_ex = '지옥에서 온 개발자'
        explanation = '프로그래밍을 배워둬야 할 것 같아서 시작했지만 하다보니 의외로 재미있어서 꾸준히 코딩을 하고 있다. 학구열이 높고 배우고 싶은 것도 많아 자신의 능력치보다 높은 일거리들을 맡는 경우가 잦다. 이 때문에 항상 다크서클을 달고 살지만 그만큼 코딩 실력은 수직 상승 중이다. 스스로 코딩 실력이 부족하다고 생각되더라도 포기하지 말고 이대로만 하면 곧 멋진 프로그래머로 거듭날 유형이다.'
    elif type_name == 'AFCI':
        img_src = '../static/img/아리_움짤.gif'
        type_ex = '내일은 코딩왕'
        explanation = '코딩서적을 찾아 읽으며 차근차근 프로그래밍을 배워나가고 있는 병아리 프로그래머. 잦은 오류 덕에 에러 메시지도 이제는 익숙하다! 코드를 작성할 때는 무계획이 계획이라 믿으며 일단 생각나는 대로 적고 보는 것은 여전하지만, 오랜시간 투자해 완성도 높은 결과물을 척척 내는 모습이 감탄할 만하다. 자신과 비슷한 실력의 동료와 서로 피드백을 주고 받고 경쟁하기도 하면서 성장할 유형이다.'
    elif type_name == 'AFCP':
        img_src = '../static/img/부기_움짤.gif'
        type_ex = '꾸준한 거북이'
        explanation = '항상 마감 1시간 전 결과물을 제출하는 유형이다. 계속 미루다가 그런 것이 아니라 몇차례 수정하다보니 그렇다. 수정1, 수정2, 최종, 진짜 최종, ... 꾸준함과 성실함이 무기인 이러한 성격은 코드를 작성할 때도 빛을 발하며 결과물의 퀄리티는 최상급이다. 하지만 개발할 때는 예민해지고, 주변을 신경쓸 여력이 남아있지 않은 유형이니 건드리지 말도록 하자. 참고로 영타는 빠를 확률 98.88%이다!'
    elif type_name == 'TREI':
        img_src = '../static/img/매기_움짤.gif'
        type_ex = '환상의 효율장인'
        explanation = '학창시절 반장, 부반장 또는 과생활에서 과대를 하거나, 그게 아니더라도 나서서 공지를 올리거나 공모전, 대회를 찾아오는 등 카톡 게시판의 높은 지분을 차지하고 있을 확률이 높다. 모르는게 없어서 궁금한걸 물어보면 친절하게 대답해줄 뿐만 아니라 관련된 자료들도 보내준다. 코드를 쓰더라도 항상 조리 있게, 가독성을 생각해 주석도 꼼꼼히 써서 말 그대로 효율 최적화 인간.'
    elif type_name == 'TREP':
        img_src = '../static/img/사스미_움짤.gif'
        type_ex = '유니콘형'
        explanation = '친구들 사이에서도 항상 중심에 서고, 코딩도 좋아하는 개발자이며, 감정선이 섬세해 주변의 변화를 금새 알아채고 일도 꼼꼼히, 계획을 세워 처리하는 말 그대로 환상의 동물, 유니콘 같은 타입. HDTI중에 가장 희소한 유형이다. 이상적인 개발자가 존재한다면 TREP 같은 사람이 아닐까?'
    elif type_name == 'TRCI':
        img_src = '../static/img/부기_움짤.gif'
        type_ex = '코딩계 스파크'
        explanation = '사람들과 어울리는 것을 좋아하고, 여러 사람들과 어울리다 떠올린 아이디어가 있으면 꼭 실천에 옮겨서 해봐야만 직성이 풀리는 유형. 종종 엉뚱하고 기발한 아이디어 하나 때문에 개발을 시작해 본적이 있을것이다. 하지만 이 유형의 사람들은 아이디어를 완성시키기가 다른 유형보다 어려운 편이다. 왜냐하면 아이디어 하나를 빌드업 하다보면 다른 아이디어가 떠오르기 때문.'
    elif type_name == 'TRCP':
        img_src = '../static/img/시라용_움짤.gif'
        type_ex = '기가지니'
        explanation = '이 유형의 사람들은 종종 인공지능 같다는 소리를 듣는 사람일 수도 있다. 코딩에 탁월한 적성을 가졌으며 컴퓨터친화적이라 간혹 컴퓨터와 대화를 시도하는 특이한 케이스도 보인다. 머릿속으로 이해는 잘 되지만 남에게 설명하기 힘든 경우가 많다. 차라리 코드로 대화하는게 더 편하겠다고 종종 생각해본 적이 있다. 보통 새로운 언어를 배우는데 어려움이 없는 경우가 많다.'
    elif type_name == 'TFEI':
        img_src = '../static/img/김두근_움짤.gif'
        type_ex = '인스타스타'
        explanation = '개발자면서 개발보다 여기저기 돌아다니는 걸 더 많이 하는듯한 유형이다. 사람들과 어울리기를 좋아하고, 열린 마음을 가졌으며 남들이 좋아하는걸 금새 캐치해 다른사람들에게 인기가 많을 타입이다. 일을 잘 벌리기 때문에 옆에서 봤을 때는 저걸 어떻게 다 하나 싶지만 생각보다 모든걸 다 해내고 성과까지 좋은 타입이다. 인스타그램을 보면 항상 수상 관련 내용으로 도배되어있다.'
    elif type_name == 'TFEP':
        img_src = '../static/img/흐규_움짤.gif'
        type_ex = '조별과제의 왕'
        explanation = '조별과제를 하게 된다면 항상 조장을 맡게 되는 유형! 남들이 어설프게 하는 걸 보는 것 보다, 자신이 한발 나서서 지휘하고 역할을 분배하는 것을 좋아한다. 남들에게는 보이지 않는 부분도 캐치해 척척 해결하는 성격. 스스로 일을 무에서 유로 창조해내는 타입이니 너무 일에 치여 지치지 않게 주의하는 것이 중요!'
    elif type_name == 'TFCI':
        img_src = '../static/img/아리_움짤.gif'
        type_ex = '아이디어 뱅크'
        explanation = '머릿속에 금고가 있다면 아이디어로 가득 채워져 있다는 아이디어 뱅크형은 즉흥적이면서도 논리적인 사고방식 덕분에 샘솟는 아이디어를 구체적으로 실현시키기 까지 일사천리다. 이런 유형은 재밌는 것을 추구하며 우선순위에 자신의 즐거운 것을 가장 앞에 두는 타입이 많다. 자신과 비슷한 사람들과 의견을 나누는 것을 좋아하며, 새로운 것도 주저하지 않는다.'
    elif type_name == 'TFCP':
        img_src = '../static/img/해달이_움짤.gif'
        type_ex = '회장의 재목'
        explanation = '태어날 때부터 이마에 ‘회장’ 두 글자를 머리에 새기고 태어났다고 해도 과언이 아닐 정도로, 무리의 장을 맡기에 가장 적합한 성격. 나서기를 좋아하고, 현실적인 판단력과 지도력을 가졌으며 설득력이 좋아 남들을 쉽게 자신의 목표에 따르게 하는 재능을 가졌다. 다만 신경쓸게 많아지면 이것저것 챙기느라 집중력이 떨어질 수 있으니 주의.'

    if type_5 == '개':
        explanation2 = '아이디어를 코드로 풀어내는 것을 선호하는 개발자 유형이다. 문서 작성 시에는 주로 깃허브나 노션을 이용한다. 창의력은 부족하지만 맡은 일만큼은 훌륭하게 해낸다.'
    elif type_5 == '기':
        explanation2 = '아이디어를 말이나 글로 풀어내는 것을 선호하는 기획자 유형이다. 문서 작성 시에는 주로 워드나 한글을 이용한다. 상상력이 풍부하고 타인에게 일을 시키는 것을 잘 하는 편이다.'
    return render_template('result.html', img=img_src, type=type_name, explanation=explanation, type_ex=type_ex)

@app.route('/types')
def types():
    return render_template('types.html')

if __name__ == '__main__':
    app.run() #host='0.0.0.0', port=80)