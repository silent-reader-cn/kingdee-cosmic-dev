# 知识库设置-bos_knl_kmconfig

## 知识库设置-主表 t_corpus_libs

- **表名称：** 知识库设置-主表
- **表名：** t_corpus_libs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskepseprator | 保留分割符 | varchar | 50 |  | √ | ' ' | 保留分割符 |
| 3 | fcleantype | 清洗策略 | varchar | 50 |  | √ | ' ' | 清洗策略,枚举: W :水印 I :目录 |
| 4 | fkeepseparator | 保留分割符 | varchar | 50 |  | √ | '0' | 保留分割符 |
| 5 | fenableocr | 视觉识别服务 | bpchar | 1 |  | √ | '0' | 视觉识别服务 |
| 6 | fpkepseprator | 保留分割符 | varchar | 50 |  | √ | ' ' | 保留分割符 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fes | 全文存储 | varchar | 50 |  | √ | '0' | 全文存储 |
| 9 | fname | 知识库名称 | varchar | 50 |  | √ | ' ' | 知识库名称 |
| 10 | fmaxq | 关联问题上限 | numeric | 23 |  | √ | 0 | 关联问题上限 |
| 11 | fcleanemailurl | 删除所有的URL和电子邮件地址 | varchar | 1 |  | √ | '0' | 删除所有的URL和电子邮件地址 |
| 12 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fenableindex | 检索增强 | bpchar | 1 |  | √ | '0' | 检索增强 |
| 14 | fcloudid | fcloudid | varchar | 36 |  | √ | ' ' |  |
| 15 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 16 | fdatasource | fdatasource | varchar | 50 |  | √ | 'community' |  |
| 17 | fnumber | 知识库编号 | varchar | 30 |  | √ | ' ' | 知识库编号 |
| 18 | fenablererank | 启用重排序 | bpchar | 1 |  | √ | '0' | 启用重排序 |
| 19 | fdstrategy | 分块策略 | varchar | 50 |  | √ | 'general' | 分块策略,枚举: general :通用分块 pson :父子分块 |
| 20 | fmodeltype | 向量服务接口 | int8 | 64 |  | √ | 0 | [模型服务 aicc_service](../aicc_files/aicc_service.md) |
| 21 | fchunkstrategy | fchunkstrategy | varchar | 50 |  | √ | 'auto' |  |
| 22 | fq | Q | bpchar | 1 |  | √ | ' ' | Q |
| 23 | freranknumber | 重排序模型 | varchar | 200 |  | √ | ' ' | 重排序模型,枚举: |
| 24 | fpreprocessrule | fpreprocessrule | varchar | 50 |  | √ | ' ' |  |
| 25 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :禁用 C :启用 |
| 26 | fpseparators | 分割符 | varchar | 50 |  | √ | ' ' | 分割符,枚举: \n\n :空两行 \n :换行 。 :中文句号 . :英文句号 ！ :中文叹号 ! :英文叹号 ？ :中文问号 ? :英文问号 |
| 27 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 28 | fmasterid | fmasterid | int8 | 64 |  |  | null |  |
| 29 | fproductline | fproductline | varchar | 50 |  | √ | ' ' |  |
| 30 | fschunksize | 分块长度 | int8 | 64 |  | √ | 0 | 分块长度 |
| 31 | fupdatestrategy | fupdatestrategy | varchar | 50 |  | √ | ' ' |  |
| 32 | fpchunksize | 分块长度 | int8 | 64 |  | √ | 0 | 分块长度 |
| 33 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | frerankllmtype | 重排序llm类型 | varchar | 200 |  | √ | ' ' | 重排序llm类型 |
| 35 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 36 | fseparators | 分割符 | varchar | 50 |  | √ | ' ' | 分割符,枚举: \n\n :空两行 \n :换行 。 :中文句号 . :英文句号 ！ :中文叹号 ! :英文叹号 ？ :中文问号 ? :英文问号 |
| 37 | fdivideway | 分块方式 | varchar | 50 |  | √ | ' ' | 分块方式,枚举: paragraph :段落 fulltext :全文 |
| 38 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: word :Word pdf :PDF |
| 39 | findexmethod | 向量服务接口 | varchar | 50 |  | √ | ' ' | 向量服务接口,枚举: AZURE_EMBEDDING_ADA_002 :GPT-4 BAIDU_EMBEDDING_V1 :百度 KINGDEE_EMBEDDING :金蝶自研 BAIDU_EMBEDDING_BGE_LARGE_ZH :BGE BAIDU_EMBEDDING_TAO_8K :TAO8K KINGDEE_EMBEDDING_NEW :KINGDEE_EMBEDDING_NEW |
| 40 | fsseparators | 分割符 | varchar | 50 |  | √ | ' ' | 分割符,枚举: \n\n :空两行 \n :换行 。 :中文句号 . :英文句号 ！ :中文叹号 ! :英文叹号 ？ :中文问号 ? :英文问号 |
| 41 | fknlcount | fknlcount | int4 | 32 |  | √ | 0 |  |
| 42 | fkmformid | 知识库 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 43 | fdatasourceurl | fdatasourceurl | varchar | 50 |  | √ | ' ' |  |
| 44 | ftype | ftype | int8 | 64 |  | √ | 0 |  |
| 45 | fchunksize | 分块长度 | int8 | 64 |  |  | null | 分块长度 |
| 46 | fupdatetime | 知识库更新时间 | int8 | 64 |  | √ | 0 | 知识库更新时间 |
| 47 | fqa | Q&A | bpchar | 1 |  | √ | ' ' | Q&A |
| 48 | fchunkoverlap | 分块重复长度 | int8 | 64 |  | √ | 0 | 分块重复长度 |
| 49 | fvector | 向量存储 | bpchar | 1 |  | √ | '0' | 向量存储 |
| 50 | fcleanspecsym | 替换连续的空格、换行符和制表符 | varchar | 1 |  | √ | '1' | 替换连续的空格、换行符和制表符 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_corpus_libs |  | fnumber |
| 2 | pk_t_corpus_libs |  | fid |

---

## 知识库设置-多语言表 t_corpus_libs_l

- **表名称：** 知识库设置-多语言表
- **表名：** t_corpus_libs_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 知识库名称 | varchar | 72 |  | √ | ' ' | 知识库名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_corpus_libs_l |  | fpkid |
| 2 | idx_corpus_libs_l_0 |  | fid,flocaleid |
