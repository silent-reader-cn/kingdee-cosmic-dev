# 自定义费用分配标准值维护-sca_diycostdriver

## 自定义费用分配标准值维护-主表 t_sca_diycostdriver

- **表名称：** 自定义费用分配标准值维护-主表
- **表名：** t_sca_diycostdriver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsourceid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 5 | feffectstatus | 生效状态 | varchar | 30 |  | √ | ' ' | 生效状态,枚举: A :未生效 E :已生效 F :已失效 |
| 6 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 7 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 8 | fcostbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 14 | fcostdriverid | 费用分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 cad_costdriver |
| 15 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 16 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fexpperiodid | 失效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 23 | fmaterialgroupstdid | 物料分类标准 | int8 | 64 |  | √ | 0 | 物料分类标准 bd_materialgroupstandard |
| 24 | feffectperiodid | 生效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 25 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_diycostdriver |  | forgid,fcostcenterid,fcostdriverid |
| 2 | t_sca_diycostdriver_pkey |  | fid |
| 3 | idx_t_sca_diycostdriver_o_c_f |  | forgid,fcostaccountid,fcostcenterid |

---

## 自定义费用分配标准值维护-多语言表 t_sca_diycostdriver_l

- **表名称：** 自定义费用分配标准值维护-多语言表
- **表名：** t_sca_diycostdriver_l

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
| 1 | idx_sca_diycostdriver_l |  | flocaleid,fremark |
| 2 | t_sca_diycostdriver_l_pkey |  | fpkid |

---

## 单据体-子表 t_sca_diycostdriverentry

- **表名称：** 单据体-子表
- **表名：** t_sca_diycostdriverentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatnumid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 4 | fentryqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 5 | fmaterialid | 产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fmatauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_diycostdriverentry_pkey |  | fentryid |
| 2 | idx_sca_diycostdriverentry |  | fbenefcostcenterid,fcostobjectid |
| 3 | idx_sca_diycostdriverentry2 |  | fid |
