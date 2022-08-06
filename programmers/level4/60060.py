def add(head, word, l):
    node = head
    for w in word:
        if w not in node:
            node[w] = {}
        node = node[w]
        if 'len' not in node:
            node['len'] = [l]
        else:
            node['len'].append(l)
    node['end'] = True


def search(head, querie, l):
    count = 0
    node = head
    for q in querie:
        if q == '?':
            return node['len'].count(l)
        elif q not in node:
            break
        node = node[q]
    return count


def solution(words, queries):
    head, head_rev = {}, {}
    wc = []

    for word in words:
        l = len(word)
        add(head, word, l)
        add(head_rev, word[::-1], l)
        wc.append(l)

    answer = []

    for querie in queries:
        l = len(querie)
        if querie[0] == '?':
            if querie[-1] == '?':
                answer.append(wc.count(l))
            else:
                answer.append(search(head_rev, querie[::-1], l))
        else:
            answer.append(search(head, querie, l))

    return answer