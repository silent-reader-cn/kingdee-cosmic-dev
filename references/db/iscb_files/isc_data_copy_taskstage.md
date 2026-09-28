# 分批结果-isc_data_copy_taskstage

## 执行参数-子表 t_isc_dc_execution_params

- **表名称：** 执行参数-子表
- **表名：** t_isc_dc_execution_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparams_value | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 3 | fparams_index | 序号 | varchar | 100 |  | √ | ' ' | 序号 |
| 4 | fparams_name | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fparams_data_type | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fparams_label | 标题 | varchar | 100 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_dc_execution_params_pkey |  | fentryid |
| 2 | idx_isc_dc_exe_params_0 |  | fid |

---

## 分批结果-主表 t_isc_data_copy_taskstage

- **表名称：** 分批结果-主表
- **表名：** t_isc_data_copy_taskstage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhost | 执行服务器 | varchar | 150 |  | √ | ' ' | 执行服务器 |
| 3 | fbegin_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | flog_tag | 分批日志_详情 | text | 0 |  |  | null | 分批日志_详情 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | ftotal_failed | 失败批数 | int8 | 64 |  | √ | 0 | 失败批数 |
| 9 | flog | 分批日志 | varchar | 255 |  | √ | ' ' | 分批日志 |
| 10 | fmodifytime | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 11 | fdata_trigger | 启动方案 | int8 | 64 |  | √ | 0 | 启动方案 isc_data_copy_trigger |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fstate | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: C :创建 R :执行中 S :完成 F :失败 X :已撤销 W :等待中 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fdata_copy | 数据集成方案 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |
| 17 | ftotal_count | 总行数 | int8 | 64 |  | √ | 0 | 总行数 |
| 18 | fenable | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 20 | ftotal_batch | 总批数 | int8 | 64 |  | √ | 0 | 总批数 |
| 21 | ftotal_success | 成功批数 | int8 | 64 |  | √ | 0 | 成功批数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_data_copy_taskstage_pkey |  | fid |
| 2 | idx_isc_data_copy_ts_0 |  | fmodifierid |
| 3 | idx_isc_data_copy_ts_1 |  | fnumber |

---

## 分批结果-多语言表 t_isc_data_copy_taskstage_l

- **表名称：** 分批结果-多语言表
- **表名：** t_isc_data_copy_taskstage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 分批任务名称 | varchar | 100 |  | √ | ' ' | 分批任务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_data_copy_ts_l_0 |  | fid,flocaleid |
| 2 | t_isc_data_copy_taskstage_l_pkey |  | fpkid |
