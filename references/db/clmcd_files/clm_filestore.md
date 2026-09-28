# 文件存储-clm_filestore

## 文件存储-主表 t_clm_filestore

- **表名称：** 文件存储-主表
- **表名：** t_clm_filestore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffilecontent_tag | 合同文本_详情 | text | 0 |  |  | null | 合同文本_详情 |
| 3 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ffilecontent | 合同文本 | text | 0 |  |  | null | 合同文本 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | ffilecomment | 合同评论 | text | 0 |  |  | null | 合同评论 |
| 14 | foriginalfileid | 原始文件id | varchar | 50 |  | √ | ' ' | 原始文件id |
| 15 | fversion | 文件版本号 | int4 | 32 |  | √ | 1 | 文件版本号 |
| 16 | ffilecomment_tag | 合同评论_详情 | text | 0 |  |  | null | 合同评论_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_filestore |  | fid |
| 2 | idx_clm_filestore_number |  | fnumber |

---

## 文件存储-多语言表 t_clm_filestore_l

- **表名称：** 文件存储-多语言表
- **表名：** t_clm_filestore_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_contract_filestore_l_fid |  | fid,flocaleid |
| 2 | pk_t_clm_filestore_l |  | fpkid |
