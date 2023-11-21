#!/usr/bin/env python3

# Author: Karolos Potamianos <karolos.potamianos@cern.ch>

import sys
import csv

oF = open("Endorsers.html", "w")
oFi = open("Endorsers_insert.html", "w")

print("""
<html>
  <head>
    <title>Sustainable HECAP+ Initiative Endorsers</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <meta http-equiv="Permissions-Policy" content="interest-cohort=()">
    <link rel="stylesheet" href="assets/css/main.css" />
  </head>
  <body class="is-preload">
  <!-- Header -->
    <div id="header">
      <!--<span class="logo icon fa-paper-plane"></span>-->
      <h1>Sustainability <br />in <br /> HECAP+</h1>
      <br />
      <p>"Environmental sustainability in basic research: a perspective from HECAP+" <br /> (<a href="https://arxiv.org/abs/2306.02837">Link to arXiv</a>)</p>
      <br /><br />
      <center>

      <div style="width: 1200px;align:center;">
      <p>An initiative of scientists in the High Energy Physics, Cosmology, Astroparticle Physics, and Hadron and Nuclear Physics (HECAP+) communities
      concerned about the climate crisis and advocating for a transition towards
      fairer and more sustainable practices in our fields.</p>
      </div>
      </center>
    </div>

    <!-- Main -->
    <div id="main">
      <div class="box container">
        <h3>Endorsers<br><span>
        (Click <a href="https://indico.cern.ch/e/sustainable-hecap-plus">here</a> to endorse!)
        </span></h3>
""", file=oF)

print("""
  <div>
  Below is the list of persons who have endorsed the initiative. Click <a href="https://indico.cern.ch/e/sustainable-hecap-plus">here</a> to endorse!
  </div>
  <br />
  <div class="endorsers">
""", file=oFi)


with open(sys.argv[1], newline='') as csvfile:
  reader = csv.DictReader(csvfile, delimiter=",")
  data = [ ]
  for r in reader:
    data.append(r)

  sorter = lambda x: (int(x["\ufeffID"]))
  data =  sorted(data, key=sorter)
  #print(data)

  for r in data:
    if r["Registration state"] != "Completed":
      print("Skipping "+r["Name"])
      continue
    if r["Name"].isupper():
      r["Name"] = r["Name"].title()
    if r["Affiliation"].find("UNIV") != -1:
      r["Affiliation"] = r["Affiliation"].title()
    print("<p>"+", ".join([r["Name"],r["Affiliation"]])+"</p>", file=oF)
    print("<p>"+", ".join([r["Name"],r["Affiliation"]])+"</p>", file=oFi)


print("""
      </div>
    </div>
    <!-- Footer -->
    <div id="footer">
      <div class="container medium">
        <p class="copyright">The opinions expressed in this website are those of the astrophysicists and particle physicists concerned about the climate and environmental crises. These opinions do not necessarily reflect those of the author's employer, organization, committee or other group or individual.</p>
        <ul class="copyright">
          <li>&copy; Sustainability in HECAP+ Initiative. All rights reserved.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
        </ul>
      </div>
    </div>
    <!-- Scripts -->
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/browser.min.js"></script>
    <script src="assets/js/breakpoints.min.js"></script>
    <script src="assets/js/util.js"></script>
    <script src="assets/js/main.js"></script>
  </body>
</html>
""", file=oF)

print("""
  </div>
""", file=oFi)

oF.close()
oFi.close()
