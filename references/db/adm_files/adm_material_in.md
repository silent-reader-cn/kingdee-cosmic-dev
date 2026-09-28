# 物料试用-adm_material_in

## 物料试用-多语言表 t_pur_material_l

- **表名称：** 物料试用-多语言表
- **表名：** t_pur_material_l

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
| 1 | t_pur_material_l_pkey |  | fpkid |
| 2 | idx_pur_material_l_fid |  | fid,flocaleid |

---

## 物料试用-分表 t_pur_material_a

- **表名称：** 物料试用-分表
- **表名：** t_pur_material_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_material_a_ftime |  | fcreatetime |
| 2 | t_pur_material_a_pkey |  | fid |

---

## 物料试用-主表 t_pur_material

- **表名称：** 物料试用-主表
- **表名：** t_pur_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 7 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 9 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 10 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 |
| 11 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 12 | fcertifiapplyid | 认证申请单号 | int8 | 64 |  | √ | 0 | 供应商认证申请编号 pbd_certificationapplyno |
| 13 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 5 :物料试用 |
| 14 | ftype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 0 :邀约注册 1 :公开注册 |
| 15 | ftryresult | 试用结果 | bpchar | 1 |  | √ | ' ' | 试用结果,枚举: 1 :合格 2 :不合格 |
| 16 | faptitudenoid | 资审审查单号 | int8 | 64 |  | √ | 0 | 资质审查单号 srm_aptitudebillno |
| 17 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_material_fbilldate |  | fbilldate |
| 2 | idx_pur_material_fbillno |  | fbillno |
| 3 | idx_pur_material_aptitudeid |  | faptitudenoid |
| 4 | t_pur_material_pkey |  | fid |

---

## 物料分录-子表 t_pur_materialentry

- **表名称：** 物料分录-子表
- **表名：** t_pur_materialentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 3 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | funitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fnumber | fnumber | numeric | 19 | 6 | √ | 0.000000 |  |
| 9 | fcount | 第几次试用 | int8 | 64 |  | √ | 0 | 第几次试用 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | funit | funit | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_material_fid_fseq |  | fid,fseq |
| 2 | t_pur_materialentry_pkey |  | fentryid |
