# 收票助手配置-rim_fpzs_config

## 收票助手配置-主表 t_rim_fpzs_config

- **表名称：** 收票助手配置-主表
- **表名：** t_rim_fpzs_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmobile_config | 移动端配置 | varchar | 255 |  | √ | ' ' | 移动端配置 |
| 3 | fqrcode_type | 二维码类型单选按钮组 | varchar | 5 |  | √ | ' ' | 二维码类型单选按钮组,枚举: 1 :云之家 2 :微信 |
| 4 | fschema_name | 发票助手方案名称 | varchar | 200 |  | √ | ' ' | 发票助手方案名称 |
| 5 | fschema_number | 采集助手方案编码 | varchar | 50 |  | √ | ' ' | 采集助手方案编码 |
| 6 | fmobile_config_tag | 移动端配置_详情 | text | 0 |  |  | ' ' | 移动端配置_详情 |
| 7 | fsuitable_bill_types | 适用单据类型组 | varchar | 5 |  | √ | ' ' | 适用单据类型组,枚举: 1 :全部单据类型 0 :指定单据类型 |
| 8 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: 1 :启用 0 :停用 |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fpc_config_tag | pc端配置_详情 | text | 0 |  |  | ' ' | pc端配置_详情 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fpc_config | pc端配置 | varchar | 255 |  | √ | ' ' | pc端配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_fpzs_config |  | fschema_number |
| 2 | pk_t_rim_fpzs_config |  | fid |

---

## 适用单据类型单据体-子表 t_rim_fpzs_config_entry

- **表名称：** 适用单据类型单据体-子表
- **表名：** t_rim_fpzs_config_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbill_number | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 3 | fbill_name | 单据名称 | varchar | 100 |  | √ | ' ' | 单据名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_fpzs_config_entry |  | fentryid |
| 2 | idx_rim_fpzs_config_entry_fk |  | fid |
