from gendiff import generate_diff

def test_generate_diff():
    file1path = 'tests/fixtures/file1.json'
    file2path = 'tests/fixtures/file2.json'
    difresult = generate_diff(file1path, file2path)
    correctresult = open('tests/fixtures/result.txt', 'r')
    assert difresult == correctresult.read()
    
    file1path = 'tests/fixtures/file1.yml'
    file2path = 'tests/fixtures/file2.yml'
    difresult = generate_diff(file1path, file2path)
    correctresult = open('tests/fixtures/result.txt', 'r')
    assert difresult == correctresult.read()
    