import os  # for the cwd 
import re
import json
import requests
import leetcode.auth


def urlify(s):
    '''
    Removes special characters and replaces the white space with a dash

    :param s: string
    :return: string
    '''

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", ' ', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s


def make_directory(path):
    '''
    :param path: String
    :return: NULL
    '''
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


def create_file(title, code, language='Python', dir="./leet_code_solutions/", check_file_exists=0):
    '''
    Creates the file with the name of title, and inserts the code inside of it

    :param title: string
    :param code:  string
    :return:
    '''

    title = urlify(title)
    extention_of = {"cpp": ".cpp",
                    "java": ".java",
                    "python": ".py",
                    "python3": ".py",
                    "c": ".c",
                    "csharp": ".cs",
                    "javascript": ".js",
                    "ruby": ".ruby",
                    "swift": ".swift",
                    "golang": ".go",
                    "scala": ".scala",
                    "kotlin": ".kt",
                    "rust": ".rs",
                    "mysql": ".sql",
                    "bash": ".sh"}
    # if language == "Cpp":
    #     extension = ".cpp"
    # elif language == "Java":
    #     extension = ".java"
    # elif language == "Python":
    #     extension = ".py"
    # elif language == "Python3":
    #     extension = ".py"
    # elif language == "C":
    #     extension = ".c"
    # elif language == "C#":
    #     extension = ".cs"
    # elif language == "JavaScript":
    #     extension = ".js"
    # elif language == "Ruby":
    #     extension = ".rb"
    # elif language == "Swift":
    #     extension = ".swift"
    # else:
    #     extension = ".go"

    for l_key in extention_of:
        temp_file_name = dir + title + extention_of[l_key]
        if check_file_exists and os.path.isfile(temp_file_name):
            return 1
    if check_file_exists:
        return 0

    extension = extention_of.get(language.lower(), '.py')
    title = dir + title + extension

    file = open(title, 'w')
    file.write(code)
    file.close()


def fetch_the_solution_content(solution_id):
    url = 'https://leetcode.com/graphql/'
    # solution_id = 3702460
    ob = {
        "query": "\n    query communitySolution($topicId: Int!) {\n  topic(id: $topicId) {\n    id\n  post {\n      id\n   content\n            isOwnPost\n    }\n  }\n}\n    ",
        "variables": {
            "topicId": solution_id
        },
        "operationName": "communitySolution"
    }
    response = requests.post(url = url, json = ob)
    try:
        if response.status_code != 200:
            raise Exception('200 not returned')
        response_object = json.loads(response.content)
        content_solution = response_object['data']['topic']['post']['content']
    except Exception as e:
        print('Error in fetching the solution', e)
        content_solution = ''
    return content_solution


def fetch_leetcode_api_instance(LEETCODE_SESSION, referer="https://leetcode.com/graphql/"):
    # Experimental: Or CSRF token can be obtained automatically
    csrf_token = leetcode.auth.get_csrf_cookie(LEETCODE_SESSION)
    configuration = leetcode.Configuration()
    configuration.api_key["x-csrftoken"] = csrf_token
    configuration.api_key["csrftoken"] = csrf_token
    configuration.api_key["LEETCODE_SESSION"] = LEETCODE_SESSION
    configuration.api_key["Referer"] = referer
    configuration.debug = False
    api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))
    return api_instance


def update_code_editor_solution_using_leetcode_api(LEETCODE_SESSION, solution_string, questionId, language_id=11):
    api_instance = fetch_leetcode_api_instance(LEETCODE_SESSION, referer = "https://leetcode.com/graphql/")

    ob_for_append_code = {
        "query": "\n    mutation updateSyncedCode($code: String!, $lang: Int!, $questionId: Int!) {\n  updateSyncedCode(code: $code, lang: $lang, questionId: $questionId) {\n    ok\n  }\n}\n    ",
        "variables": {
            "code": solution_string,
            "lang": language_id,
            "questionId": questionId
        },
        "operationName": "updateSyncedCode"
    }

    # error in below code
    # graphql_request = leetcode.GraphqlQuery(
    #     query = """
    #                 mutation
    #                     updateSyncedCode($code: String!, $lang: Int!, $questionId: Int!) {
    #                         updateSyncedCode(code: $code, lang: $lang, questionId: $questionId) {
    #                         ok
    #                     }
    #                     }
    #                 """,
    #     variables = leetcode.GraphqlQueryVariables(coder = "run", lang = 11, questionId = 1723),
    #     operation_name = "updateSyncedCode",
    # )
    print('Updating code in the editor',
          api_instance.graphql_post(body = ob_for_append_code))  # Both returns same response.


def get_logged_in_confirmation_using_leetcode_api(LEETCODE_SESSION):
    api_instance = fetch_leetcode_api_instance(LEETCODE_SESSION, referer = "https://leetcode.com")

    graphql_request = leetcode.GraphqlQuery(
        query = """
                     {
                       user {
                            username
                            isCurrentUserPremium
                         }
                     }
                     """,
        variables = leetcode.GraphqlQueryVariables(),
    )
    using_payload = {'operation_name': None,
                     'query': '\n'
                              '     {\n'
                              '       user {\n'
                              '            username\n'
                              '            isCurrentUserPremium\n'
                              '         }\n'
                              '     }\n'
                              '     ',
                     'variables': {}}
    print(api_instance.graphql_post(body = graphql_request))
    print(api_instance.graphql_post(body = using_payload))  # Both returns same response.


def get_question_id_using_leetcode_api(LEETCODE_SESSION, prob_title):
    api_instance = fetch_leetcode_api_instance(LEETCODE_SESSION, referer = "https://leetcode.com/graphql/")

    ob_for_fetch_questionId = {
        "query": "\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n  }\n}\n    ",
        "variables": {
            "titleSlug": prob_title
        },
        "operationName": "questionTitle"
    }
    print('Fetch questionId using leetcode.auth')
    response = api_instance.graphql_post(body = ob_for_fetch_questionId)
    questionId = response.data.question.question_id
    return int(questionId)


def get_language_id_using_leetocde_api(LEETCODE_SESSION, choosen_language):
    try:
        api_instance = fetch_leetcode_api_instance(LEETCODE_SESSION, referer = "https://leetcode.com/graphql/")
        ob_for_fetch_language_id = {
            "query": "\n    query languageList {\n  languageList {\n    id\n    name\n  }\n}\n    ",
            "variables": {},
            "operationName": "languageList"
        }
        print('Fetch Language Id to Name mapping using requests')
        resp = requests.post(url = 'https://leetcode.com/graphql/', json = ob_for_fetch_language_id)
        data = resp.json()
        for lang in data['data']['languageList']:
            if lang['name'] == choosen_language.lower():
                return lang['id']

        # response = api_instance.graphql_post(body = ob_for_fetch_language_id)
        # questionId = response.data.question.question_id
        return 0  # C++ language_id
    except Exception as e:
        print('E in get_language_id_using_leetocde_api', e)
    return 11  # Python


def submit_code_solution_using_leetcode_api(LEETCODE_SESSION, submissionId):
    api_instance = fetch_leetcode_api_instance(LEETCODE_SESSION, referer = "https://leetcode.com/graphql/")

    submit_code_json = {
        "query": "\n    query submitModalInfo($submissionId: ID!) {\n  validTimeTravelTicketCount\n  dccSubmissionPolling(submissionId: $submissionId) {\n    keepPolling\n    dccSubmissionInfo {\n      showCompleteModal\n      showTttModal\n      discussLink\n      dailyChallengeMedal {\n        name\n        shortName\n        config {\n          iconGif\n        }\n      }\n      streakCounter {\n        streakCount\n        daysSkipped\n        currentDayCompleted\n        hasCompletedChallenge\n      }\n    }\n  }\n  showAnnualModalOnQd {\n    name\n    config {\n      iconGif\n    }\n  }\n}\n    ",
        "variables": {
            "submissionId": submissionId
        },
        "operationName": "submitModalInfo"
    }
    print('Submit code in the editor',
          api_instance.graphql_post(body = submit_code_json))
