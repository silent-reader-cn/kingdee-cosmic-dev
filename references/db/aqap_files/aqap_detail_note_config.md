# 交易明细摘要取值规则-aqap_detail_note_config

## 单据体-子表 t_aqap_detail_note_rule

- **表名称：** 单据体-子表
- **表名：** t_aqap_detail_note_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetail_field | 摘要字段名称 | int8 | 64 |  |  | null | [自定义摘要 aqap_custom_note](../aqap_files/aqap_custom_note.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  |  | null | 分录行号 |
| 4 | flogic | 逻辑 | varchar | 50 |  |  | null | 逻辑,枚举: and :并且 or :或者 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_detail_note_rule |  | fid |
| 2 | pk_t_aqap_detail_note_rule |  | fentryid |

---

## 交易明细摘要取值规则-主表 t_aqap_detail_note_config

- **表名称：** 交易明细摘要取值规则-主表
- **表名：** t_aqap_detail_note_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  |  | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 银行版本 | int8 | 64 |  | √ | 0 | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffield_name | 交易明细摘要取值字段 | varchar | 100 |  |  | null | 交易明细摘要取值字段 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbank_version | 银行版本简码 | varchar | 50 |  |  | null | 银行版本简码 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 50 |  |  | ' ' | 编码 |
| 14 | fdetail_interface | 交易明细接口 | int8 | 64 |  |  | null | [银行接口维护 aqap_pay_interface](../aqap_files/aqap_pay_interface.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_detail_note_config |  | fid |
| 2 | idx_aqap_detail_note_conf |  | fnumber |

---

## 交易明细摘要取值规则-多语言表 t_aqap_detail_note_config_l

- **表名称：** 交易明细摘要取值规则-多语言表
- **表名：** t_aqap_detail_note_config_l

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
| 1 | idx_aqap_detail_note_config_l |  | fid |
| 2 | pk_t_aqap_detail_note_config_l |  | fpkid |
