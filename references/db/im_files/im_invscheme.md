# 库存事务-im_invscheme

## 出库库存状态单据体-子表 t_im_outinvstatusentry

- **表名称：** 出库库存状态单据体-子表
- **表名：** t_im_outinvstatusentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | foutinvstatusispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 6 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_outinvstatusentry |  | fid |
| 2 | pk_t_im_outinvstatusentry |  | fentryid |

---

## 库存事务-主表 t_im_invschemes

- **表名称：** 库存事务-主表
- **表名：** t_im_invschemes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 事务分组 im_invschemegroup |
| 3 | fbillformid | 单据 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | finvdc | 库存方向 | bpchar | 1 |  | √ | 'A' | 库存方向,枚举: A :普通 B :退库 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | foutkeepertype | 出库保管者类型（废弃） | varchar | 30 |  | √ | ' ' | 出库保管者类型（废弃）,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 7 | ftransceivertypeid | 收发类型 | int8 | 64 |  | √ | 0 | 收发类型 bd_transceivertype |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | finvstatusid | 入库库存状态（废弃） | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 11 | fbizdirection | 业务方向 | bpchar | 1 |  | √ | '0' | 业务方向,枚举: 0 :正向 1 :反向 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftransceiver | 收/发 | bpchar | 1 |  | √ | '0' | 收/发,枚举: 0 :收 1 :发 2 :收、发 |
| 15 | fownertype | 入库货主类型（废弃） | varchar | 30 |  | √ | ' ' | 入库货主类型（废弃）,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 16 | fisforwardamount | 是否参与存货核算 | bpchar | 1 |  | √ | '1' | 是否参与存货核算 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | foutownertype | 出库货主类型（废弃） | varchar | 30 |  | √ | ' ' | 出库货主类型（废弃）,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fkeepertype | 入库保管者类型（废弃） | varchar | 30 |  | √ | ' ' | 入库保管者类型（废弃）,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 23 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 24 | foutinvstatusid | 出库库存状态（废弃） | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 27 | fisinupdate | 入库方向设置 | bpchar | 1 |  | √ | '0' | 入库方向设置 |
| 28 | fisoutupdate | 出库方向设置 | bpchar | 1 |  | √ | '0' | 出库方向设置 |
| 29 | fisnotupdate | 不更新库存 | bpchar | 1 |  | √ | '0' | 不更新库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_invschemes_pkey |  | fid |
| 2 | idx_im_ivs_fgp |  | fgroupid |
| 3 | idx_im_ivs_fbf |  | fnumber |

---

## 出库库存类型单据体-子表 t_im_outinvtypeentry

- **表名称：** 出库库存类型单据体-子表
- **表名：** t_im_outinvtypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feoutownertype | 出库货主类型 | varchar | 50 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 3 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 4 | foutinvtypeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | feoutkeepertype | 出库保管者类型 | varchar | 50 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_outinvtypeentry_pkey |  | fentryid |
| 2 | idx_im_outt_e_fid |  | fid |

---

## 入库库存类型单据体-子表 t_im_invtypeentry

- **表名称：** 入库库存类型单据体-子表
- **表名：** t_im_invtypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fekeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 3 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | finvtypeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | feownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_intt_e_fid |  | fid |
| 2 | t_im_invtypeentry_pkey |  | fentryid |

---

## 业务类型单据体-子表 t_im_biztypeentry

- **表名称：** 业务类型单据体-子表
- **表名：** t_im_biztypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fallowmanualadd | 允许手工制单 | bpchar | 1 |  | √ | '0' | 允许手工制单 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fbiztypeid | 业务类型编码 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 5 | fbiztypeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_biztypeentry_pkey |  | fentryid |
| 2 | idx_im_bt_e_fid |  | fid |

---

## 库存事务-多语言表 t_im_invschemes_l

- **表名称：** 库存事务-多语言表
- **表名：** t_im_invschemes_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_invschemes_l_pkey |  | fpkid |
| 2 | idx_im_invs_l_fid |  | fid,flocaleid |

---

## 入库库存状态单据体-子表 t_im_invstatusentry

- **表名称：** 入库库存状态单据体-子表
- **表名：** t_im_invstatusentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 6 | finvstatusispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invstatusentry |  | fid |
| 2 | pk_t_im_invstatusentry |  | fentryid |
