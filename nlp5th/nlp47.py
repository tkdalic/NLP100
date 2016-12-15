#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp41 import chunks_list


if __name__ == '__main__':
    for chunks in chunks_list('neko.txt.cabocha'):
        for chunk in chunks:
            for morph in chunk.morphs[:]:
                if morph.pos == '記号':
                    chunk.morphs.remove(morph)

        for chunk in chunks:
            if len(chunk.morphs) > 1 and chunk.morphs[-2].pos1 == 'サ変接続'and chunk.morphs[-1].base == 'を' and chunk.dst != '-1' and '動詞' == chunks[int(chunk.dst)].morphs[0].pos:
                noun = [
                    morph.base for morph in chunk.morphs if morph.pos1 == 'サ変接続'][-1]
                verb = [morph.base for morph in chunks[
                    int(chunk.dst)].morphs if morph.pos == '動詞'][0]
                case = []
                case_chunk = []
                for k in sorted([[chunks[src].morphs[-1].surface, ''.join([morph.surface for morph in chunks[src].morphs])]
                                 for src in chunks[int(chunk.dst)].srcs if len(chunks[src].morphs) > 0 and chunks[src].morphs[-1].pos == '助詞' and chunks[src] != chunk], key=lambda x: (x[0], x[1])):
                    case.append(k[0])
                    case_chunk.append(k[1])

                if len(case) > 0:
                    print('{0}を{1}\t{2}\t{3}'.format(noun, verb, ' '.join(
                        case), ' '.join(case_chunk)))
