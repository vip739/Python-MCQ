# Python-MCQ
questions = {
    "1. Which of the following is not a result of cell division?":{"correct":"c", "answers":["Growth","Repair","Metabolism","Reproduction"]},
    "2. Mark the incorrect pair.":{"correct":"c", "answers":["Hydra – Budding","Flatworm – Regeneration","Amoeba – Fragmentation","Yeast – Budding"]},
    "3. Which of the following is incorrect for reproduction?":{"correct":"b", "answers":["Unicellular organisms reproduce by cell division","Reproduction is a characteristic of all living organisms","In unicellular organisms, reproduction and growth are linked together","Non-living objects are incapable of reproducing"]},
    "4. Mark the incorrect statement w.r.t. metabolism.":{"correct":"d", "answers":["Microbes exhibit the metabolism","It is the property of all living forms","The metabolic reactions can be demonstrated in-vitro","It is not a defining feature of life forms"]},
    "5. Non-living objects exhibit/show":{"correct":"d", "answers":["Property of self-replication","Evolution","Self-regulating","interactive systems","Reversible growth"]},
    "6. Which statement is false about the growth shown by non-living objects?":{"correct":"d", "answers":["The growth occurs from outside","The growth is reversible","The growth is due to the accumulation of material on the surface","The growth is intrinsic"]},
    "7. Local names of various plants and animals":{"correct":"d", "answers":["Help in recognizing organisms worldwide","Are used universally","Are specific and distinct names","Vary from place to place"]},
    "8. Which of the following is incorrect w.r.t. Binomial nomenclature?":{"correct":"d", "answers":["Biological names are generally in Latin","The first word in a biological name represents the genus","Biological names are printed in italics","The first word of the genus starts with a small letter"]},
    "9. Which of the following is incorrect regarding scientific names?":{"correct":"a", "answers":["These are also known as common names","These ensure that each organism has only one name","These have two components – the generic name and specific epithet","These are universally accepted names"]},
    "10. According to binomial nomenclature, every living organism has":{"correct":"b", "answers":["Two scientific names with single component","One scientific name with two components","Two names, one Latin and other common","One common name with three components"]},
    "11. Which of the following is incorrect w.r.t. Species?":{"correct":"b", "answers":["A group of individual organisms with fundamental similarities","Two different species breed together to produce fertile offsprings","Human beings belong to the species sapiens","Panthera has many specific epithet as tigris, leo and pardus"]},
    "12. Taxonomy deals with":{"correct":"d", "answers":["Development of zoological parks","Study of kinds and diversity of microorganisms only","Evolutionary relationships between organisms","Classification of diverse organisms in different taxa"]},
    "13. Which of the following features are not shown by scientific names of various organism?":{"correct":"c", "answers":["They consists of two components","They have Latin origin","They always have “linn” abbreviation at the end of second component","They are printed in italics"]},
    "14. The correct sequence of taxonomic study of a newly discovered organism is":{"correct":"d", "answers":["First classification then identification, nomenclature and characterization","First identification then classifying organism and then characterizations and nomenclature","First nomenclature then characterization, identification and classification","First characterisation then identification and classification and then nomenclature"]},
    "15. Which one of the following statements given below is not included in universal rules of nomenclature?":{"correct":"b", "answers":["Generic names and specific epithet should be in Latin words","Generic name is immediately followed by name of taxonomists who described it firstly","Generic name must begin with capital letter","All letters of the specific name must be small"]}
    
    
}
anslabels = ['a','b','c','d','e','f','g','h','i','j','k','l']
correct = 0
total = len(questions)
input("\nSECTION - A\n\nObjective Type Questions\nPress ENTER to start!\n")
for k, v in questions.items():
    print(k)
    x = 0
    for ans in v["answers"]:
        print(anslabels[x] + ": " + str(ans))
        x += 1
    answer = input("\nType a, b, c, or d to select your answer. Then press ENTER.\n")
    if(answer == v["correct"]):
        correct += 1
    print("\n")
score = str((correct / total) * 100) + "%"
print("\nQuiz Complete!\nYour score is " + score + " on this quiz.")
print("\n Congratulations for completing the Quiz.")
