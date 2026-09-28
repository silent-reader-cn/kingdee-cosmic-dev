# 生产成本更新差异单-cad_costrenewaldif

## 生产成本更新差异单-主表 t_cad_costrenewaldif

- **表名称：** 生产成本更新差异单-主表
- **表名：** t_cad_costrenewaldif

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcostaccountbook | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 6 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | frenewreqno | 更新申请单号 | varchar | 80 |  | √ | ' ' | 更新申请单号 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmanbuild | 手工创建 | varchar | 1 |  | √ | '0' | 手工创建 |
| 10 | forg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 14 | feffecttime | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fperiod | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 16 | fbillno | 更新差异单号 | varchar | 80 |  | √ | ' ' | 更新差异单号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_costrenewaldif |  | fid |
| 2 | idx_cad_costrenewaldif |  | frenewreqno,fcostaccountbook |

---

## 单据体-子表 t_cad_difdtlentry

- **表名称：** 单据体-子表
- **表名：** t_cad_difdtlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadditionamt | 外协加工费 | numeric | 23 | 10 | √ | 0.0000000000 | 外协加工费 |
| 3 | fmaterielcode | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fmaterialfee | 物料费用 | numeric | 23 | 10 | √ | 0.0000000000 | 物料费用 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fresourceamt | 资源 | numeric | 23 | 10 | √ | 0.0000000000 | 资源 |
| 7 | fmaterialamt | 物料 | numeric | 23 | 10 | √ | 0.0000000000 | 物料 |
| 8 | fmakeamt | 制造费用 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用 |
| 9 | fupdatediff | 更新差异金额 | numeric | 23 | 10 | √ | 0.0000000000 | 更新差异金额 |
| 10 | fprocsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fcostobject | 成本核算对象编码 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_difdtlentry |  | fid |
| 2 | pk_t_cad_difdtlentry |  | fentryid |
