# 科目表版本化操作报告-bd_refop_report

## 单据体-子表 t_bd_refop_reportentry

- **表名称：** 单据体-子表
- **表名：** t_bd_refop_reportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrormsg | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fresult | 执行结果 | bpchar | 1 |  | √ | '0' | 执行结果,枚举: 0 :失败 1 :成功 |
| 5 | fchildorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_refop_reportentry |  | fid |
| 2 | pk_t_bd_refop_reportentry |  | fentryid |

---

## 科目表版本化操作报告-主表 t_bd_refop_report

- **表名称：** 科目表版本化操作报告-主表
- **表名：** t_bd_refop_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | faccttabrefid | 科目表版本化 | int8 | 64 |  | √ | 0 | 科目表版本化 bd_accounttableref |
| 4 | fop | 操作 | bpchar | 1 |  | √ | '1' | 操作,枚举: 1 :启用 2 :反启用 3 :删除 4 :重新启用 5 :余额结转 6 :还原修改的对照关系 |
| 5 | fdate | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 6 | fuserid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fopdate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_refop_report |  | fid |
| 2 | idx_bd_refop_report |  | forgid |
