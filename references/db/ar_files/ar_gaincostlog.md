# 执行结果-ar_gaincostlog

## 失败详情-子表 t_ar_gaincostlogentry

- **表名称：** 失败详情-子表
- **表名：** t_ar_gaincostlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 3 | fgainstatus | 状态 | varchar | 5 |  | √ | ' ' | 状态,枚举: 1 :成功 0 :失败 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_gaincostlogentry |  | fentryid |
| 2 | idx_ar_gaincostlogentry_fid |  | fid |

---

## 执行结果-主表 t_ar_gaincostlog

- **表名称：** 执行结果-主表
- **表名：** t_ar_gaincostlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fsucessnum | 执行成功数量 | int4 | 32 |  | √ | 0 | 执行成功数量 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | foperate | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: A :查看失败详情 |
| 9 | ffailnum | 执行失败数量 | int4 | 32 |  | √ | 0 | 执行失败数量 |
| 10 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fexecutetype | 执行方式 | varchar | 5 |  | √ | ' ' | 执行方式,枚举: 1 :手工 0 :自动 |
| 12 | fbillno | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_gaincostlog |  | fid |
| 2 | idx_ar_gaincostlog_num |  | fbillno |
