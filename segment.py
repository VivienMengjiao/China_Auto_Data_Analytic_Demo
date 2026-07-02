
import jieba
import pandas as pd
import os
os.chdir('S:/Private/Job/CH_Auto')


def create_custom_dict(output_path='user_dict.txt'):

    custom_dict = [
        '森林人 100 n',
        '野帝 10 n',
        'XC60 10 n',
        '大众 100 n',
        '斯柯达 50 n',
        '宝马 50 n',
        '奔驰 50 n',
        '奥迪 50 n',
        '丰田 50 n',
        '特斯拉 10 n',
        '比亚迪 10 n',
        '蔚来 10 n',
    ]

    with open(output_path, 'w', encoding='utf-8') as f:
        for line in custom_dict:
            f.write(line + '\n')

    print(f"✓ 自定义词典已保存: {output_path} ({len(custom_dict)} 条词)")
    return output_path

df = pd.read_csv('train.csv', encoding='utf-8')


jieba.load_userdict('user_dict.txt')


df['text_seg'] = df['content'].apply(lambda x: ' '.join(jieba.cut(x)))

df.to_csv('train_segmented.csv', index=False, encoding='utf-8')
print("✓ 完成！已保存到 train_segmented.csv")