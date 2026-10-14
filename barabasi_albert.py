import random

def build_ba(n_new=1000, m0=3, m=2, seed=42):
    random.seed(seed)
    # стартовая полная сеть из m0 узлов
    edges = [(i, j) for i in range(m0) for j in range(i + 1, m0)]
    degree = {i: m0 - 1 for i in range(m0)}
    # список, где каждый узел записан столько раз, какова его степень:
    # случайный выбор из него = выбор пропорционально степени
    pool = [v for e in edges for v in e]
    for new in range(m0, m0 + n_new):
        targets = set()
        while len(targets) < m:          # m разных старых узлов
            targets.add(random.choice(pool))
        degree[new] = 0
        for t in targets:
            edges.append((new, t))
            degree[new] += 1
            degree[t] += 1
            pool += [new, t]
    return degree, edges

if __name__ == '__main__':
    degree, edges = build_ba()
    print('Узлов:', len(degree), 'рёбер:', len(edges))
    top = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:5]
    print('Топ-5 хабов (узел: степень):')
    for node, deg in top:
        print(f'  узел {node}: {deg}')
    print('Средняя степень:', round(2 * len(edges) / len(degree), 2))
