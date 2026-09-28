# 巡检检查异常结果-xkcts_inspectjob_detail

## 单据体-子表 t_xkinsp_res_dtlentry

- **表名称：** 单据体-子表
- **表名：** t_xkinsp_res_dtlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fobjtypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fobjid | 业务对象id | varchar | 50 |  | √ | ' ' | 业务对象id |
| 4 | fobjbillno | 单据/基础资料编码 | varchar | 50 |  | √ | ' ' | 单据/基础资料编码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fobjdes | 异常描述 | varchar | 300 |  | √ | ' ' | 异常描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_res_dtlentry |  | fentryid |
| 2 | idx_res_dtlentry_fid |  | fid,fseq |

---

## 巡检检查异常结果-主表 t_xkinsp_res_dtl

- **表名称：** 巡检检查异常结果-主表
- **表名：** t_xkinsp_res_dtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillno | 检查结果分录id | varchar | 50 |  | √ | ' ' | 检查结果分录id |
| 3 | fitemid | 检查项 | int8 | 64 |  | √ | 0 | [巡检检查项 xkcts_inspectitem](../cts_files/xkcts_inspectitem.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkinsp_resdtl_no |  | fbillno |
| 2 | pk_xkinsp_res_dtl |  | fid |
