import os
import io
from openai import OpenAI
from xoxxox.shared import Custom

#---------------------------------------------------------------------------

class SttPrc():

  def __init__(self, config="xoxxox/config_sttoaw_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.nmodel = diccnf["nmodel"]
    self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"] )

  def infere(self, datwav):
    objwav = io.BytesIO(datwav)
    objwav.name = "output.wav"
    objres = self.client.audio.transcriptions.create(
      model=self.nmodel,
      file=objwav
    )
    return objres.text
