from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
import cohere
co = cohere.Client('yvcaQfl2917ThuWoHeKVoLVp5W5TZPLSQjnTmcb3') # This is your trial API key
response = co.embed(
  model='large',
  texts=["الزخم هو كمية الحركة التي يمتلكها جسم، ويتأثر بكتلته وسرعته", " يمكن حساب الزخم باستخدام الصيغة الرياضية P = m*v ، حيث P هو الزخم و m و v هي كتلة وسرعة الجسم على التوالي.", "التصادم المرن يحدث عندما تتعرض الكتل المتصادمة لتغييرات في السرعة والاتجاه دون تغيير في الكتلة.", "مثال على التصادم المرن هو اصطدام كرات بلياردو، حيث تتحرك الكرات بسرعة مختلفة وتتغير اتجاهاتها عند التصادم دون تغيير في كتلتها", "التصادم غير المرن يحدث عندما تتعرض الكتل المتصادمة لتغييرات في السرعة والاتجاه وفي الوقت ذاته يتم تغيير في كتلة الأجسام.", "مثال على التصادم غير المرن هو اصطدام سيارتين، حيث يحدث تغيير في الكتلة والشكل الأصلي للسيارات.", "يمكن حساب زخم الجسم الناتج عن التصادم باستخدام الصيغة P = m1v1 + m2v2 ، حيث m1 و v1 هي كتلة وسرعة الجسم الأول و m2 و v2 هي كتلة وسرعة الجسم الثاني.", "الزخم الكلي في نظام مغلق يتحول إلى زخم حركة داخلي للأجسام بعد التصادم.", "قانون الحفاظ من الزخم ينص على أن إجمالي الزخم في نظام مغلق يجب أن يبقى ثابتًا، مما يعني أن زخم الجسم الأول يتحول إلى زخم الجسم الثاني بعد التصادم.", "قانون الحفاظ من الزخم ينطبق على جميع أنواع التصادم", "في التصادم المرن، يحافظ قانون الحفاظ من الزخم على إجمالي الزخم، ولكنه يحافظ أيضًا على طاقة الحركة.", "في التصادم غير المرن، يمكن أن يتحول بعض الزخم إلى طاقة حرارية ويتفاقم فقدان الزخم في حالات التصادم الشديد.", "يمكن استخدام مفهوم الزخم في تفسير سلوك الجسم المتحرك وتحديد كيفية تأثير القوى عليه.", "الزخم يمثل كمية الحركة التي تملكها جسم، وتزيد قيمته بزيادة كتلة الجسم أو سرعته.", "إذا تم تطبيق قوة على جسم لفترة طويلة، فإنه سيكتسب كمية كبيرة من الزخم وبالتالي سيتحرك بسرعة عالية.", "إذا تم تطبيق قوة على جسم لفترة قصيرة، فإن الجسم قد يتحرك بسرعة أقل، لأنه لن يكتسب كمية كبيرة من الزخم.", "يمكن استخدام مفهوم الزخم لتفسير حركة الأجسام في الفضاء الخارجي وحركة الكواكب حول الشمس.", "في تصادم كرة القدم، تتحرك الكرة في الاتجاه المعاكس بعد التصادم، لأن الزخم ينقل من اللاعب الذي قام بتسديد الكرة إلى الكرة نفسها.", "في حادث سيارة، يحدث التصادم غير المرن ويتحول جزء من الزخم إلى طاقة حرارية، مما يؤدي إلى تلف السيارة وإصابة الأشخاص داخلها.", " يمكن استخدام مفهوم الزخم لحساب الطاقة الحركية للجسم باستخدام الصيغة E = 1/2mv^2.", "في حالة تصادم الملاكمين في حلبة الملاكمة، يتحرك كل ملاكم باتجاه معاكس بعد التصادم، ويخسر بعض الز"])
print('Embeddings: {}'.format(response.embeddings))
