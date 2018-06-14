from django.shortcuts import render
from questions.models import Question
from django.http import HttpResponse
import os
from astrotest.settings import MEDIA_ROOT
from subprocess import call
from tempfile import mkdtemp, mkstemp, TemporaryDirectory
from django.template.loader import render_to_string

# Create your views here.

def exam(request):
    master_question_list = Question.objects.all()

    version = "THE_VERSION"
    course = "THE COURSE"

    with TemporaryDirectory() as tmp_dir:
        texfile, texfilename = mkstemp(dir=tmp_dir)

        os.write(
                texfile,
                str(render_to_string(
                    'tex/exam.tex',
                    {"master_question_list":master_question_list,
                    "version":version,
                    "course":course,
                    }) + "").encode(),
                )
        os.close(texfile)

        call(['pdflatex', '-output-directory', tmp_dir, texfilename])

        #dest_folder = MEDIA_ROOT
        #os.rename(texfilename + '.pdf', dest_folder + '/NEW.pdf')

        #os.remove(texfilename)
        #os.remove(texfilename + '.aux')
        #os.remove(texfilename + '.log')

        with open(os.path.join(texfilename + '.pdf'), 'rb') as f:
            pdf = f.read()
        r = HttpResponse(content_type='application/pdf')
        r.write(pdf)
    return r

    #return os.path.join(dest_folder, 'NEW.pdf')
