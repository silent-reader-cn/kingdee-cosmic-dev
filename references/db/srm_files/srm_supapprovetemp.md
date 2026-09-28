# 临时供应商申请-srm_supapprovetemp

## 临时供应商申请-主表 t_pur_tempapprove

- **表名称：** 临时供应商申请-主表
- **表名：** t_pur_tempapprove

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftempstatus | 临时生效状态 | bpchar | 1 |  | √ | ' ' | 临时生效状态,枚举: A :待生效 B :已生效 C :已失效 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 |
| 6 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbdsupplier | 供应商(主数据) | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 16 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fapplyreason | 申请原因 | varchar | 512 |  | √ | ' ' | 申请原因 |
| 19 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 20 | fremaindate | 剩余可用天数 | int4 | 32 |  | √ | 0 | 剩余可用天数 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_tempapprove_billno |  | fbillno |
| 2 | pk_t_pur_tempapprove |  | fid |
| 3 | idx_pur_tempapprove_supp |  | fsupplierid |
| 4 | idx_pur_tempapprove_org |  | forgid |

---

## 临时供应商申请-关联追踪表 t_pur_tempapprove_tc

- **表名称：** 临时供应商申请-关联追踪表
- **表名：** t_pur_tempapprove_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_tempapprove_tc |  | fid |
| 2 | idx_pur_tempapprove_tc_tid |  | ftid |
| 3 | idx_pur_tempapprove_tc_tbill |  | ftbillid |

---

## 临时供应商申请-反写记录表 t_pur_tempapprove_wb

- **表名称：** 临时供应商申请-反写记录表
- **表名：** t_pur_tempapprove_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_tempapprove_wb_fk |  | fid |
| 2 | pk_pur_tempapprove_wb |  | fentryid |

---

## 关联子实体-子表 t_pur_tempapprove_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_tempapprove_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_tempapprove_lk |  | fpkid |
| 2 | idx_pur_tempapprove_lk_fk |  | fid |

---

## 临时供应商申请-多语言表 t_pur_tempapprove_l

- **表名称：** 临时供应商申请-多语言表
- **表名：** t_pur_tempapprove_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_tempapprove_lfid |  | fid,flocaleid |
| 2 | pk_t_pur_tempapprove_l |  | fpkid |
