import libcst
import libcst.matchers as m


if __name__ == '__main__':
    print(m.matches(libcst.Name('print'), m.Name('import')))
    print(m.matches(libcst.Name('import'), m.Name('import')))
