# 知识管理-corpus_libs

## 知识管理-多语言表 t_corpus_libs_l

- **表名称：** 知识管理-多语言表
- **表名：** t_corpus_libs_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 知识库名称 | varchar | 72 |  | √ | ' ' | 知识库名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_corpus_libs_l |  | fpkid |
| 2 | idx_corpus_libs_l_0 |  | fid,flocaleid |

---

## 知识管理-主表 t_corpus_libs

- **表名称：** 知识管理-主表
- **表名：** t_corpus_libs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkeepseparator | 保留分割符 | varchar | 50 |  | √ | '0' | 保留分割符 |
| 3 | fchunkstrategy | 分块策略 | varchar | 50 |  | √ | 'auto' | 分块策略,枚举: auto :自动分块 custom :自定义分块 |
| 4 | fpreprocessrule | 预处理规则值 | varchar | 50 |  | √ | ' ' | 预处理规则值,枚举: deleteurl :删除所有URL和电子邮件地址 replacesymbol :替换连续的空格、换行符和制表符 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :禁用 C :启用 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 9 | fproductline | 所属产品 | varchar | 50 |  | √ | ' ' | 所属产品,枚举: S081,S082,S0821,S0822 :精斗云 S041 :星辰 S027,S028,S031,S033,S062 :KIS developer01 :苍穹 |
| 10 | fupdatestrategy | 更新策略 | varchar | 50 |  | √ | ' ' | 更新策略,枚举: day :每天 week :每周 month :每月 |
| 11 | fname | 知识库名称 | varchar | 50 |  | √ | ' ' | 知识库名称 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fseparators | 分隔符 | varchar | 50 |  | √ | ' ' | 分隔符,枚举: \n\n :空两行 \n :换行 。 :中文句号 . :英文句号 ！ :中文叹号 ! :英文叹号 ？ :中文问号 ? :英文问号 |
| 15 | findexmethod | 向量服务接口 | varchar | 50 |  | √ | ' ' | 向量服务接口,枚举: AZURE_EMBEDDING_ADA_002 :GPT-4 BAIDU_EMBEDDING_V1 :百度 KINGDEE_EMBEDDING :金蝶自研 |
| 16 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 17 | fknlcount | 知识数量 | int4 | 32 |  | √ | 0 | 知识数量 |
| 18 | fdatasourceurl | 数据源地址 | varchar | 50 |  | √ | ' ' | 数据源地址 |
| 19 | ftype | 知识库类型 | int8 | 64 |  | √ | 0 | 语料知识库类型 corpus_lib_type |
| 20 | fchunksize | 分块长度 | int8 | 64 |  |  | null | 分块长度 |
| 21 | fcloudid | 所属云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 22 | fupdatetime | 知识库更新时间 | int8 | 64 |  | √ | 0 | 知识库更新时间 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fdatasource | 数据来源 | varchar | 50 |  | √ | 'community' | 数据来源,枚举: community :苍穹社区知识 local :本地知识 |
| 25 | fchunkoverlap | 分块重复长度 | int8 | 64 |  | √ | 0 | 分块重复长度 |
| 26 | fnumber | 知识库编号 | varchar | 30 |  | √ | ' ' | 知识库编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_corpus_libs |  | fnumber |
| 2 | pk_t_corpus_libs |  | fid |
