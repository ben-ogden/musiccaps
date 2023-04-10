#
# UI Helpers for MusicCaps Search App
#
import streamlit as st


def html(h):
    st.write(h, unsafe_allow_html=True)


def bg():
    html(
        f"""
        <style>
        .stApp {{
            position: absolute;
            inset: 0;
            background: url(https://production-console.firebaseapp.com/assets/bg.svg) no-repeat center center;
            z-index: 1;
        }}
        </style>
        """
    )


def video_card(ytid, start_s, caption, score):
    html(
        f"""
        <div style="margin-bottom: 1rem; background-color: rgba(255,255,255,0.7); padding: 1rem; 
            border-radius: 4px; box-shadow: 0px 0px 14px rgba(0, 0, 0, 0.25);">
            <div style="float:right; width:50%">
                <p>{caption}</p>
                <p style="vertical-align: bottom; color:#aaa">Score: {score}</p>
            </div>
            <iframe style="vertical-align: bottom; border-radius: 4px;" width="300" height="300"
                src="http://www.youtube.com/embed/{ytid}?start={start_s}"></iframe>
        </div>
    """
    )


def title():
    html(
        """
        <div style="float:right; margin-top:20px">
            <div style="color:#000; font-size: 80%;">Powered by</div>
            <img alt="Pinecone" src="https://www.pinecone.io/images/pinecone-logo.svg">
        </div>
        <div style="font-family: 'MediumLLWeb', sans-serif;">
            <div style="color:#030080; font-weight: bold; font-size: 2.4em; padding:0px;">MusicCaps</div>
            <div style="color:#1c17ff; padding:0px; margin-top:-10px">Semantic Seach</div>
        </div>
        """
    )


def footer():
    html(
        """
        <div style="margin-bottom: 1rem; background-color: rgba(255,255,255,0.7); padding: 1rem;
            border-radius: 4px; box-shadow: 0px 0px 14px rgba(0, 0, 0, 0.25);">

        <p>The MusicCaps dataset contains 5,521 music examples, each of which is labeled with 
        a free text caption written by musicians. The caption consists of multiple sentences
        about the music, e.g.,</p>
        
        <p><em>"A low sounding male voice is rapping over a fast paced drums playing a reggaeton beat
        along with a bass. Something like a guitar is playing the melody along. This recording
        is of poor audio-quality. In the background a laughter can be noticed. This song may 
        be playing in a bar."</em></p>

        <p>The text is solely focused on describing how the music sounds, not the metadata like 
        the artist name. The labeled examples are 10s music clips from the <a href="https://research.google.com/audioset/">AudioSet</a> dataset.</p>

        </div>

        <p style="font-size: 80%">
        <a href="https://huggingface.co/datasets/google/MusicCaps">MusicCaps Dataset</a> from Google AI</a> <br/>
        <a href="http://arxiv.org/abs/2301.11325">MusicLM: Generating Music From Text</a> (DOI: 10.48550/arXiv.2301.11325)  <br/>
        Portions adapted from James Briggs' <a href="https://github.com/jamescalam/ask-youtube">Ask Youtube<a/>
        <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
        <br />
        <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
            <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" />
        </a>
        </p>
        
    """
    )


def svg_logo():
    html(
        """
        <div style="margin: 1rem">
        <div style="color:#f2f2f2; font-size: 60%;">Powered by</div>
        <svg height="30" viewBox="0 0 142 30" width="142" xmlns="http://www.w3.org/2000/svg">
          <g fill="none" fill-rule="evenodd" transform="translate(0 1)">
            <path d="m31.85 6.42h7.31c5.29 0 6.63 3.19 6.63 5.79s-1.37 5.79-6.63 5.79h-4.51v9.12h-2.8zm2.8 9.12h3.69c2.22 0 4.44-.52 4.44-3.33s-2.22-3.33-4.44-3.33h-3.69z" fill="#fff" fill-rule="nonzero"></path>
            <path d="m49.45 6.32c1.0566415.00069523 1.9162854.85093806 1.9285991 1.90750808.0123137 1.05657001-.8272812 1.92661652-1.8836195 1.95193732-1.0563383.0253207-1.9366556-.80349887-1.9749796-1.8594454-.016192-.52310454.1796529-1.03056108.5430717-1.40716082.3634187-.37659973.8635789-.59039201 1.3869283-.59283918zm-1.29 6.94h2.6v13.86h-2.6z" fill="#fff" fill-rule="nonzero"></path>
            <path d="m53.77 13.26h2.63v2.14h.06c.9168846-1.6356258 2.6883168-2.602921 4.56-2.49 2.69 0 5 1.61 5 5.29v8.92h-2.6v-8.18c0-2.61-1.49-3.57-3.16-3.57-2.19 0-3.86 1.4-3.86 4.62v7.13h-2.63z" fill="#fff" fill-rule="nonzero"></path>
            <path d="m70.84 21.16c0 2.42 2.25 4 4.68 4 1.5243479-.0443266 2.9360567-.8133365 3.8-2.07l2 1.52c-1.4522206 1.9156-3.7595042 2.9868388-6.16 2.86-4.39 0-7.13-3.15-7.13-7.28-.0775176-1.9273249.6436889-3.8012232 1.9933444-5.1792726s3.2081347-2.1381078 5.1366556-2.1007274c4.88 0 6.75 3.74 6.75 7.31v.94zm8.32-2.11c-.06-2.31-1.35-4-4-4-2.2663131-.0154421-4.1517857 1.7384859-4.3 4z" fill="#fff" fill-rule="nonzero"></path>
            <path d="m93.85 16.95c-.8561703-1.0121496-2.1246901-1.5820643-3.45-1.55-2.86 0-4.33 2.31-4.33 4.91-.0720213 1.2298113.3689911 2.434453 1.2180219 3.3270725.8490309.8926196 2.0301037 1.3933396 3.2619781 1.3829275 1.3020714.0436331 2.5480605-.5311536 3.36-1.55l1.87 1.85c-1.3606632 1.4403962-3.2804967 2.2178192-5.26 2.13-1.9459184.0979421-3.842755-.6301819-5.2233223-2.0050365-1.3805672-1.3748546-2.1165503-3.2686557-2.0266777-5.2149635-.0879343-1.9538421.6455561-3.8553698 2.0228188-5.2440306 1.3772627-1.3886607 3.2726808-2.1377979 5.2271812-2.0659694 2.0024423-.0508447 3.9336759.7441556 5.32 2.19z" fill="#fff" fill-rule="nonzero"></path>
            <path d="m103.56 12.91c4.004347.0660147 7.203394 3.3540316 7.159564 7.3586833s-3.314073 7.2218644-7.318906 7.2003299c-4.0048334-.0217516-7.2401139-3.2741217-7.2406581-7.2790132-.0002651-1.9517484.7831834-3.8218653 2.1745128-5.1906327 1.3913295-1.3687673 3.2740043-2.121539 5.2254873-2.0893673zm0 12.11c2.8 0 4.56-2 4.56-4.83s-1.76-4.82-4.56-4.82-4.57 2-4.57 4.82 1.76 4.83 4.57 4.83z" fill="#fff" fill-rule="nonzero"></path>
            <path d="m113.06 13.26h2.63v2.14c.920247-1.6372339 2.695354-2.6044142 4.57-2.49 2.69 0 5 1.61 5 5.29v8.92h-2.63v-8.18c0-2.61-1.49-3.57-3.15-3.57-2.2 0-3.86 1.4-3.86 4.62v7.13h-2.56z" fill="#fff" fill-rule="nonzero"></path>
            <path d="m130.16 21.16c0 2.42 2.25 4 4.68 4 1.523051-.0491116 2.93274-.8170213 3.8-2.07l2 1.52c-1.453513 1.8996886-3.751504 2.9588601-6.14 2.83-4.38 0-7.13-3.15-7.13-7.28-.07791-1.9326457.647326-3.8113902 2.00361-5.1904053 1.356284-1.3790152 3.222716-2.1353751 5.15639-2.0895947 4.89 0 6.76 3.74 6.76 7.31v.94zm8.3-2.11c-.06-2.31-1.34-4-4-4-2.268267-.0204704-4.15666 1.7361737-4.3 4z" fill="#fff" fill-rule="nonzero"></path>
            <path d="m14.58 5.24.7-3.89" stroke="#fff" stroke-linecap="square" stroke-width="1.77"></path>
            <path d="m17.8 3.86-2.44-2.98-3.32 1.94" stroke="#fff" stroke-linecap="square" stroke-linejoin="round" stroke-width="1.77"></path>
            <path d="m11.66 21.84.68-3.89" stroke="#fff" stroke-linecap="square" stroke-width="1.77"></path>
            <path d="m14.88 20.45-2.46-2.97-3.31 1.95" stroke="#fff" stroke-linecap="square" stroke-linejoin="round" stroke-width="1.77"></path>
            <path d="m13.07 13.82.68-3.89" stroke="#fff" stroke-linecap="square" stroke-width="1.77"></path>
            <path d="m16.29 12.43-2.45-2.96-3.31 1.94" stroke="#fff" stroke-linecap="square" stroke-linejoin="round" stroke-width="1.77"></path>
            <circle cx="10.77" cy="26.85" fill="#fff" fill-rule="nonzero" r="1.63"></circle>
            <g stroke="#fff" stroke-linecap="square">
              <path d="m6.15 21.5-2.99 2.08" stroke-width="1.68"></path>
              <path d="m6.33 24.87-3.53-1.04.26-3.67" stroke-linejoin="round" stroke-width="1.68"></path>
              <path d="m17.01 23.45 2.08 3" stroke-width="1.68"></path>
              <path d="m15.67 26.55 3.67.25 1.04-3.51" stroke-linejoin="round" stroke-width="1.68"></path>
              <path d="m20.42 17.36 3.66.66" stroke-width="1.72"></path>
              <path d="m21.68 20.57 2.84-2.47-1.79-3.29" stroke-linejoin="round" stroke-width="1.72"></path>
              <path d="m19.35 10.1 3.26-1.8" stroke-width="1.72"></path>
              <path d="m19.53 6.65 3.47 1.44-.65 3.69" stroke-linejoin="round" stroke-width="1.72"></path>
              <path d="m4.97 14.64-3.67-.64" stroke-width="1.72"></path>
              <path d="m2.68 17.22-1.82-3.29 2.81-2.48" stroke-linejoin="round" stroke-width="1.72"></path>
              <path d="m8.45 8.17-2.45-2.8" stroke-width="1.72"></path>
              <path d="m9.46 4.88-3.75.16-.66 3.69" stroke-linejoin="round" stroke-width="1.72"></path>
            </g>
          </g>
        </svg>
        </div>
        """
    )
