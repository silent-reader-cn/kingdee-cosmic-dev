# 缺料运算记录-mrp_smacalcrecord

## 缺料运算记录-主表 t_mrp_smacalcrecord

- **表名称：** 缺料运算记录-主表
- **表名：** t_mrp_smacalcrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsubstituted | 物料替代 | varchar | 50 |  | √ | ' ' | 物料替代,枚举: 1 :考虑替代 0 :忽略替代 |
| 4 | fcreatetime | 运算时间 | timestamp | 0 |  |  | null | 运算时间 |
| 5 | fsmaid | 缺料单id | int8 | 64 |  | √ | 0 | 缺料单id |
| 6 | fcalculateid | 本次计算id | varchar | 50 |  | √ | ' ' | 本次计算id |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ffexceptcheck | 收料忽略质检结果 | bpchar | 1 |  | √ | '0' | 收料忽略质检结果 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | freserved | 考虑预留 | varchar | 50 |  | √ | ' ' | 考虑预留,枚举: 0 :忽略弱预留 1 :考虑弱预留 2 :仅考虑库存强预留 |
| 11 | fcalcelapsedtime | 计算耗时(秒) | varchar | 50 |  | √ | '0' | 计算耗时(秒) |
| 12 | fprioritytype | 优先顺序 | varchar | 50 |  | √ | ' ' | 优先顺序,枚举: demandpriority :需求优先级 planbegintime :计划开工日期 planendtime :计划完工日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fisincludetransstk | 强制考虑调拨仓库 | bpchar | 1 |  | √ | '0' | 强制考虑调拨仓库 |
| 15 | fisincludeppbomstk | 强制考虑领料仓库 | bpchar | 1 |  | √ | '0' | 强制考虑领料仓库 |
| 16 | fmatchowner | 匹配供应考虑货主和货主类型 | bpchar | 1 |  | √ | '0' | 匹配供应考虑货主和货主类型 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smacalcrecord |  | fid |
| 2 | idx_mrp_smacalcrecord |  | fsmaid |

---

## 单据体-子表 t_mrp_smacalcrecordentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_smacalcrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fmaterial | 物料范围 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fwarehouseid | 仓库范围 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | forg | 组织范围 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smacalcrecordentry |  | fentryid |
| 2 | idx_mrp_smacalcrecordentry |  | fid,fseq |
