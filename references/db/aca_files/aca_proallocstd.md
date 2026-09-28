# 在产品分配标准-aca_proallocstd

## 成本子要素明细-子表 t_aca_proallocstdsubentry

- **表名称：** 成本子要素明细-子表
- **表名：** t_aca_proallocstdsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 2 | fcostdriverdetail | 明细项分配标准 | varchar | 30 |  | √ | ' ' | 明细项分配标准,枚举: 0 :不计算在产品成本 1 :约当完工产量 2 :约当系数 3 :按用料清单计算 5 :在产材料归集 4 :在产材料盘点 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_proallocstdsubentry |  | fdetailid |
| 2 | idk_aca_proallocstdsubentry |  | fentryid,fseq |
| 3 | idx_passube_sube |  | fsubelementid |

---

## 分配标准-子表 t_aca_proallocstdentry

- **表名称：** 分配标准-子表
- **表名：** t_aca_proallocstdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fcostdriver | 综合分配标准 | varchar | 30 |  | √ | ' ' | 综合分配标准,枚举: 0 :不计算在产品成本 1 :约当完工产量 2 :约当系数 3 :按用料清单计算 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_proallocstdentry |  | fentryid |
| 2 | idk_aca_proallocstdentry |  | fid,fseq |
| 3 | idx_pasentry_costc |  | fcostcenterid |

---

## 在产品分配标准-主表 t_aca_proallocstd

- **表名称：** 在产品分配标准-主表
- **表名：** t_aca_proallocstd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsourceid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 7 | feffectstatus | 生效状态 | varchar | 50 |  | √ | '1' | 生效状态,枚举: 0 :失效 1 :生效 |
| 8 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fappnum | 业务标识 | varchar | 50 |  | √ | ' ' | 业务标识 |
| 11 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 15 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idk_aca_proallocstd |  | forgid,fcostaccountid |
| 2 | pk_t_aca_proallocstd |  | fid |
