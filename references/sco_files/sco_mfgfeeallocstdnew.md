# 成本中心间费用分配标准-sco_mfgfeeallocstdnew

## 成本中心间费用分配标准-多语言表 t_sco_mfgfeeallocstd_l

- **表名称：** 成本中心间费用分配标准-多语言表
- **表名：** t_sco_mfgfeeallocstd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgfeeallocstd_l |  | fpkid |
| 2 | idx_sco_mfgfeeallocstd_l |  | fid,flocaleid |

---

## 受益成本中心-子表 t_sco_mfgfeeallocstdsuben

- **表名称：** 受益成本中心-子表
- **表名：** t_sco_mfgfeeallocstdsuben

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcentergroupid | 成本中心组编码 | int8 | 64 |  | √ | 0 | 成本中心组 cad_costcentergroup |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
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
| 1 | pk_sco_mfgfeeallocstdsuben |  | fdetailid |
| 2 | idx_sco_mfgfeeallocstdsuben |  | fentryid,fbenefcostcenterid |

---

## 成本中心间费用分配标准-主表 t_sco_mfgfeeallocstd

- **表名称：** 成本中心间费用分配标准-主表
- **表名：** t_sco_mfgfeeallocstd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcostcentergroupid | 成本中心组 | int8 | 64 |  | √ | 0 | 成本中心组 cad_costcentergroup |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fallocmold | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 10 | fissender | 按成本中心设置发送方 | bpchar | 1 |  | √ | '0' | 按成本中心设置发送方 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sco :标准成本 aca :实际成本 eca :服务成本 |
| 13 | fexecondition | 执行条件 | varchar | 30 |  | √ | ' ' | 执行条件,枚举: NO_WORK :当期无工时投入执行 NO_COM :当期无完工执行 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fisbeneficiary | 按成本中心设置受益方 | bpchar | 1 |  | √ | '0' | 按成本中心设置受益方 |
| 16 | fnoproduction | 当期无工时投入执行 | bpchar | 1 |  | √ | '0' | 当期无工时投入执行 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fisexpense | 按费用项目设置分配标准 | bpchar | 1 |  | √ | '0' | 按费用项目设置分配标准 |
| 19 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 20 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgfeeallocstd |  | fid |
| 2 | idx_sco_mfgfeeallocstd |  | forgid,fcostcenterid |

---

## 分配标准设置-子表 t_sco_mfgfeeallocstdentry

- **表名称：** 分配标准设置-子表
- **表名：** t_sco_mfgfeeallocstdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fproductgroupid | fproductgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 sco_costdriver |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_mfgfeeallocstdentry |  | fid,fcostdriverid,fexpenseitemid |
| 2 | pk_sco_mfgfeeallocstdentry |  | fentryid |
