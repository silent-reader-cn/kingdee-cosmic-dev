# 标的流标变更-src_materialend

## 标的流标变更-主表 t_src_materialend

- **表名称：** 标的流标变更-主表
- **表名：** t_src_materialend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fschemeid | 标的流标方案 | int8 | 64 |  | √ | 0 | 扩展过滤 pds_extfilter |
| 9 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 10 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_materialend_pid |  | fparentid |
| 2 | pk_src_materialend |  | fid |

---

## 标的分录-子表 t_src_materialendentry

- **表名称：** 标的分录-子表
- **表名：** t_src_materialendentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 招标数量 | numeric | 23 | 10 | √ | 0 | 招标数量 |
| 3 | fprojectid | 招标项目编号 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fpurlistid | 流标标的名称 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 8 | fsrctypeid | 招标流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 9 | fsupplierid | 流标供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fissource | 是否重新招标 | bpchar | 1 |  | √ | '1' | 是否重新招标 |
| 11 | fcount | 报价供应商数 | int4 | 32 |  | √ | 0 | 报价供应商数 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbidname | 招标项目名称 | varchar | 80 |  | √ | ' ' | 招标项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_materialendentry_fid |  | fid |
| 2 | pk_src_materialendentry |  | fentryid |
