# 银企对账码历史规则-aqap_rc_history_rule

## 银企对账码历史规则-多语言表 t_aqap_rc_history_rule_l

- **表名称：** 银企对账码历史规则-多语言表
- **表名：** t_aqap_rc_history_rule_l

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
| 1 | pk_t_aqap_rc_history_rule_l |  | fpkid |
| 2 | idx_c_rc_history_rule_l |  | fname |
| 3 | idx_aqap_rc_history_rule_l_0 |  | fid,flocaleid |

---

## 银企对账码历史规则-主表 t_aqap_rc_history_rule

- **表名称：** 银企对账码历史规则-主表
- **表名：** t_aqap_rc_history_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnode_name | KD对账码字段 | varchar | 255 |  | √ | ' ' | KD对账码字段 |
| 3 | fkd_size | 对账码长度 | int8 | 64 |  | √ | 0 | 对账码长度 |
| 4 | fbiz_type | 接口类型 | varchar | 50 |  | √ | ' ' | 接口类型,枚举: pay :付款接口 detail :明细接口 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | frecord_num | 每条记录的字段数 | int4 | 32 |  | √ | 0 | 每条记录的字段数 |
| 7 | fbank_field_size | 对账字段最大长度 | int8 | 64 |  | √ | 0 | 对账字段最大长度 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fis_merge | 汇总明细 | varchar | 50 |  | √ | ' ' | 汇总明细,枚举: true :是 false :否 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fnode_path | 字段路径 | varchar | 255 |  | √ | ' ' | 字段路径 |
| 13 | finterface_code | 接口代码 | int8 | 64 |  | √ | 0 | [银行接口维护 aqap_pay_interface](../aqap_files/aqap_pay_interface.md) |
| 14 | fis_skip_first_row | 首行是否存在字段名 | varchar | 10 |  | √ | ' ' | 首行是否存在字段名,枚举: true :是 false :否 |
| 15 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fkd_flag | KD规则 | varchar | 255 |  | √ | ' ' | KD规则 |
| 19 | fcontent_type | 格式 | varchar | 50 |  | √ | ' ' | 格式,枚举: xml :XML json :JSON file :文件 xml_data_domain :数据域 |
| 20 | fbank_version | 银行版本 | int8 | 64 |  | √ | 0 | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 21 | foperate | 操作 | varchar | 50 |  |  | ' ' | 操作,枚举: update :修改规则 delete :删除规则 |
| 22 | fis_bank_ref | 是否预设数据 | varchar | 50 |  | √ | ' ' | 是否预设数据,枚举: true :是 false :否 |
| 23 | fstate | 初始状态 | varchar | 50 |  | √ | ' ' | 初始状态,枚举: 1 :启用 0 :禁用 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_rc_history_rule |  | fid |
| 2 | idx_c_aqap_rc_history_rule |  | fnumber |
