# 在制品分配标准-sco_proallocstd

## 在制品分配标准-主表 t_sco_proallocstd

- **表名称：** 在制品分配标准-主表
- **表名：** t_sco_proallocstd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsourceid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 7 | feffectstatus | 生效状态 | varchar | 30 |  | √ | ' ' | 生效状态,枚举: 0 :失效 1 :生效 |
| 8 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fappnum | 业务标识 | varchar | 10 |  | √ | ' ' | 业务标识 |
| 11 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 15 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_proallocstd |  | forgid,fcostaccountid |
| 2 | pk_sco_proallocstd |  | fid |

---

## 分配标准-子表 t_sco_proallocstdentry

- **表名称：** 分配标准-子表
- **表名：** t_sco_proallocstdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | funabsorbcostdriver | 未吸收费用综合分配标准 | varchar | 30 |  | √ | ' ' | 未吸收费用综合分配标准,枚举: 0 :不计算在产品成本 1 :约当完工产量 2 :约当系数 3 :按组件清单计算 4 :按在产材料盘点计算 5 :不计算完工成本 |
| 4 | fcostdriver | 结算差异综合分配标准 | varchar | 50 |  | √ | ' ' | 结算差异综合分配标准,枚举: 0 :不计算在产品成本 1 :约当完工产量 2 :约当系数 3 :按组件清单计算 4 :按在产材料盘点计算 5 :不计算完工成本 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdiffcalccostdriver | 差异分摊综合分配标准 | varchar | 30 |  | √ | ' ' | 差异分摊综合分配标准,枚举: 0 :不计算在产品成本 1 :约当完工产量 2 :约当系数 3 :按组件清单计算 4 :按在产材料盘点计算 5 :不计算完工成本 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_proallocstdentry |  | fid,fcostcenterid |
| 2 | pk_sco_proallocstdentry |  | fentryid |

---

## 成本子要素明细-子表 t_sco_proallocstdsubentry

- **表名称：** 成本子要素明细-子表
- **表名：** t_sco_proallocstdsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 2 | fcostdriverdetail | 明细项分配标准 | varchar | 50 |  | √ | ' ' | 明细项分配标准,枚举: 0 :不计算在产品成本 1 :约当完工产量 2 :约当系数 3 :按组件清单计算 4 :在产成本按材料盘点计算 5 :不计算完工成本 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fdiffcalccdriverdetail | 差异分摊明细分配标准 | varchar | 30 |  | √ | ' ' | 差异分摊明细分配标准,枚举: 0 :不计算在产品成本 1 :约当完工产量 2 :约当系数 3 :按组件清单计算 4 :按在产材料盘点计算 5 :不计算完工成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_proallocstdsubentry |  | fdetailid |
| 2 | idx_sco_proallosubentry |  | fentryid |
