# 成本中心间费用分配标准-sca_mfgfeeallocstdnew

## 成本中心间费用分配标准-多语言表 t_sca_mfgfeeallocstd_l

- **表名称：** 成本中心间费用分配标准-多语言表
- **表名：** t_sca_mfgfeeallocstd_l

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
| 1 | index_sca_mfgfeeallocstd_l |  | fid,flocaleid |
| 2 | t_sca_mfgfeeallocstd_l_pkey |  | fpkid |
| 3 | idx_sca_mfgfeeallocstd_l |  | fid,flocaleid |

---

## 分配标准设置-子表 t_sca_mfgfeeallocstdentry

- **表名称：** 分配标准设置-子表
- **表名：** t_sca_mfgfeeallocstdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fproductgroupid | fproductgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_mfgfeeallocstdentry |  | fid,fcostdriverid,fexpenseitemid |
| 2 | index_sca_mfgallocstdentry |  | fexpenseitemid,fcostdriverid |
| 3 | pk_t_sca_mfgfeeallocstdentry |  | fentryid |

---

## 成本中心间费用分配标准-主表 t_sca_mfgfeeallocstd

- **表名称：** 成本中心间费用分配标准-主表
- **表名：** t_sca_mfgfeeallocstd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcostcentergroupid | 成本中心组 | int8 | 64 |  | √ | 0 | [成本中心组 cad_costcentergroup](../aca_files/cad_costcentergroup.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fallocmold | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 10 | fissender | 按成本中心设置发送方 | bpchar | 1 |  | √ | '0' | 按成本中心设置发送方 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 eca :服务成本 |
| 13 | fexecondition | 执行条件 | varchar | 30 |  | √ | ' ' | 执行条件,枚举: NO_WORK :当期无工时投入执行 NO_COM :当期无完工执行 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fisbeneficiary | 按成本中心设置受益方 | bpchar | 1 |  | √ | '0' | 按成本中心设置受益方 |
| 16 | fnoproduction | 当期无工时投入执行 | bpchar | 1 |  | √ | '0' | 当期无工时投入执行 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fisexpense | 按费用项目设置分配标准 | bpchar | 1 |  | √ | '0' | 按费用项目设置分配标准 |
| 19 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 20 | fxkcostaccountid | fxkcostaccountid | int8 | 64 |  | √ | 0 |  |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sca_mfgfeeallocstd |  | forgid,fcostcenterid |
| 2 | t_sca_mfgfeeallocstd_pkey |  | fid |
| 3 | idx_sca_mfgfeeallocstd |  | forgid,fcostcenterid |

---

## 受益成本中心-子表 t_sca_mfgfeeallocstdsuben

- **表名称：** 受益成本中心-子表
- **表名：** t_sca_mfgfeeallocstdsuben

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcentergroupid | 成本中心组编码 | int8 | 64 |  | √ | 0 | [成本中心组 cad_costcentergroup](../aca_files/cad_costcentergroup.md) |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fbenefcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_mfgfeeallocstdsuben |  | fentryid,fbenefcostcenterid |
| 2 | index_sca_mfgallocstdsuen |  | fentryid,fbenefcostcenterid |
| 3 | t_sca_mfgfeeallocstdsuben_pkey |  | fdetailid |
