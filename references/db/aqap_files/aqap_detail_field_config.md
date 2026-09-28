# 交易明细字段配置-aqap_detail_field_config

## 单据体-子表 t_aqap_detail_field

- **表名称：** 单据体-子表
- **表名：** t_aqap_detail_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetail_field | 明细字段 | int8 | 64 |  |  | null | [交易明细字段模板 aqap_detail_field_tpl](../aqap_files/aqap_detail_field_tpl.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  |  | null | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_detail_field |  | fentryid |
| 2 | idx_aqap_detail_field |  | fid |

---

## 交易明细字段配置-多语言表 t_aqap_detail_field_conf_l

- **表名称：** 交易明细字段配置-多语言表
- **表名：** t_aqap_detail_field_conf_l

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
| 1 | pk_t_aqap_detail_field_conf_l |  | fpkid |
| 2 | idx_aqap_detail_field_conf_l |  | fid |

---

## 交易明细字段配置-主表 t_aqap_detail_field_conf

- **表名称：** 交易明细字段配置-主表
- **表名：** t_aqap_detail_field_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 银行版本 | int8 | 64 |  | √ | 0 | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 5 | fsplit | 分隔符 | varchar | 50 |  | √ | ' ' | 分隔符 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | fdetail_interface | 明细接口代码 | int8 | 64 |  |  | null | [银行接口维护 aqap_pay_interface](../aqap_files/aqap_pay_interface.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_detail_field_conf |  | fnumber |
| 2 | pk_t_aqap_detail_field_conf |  | fid |
