# 印章-fmm_seal

## 印章-主表 t_fmm_seal

- **表名称：** 印章-主表
- **表名：** t_fmm_seal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | frepertorynum | 在库数量 | int4 | 32 |  | √ | 0 | 在库数量 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fconferdate | 授予日期 | timestamp | 0 |  |  | null | 授予日期 |
| 13 | fsealsample | 印章样本 | varchar | 255 |  | √ | ' ' | 印章样本 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fsealtypeid | 印章类别 | int8 | 64 |  | √ | 0 | 印章类别 fmm_seal_type |
| 20 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fownerid | 持有人工号 | int8 | 64 |  | √ | 0 | 企业人力资源池 pmbd_enterprise_hm_res_po |
| 22 | fsignsample | 签名样本 | varchar | 255 |  | √ | ' ' | 签名样本 |
| 23 | fconfernum | 授予数量 | int4 | 32 |  | √ | 0 | 授予数量 |
| 24 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 印章编号 | varchar | 50 |  | √ | ' ' | 印章编号 |
| 26 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_seal_fcreatetime |  | fcreatetime |
| 2 | idx_fmm_seal_fnumber |  | fnumber |
| 3 | idx_t_fmm_seal_createorg |  | fcreateorgid |
| 4 | idx_t_fmm_seal_master |  | fmasterid |
| 5 | pk_fmm_seal |  | fid |

---

## 印章-多语言表 t_fmm_seal_l

- **表名称：** 印章-多语言表
- **表名：** t_fmm_seal_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_seall_fid |  | fid,flocaleid |
| 2 | idx_fmm_seall_fname |  | fname |
| 3 | pk_fmm_seal_l |  | fpkid |

---

## 印章-使用范围位图表 t_fmm_seal_m

- **表名称：** 印章-使用范围位图表
- **表名：** t_fmm_seal_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fmm_seal_m |  | forgid |

---

## 印章-使用范围表 t_fmm_seal_u

- **表名称：** 印章-使用范围表
- **表名：** t_fmm_seal_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fmm_seal_u_uo |  | fuseorgid |
| 2 | pk_t_fmm_seal_u |  | fdataid,fuseorgid |
