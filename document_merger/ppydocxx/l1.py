import docx

doc1 = docx.Document('doc1.docx')
doc2 = docx.Document('doc2.docx')

doc1_elm = doc1._document_part._element
doc2_elm = doc2._document_part._element

for child_elm in doc2_elm:
    doc1_elm.append(child_elm)

doc1.save('doc2_appended_to_doc1.docx')