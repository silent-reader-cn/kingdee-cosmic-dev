# 交易明细扩展字段配置-detail_extra_field_r

## 交易明细扩展字段配置-多语言表 t_aqap_bank_detail_extra2_l

- **表名称：** 交易明细扩展字段配置-多语言表
- **表名：** t_aqap_bank_detail_extra2_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_bank_detail_extra2_l_0 |  | fid,flocaleid |
| 2 | t_aqap_bank_detail_extra2_l_pkey |  | fpkid |

---

## 交易明细扩展字段配置-主表 t_aqap_bank_detail_extra2

- **表名称：** 交易明细扩展字段配置-主表
- **表名：** t_aqap_bank_detail_extra2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 分组 | int8 | 64 |  |  | null | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 4 | fdes | 字段说明 | varchar | 500 |  | √ | ' ' | 字段说明 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbank_version_id | 银行版本ID | varchar | 50 |  | √ | ' ' | 银行版本ID |
| 7 | fspare | 备用字段 | varchar | 50 |  | √ | ' ' | 备用字段 |
| 8 | fupdate_name | 修改人 | varchar | 50 |  | √ | ' ' | 修改人 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: |
| 11 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fextra_field | 扩展字段 | varchar | 50 |  | √ | ' ' | 扩展字段 |
| 16 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 17 | fdetail_interface | 交易明细接口 | varchar | 50 |  | √ | ' ' | 交易明细接口 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_detail_extra2_pkey |  | fid |
