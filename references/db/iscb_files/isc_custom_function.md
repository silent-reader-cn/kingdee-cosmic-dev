# 自定义函数-isc_custom_function

## 自定义函数-多语言表 t_isc_custom_function_l

- **表名称：** 自定义函数-多语言表
- **表名：** t_isc_custom_function_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 函数描述 | varchar | 50 |  | √ | ' ' | 函数描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_custom_function_l_pkey |  | fpkid |
| 2 | idx_isc_custom_fc_l |  | fid,flocaleid |

---

## 函数结果-子表 t_isc_function_result

- **表名称：** 函数结果-子表
- **表名：** t_isc_function_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresult_remark | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 3 | fresult_type | 结果类型 | varchar | 30 |  | √ | ' ' | 结果类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 boolean :布尔值 other :其他 |
| 4 | fresult_name | 结果名称 | varchar | 150 |  | √ | ' ' | 结果名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fresult_title | 结果标题 | varchar | 150 |  | √ | ' ' | 结果标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_function_result_pkey |  | fentryid |
| 2 | idx_isc_function_rt |  | fid |

---

## 函数参数-子表 t_isc_function_param

- **表名称：** 函数参数-子表
- **表名：** t_isc_function_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffunction_remark | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ffunction_title | 参数标题 | varchar | 150 |  | √ | ' ' | 参数标题 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ffunction_type | 参数类型 | varchar | 30 |  | √ | ' ' | 参数类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 boolean :布尔值 other :其他 |
| 7 | ffunction_name | 参数名称 | varchar | 150 |  | √ | ' ' | 参数名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_function_param_pkey |  | fentryid |
| 2 | idx_isc_function_pm |  | fid |

---

## 自定义函数-主表 t_isc_custom_function

- **表名称：** 自定义函数-主表
- **表名：** t_isc_custom_function

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 函数描述 | varchar | 50 |  | √ | ' ' | 函数描述 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fscript | 函数脚本 | varchar | 2000 |  | √ | ' ' | 函数脚本 |
| 11 | fstatus | 数据状态 | varchar | 20 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 15 | fgroup | 分组 | int8 | 64 |  | √ | 0 | [自定义函数分组 isc_custom_function_group](../iscb_files/isc_custom_function_group.md) |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fscript_tag | 函数脚本_详情 | text | 0 |  |  | null | 函数脚本_详情 |
| 18 | fnumber | 函数名称 | varchar | 30 |  | √ | ' ' | 函数名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_custom_function_pkey |  | fid |
| 2 | idx_isc_custom_fc |  | fgroup |
