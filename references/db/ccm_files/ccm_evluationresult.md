# 信用评估生成日志-ccm_evluationresult

## 生成结果-子表 t_ccm_evalresultentry

- **表名称：** 生成结果-子表
- **表名：** t_ccm_evalresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscoretablebillno | 信用评分表编号 | varchar | 80 |  | √ | ' ' | 信用评分表编号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fscoretablebillid | 信用评分表单据ID | int8 | 64 |  | √ | 0 | 信用评分表单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evalresultentry |  | fentryid |
| 2 | idx_ccm_evalresultentry |  | fid |

---

## 异常信息-子表 t_ccm_evalresult_ex

- **表名称：** 异常信息-子表
- **表名：** t_ccm_evalresult_ex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrmsg | 异常描述 | varchar | 1024 |  | √ | ' ' | 异常描述 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evalresult_ex |  | fentryid |
| 2 | idx_ccm_evalresult_ex |  | fid |

---

## 信用评估生成日志-主表 t_ccm_evalresult

- **表名称：** 信用评估生成日志-主表
- **表名：** t_ccm_evalresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresultbillcount | 生成评分表数量 | int4 | 32 |  | √ | 0 | 生成评分表数量 |
| 3 | fgradegroupid | 信用等级方案 | int8 | 64 |  | √ | 0 | [信用等级方案 ccm_newgradegroup](../ccm_files/ccm_newgradegroup.md) |
| 4 | fexecstarttime | 计划执行开始时间 | timestamp | 0 |  |  | null | 计划执行开始时间 |
| 5 | fplanbillno | 评估计划编号 | varchar | 80 |  | √ | ' ' | 评估计划编号 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fplanbillid | 评估计划ID | int8 | 64 |  | √ | 0 | 评估计划ID |
| 8 | fexecdate | 计划执行日期 | timestamp | 0 |  |  | null | 计划执行日期 |
| 9 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdescription | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 11 | fevalschemeid | 信用评估方案 | int8 | 64 |  | √ | 0 | [信用评估方案 ccm_evalscheme](../ccm_files/ccm_evalscheme.md) |
| 12 | fexecstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 0 :计划执行中 1 :计划执行完成 9 :计划执行失败 |
| 13 | fexecendtime | 计划执行结束时间 | timestamp | 0 |  |  | null | 计划执行结束时间 |
| 14 | fsessionid | 线程ID | varchar | 50 |  | √ | ' ' | 线程ID |
| 15 | fexectype | 执行类型 | varchar | 50 |  | √ | ' ' | 执行类型,枚举: auto :自动执行 manual :手工执行 |
| 16 | fobjecttype | 评估对象类型 | varchar | 50 |  | √ | ' ' | 评估对象类型,枚举: bd_customer :客户 |
| 17 | fevalorgid | 信用评估组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbillno | 执行日志编号 | varchar | 80 |  | √ | ' ' | 执行日志编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evalresult |  | fid |
| 2 | idx_ccm_evalresult_sid |  | fsessionid |
