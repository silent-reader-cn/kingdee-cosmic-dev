# 银行文件表-aqap_bank_file

## 银行文件表-主表 t_aqap_bank_file

- **表名称：** 银行文件表-主表
- **表名：** t_aqap_bank_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  |  | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffile_name | 文件名 | varchar | 250 |  |  | null | 文件名 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | facc_no | 账号 | varchar | 100 |  |  | null | 账号 |
| 7 | ftrans_date | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbank_version | 银行版本 | int8 | 64 |  | √ | 0 | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 10 | ffile_content | 文件内容 | varchar | 255 |  |  | null | 文件内容 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | ffile_type | 文件类型 | varchar | 50 |  |  | null | 文件类型 |
| 17 | ffile_content_tag | 文件内容_详情 | text | 0 |  |  | null | 文件内容_详情 |
| 18 | fnumber | 编码 | varchar | 50 |  |  | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aqap_bank_file_time |  | fcreatetime |
| 2 | pk_t_aqap_bank_file |  | fid |
| 3 | idx_t_aqap_bank_file_name |  | ffile_name |

---

## 银行文件表-多语言表 t_aqap_bank_file_l

- **表名称：** 银行文件表-多语言表
- **表名：** t_aqap_bank_file_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aqap_bank_file_l |  | fid |
| 2 | pk_t_aqap_bank_file_l |  | fpkid |
