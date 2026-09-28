# 约当系数维护-aca_equivalent

## 约当系数维护-主表 t_aca_equivalent

- **表名称：** 约当系数维护-主表
- **表名：** t_aca_equivalent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织(202306多核算体系改造废弃) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmakeuserid | fmakeuserid | int8 | 64 |  | √ | 0 |  |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | fmaketime | fmaketime | timestamp | 0 |  |  | null |  |
| 14 | fbillno | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_equivalent |  | fid |
| 2 | idx_t_aca_equivalent |  | forgid,fcostaccountid |

---

## 综合约当系数-子表 t_aca_equivalententry

- **表名称：** 综合约当系数-子表
- **表名：** t_aca_equivalententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | ftotalvalen | 综合约当系数 | numeric | 23 | 10 | √ | 0 | 综合约当系数 |
| 4 | fmaterialid | 产品编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_equivalententry |  | fentryid |
| 2 | idx_t_aca_equivalententry |  | fid,fcostcenterid |
| 3 | idx_eqvaentry_costaobj |  | fcostobjectid |

---

## 明细约当系数-子表 t_aca_entitydetail

- **表名称：** 明细约当系数-子表
- **表名：** t_aca_entitydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 2 | fdetailvalen | 明细约当系数 | numeric | 23 | 10 | √ | 0 | 明细约当系数 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_entitydetail |  | fdetailid |
| 2 | idx_t_aca_entitydetail |  | fentryid |
