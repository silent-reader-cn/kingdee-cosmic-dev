# 法律文件-chatbi_legal_document

## 法律文件-主表 t_cbi_legal_document

- **表名称：** 法律文件-主表
- **表名：** t_cbi_legal_document

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 法律文件名称 | varchar | 50 |  | √ | ' ' | 法律文件名称 |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 4 | fupdatetype | 更新方式 | varchar | 50 |  | √ | 'MANUAL' | 更新方式,枚举: manual :手动更新 |
| 5 | forder | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |
| 6 | furl | URL | varchar | 250 |  | √ | ' ' | URL |
| 7 | fneeduseragree | 需要同意 | bpchar | 1 |  | √ | '0' | 需要同意 |
| 8 | fishistorical | 是否历史文件 | varchar | 50 |  | √ | 'A' | 是否历史文件,枚举: A :最新文件 B :历史文件 |
| 9 | fversion | 当前版本 | varchar | 50 |  | √ | ' ' | 当前版本 |
| 10 | fcode | 法律文件编码 | varchar | 50 |  | √ | ' ' | 法律文件编码 |
| 11 | fmodifytime | 更新时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_legal_document |  | fid |

---

## 法律文件-多语言表 t_cbi_legal_document_l

- **表名称：** 法律文件-多语言表
- **表名：** t_cbi_legal_document_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 法律文件名称 | varchar | 50 |  | √ | ' ' | 法律文件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_legal_document_l_0 |  | fid,flocaleid |
| 2 | pk_cbi_legal_document_l |  | fpkid |
