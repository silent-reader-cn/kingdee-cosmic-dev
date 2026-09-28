# 知识库配置方案-aikm_repo_scheme

## 知识库配置方案-多语言表 t_repo_configscheme_l

- **表名称：** 知识库配置方案-多语言表
- **表名：** t_repo_configscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 方案描述 | varchar | 255 |  | √ | ' ' | 方案描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_repo_configscheme_l |  | fpkid |
| 2 | idx_repo_configscheme_l |  | fid,flocaleid |

---

## 知识库配置方案-主表 t_repo_configscheme

- **表名称：** 知识库配置方案-主表
- **表名：** t_repo_configscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskepseprator | 保留分割符 | bpchar | 1 |  | √ | '0' | 保留分割符 |
| 3 | fcleantype | 清洗策略 | varchar | 50 |  | √ | ' ' | 清洗策略,枚举: W :水印 I :目录 |
| 4 | fmodeltype | 向量服务接口 | int8 | 64 |  | √ | 0 | [模型服务 aicc_service](../aicc_files/aicc_service.md) |
| 5 | fkeepseparator | 保留分割符 | varchar | 50 |  | √ | '0' | 保留分割符 |
| 6 | fenableocr | 视觉识别服务 | bpchar | 1 |  | √ | '0' | 视觉识别服务 |
| 7 | fq | Q | varchar | 50 |  | √ | '0' | Q |
| 8 | fpkepseprator | 保留分割符 | bpchar | 1 |  | √ | '0' | 保留分割符 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :禁用 C :启用 |
| 11 | fpseparators | 分割符 | varchar | 50 |  | √ | ' ' | 分割符,枚举: \n\n :空两行 \n :换行 。 :中文句号 . :英文句号 ！ :中文叹号 ! :英文叹号 ？ :中文问号 ? :英文问号 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fes | 全文存储 | varchar | 50 |  | √ | '0' | 全文存储 |
| 14 | fschunksize | 分块长度 | int8 | 64 |  | √ | 0 | 分块长度 |
| 15 | fsearchtype | fsearchtype | varchar | 50 |  | √ | ' ' |  |
| 16 | fpchunksize | 分块长度 | int8 | 64 |  | √ | 0 | 分块长度 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 19 | fmaxq | 关联问题上限 | numeric | 23 |  | √ | 0 | 关联问题上限 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 21 | fseparators | 分割符 | varchar | 50 |  | √ | ' ' | 分割符,枚举: \n\n :空两行 \n :换行 。 :中文句号 . :英文句号 ！ :中文叹号 ! :英文叹号 ？ :中文问号 ? :英文问号 |
| 22 | fcleanemailurl | 删除所有的URL和电子邮件地址 | varchar | 1 |  | √ | '0' | 删除所有的URL和电子邮件地址 |
| 23 | fdivideway | 分块方式 | varchar | 50 |  | √ | ' ' | 分块方式,枚举: paragraph :段落 fulltext :全文 |
| 24 | ffunc | ffunc | varchar | 50 |  | √ | '0' |  |
| 25 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: word :Word pdf :PDF |
| 26 | findexmethod | 向量服务接口 | varchar | 50 |  | √ | ' ' | 向量服务接口,枚举: AZURE_EMBEDDING_ADA_002 :GPT-4 BAIDU_EMBEDDING_V1 :百度 KINGDEE_EMBEDDING :金蝶自研 BAIDU_EMBEDDING_BGE_LARGE_ZH :BGE BAIDU_EMBEDDING_TAO_8K :TAO8K |
| 27 | fdescription | 方案描述 | varchar | 255 |  | √ | ' ' | 方案描述 |
| 28 | fsseparators | 分割符 | varchar | 50 |  | √ | ' ' | 分割符,枚举: \n\n :空两行 \n :换行 。 :中文句号 . :英文句号 ！ :中文叹号 ! :英文叹号 ？ :中文问号 ? :英文问号 |
| 29 | fenableindex | 检索增强 | bpchar | 1 |  | √ | '0' | 检索增强 |
| 30 | fchunksize | 分块长度 | int8 | 64 |  | √ | 0 | 分块长度 |
| 31 | fqa | Q&A | varchar | 50 |  | √ | '0' | Q&A |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: |
| 33 | fchunkoverlap | 分块重复长度 | int8 | 64 |  | √ | 0 | 分块重复长度 |
| 34 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 35 | fvector | 向量存储 | varchar | 50 |  | √ | '0' | 向量存储 |
| 36 | fcleanspecsym | 替换连续的空格、换行符和制表符 | varchar | 1 |  | √ | '1' | 替换连续的空格、换行符和制表符 |
| 37 | fdstrategy | 分块策略 | varchar | 50 |  | √ | 'general' | 分块策略,枚举: general :通用分块 pson :父子分块 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_repo_configscheme_fnumber |  | fnumber |
| 2 | pk_repo_configscheme |  | fid |
