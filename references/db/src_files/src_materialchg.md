# 更新标的、补充标的-src_materialchg

## 更新标的、补充标的-主表 t_src_materialchg

- **表名称：** 更新标的、补充标的-主表
- **表名：** t_src_materialchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 3 | fprojectid | 项目ID | int8 | 64 |  | √ | 0 | 项目ID |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_materialchg_pid |  | fparentid |
| 2 | pk_src_materialchg |  | fid |

---

## 采购方附件-附件表 t_src_purlistentry_fj

- **表名称：** 采购方附件-附件表
- **表名：** t_src_purlistentry_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlistentry_fj_bid |  | fbasedataid |
| 2 | pk_src_purlistentry_fj |  | fpkid |
| 3 | idx_src_purlistentry_fj_fid |  | fentryid |

---

## 标的分录-子表 t_src_materialchgentry

- **表名称：** 标的分录-子表
- **表名：** t_src_materialchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fsrcentryid | 采购清单分录ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 4 | fischanged | 是否更新 | bpchar | 1 |  | √ | '0' | 是否更新 |
| 5 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdescription | 标的描述 | varchar | 1024 |  | √ | ' ' | 标的描述 |
| 9 | fmaterialnane | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 10 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_materialchgentry |  | fentryid |
| 2 | idx_src_materialchgentry_fid |  | fid |
