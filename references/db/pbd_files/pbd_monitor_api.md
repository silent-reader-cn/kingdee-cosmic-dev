# 外部系统回调API-pbd_monitor_api

## 结果字段-子表 t_pbd_monitorapi_outputs

- **表名称：** 结果字段-子表
- **表名：** t_pbd_monitorapi_outputs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finput_data_type | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 |
| 3 | finput_is_array | 是否数组 | bpchar | 1 |  | √ | ' ' | 是否数组 |
| 4 | finput_field | 字段名 | varchar | 100 |  | √ | ' ' | 字段名 |
| 5 | finput_description | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_mapi_outputs_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_monitorapi_outputs |  | fentryid |

---

## 外部系统回调API-多语言表 t_pbd_monitor_api_l

- **表名称：** 外部系统回调API-多语言表
- **表名：** t_pbd_monitor_api_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | API名称 | varchar | 255 |  | √ | ' ' | API名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_monitor_api_l_fid |  | flocaleid |
| 2 | pk_pbd_monitor_api_l |  | fpkid |

---

## 外部系统回调API-主表 t_pbd_monitor_api

- **表名称：** 外部系统回调API-主表
- **表名：** t_pbd_monitor_api

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | API名称 | varchar | 255 |  | √ | ' ' | API名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fplatformapitype | API分类 | int8 | 64 |  | √ | 0 | [接口分类 pbd_api_type](../pbd_files/pbd_api_type.md) |
| 6 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fispreset | 预置 | bpchar | 1 |  | √ | ' ' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | API编码 | varchar | 80 |  | √ | ' ' | API编码 |
| 14 | ffull_name | 类型 | varchar | 255 |  | √ | ' ' | 类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_monitor_api |  | fid |
| 2 | idx_pbd_monitor_api_fnumber |  | fnumber |

---

## 输入参数-子表 t_pbd_monitorapi_inputs

- **表名称：** 输入参数-子表
- **表名：** t_pbd_monitorapi_inputs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequired | 是否必须 | bpchar | 1 |  | √ | ' ' | 是否必须 |
| 3 | finput_data_type | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 |
| 4 | finput_is_array | 是否数组 | bpchar | 1 |  | √ | ' ' | 是否数组 |
| 5 | finput_field | 字段名 | varchar | 100 |  | √ | ' ' | 字段名 |
| 6 | finput_description | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdefault_value | 默认值 | varchar | 500 |  | √ | ' ' | 默认值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_monitorapi_inputs |  | fentryid |
| 2 | idx_pbd_mapi_inputs_fid_fseq |  | fid,fseq |
