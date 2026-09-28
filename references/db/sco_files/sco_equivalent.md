# 约当系数维护-sco_equivalent

## 综合约当系数-子表 t_sco_equivalententry

- **表名称：** 综合约当系数-子表
- **表名：** t_sco_equivalententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedatapropfield1 | fbasedatapropfield1 | varchar | 50 |  | √ | ' ' |  |
| 3 | fcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | ftotalvalen | 综合约当系数 | numeric | 23 | 10 | √ | 0 | 综合约当系数 |
| 5 | fmaterialid | 产品编号 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fbasedatapropfield4 | fbasedatapropfield4 | varchar | 50 |  | √ | ' ' |  |
| 7 | fbasedatapropfield2 | fbasedatapropfield2 | varchar | 50 |  | √ | ' ' |  |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdiffcalctotalvalen | 差异分摊综合约当系数 | numeric | 23 | 10 | √ | 0 | 差异分摊综合约当系数 |
| 10 | fbasedatapropfield7 | fbasedatapropfield7 | varchar | 50 |  | √ | ' ' |  |
| 11 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 12 | fbasedatapropfield6 | fbasedatapropfield6 | varchar | 50 |  | √ | ' ' |  |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_equivalententry |  | fid,fcostobjectid |
| 2 | pk_sco_equivalententry |  | fentryid |

---

## 约当系数维护-主表 t_sco_equivalent

- **表名称：** 约当系数维护-主表
- **表名：** t_sco_equivalent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织(20240613版本多核算体系废弃) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_equivalent |  | fid |
| 2 | idx_sco_equivalent |  | forgid,fcostaccountid |

---

## 明细约当系数-子表 t_sco_entitydetail

- **表名称：** 明细约当系数-子表
- **表名：** t_sco_entitydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 2 | fdetailvalen | 明细约当系数 | numeric | 23 | 10 | √ | 0 | 明细约当系数 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdiffcalcdetailvalen | 差异分摊明细约当系数 | numeric | 23 | 10 | √ | 0 | 差异分摊明细约当系数 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_entitydetail |  | fdetailid |
| 2 | idx_sco_entitydetail |  | fentryid |
