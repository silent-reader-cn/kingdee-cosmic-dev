# 采购预测单-mrp_purforecast

## 采购预测单-主表 t_mrp_purforecast

- **表名称：** 采购预测单-主表
- **表名：** t_mrp_purforecast

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fplanorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fplanprogramid | 计划方案 | int8 | 64 |  | √ | 0 | [计划方案定义(作废) mrp_planprogram](../msplan_files/mrp_planprogram.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fwarnning | 预警百分比 | numeric | 23 | 10 | √ | 0.0000000000 | 预警百分比 |
| 11 | frunlog | 计算日志 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 12 | fbillno | 计划运算号 | varchar | 30 |  | √ | ' ' | 计划运算号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_purforecast |  | fbillno,fplanorgid |
| 2 | pk_t_mrp_purforecast |  | fid |

---

## 单据体-子表 t_mrp_purforecastentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_purforecastentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 调整原因备注 | varchar | 255 |  | √ | ' ' | 调整原因备注 |
| 3 | freleasetime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 4 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 5 | fchangeqty | 修改数量 | numeric | 23 | 10 | √ | 0.0000000000 | 修改数量 |
| 6 | fiswarnning | 是否预警 | bpchar | 1 |  | √ | ' ' | 是否预警 |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | frowtype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: A :SYS B :ADDNEW |
| 9 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fisrelease | 是否发布 | bpchar | 1 |  | √ | ' ' | 是否发布 |
| 12 | feditpersonid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fplantag | 计划标识 | bpchar | 1 |  | √ | ' ' | 计划标识,枚举: A :通用 B :定制 C :选配 |
| 14 | fpurpattern | 采购模式 | varchar | 255 |  | √ | ' ' | 采购模式 |
| 15 | freleasepersonid | 发布人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fedittime | 修改日 | timestamp | 0 |  |  | null | 修改日 |
| 17 | ftype | PO&PROC | varchar | 50 |  | √ | ' ' | PO&PROC |
| 18 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 19 | fpurperson | 采购计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_purforecastentry |  | fid,fseq |
| 2 | pk_t_mrp_purforecastentry |  | fentryid |
