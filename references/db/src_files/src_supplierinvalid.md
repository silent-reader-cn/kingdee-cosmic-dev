# 供应商废标/弃标段-src_supplierinvalid

## 回标详情分录-子表 t_src_supinvalidentry

- **表名称：** 回标详情分录-子表
- **表名：** t_src_supinvalidentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 3 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 4 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 5 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 6 | fentrystatus | 评标状态 | bpchar | 1 |  | √ | ' ' | 评标状态,枚举: A :待下达 B :已下达 C :部分评标 D :已评标 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 11 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 12 | fispayfee | 是否已缴纳 | bpchar | 1 |  | √ | '0' | 是否已缴纳 |
| 13 | fisdiscard | 是否废标/弃标段 | bpchar | 1 |  | √ | '0' | 是否废标/弃标段 |
| 14 | ffeeamount | 投标保证金 | numeric | 23 | 10 | √ | 0 | 投标保证金 |
| 15 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 16 | fisabandon | 是否拒标 | bpchar | 1 |  | √ | '0' | 是否拒标 |
| 17 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 18 | fisconfirm | 是否应标 | bpchar | 1 |  | √ | '0' | 是否应标 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fisquote | 是否报价 | bpchar | 1 |  | √ | '0' | 是否报价 |
| 21 | fisnegotiate | 是否议标报价 | bpchar | 1 |  | √ | '0' | 是否议标报价 |
| 22 | fabandonreason | 拒标原因 | varchar | 255 |  | √ | ' ' | 拒标原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supinvalidentry |  | fentryid |
| 2 | idx_src_supinvalidentry |  | fid |
| 3 | idx_src_supinvalidentry_eid |  | fsrcentryid |

---

## 供应商废标/弃标段-主表 t_src_supplierinvalid

- **表名称：** 供应商废标/弃标段-主表
- **表名：** t_src_supplierinvalid

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 1 | idx_src_supplierinvalid_comp |  | fparentid,fpentitykey,fentitykey |
| 2 | pk_src_supplierinvalid |  | fid |
