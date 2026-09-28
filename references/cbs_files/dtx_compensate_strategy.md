# 补偿策略-dtx_compensate_strategy

## 单据体-子表 t_cbs_dtx_retry_detail

- **表名称：** 单据体-子表
- **表名：** t_cbs_dtx_retry_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fday | 第几天 | int4 | 32 |  |  | 0 | 第几天 |
| 4 | fcount | 重试次数 | int4 | 32 |  |  | 0 | 重试次数 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbs_dtx_retry_detail |  | fentryid |
| 2 | idx_cbs_dtx_retry_detail_fid |  | fid |

---

## 补偿策略-主表 t_cbs_dtx_retry_strategy

- **表名称：** 补偿策略-主表
- **表名：** t_cbs_dtx_retry_strategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 策略名称 | varchar | 50 |  | √ | ' ' | 策略名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmin_retry_count | 递减后最小重试次数 | int4 | 32 |  |  | 0 | 递减后最小重试次数 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | ffirst_retry_count | 第一次重试次数 | int4 | 32 |  |  | 0 | 第一次重试次数 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | ftype | 策略类型 | bpchar | 1 |  | √ | ' ' | 策略类型,枚举: 1 :自定义策略 2 :递减策略 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftotal_days | 重试天数 | int4 | 32 |  | √ | 0 | 重试天数 |
| 13 | fexpress | 效果示例 | varchar | 500 |  | √ | ' ' | 效果示例 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fday_decline_count | 日递减次数 | int4 | 32 |  |  | 0 | 日递减次数 |
| 16 | fcode | 策略编码 | varchar | 50 |  | √ | ' ' | 策略编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbs_dtx_retry_strategy |  | fid |
| 2 | idx_cbs_dtx_retry_strategy_fcode |  | fcode |

---

## 补偿策略-多语言表 t_cbs_dtx_retry_strategy_l

- **表名称：** 补偿策略-多语言表
- **表名：** t_cbs_dtx_retry_strategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 策略名称 | varchar | 50 |  | √ | ' ' | 策略名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbs_dtx_retry_strategy_l |  | fpkid |
| 2 | idx_cbs_dtx_retry_strategy_l_0 |  | fid,flocaleid |
