# 质量变更管理-srm_quality

## 供应商联系人-子表 t_pur_quality_link

- **表名称：** 供应商联系人-子表
- **表名：** t_pur_quality_link

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 3 | fphone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 4 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 5 | fgender | 性别 | bpchar | 1 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 |
| 6 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 7 | fdept | 部门 | varchar | 50 |  | √ | ' ' | 部门 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fmobile | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 11 | fduty | 职务 | varchar | 50 |  | √ | ' ' | 职务 |
| 12 | fpost | 邮编 | varchar | 10 |  | √ | ' ' | 邮编 |
| 13 | ffax | 传真 | varchar | 50 |  | √ | ' ' | 传真 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fisdefault | 默认 | bpchar | 1 |  | √ | ' ' | 默认 |
| 16 | fbizscope | 负责业务 | varchar | 50 |  | √ | ' ' | 负责业务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_quality_link_fid |  | fid,fseq |
| 2 | t_pur_quality_link_pkey |  | fentryid |

---

## 质量变更管理-多语言表 t_pur_quality_l

- **表名称：** 质量变更管理-多语言表
- **表名：** t_pur_quality_l

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
| 1 | t_pur_quality_l_pkey |  | fpkid |
| 2 | idx_pur_quality_l_fid |  | fid,flocaleid |

---

## 质量变更管理-分表 t_pur_quality_a

- **表名称：** 质量变更管理-分表
- **表名：** t_pur_quality_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcfmopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fcfmdate | 审批时间 | timestamp | 0 |  |  | null | 审批时间 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcfmid | 审批人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_quality_a_ftime |  | fcreatetime |
| 2 | t_pur_quality_a_pkey |  | fid |

---

## 生产工艺-子表 t_pur_quality_tech

- **表名称：** 生产工艺-子表
- **表名：** t_pur_quality_tech

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类别 | bpchar | 1 |  | √ | ' ' | 类别,枚举: 1 :变更前 2 :变更后 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnote | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fprocess | 工序 | varchar | 50 |  | √ | ' ' | 工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_quality_tech_pkey |  | fentryid |
| 2 | idx_pur_quality_tech_fid |  | fid,fseq |

---

## 运输方式-子表 t_pur_quality_ship

- **表名称：** 运输方式-子表
- **表名：** t_pur_quality_ship

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类别 | bpchar | 1 |  | √ | ' ' | 类别,枚举: 1 :变更前 2 :变更后 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnote | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_quality_ship_fid |  | fid,fseq |
| 2 | t_pur_quality_ship_pkey |  | fentryid |

---

## 管理体系-子表 t_pur_quality_manage

- **表名称：** 管理体系-子表
- **表名：** t_pur_quality_manage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypeid | 体系类型 | int8 | 64 |  | √ | 0 | [供应商辅助资料 srm_extdata](../pbd_files/srm_extdata.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fdateto | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fauditdate | 审核通过日期 | timestamp | 0 |  |  | null | 审核通过日期 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fauditorg | 审核单位 | varchar | 100 |  | √ | ' ' | 审核单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_quality_manage_pkey |  | fentryid |
| 2 | idx_pur_quality_manage_fid |  | fid,fseq |

---

## 原材料-子表 t_pur_quality_mat

- **表名称：** 原材料-子表
- **表名：** t_pur_quality_mat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 原材料名称 | varchar | 100 |  | √ | ' ' | 原材料名称 |
| 3 | fmodel | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 4 | ftype | ftype | bpchar | 1 |  | √ | ' ' |  |
| 5 | fsupmodel_new | 变更后厂商型号 | varchar | 100 |  | √ | ' ' | 变更后厂商型号 |
| 6 | fsupmodel | 原厂商型号 | varchar | 100 |  | √ | ' ' | 原厂商型号 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 说明 | varchar | 100 |  | √ | ' ' | 说明 |
| 9 | fsupname | 原厂商 | varchar | 100 |  | √ | ' ' | 原厂商 |
| 10 | fsupname_new | 变更后厂商 | varchar | 100 |  | √ | ' ' | 变更后厂商 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_quality_mat_pkey |  | fentryid |
| 2 | idx_pur_quality_mat_fid |  | fid,fseq |

---

## 包装方式-子表 t_pur_quality_pack

- **表名称：** 包装方式-子表
- **表名：** t_pur_quality_pack

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类别 | bpchar | 1 |  | √ | ' ' | 类别,枚举: 1 :变更前 2 :变更后 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnote | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_quality_pack_fid |  | fid,fseq |
| 2 | t_pur_quality_pack_pkey |  | fentryid |

---

## 生产设备-子表 t_pur_quality_equip

- **表名称：** 生产设备-子表
- **表名：** t_pur_quality_equip

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fequip1 | 设备1 | varchar | 100 |  | √ | ' ' | 设备1 |
| 3 | fsupplier4 | 设备厂商 | varchar | 100 |  | √ | ' ' | 设备厂商 |
| 4 | fsupplier5 | 设备厂商 | varchar | 100 |  | √ | ' ' | 设备厂商 |
| 5 | fsupplier2 | 设备厂商 | varchar | 100 |  | √ | ' ' | 设备厂商 |
| 6 | fsupplier3 | 设备厂商 | varchar | 100 |  | √ | ' ' | 设备厂商 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | fnote | varchar | 100 |  | √ | ' ' |  |
| 9 | fequip2 | 设备2 | varchar | 100 |  | √ | ' ' | 设备2 |
| 10 | fequip3 | 设备3 | varchar | 100 |  | √ | ' ' | 设备3 |
| 11 | fequip4 | 设备4 | varchar | 100 |  | √ | ' ' | 设备4 |
| 12 | fequip5 | 设备5 | varchar | 100 |  | √ | ' ' | 设备5 |
| 13 | ftype | 类别 | bpchar | 1 |  | √ | ' ' | 类别,枚举: 1 :变更前 2 :变更后 |
| 14 | fsupplier1 | 设备厂商 | varchar | 100 |  | √ | ' ' | 设备厂商 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_quality_equip_pkey |  | fentryid |
| 2 | idx_pur_quality_equip_fid |  | fid,fseq |

---

## 质量变更管理-主表 t_pur_quality

- **表名称：** 质量变更管理-主表
- **表名：** t_pur_quality

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fsubject | 变更主题 | varchar | 255 |  | √ | ' ' | 变更主题 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: C :已审核 |
| 5 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcfmstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :待审批 B :审批通过 C :审批驳回 |
| 13 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 14 | fchgtypeid | 变更类型 | int8 | 64 |  | √ | 0 | [供应商辅助资料 srm_extdata](../pbd_files/srm_extdata.md) |
| 15 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_quality_pkey |  | fid |
| 2 | idx_pur_quality_fbilldate |  | fbilldate |
| 3 | idx_pur_quality_fbillno |  | fbillno |

---

## 储存方式-子表 t_pur_quality_store

- **表名称：** 储存方式-子表
- **表名：** t_pur_quality_store

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类别 | bpchar | 1 |  | √ | ' ' | 类别,枚举: 1 :变更前 2 :变更后 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnote | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_quality_store_fid |  | fid,fseq |
| 2 | t_pur_quality_store_pkey |  | fentryid |
