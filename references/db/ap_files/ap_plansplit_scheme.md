# 付款计划方案-ap_plansplit_scheme

## 条件分录-子表 t_ap_psscheme_centry

- **表名称：** 条件分录-子表
- **表名：** t_ap_psscheme_centry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldvalue | 值 | varchar | 2000 |  | √ | ' ' | 值 |
| 3 | fclargevalue | 条件值(大文本)-暂可见 | varchar | 255 |  | √ | ' ' | 条件值(大文本)-暂可见 |
| 4 | fclargevalue_tag | 条件值(大文本)-暂可见_详情 | text | 0 |  |  | null | 条件值(大文本)-暂可见_详情 |
| 5 | ffield | 字段 | varchar | 255 |  | √ | ' ' | 字段,枚举: |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcondition | 条件 | varchar | 30 |  | √ | ' ' | 条件,枚举: = :等于 in :在...中 |
| 8 | flogic | 逻辑 | varchar | 255 |  | √ | ' ' | 逻辑,枚举: && :并且 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ap_psscheme_centry |  | fentryid |
| 2 | idx_ap_psse_fid |  | fid |

---

## 维度分录-子表 t_ap_psscheme_dentry

- **表名称：** 维度分录-子表
- **表名：** t_ap_psscheme_dentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailkey | 财务应付单物料行字段 | varchar | 255 |  | √ | ' ' | 财务应付单物料行字段,枚举: |
| 3 | fhtdetailkey | 采购合同物料行字段 | varchar | 255 |  | √ | ' ' | 采购合同物料行字段,枚举: |
| 4 | fddplankey | 采购订单计划行字段 | varchar | 255 |  | √ | ' ' | 采购订单计划行字段,枚举: |
| 5 | fplankey | 财务应付单计划行字段 | varchar | 255 |  | √ | ' ' | 财务应付单计划行字段,枚举: |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdddetailkey | 采购订单物料行字段 | varchar | 255 |  | √ | ' ' | 采购订单物料行字段,枚举: |
| 8 | fhtplankey | 采购合同计划行字段 | varchar | 255 |  | √ | ' ' | 采购合同计划行字段,枚举: |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_pssd_fid |  | fid |
| 2 | pk_ap_psscheme_dentry |  | fentryid |

---

## 付款计划方案-主表 t_ap_plansplitscheme

- **表名称：** 付款计划方案-主表
- **表名：** t_ap_plansplitscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 160 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 11 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ap_plansplitscheme |  | fid |
| 2 | idx_ap_planss_number |  | fnumber |

---

## 组织分录-子表 t_ap_psscheme_oentry

- **表名称：** 组织分录-子表
- **表名：** t_ap_psscheme_oentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pss_oe_org |  | forg |
| 2 | pk_ap_psscheme_oentry |  | fentryid |
| 3 | idx_pss_oe_fid |  | fid |

---

## 付款计划方案-多语言表 t_ap_plansplitscheme_l

- **表名称：** 付款计划方案-多语言表
- **表名：** t_ap_plansplitscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_planss_fid |  | fid,flocaleid |
| 2 | pk_ap_plansplitscheme_l |  | fpkid |
