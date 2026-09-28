# 成本中心内费用分配标准-sca_overheadallotcost

## 产品明细-子表 t_sca_allocprosubentry

- **表名称：** 产品明细-子表
- **表名：** t_sca_allocprosubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fproductid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_allocprosubentry |  | fentryid |
| 2 | pk_t_sca_allocprosubentry |  | fdetailid |

---

## 受益成本中心-子表 t_sca_overheadallotbenefi

- **表名称：** 受益成本中心-子表
- **表名：** t_sca_overheadallotbenefi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcentergroupid | 成本中心组编码 | int8 | 64 |  | √ | 0 | 成本中心组 cad_costcentergroup |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fbenefcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_overheadallotbenefi |  | fdetailid |
| 2 | idx_sca_overheadallotbenefi |  | fentryid,fseq |

---

## 成本中心内费用分配标准-主表 t_sca_overheadallotcost

- **表名称：** 成本中心内费用分配标准-主表
- **表名：** t_sca_overheadallotcost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fcostcentergroupid | 成本中心组 | int8 | 64 |  | √ | 0 | 成本中心组 cad_costcentergroup |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fallocmold | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 E :委外生产分配 |
| 10 | fissender | 按成本中心设置发送方 | bpchar | 1 |  | √ | '0' | 按成本中心设置发送方 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 eca :服务成本 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fisbeneficiary | 按成本中心设置受益方 | bpchar | 1 |  | √ | '0' | 按成本中心设置受益方 |
| 15 | fnoproduction | 当期无工时投入执行 | bpchar | 1 |  | √ | '0' | 当期无工时投入执行 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fisexpense | 按费用项目设置分配标准 | bpchar | 1 |  | √ | '0' | 按费用项目设置分配标准 |
| 18 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 19 | fxkcostaccountid | fxkcostaccountid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_overheadallotcost |  | fid |
| 2 | idx_sca_overheadallotcost |  | forgid |

---

## 分配标准设置-子表 t_sca_overheadallotentry

- **表名称：** 分配标准设置-子表
- **表名：** t_sca_overheadallotentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fproductitem | 产品组 | int8 | 64 |  | √ | 0 | 产品组 cad_productintogroup |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 cad_costdriver |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_overheadallotentry |  | fentryid |
| 2 | idx_sca_overheadallotentry |  | fid,fseq |

---

## 成本中心内费用分配标准-多语言表 t_sca_overheadallotcost_l

- **表名称：** 成本中心内费用分配标准-多语言表
- **表名：** t_sca_overheadallotcost_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_overheadallotcost_l |  | fid,flocaleid |
| 2 | pk_t_sca_overheadallotcost_l |  | fpkid |
