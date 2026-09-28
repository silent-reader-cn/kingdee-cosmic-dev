# 在产材料归集-aca_wipcostbomputbill

## 在产材料归集-主表 t_aca_wipbomcoll

- **表名称：** 在产材料归集-主表
- **表名：** t_aca_wipbomcoll

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fendrptwipqty | 期末汇报在制数量 | numeric | 23 | 10 | √ | 0 | 期末汇报在制数量 |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fcostmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fbaseunit | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fbaseorderqty | 订单下达数量 | numeric | 23 | 10 | √ | 0 | 订单下达数量 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcompleteqty | 订单完工数量 | numeric | 23 | 10 | √ | 0 | 订单完工数量 |
| 18 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 19 | fendsfcwipqty | 期末工序在制数量 | numeric | 23 | 10 | √ | 0 | 期末工序在制数量 |
| 20 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 21 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_wipbomcoll |  | forgid,fcostaccountid |
| 2 | pk_t_aca_wipbomcoll |  | fid |

---

## 单据体-子表 t_aca_wipbomcollentry

- **表名称：** 单据体-子表
- **表名：** t_aca_wipbomcollentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrgoodrejectedqty | 本期良品退料数量 | numeric | 23 | 10 | √ | 0 | 本期良品退料数量 |
| 3 | fbusdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 4 | fcurrbadincomerejectedqty | 本期来料不良退料数量 | numeric | 23 | 10 | √ | 0 | 本期来料不良退料数量 |
| 5 | fmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fstandqty | 标准用料数量 | numeric | 23 | 10 | √ | 0 | 标准用料数量 |
| 7 | fendadjqty | 期末调整数量 | numeric | 23 | 10 | √ | 0 | 期末调整数量 |
| 8 | fbadtaskrejectedqty | 累计作业不良退料数量 | numeric | 23 | 10 | √ | 0 | 累计作业不良退料数量 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fgoodrejectedqty | 累计良品退料数量 | numeric | 23 | 10 | √ | 0 | 累计良品退料数量 |
| 11 | fcurrbadtaskrejectedqty | 本期作业不良退料数量 | numeric | 23 | 10 | √ | 0 | 本期作业不良退料数量 |
| 12 | ffeedingqty | 累计补料数量 | numeric | 23 | 10 | √ | 0 | 累计补料数量 |
| 13 | fdatasourcetype | 数据来源 | bpchar | 1 |  | √ | ' ' | 数据来源,枚举: 0 :手工修改 1 :自动生成 |
| 14 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 15 | fbadincomerejectedqty | 累计来料不良退料数量 | numeric | 23 | 10 | √ | 0 | 累计来料不良退料数量 |
| 16 | fpdstartqty | 期初在产品数量 | numeric | 23 | 10 | √ | 0 | 期初在产品数量 |
| 17 | factissueqty | 累计已领数量 | numeric | 23 | 10 | √ | 0 | 累计已领数量 |
| 18 | fpdendqty | 期末在产品数量 | numeric | 23 | 10 | √ | 0 | 期末在产品数量 |
| 19 | fwipruleid | 计算规则 | int8 | 64 |  | √ | 0 | [在产材料归集计算规则 aca_wipbomrule](../aca_files/aca_wipbomrule.md) |
| 20 | fstartadjqty | 期初调整数量 | numeric | 23 | 10 | √ | 0 | 期初调整数量 |
| 21 | fneedbaseqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 22 | fcurrrejectedqty | 本期退料数量（合计）数量 | numeric | 23 | 10 | √ | 0 | 本期退料数量（合计）数量 |
| 23 | fuseratio | 子项使用比例 | numeric | 23 | 10 | √ | 0 | 子项使用比例 |
| 24 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fmodifyrowdate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 26 | frejectedqty | 累计退料数量（合计）数量 | numeric | 23 | 10 | √ | 0 | 累计退料数量（合计）数量 |
| 27 | fcurrfeedingqty | 本期补料数量 | numeric | 23 | 10 | √ | 0 | 本期补料数量 |
| 28 | fbusnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 29 | fcurrcomqty | 本期完工数量 | numeric | 23 | 10 | √ | 0 | 本期完工数量 |
| 30 | fcurractissueqty | 本期已领数量 | numeric | 23 | 10 | √ | 0 | 本期已领数量 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fmodifierowrid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fpdcurrqty | 本期投入数量 | numeric | 23 | 10 | √ | 0 | 本期投入数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_wipbomcollentry |  | fid |
| 2 | pk_t_aca_wipbomcollentry |  | fentryid |

---

## 在产材料归集-多语言表 t_aca_wipbomcoll_l

- **表名称：** 在产材料归集-多语言表
- **表名：** t_aca_wipbomcoll_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_wipbomcoll_l |  | fpkid |
| 2 | idx_aca_wipbomcoll_l |  | fid,flocaleid |
