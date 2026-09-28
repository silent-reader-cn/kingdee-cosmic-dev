# 客户物料对应表-bd_customermaterial

## 单据体-子表 t_bd_customermaterialinfo

- **表名称：** 单据体-子表
- **表名：** t_bd_customermaterialinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcusmatmod | 客户物料规格型号 | varchar | 255 |  | √ | ' ' | 客户物料规格型号 |
| 3 | fcusmatgroupnumber | 客户物料分组编码 | varchar | 50 |  | √ | ' ' | 客户物料分组编码 |
| 4 | fismatch | 默认携带 | bpchar | 1 |  | √ | '0' | 默认携带 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fcusmatname | 客户物料名称 | varchar | 255 |  | √ | ' ' | 客户物料名称 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fcusmatgroupname | 客户物料分组名称 | varchar | 500 |  | √ | ' ' | 客户物料分组名称 |
| 10 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 11 | fentrycomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 12 | fcusmatid | 客户物料编码 | varchar | 255 |  | √ | ' ' | 客户物料编码 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_customermaterialinfo |  | fentryid |
| 2 | idx_bd_customermaterialinfo_fk |  | fid |

---

## 单据体-多语言表 t_bd_customermaterialinfo_l

- **表名称：** 单据体-多语言表
- **表名：** t_bd_customermaterialinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcusmatmod | 客户物料规格型号 | varchar | 255 |  | √ | ' ' | 客户物料规格型号 |
| 2 | fcusmatname | 客户物料名称 | varchar | 255 |  | √ | ' ' | 客户物料名称 |
| 3 | fentrycomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fcusmatgroupname | 客户物料分组名称 | varchar | 500 |  | √ | ' ' | 客户物料分组名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_customermaterialinfo_l |  | fentryid,flocaleid |
| 2 | pk_t_bd_customermaterialinfo_l |  | fpkid |

---

## 客户分类-多选基础资料表 t_bd_customermaterial_grp

- **表名称：** 客户分类-多选基础资料表
- **表名：** t_bd_customermaterial_grp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 客户分类 bd_customergroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_customermaterial_grp |  | fpkid |
| 2 | idx_bd_customermaterial_grp_fk |  | fid |

---

## 客户-多选基础资料表 t_bd_customermaterial_cus

- **表名称：** 客户-多选基础资料表
- **表名：** t_bd_customermaterial_cus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_customermaterial_cus_fk |  | fid |
| 2 | pk_bd_customermaterial_cus |  | fpkid |

---

## 客户物料对应表-使用范围表 t_bd_customermaterial_u

- **表名称：** 客户物料对应表-使用范围表
- **表名：** t_bd_customermaterial_u

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
| 1 | pk_t_bd_customermaterial_u |  | fdataid,fuseorgid |
| 2 | idx_t_bd_customermaterial_u_uo |  | fuseorgid |

---

## 客户物料对应表-多语言表 t_bd_customermaterial_l

- **表名称：** 客户物料对应表-多语言表
- **表名：** t_bd_customermaterial_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_customermaterial_l |  | fid,flocaleid |
| 2 | pk_t_bd_customermaterial_l |  | fpkid |

---

## 客户物料对应表-主表 t_bd_customermaterial

- **表名称：** 客户物料对应表-主表
- **表名：** t_bd_customermaterial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fapprovedate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 5 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsettingtype | 设置类型 | varchar | 10 |  | √ | ' ' | 设置类型,枚举: A :客户 B :客户分类 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fbizorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 22 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_customermaterial |  | fid |
| 2 | idx_bd_customermaterial |  | fnumber |
| 3 | idx_t_bd_customermaterial_createorg |  | fcreateorgid |
| 4 | idx_t_bd_customermaterial_master |  | fmasterid |
