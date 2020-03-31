import os, re, sys


r = re.compile("<script defer>(.*?)</script>", re.DOTALL)
r_pomo = re.compile("\" *<script defer>(.*?)</script>", re.DOTALL, )
top = sys.argv[1]
for root, _, files in os.walk(top, topdown=True, onerror=None, followlinks=False):
    for f in files:
        if f == "task.yaml":
            print(os.path.join(root, f))
            with open(os.path.join(root, f), "r") as file:
                str = file.read()
            with open(os.path.join(root, f), "w") as file:
                replaced = r.sub("""<script defer>

       bodyHeight = 0;
       function postSize() {
           if (document.body.scrollHeight != bodyHeight) {
               bodyHeight = document.body.scrollHeight;
               window.parent.postMessage({height: document.body.scrollHeight}, "*");
           }
       };
       var target = document.querySelector('body');

       var observer = new MutationObserver(postSize);

       var config = { attributes: true, subtree: true }

       observer.observe(target, config);
       $(document).ready(function(){
           setTimeout(postSize, 0);
       });
       </script>""", str)
                file.seek(0)
                file.write(replaced)

        elif f[-3:] == ".po":
            print(os.path.join(root, f))
            with open(os.path.join(root, f), "r") as file:
                str = file.read()
            with open(os.path.join(root, f), "w") as file:
                replaced = r_pomo.sub(""""   <script defer>\\\\n"
"\\\\n"
"   bodyHeight = 0;\\\\n"
"   function postSize() {\\\\n"
"       if (document.body.scrollHeight != bodyHeight) {\\\\n"
"           bodyHeight = document.body.scrollHeight;\\\\n"
"           window.parent.postMessage({height: document.body.scrollHeight}, \\\\"*\\\\");\\\\n"
"       }\\\\n"
"   };\\\\n"
"   var target = document.querySelector('body');\\\\n"
"\\\\n"
"   var observer = new MutationObserver(postSize);\\\\n"
"\\\\n"
"   var config = { attributes: true, subtree: true }\\\\n"
"\\\\n"
"   observer.observe(target, config);\\\\n"
"   $(document).ready(function(){\\\\n"
"       setTimeout(postSize, 0);\\\\n"
"   });\\\\n"
"   </script>""", str)
                file.seek(0)
                file.write(replaced)

