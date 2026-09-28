# 折旧分摊设置-fa_depresplitsetup

## 分摊维度-子表 t_fa_depresplitsubentry

- **表名称：** 分摊维度-子表
- **表名：** t_fa_depresplitsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fasstypename | 基础资料类型名称 | varchar | 200 |  | √ | ' ' | 基础资料类型名称 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fasstype | 基础资料类型 | varchar | 100 |  | √ | ' ' | 基础资料类型 |
| 4 | fcalculateid | 核算维度ID | int8 | 64 |  | √ | 0 | 核算维度ID |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fassid | 基础资料id | int8 | 64 |  | √ | 0 | 基础资料id |
| 8 | fassname | 基础资料名称 | varchar | 200 |  | √ | ' ' | 基础资料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depresplitsubentry_pkey |  | fdetailid |
| 2 | idx_fa_depresplitsubentry_fid |  | fentryid |

---

## 折旧分摊维度-多选基础资料表 t_fa_depresplitdims

- **表名称：** 折旧分摊维度-多选基础资料表
- **表名：** t_fa_depresplitdims

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depresplitdims_pkey |  | fpkid |
| 2 | idx_fa_depresplitdims_fk |  | fid |

---

## 折旧分摊设置-主表 t_fa_depresplitsetup

- **表名称：** 折旧分摊设置-主表
- **表名：** t_fa_depresplitsetup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmsg | 折旧费分摊信息 | text | 0 |  |  | null | 折旧费分摊信息 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | frealcardid | 资产卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 10 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fendperiodid | 失效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fbeginperiodid | 生效开始期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 21 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fa_depresplitsetup_master |  | fmasterid |
| 2 | idx_fa_depresplitsetup |  | forgid,fdepreuseid,fbeginperiodid,fendperiodid |
| 3 | idx_t_fa_depresplitsetup_createorg |  | fcreateorgid |
| 4 | t_fa_depresplitsetup_pkey |  | fid |
| 5 | idx_fa_depresplitsetupcard |  | frealcardid |

---

## 折旧分摊设置-多语言表 t_fa_depresplitsetup_l

- **表名称：** 折旧分摊设置-多语言表
- **表名：** t_fa_depresplitsetup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_dpsu_fid_flocaleid |  | fid,flocaleid |
| 2 | t_fa_depresplitsetup_l_pkey |  | fpkid |

---

## 折旧分摊设置-使用范围位图表 t_fa_depresplitsetup_m

- **表名称：** 折旧分摊设置-使用范围位图表
- **表名：** t_fa_depresplitsetup_m

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
| 1 | pk_t_fa_depresplitsetup_m |  | forgid |

---

## 分摊维度-多语言表 t_fa_depresplitsubentry_l

- **表名称：** 分摊维度-多语言表
- **表名：** t_fa_depresplitsubentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fasstypename | 基础资料类型名称 | varchar | 200 |  |  | ' ' | 基础资料类型名称 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fassname | 基础资料名称 | varchar | 200 |  |  | ' ' | 基础资料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_depresplitsubentry_l |  | fpkid |
| 2 | idx_fa_depspsubentry_l_fid |  | fdetailid,flocaleid |

---

## 分摊比例-子表 t_fa_depresplitentry

- **表名称：** 分摊比例-子表
- **表名：** t_fa_depresplitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forgdutyid | 部门属性 | int8 | 64 |  | √ | 0 | 部门属性 bos_org_duty |
| 5 | fassinfo | 横表组合信息 | varchar | 4000 |  |  | null | 横表组合信息 |
| 6 | fpercent | 分摊比例(%) | numeric | 19 | 6 | √ | 0.000000 | 分摊比例(%) |
| 7 | fassinfoimport | 横表组合信息(引入) | varchar | 4000 |  |  | null | 横表组合信息(引入) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depresplitentry_pkey |  | fentryid |
| 2 | idx_fa_depresplitentry_fid |  | fid |

---

## 折旧分摊设置-使用范围表 t_fa_depresplitsetup_u

- **表名称：** 折旧分摊设置-使用范围表
- **表名：** t_fa_depresplitsetup_u

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
| 1 | t_fa_depresplitsetup_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_fa_depresplitsetup_u_uo |  | fuseorgid |
