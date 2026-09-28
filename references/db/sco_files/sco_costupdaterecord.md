# 标准成本更新任务报告-sco_costupdaterecord

## 标准成本更新任务报告-主表 t_sco_costupdaterecord

- **表名称：** 标准成本更新任务报告-主表
- **表名：** t_sco_costupdaterecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetcosttypeid | 目标标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsrccosttypeid | 源标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftasktype | 任务类型 | varchar | 255 |  | √ | ' ' | 任务类型,枚举: cad_taskexecutelog :任务执行日志 cad_checkitem :合法性检查项 |
| 8 | fisupdatecheckpass | 仅更新合法数据 | bpchar | 1 |  | √ | '0' | 仅更新合法数据 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fnextpagepara | 页面携带参数 | varchar | 512 |  | √ | ' ' | 页面携带参数 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fupdatebillno | 更新申请单单号 | varchar | 255 |  | √ | ' ' | 更新申请单单号 |
| 14 | fisupdatecurlevel | 仅更新本层 | bpchar | 1 |  | √ | ' ' | 仅更新本层 |
| 15 | fisspecifymaterial | 指定物料更新 | bpchar | 1 |  | √ | ' ' | 指定物料更新 |
| 16 | ftask | 任务 | int8 | 64 |  | √ | 0 | [标准成本任务 sco_task](../sco_files/sco_task.md) |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costupdaterecord |  | fid |
| 2 | idx_sco_updaterecord_billno |  | fbillno |

---

## 失败物料明细-子表 t_sco_costupdatefailentry

- **表名称：** 失败物料明细-子表
- **表名：** t_sco_costupdatefailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costupdatefailentry |  | fentryid |
| 2 | idx_sco_costupdatefails_fid |  | fid |
