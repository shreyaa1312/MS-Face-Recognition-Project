import json
import os
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.operations import FaceListOperations
from msrest.authentication import CognitiveServicesCredentials
from util import check_face_in_facelist

# Adds new persons in known-persons-facelist


def addface(detail, image):
    credential = json.load(open('Authentication.json'))
    face_client = FaceClient(
        credential['ENDPOINT'], CognitiveServicesCredentials(credential['API_KEY']))
    face_list_id = "known-persons-facelist"
    img_source = open('./img.jpeg', 'rb')

    try:
        face_client.face_list.create(
            face_list_id=face_list_id, recognition_model='recognition_04', name=face_list_id)
    except:
        pass

    similar_faces = check_face_in_facelist(face_client)

    if not similar_faces:
        try:
            face_client.face_list.add_face_from_stream(face_list_id=face_list_id,
                                                       image=img_source,
                                                       detection_model='detection_01',
                                                       user_data=detail)
        except:
            message = "No Face Detected"
        else:
            message = "Details added successfully."
    else:
        message = "Face already exists"

    img_source.close()
    os.remove('./img.jpeg')
    return message
