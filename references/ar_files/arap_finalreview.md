# 结账检查-arap_finalreview

## 检查项-子表 t_arap_finalreviewentry

- **表名称：** 检查项-子表
- **表名：** t_arap_finalreviewentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fformquery | 查询条件 | varchar | 255 |  | √ | ' ' | 查询条件 |
| 3 | fcheckresult | 检查结果（废弃） | varchar | 30 |  | √ | ' ' | 检查结果（废弃） |
| 4 | fformnumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 5 | fresulthandle | 结果处理 | varchar | 30 |  | √ | ' ' | 结果处理 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcheckitem | 检查项 | varchar | 50 |  | √ | ' ' | 检查项 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fchecktype | 控制级别 | varchar | 30 |  | √ | ' ' | 控制级别 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arap_finalreviewentry |  | fentryid |
| 2 | idx_arap_finalreviewe_item |  | fcheckitem |

---

## 结账检查-主表 t_arap_finalreview

- **表名称：** 结账检查-主表
- **表名：** t_arap_finalreview

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fexecutetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftimeconsum | 耗时（秒） | int8 | 64 |  | √ | 0 | 耗时（秒） |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fperiod | 当前期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 12 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arap_finalreview_orgp |  | forgid,fperiod |
| 2 | pk_t_arap_finalreview |  | fid |
