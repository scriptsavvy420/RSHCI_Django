
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from homepage.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.init_superuser()
        self.init_customer_voice()
        self.init_recruitment_example()
        self.init_column_category()
        self.init_column()
        self.init_knowhow_category()
        self.init_knowhow()
        self.init_career_example()
        self.init_consultation()


    def init_superuser(self):
        try:
            User.objects.all().delete()

            User.objects.create_superuser("akiramurayama", "akira.murayama.dev@gmail.com", "password")
            User.objects.create_superuser("takehiro", "takehiro.nakamaru123works@gmail.com", "password")
            
            print("Superuser created successfully.")
        except Exception as error:
            print(str(error))

    def init_customer_voice(self):
        try:
            CustomerVoice.objects.all().delete()

            for i in range(3):
                CustomerVoice.objects.create(
                    name = '●●',
                    gender = "male" if i % 2 == 0 else "female",
                    age = '30代',
                    job = '不動産営業',
                    description = '転職を迷っている時に相談することで、自分のキャリアや目標を明確にすることができました。また、求人情報や面接対策など、転職活動に必要なサポートが充実していたので、安心して活動することができました。'
                )

            print("CustomerVoice created successfully.")
        except Exception as error:
            print(str(error))


    def init_recruitment_example(self):
        try:
            RecruitmentExample.objects.all().delete()

            for i in range(4):
                RecruitmentExample.objects.create(
                    title = '購買・調達（マネージャー経験者）',
                    company_name = '株式会社日立プラントサービス',
                    business_content = '事業部門の経営課題・調達課題を見出し、その解決に向けて調達プロセスの改革を提案実行していただきます。',
                    position = '調達マネージャー', 
                    location = '東京都豊島区 ',
                    applicant_age = '28～60歳 ',
                    annual_fee = '450万円～650万円',
                    picture = 'default.png'
                )
            print("RecruitmentExample created successfully.")
        except Exception as error:
            print(str(error))

    def init_column_category(self):
        try:
            ColumnCategory.objects.all().delete()

            ColumnCategory.objects.create(
               name = '体験談' 
            )

            print("ColumnCategory created successfully.")
        except Exception as error:
            print(str(error))



    def init_column(self):
        try:
            Column.objects.all().delete()

            Column.objects.create(
                title = 'キャリアコンサルタントが語る転職・就活のリアル',
                category = ColumnCategory.objects.get(name='体験談'),
                published_at = '2024-04-11',
                feature_img = 'default.png',
                content = """皆さん、こんにちは。キャリアコンサルタントの〇〇です。
私は、これまで多くの方の転職・就活を支援してきました。
このブログでは、私の経験に基づいたリアルな情報やアドバイスをお届けすることで、皆さんのキャリアアップにお役に立てたら幸いです。

<h1 class = "_mid--top">転職・就活のリアル</h1>


転職・就活は、人生の中でも大きな節目となる重要なイベントです。
しかし多くの場合、情報不足や不安から、闇雲に活動を始め、結果的に後悔してしまうケースも多く見られます。
そうならないため、私たちキャリアコンサルタントは、そのような方々の不安や疑問を解消し、それぞれの目標に合ったキャリアプランを一緒に考えていきます。

具体的には、以下のようなサポートを提供します。


    1. 自己分析：自分の強みや価値観を理解する
    過去の経験や性格を振り返り、自分自身の強みと価値観を探求しましょう。面談を通して自己分析を深め、性格診断ツールを使用したり、適性検査を行って理想のキャリアを明確にします。

    2. 目標設定：自分が本当に求めるキャリアを考える
    短期的な目標と長期的な目標を設定し、具体的なキャリアプランを策定します。そして、目標達成に向けた具体的な行動計画を一緒に立てていきます。

    3. 情報収集：自分に合った企業や求人情報を探す
    業界情報や企業情報、求人情報などを収集します。非公開求人情報もご紹介できますので、ご自身に合った企業や求人を見つけていきます。

    4. 書類作成：履歴書・職務経歴書などの作成をサポート
    履歴書や職務経歴書といった書類を、効果的に作成するためのアドバイスをご提供。職務経歴書に記載する、具体的な成果や経験について、一緒に考えていきます。
    書類のフォーマットや書き方など、基本的な事項についてもサポートいたします。

    5. 面接対策：面接での受け答えを練習する
    想定される質問への回答を準備し、面接での受け答えを練習する模擬面接を行います。実践的な練習を積むことで受け答えを磨き、内定獲得に近づくことができます。
    また面接でのマナーや態度などについてもアドバイスいたします。

<h1 class = "_mid--footer">最後に</h1>

転職・就活は、決して簡単ではありません。しかし、しっかりと準備をすれば、必ず成功させることができます。
このブログが、皆さんのキャリア形成に役立てていただければ幸いです。"""

            )

            print("Column created successfully.")

        except Exception as error:
            print(str(error)) 

    def init_knowhow_category(self):
        try:
            KnowhowCategory.objects.all().delete()

            KnowhowCategory.objects.create(
                name = "準備・進め方",
                second_name = "転職の「準備・進め方」",
                description = """転職活動の進め方や不安・疑問への対処法など、転職を考えている方に向けて、役に立つ情報をご紹介いたします。""",
                guide_img = "j-guide_img1.png"
            )

            KnowhowCategory.objects.create(
                name = "書類準備・面接対策",
                second_name = "面接に向けて「書類準備・面接対策」",
                description = """自己分析や企業研究が完了したら、応募に必要な書類を準備、併せて面接対策も並行して行います。""",
                guide_img = "j-guide_img2.png"
            )

            KnowhowCategory.objects.create(
                name = "内定・就職",
                second_name = "入社までの流れ「内定・就職」",
                description = """転職活動を成功させた後、いよいよ入社に向けて準備を始めましょう。
                                入社前に準備をしておくことで、入社後のスムーズなスタートと早期の戦力化につながります。""",
                guide_img = "j-guide_img3.png"
            )

            print("KnowhowCategory created successfully")
        except Exception as error:
            print(str(error))

    def init_knowhow(self):
        try:
            Knowhow.objects.all().delete()

            content = """求人情報を見つけたら、履歴書や職務経歴書などの書類を作成して応募をしましょう。
履歴書・職務経歴書は、あなたの強みや経験などを効果的にアピールする武器です。
書類選考突破は、転職活動の最初の関門なので、正しい書き方や魅力的な書類の仕上げ方をしっかりと理解して、対策をする事が大切です。
<h1 class = 'd-main__wrap--content_mid__ttl'>経歴から現在、そして将来にわたって一貫したストーリーをもって書類を作成して面接に臨む</h1>
職務経歴書は過去からの経歴から現在、そして将来にわたって

・その時々でどういったことを考えていたのか
・その後の行動に関して（なぜその会社を選んだのかなど）

一貫したストーリーをもって面接に臨む必要があります。同時に志望理由についてもこのストーリーに従った形で説明する必要があります。
これらの説明をするためには事前準備が必ず必要で、この準備無しでは転職は成功しないと考えています。この面談を通じ、壁打ち相手として皆様をご支援させていただき、一貫したストーリーの準備をするための支援をできればと思います。
この一貫したストーリーの作成が面接対策にも役に立ち、面接官に疑問を生じさせずに説明できるものと自負しています。"""

            Knowhow.objects.create(
                category = KnowhowCategory.objects.get(name="準備・進め方"),
                num = "01",
                title = "面接対策をする",
                content_overview = """後悔しない転職のために、事前準備は欠かせません。
まず、自己分析で強みや弱み、価値観を明確にします。自己分析をしておくことで、応募企業の選定に明確な軸ができ、書類作成や面接もスムーズに行えます。
また求人情報をチェックをして、気になる企業を見つけたらその企業の業界に関する情報を集め、理解を深めることが大切です。""",
                content = content,
                feature_img = "j-prepare_item1.png"
            )
            Knowhow.objects.create(
                category = KnowhowCategory.objects.get(name="準備・進め方"),
                num = "02",
                title = "事前準備をする",
                content_overview = """書類選考を通過したら、次はいよいよ企業との面接になります。
面接は、徹底した事前準備が成功を導く鍵となります。事前準備で行った自己分析や企業研究をもとに、想定質問への回答を準備し、熱意を伝えることが大切です。
また、本番さながらの状況を体験できる、模擬面接を行います。
想定質問への回答練習で、表現力を磨き自信を高めることが出来ます。""",
                content = content,
                feature_img = "j-prepare_item2.png"
            )
            Knowhow.objects.create(
                category = KnowhowCategory.objects.get(name="書類準備・面接対策"),
                num = "01",
                title = "書類の作成を行う",
                content_overview = """書類選考を通過したら、次はいよいよ企業との面接になります。
面接は、徹底した事前準備が成功を導く鍵となります。事前準備で行った自己分析や企業研究をもとに、想定質問への回答を準備し、熱意を伝えることが大切です。
また、本番さながらの状況を体験できる、模擬面接を行います。
想定質問への回答練習で、表現力を磨き自信を高めることが出来ます。""",
                content = content,
                feature_img = "j-interview_item1.png"
            )
            Knowhow.objects.create(
                category = KnowhowCategory.objects.get(name="書類準備・面接対策"),
                num = "02",
                title = "面接対策をする",
                content_overview = """書類選考を通過したら、次はいよいよ企業との面接になります。
面接は、徹底した事前準備が成功を導く鍵となります。事前準備で行った自己分析や企業研究をもとに、想定質問への回答を準備し、熱意を伝えることが大切です。また、本番さながらの状況を体験できる、模擬面接を行います。
想定質問への回答練習で、表現力を磨き自信を高めることが出来ます。""",
                content = content,
                feature_img = "j-interview_item1.png"
            )
            Knowhow.objects.create(
                category = KnowhowCategory.objects.get(name="内定・就職"),
                num = "01",
                title = "内定条件の確認・内定承諾・辞退",
                content_overview = """返事をする前に、内定通知書の内容をよく確認しましょう。勤務地、勤務時間、給与、福利厚生など、入社後に自分がどのような状況になるのかを把握しておくことが重要です。
内定承諾の場合は、企業に連絡をします。内定辞退の場合は、できるだけ早めに連絡し、理由を丁寧に伝えましょう。""",
                content = content,
                feature_img = "j-offer_item1.png"
            )
            Knowhow.objects.create(
                category = KnowhowCategory.objects.get(name="内定・就職"),
                num = "02",
                title = "内定条件の確認・内定承諾・辞退",
                content_overview = """失業中の方なら、入社日は内定先に合わせるのが基本です。
在職中の場合は、上司と相談をして正確な退職日が決定してから内定先企業の方と話し合って入社日を決めます。
退職理由は前向きな内容で伝え、後任者に丁寧に業務を引き継ぎ、最後まで責任を持って仕事を行い、円満な関係を維持することが大切です。""",
                content = content,
                feature_img = "j-offer_item2.png"
            )
            print("Knowhow created successfully")
        except Exception as error:
            print(str(error))

    def init_career_example(self):
        
        try:
            CareerExample.objects.all().delete()
            
            for i in range(3):
                CareerExample.objects.create(
                    title = "営業職から資材調達部門にキャリアチェンジ",
                    gender = "male" if i % 2 == 0 else "female",
                    description = """営業職から資材調達部門へのキャリアチェンジは、一見、異業種への転職のように思えますが、
        実は営業で培ったスキルを活かせる魅力的な選択肢です。
        営業職で培ったコミュニケーション能力や交渉力は、資材調達部門でも非常に重要です。
        また、営業職で培った顧客ニーズを把握する力は、資材調達部門においてもコスト削減や業務効
        率化につながります。"""
                )

            print("CareerExample created successfully")

        except Exception as error:
            print(str(error))

    def init_consultation(self):
        try:
            Consultation.objects.all().delete()

            Consultation.objects.create(
                title = "相談",
                description = "具体的な仕様書作成",
                time = "2024-04-15"
            )
                
            
            print("Consultation created successfully")
        except Exception as error:
            print(str(error))